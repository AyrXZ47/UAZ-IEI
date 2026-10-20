#!/usr/bin/env python3
"""Motor en vivo compartido de las practicas de Comunicaciones Inalambricas.

Reemplaza el flujo por lotes (captura -> figura -> cerrar -> otra figura) por una
sola ventana que se actualiza en tiempo real y reproduce el audio FM en vivo,
con la misma cadena de recepcion del flujo GRC que ya funciona:

    IQ del RTL-SDR -> filtro de canal +-100 kHz -> diezmado -> discriminador FM
                   -> diezmado a 48 kHz + de-enfasis 75 us -> pw-cat

Los entregables (PNG + JSON) se guardan a un golpe de tecla sin abrir mas
ventanas.  Cada practica aporta sus propios paneles definiendo una subclase de
`Practica`.

Teclas comunes:  s = guardar entregables,  a = audio on/off,  q = salir.
"""
import argparse
import shutil
import subprocess
import sys
import threading
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun  # noqa: E402

AUDIO_RATE = 48000
WBFM_MAX_DEV = 75e3
DEEMPH_TAU = 75e-6
CHANNEL_RATE = 240e3
CHANNEL_BW = 100e3
BLOQUE = 1 << 17


# --------------------------------------------------------------------------
# Cadenas de senal
# --------------------------------------------------------------------------

def fm_demod(x):
    """Discriminador FM: fase del producto x[n] * conj(x[n-1])."""
    return np.angle(x[1:] * np.conj(x[:-1]))


def make_channelizer(fs, dec, bw=CHANNEL_BW):
    """Filtro de canal y diezmado a ~240 kHz, con estado entre bloques."""
    from scipy.signal import firwin, lfilter

    taps = firwin(121, bw, fs=fs, window=("kaiser", 6.0))
    zi = np.zeros(taps.size - 1, np.complex64)

    def proc(x):
        nonlocal zi
        y, zi = lfilter(taps, 1.0, x, zi=zi)
        return y[::dec]

    return proc


def make_audio(fs, dec):
    """Diezma el discriminador a 48 kHz (anti-alias) y aplica de-enfasis."""
    from scipy.signal import firwin, lfilter

    out_rate = fs / dec
    taps = firwin(129, 15e3, fs=fs)
    zi = np.zeros(taps.size - 1)
    deemph = np.exp(-1.0 / (out_rate * DEEMPH_TAU))
    b = 1.0 - deemph
    gain = 0.7 * fs / (2 * np.pi * WBFM_MAX_DEV)
    estado = np.zeros(1)

    def proc(demod):
        nonlocal zi, estado
        a, zi = lfilter(taps, 1.0, demod, zi=zi)
        a = a[::dec] * gain
        a, estado = lfilter([b], [1.0, -deemph], a, zi=estado)
        return (np.clip(a, -1.0, 1.0) * 32767).astype(np.int16)

    return proc, out_rate


def rayleigh_sim(rate, fd=10.0, los=0.0, semilla=0, componentes=128):
    """Generador por bloques de un canal Rayleigh con Doppler maximo fd.

    Modelo de Jakes (suma de sinusoides): cada componente llega con frecuencia
    fD*cos(theta) y fase aleatoria, asi el espectro Doppler tiene ancho exacto
    2*fD.  La envolvente se sintetiza a 20*fD y se interpola al sample rate del
    receptor llevando el estado, para no reiniciar el desvanecimiento entre
    bloques.  Uso:  gen = rayleigh_sim(fs, fd);  x = gen(n_muestras).
    """
    fs_f = max(20.0 * fd, 1000.0)                     # tasa de la envolvente
    per = rate / fs_f                                 # muestras IQ por muestra
    rng = np.random.default_rng(semilla)
    theta = rng.uniform(0.0, 2.0 * np.pi, componentes)
    fase = rng.uniform(0.0, 2.0 * np.pi, componentes)
    frecuencia = fd * np.cos(theta)
    peso = 1.0 / np.sqrt(componentes)
    estado = {"n": 0, "env": np.zeros(0, complex), "pos": 0.0}

    def env_nuevo(m=4096):
        t = (estado["n"] + np.arange(m)) / fs_f
        estado["n"] += m
        y = np.zeros(m, complex)
        for f, ph in zip(frecuencia, fase):
            y += np.exp(1j * (2.0 * np.pi * f * t + ph))
        return y * peso

    def bloque(n):
        necesarias = n / per
        while estado["pos"] + necesarias > estado["env"].size - 1:
            estado["env"] = np.concatenate(
                [estado["env"][int(estado["pos"]):], env_nuevo()])
            estado["pos"] = 0.0
        env = estado["env"]
        t = estado["pos"] + np.arange(n) / per
        y = (np.interp(t, np.arange(env.size), env.real)
             + 1j * np.interp(t, np.arange(env.size), env.imag))
        estado["pos"] += necesarias
        return (y + los).astype(np.complex64)

    return bloque


def ruido_plano(rate, fd=10.0, semilla=0):
    """Generador por bloques de una envolvente con espectro Doppler plano +-fd.

    Ruido gaussiano complejo filtrado (FIR en banda base) con el estado del
    filtro y de la interpolacion continuo entre bloques, asi el desvanecimiento
    no se reinicia en cada llamada.  Es el modelo para el que esta calibrado el
    estimador de fD de la practica 5 (espectro plano: sigma_RMS = fD/sqrt(3)).
    """
    from scipy.signal import firwin, lfilter

    fs_f = max(20.0 * fd, 1000.0)                     # tasa de la envolvente
    per = rate / fs_f                                 # muestras IQ por muestra
    taps = int(min(max(7.0 * fs_f / fd, 33), 8193)) | 1
    h = firwin(taps, fd, fs=fs_f)
    rng = np.random.default_rng(semilla)
    zi = np.zeros(h.size - 1, complex)
    estado = {"env": np.zeros(0, complex), "pos": 0.0}

    def env_nuevo(m=4096):
        nonlocal zi
        z = (rng.standard_normal(m) + 1j * rng.standard_normal(m)) / np.sqrt(2)
        y, zi = lfilter(h, 1.0, z, zi=zi)
        return y

    def bloque(n):
        necesarias = n / per
        while estado["pos"] + necesarias > estado["env"].size - 1:
            estado["env"] = np.concatenate(
                [estado["env"][int(estado["pos"]):], env_nuevo()])
            estado["pos"] = 0.0
        env = estado["env"]
        t = estado["pos"] + np.arange(n) / per
        y = (np.interp(t, np.arange(env.size), env.real)
             + 1j * np.interp(t, np.arange(env.size), env.imag))
        estado["pos"] += necesarias
        return y

    return bloque


def fm_sintetica(fs, n, f0=30e3, dev=75e3, snr_db=25.0, seed=0):
    """Estacion FM sintetica (audio de banda limitada) para correr sin antena."""
    from scipy.signal import firwin, lfilter

    rng = np.random.default_rng(seed)
    audio = lfilter(firwin(129, 15e3, fs=fs), 1.0, rng.standard_normal(n))
    audio /= np.sqrt(np.mean(audio ** 2))
    audio = np.tanh(audio)                    # audio tipo radiodifusion (RMS/pico ~0.6)
    audio /= np.max(np.abs(audio))            # desviacion pico = dev
    t = np.arange(n) / fs
    fase = 2 * np.pi * f0 * t + 2 * np.pi * dev * np.cumsum(audio) / fs
    x = np.exp(1j * fase)
    ruido = (rng.standard_normal(n) + 1j * rng.standard_normal(n)) / np.sqrt(2)
    return (x + ruido * 10 ** (-snr_db / 20)).astype(np.complex64)


# --------------------------------------------------------------------------
# Fuente de muestras IQ
# --------------------------------------------------------------------------

class Fuente:
    """Bloques IQ asincronos del RTL-SDR (o sinteticos con sim=True).

    La lectura corre en un hilo; el consumidor de audio se suscribe con
    `al_bloque` para no perder muestras, y el GUI solo toma `ultimo`.
    """

    def __init__(self, freq=96.5e6, rate=comun.RATE_DEF, ganancia="auto",
                 bw=0.6e6, ppm=0.0, bloque=BLOQUE, sim=False):
        self.freq = float(freq)
        self.bloque_n = int(bloque)
        self.sim = bool(sim)
        self.ultimo = None
        self.n_bloques = 0
        self._candado = threading.Lock()
        self._oyentes = []
        self._parar = threading.Event()
        if sim:
            self.fs = float(rate)
            self._generador = sim if callable(sim) else None
            self.hilo = threading.Thread(target=self._simular, daemon=True)
        else:
            self.sdr = self._abrir(rate, ganancia, bw, ppm)
            self.fs = float(self.sdr.get_sample_rate())
            self.hilo = threading.Thread(target=self._leer, daemon=True)
        self.hilo.start()

    def _abrir(self, rate, ganancia, bw, ppm):
        from rtlsdr import RtlSdr

        sdr = RtlSdr()
        sdr.sample_rate = rate
        sdr.center_freq = self.freq
        if ppm:
            sdr.freq_correction = int(ppm)
        if bw:
            try:
                sdr.set_bandwidth(bw)
            except Exception as e:
                print(f"aviso: no se pudo fijar el filtro IF: {e}", file=sys.stderr)
        comun.fijar_ganancia(sdr, ganancia)
        return sdr

    def _simular(self):
        t = 0
        while not self._parar.is_set():
            if self._generador is not None:
                x = self._generador(self.bloque_n)
            else:
                x = fm_sintetica(self.fs, self.bloque_n, seed=t)
            self._entregar(x)
            t += 1
            time.sleep(self.bloque_n / self.fs)

    def _leer(self):
        def cb(raw, ctx):
            self._entregar(comun.bytes_a_iq(raw))

        try:
            self.sdr.read_bytes_async(cb, 2 * self.bloque_n)
        except Exception as e:            # se propaga al cerrar la ventana
            if not self._parar.is_set():
                print(f"error de lectura del SDR: {e}", file=sys.stderr)

    def _entregar(self, x):
        with self._candado:
            self.ultimo = x
            self.n_bloques += 1
        for fn in self._oyentes:
            fn(x)

    def sintonizar(self, freq):
        """Retuna el receptor (en --sim solo cambia la frecuencia anotada)."""
        self.freq = float(freq)
        if not self.sim:
            self.sdr.center_freq = self.freq

    def al_bloque(self, fn):
        """Suscribe un consumidor que corre en el hilo de lectura."""
        self._oyentes.append(fn)

    def esperar(self, timeout=5.0):
        """Bloquea hasta el primer bloque (o el timeout)."""
        t0 = time.monotonic()
        while self.ultimo is None and time.monotonic() - t0 < timeout:
            time.sleep(0.01)
        return self.ultimo is not None

    def cerrar(self):
        self._parar.set()
        if not self.sim:
            try:
                self.sdr.cancel_read_async()
            except Exception:
                pass
        self.hilo.join(timeout=2)
        if not self.sim:
            try:
                self.sdr.close()
            except Exception:
                pass


# --------------------------------------------------------------------------
# Audio
# --------------------------------------------------------------------------

def _reproductor(rate):
    """Comando que reproduce PCM s16 mono por stdin, segun lo que haya."""
    if shutil.which("pw-cat"):
        return ["pw-cat", "-p", "-a", "--format", "s16", "--rate", str(rate),
                "--channels", "1", "--latency", "200ms", "-"]
    if shutil.which("paplay"):
        return ["paplay", "--raw", "--format=s16le", f"--rate={rate}",
                "--channels=1", "--latency-msec=200"]
    if shutil.which("aplay"):
        return ["aplay", "-q", "-t", "raw", "-f", "S16_LE", "-c", "1",
                "-r", str(rate), "-"]
    return None


class AudioFM:
    """Demodula WBFM mono y la reproduce en vivo por PipeWire/Pulse/ALSA."""

    def __init__(self, fs):
        self.cdec = max(1, int(round(fs / CHANNEL_RATE)))
        self.canal = make_channelizer(fs, self.cdec)
        adec = max(1, int(round(fs / self.cdec / AUDIO_RATE)))
        self.audio, self.rate = make_audio(fs / self.cdec, adec)
        cmd = _reproductor(int(round(self.rate)))
        self.proc = None
        if cmd is None:
            print("aviso: no hay reproductor de audio (pw-cat/paplay/aplay); "
                  "sigo sin sonido", file=sys.stderr)
            return
        try:
            self.proc = subprocess.Popen(cmd, stdin=subprocess.PIPE,
                                         stderr=subprocess.DEVNULL)
        except Exception as e:
            print(f"aviso: no se pudo abrir el reproductor de audio: {e}",
                  file=sys.stderr)

    @property
    def activo(self):
        return self.proc is not None

    def escribir(self, x):
        if self.proc is None:
            return
        try:
            self.proc.stdin.write(self.audio(fm_demod(self.canal(x))).tobytes())
        except (BrokenPipeError, ValueError):
            self.proc = None

    def cerrar(self):
        if self.proc is None:
            return
        try:
            self.proc.stdin.close()
        except (BrokenPipeError, ValueError):
            pass
        self.proc.terminate()
        self.proc = None


# --------------------------------------------------------------------------
# Practica: contrato que implementa cada una
# --------------------------------------------------------------------------

class Practica:
    """Paneles y analisis propios de una practica, enchufados a la ventana."""

    titulo = "practica"
    filas = 0                 # filas extra bajo espectro y cascada
    alto = None               # height_ratios del gridspec (opcional)
    rango_db = (-90, 0)       # rango del eje de potencia (dBFS)
    audio = False             # el audio FM tiene sentido solo en radiodifusion

    def __init__(self, args):
        self.args = args
        self.freq = float(args.freq)
        self.app = None
        self.dirs = {}
        self.estado = ""      # texto extra para el titulo (lo pone actualizar)
        self._ultimo_cada = 0.0

    def generador_sim(self, rate):
        """Bloques sinteticos propios para --sim (None = FM sintetica del motor)."""
        return None

    def cada(self, segundos):
        """True como maximo una vez cada `segundos` (ritmo de la demo --sim)."""
        ahora = time.monotonic()
        if ahora - self._ultimo_cada < segundos:
            return False
        self._ultimo_cada = ahora
        return True

    def nuevo_bloque(self, n=2, timeout=1.0):
        """Espera `n` bloques nuevos de la fuente y devuelve el ultimo."""
        t0 = time.monotonic()
        inicio = self.app.fuente.n_bloques
        while (self.app.fuente.n_bloques < inicio + n
               and time.monotonic() - t0 < timeout):
            time.sleep(0.005)
        return self.app.fuente.ultimo

    # -- paneles --------------------------------------------------------
    def ejes(self, fig, gs, inicio):
        """Crea los ejes propios sobre `gs` desde la fila `inicio`."""
        return []

    def actualizar(self, x, fs, t):
        """Se llama ~`fps` veces por segundo con el ultimo bloque IQ."""

    def tecla(self, ev):
        """Teclas propias de la practica (las comunes las maneja App)."""

    def guardar(self):
        """Guarda los entregables y devuelve la lista de rutas escritas."""
        return []

    def ayuda(self):
        """Ayuda de teclas propia."""
        return ""


# --------------------------------------------------------------------------
# Ventana unica
# --------------------------------------------------------------------------

class App:
    def __init__(self, practica, fuente, audio=None, bins=1024, historia=200,
                 fps=10.0, rango_db=None):
        import matplotlib.pyplot as plt
        import mplcyberpunk  # noqa: F401  (paleta obligatoria del repo)

        self.p = practica
        self.fuente = fuente
        self.fs = fuente.fs
        self.bins = int(bins)
        self.historia = int(historia)
        self.fps = float(fps)
        self.rango_db = tuple(rango_db or practica.rango_db)
        self.p.app = self
        self.p.audio_vivo = audio if (audio is not None) else None
        if self.p.audio_vivo is not None:
            self.fuente.al_bloque(self.p.audio_vivo.escribir)

        self.f_mhz = np.fft.fftshift(np.fft.fftfreq(self.bins, 1 / self.fs)) / 1e6
        self.pdb = np.full(self.bins, self.rango_db[0], dtype=float)
        self._auto = 0

        filas = 2 + self.p.filas
        alto = self.p.alto or ([2.2, 1.6] + [1.7] * self.p.filas)
        self.fig = plt.figure(num=self.p.titulo, figsize=(10.5, 2.4 * filas + 1.2))
        gs = self.fig.add_gridspec(filas, 1, height_ratios=alto[:filas],
                                   hspace=0.45)
        self.ax_s = self.fig.add_subplot(gs[0])
        self.ax_w = self.fig.add_subplot(gs[1])
        self.ejes = [self.ax_s, self.ax_w] + list(self.p.ejes(self.fig, gs, 2))

        self.linea, = self.ax_s.plot(self.f_mhz, self.pdb, lw=0.9, color="#00e5ff")
        self.ax_s.set_ylabel("dBFS")
        self.ax_s.set_xlim(self.f_mhz[0], self.f_mhz[-1])
        self.ax_s.set_ylim(*self.rango_db)
        self.ax_s.grid(alpha=0.25)
        mplcyberpunk.make_lines_glow(self.ax_s, n_glow_lines=6, alpha_line=0.25)
        self.glow = [l for l in self.ax_s.get_lines() if l is not self.linea]

        self.cascada = np.full((self.historia, self.bins), self.rango_db[0])
        self.img = self.ax_w.imshow(
            self.cascada, aspect="auto", origin="lower", cmap="magma",
            extent=[self.f_mhz[0], self.f_mhz[-1], 0, self.historia],
            vmin=self.rango_db[0], vmax=self.rango_db[1], interpolation="nearest")
        self.ax_w.set_xlabel("Frecuencia (MHz)")
        self.ax_w.set_ylabel("Cascada")

        self.fig.canvas.mpl_connect("key_press_event", self._tecla)
        self._artistas = {}
        self._bg = None
        self._tam = None
        self._blit = hasattr(self.fig.canvas, "copy_from_bbox")
        self._titulo_base = (f"{self.p.titulo}  |  {self.p.freq/1e6:.3f} MHz  "
                             f"span {self.fs/1e6:.2f} MHz  "
                             f"{'SIM' if fuente.sim else 'RTL-SDR'}")
        self.ax_s.set_title(self._titulo_base, fontsize=9, loc="left")
        self.fig.text(0.5, 0.005,
                      "s guardar   a audio   q salir   " + self.p.ayuda(),
                      ha="center", fontsize=8, alpha=0.8)

    # -- artistas -------------------------------------------------------
    def artistas_de(self, ax):
        """Artistas que se redibujan por frame (lineas, imagenes, textos)."""
        from matplotlib.image import AxesImage
        from matplotlib.lines import Line2D
        from matplotlib.text import Text

        return [a for a in ax.get_children() if isinstance(a, (Line2D, AxesImage, Text))]

    def reencuadrar(self):
        """Redibuja la figura completa y recaptura el fondo del blit."""
        self.fig.canvas.draw()
        if self._blit:
            self._bg = self.fig.canvas.copy_from_bbox(self.fig.bbox)
            self._tam = self.fig.canvas.get_width_height()
        self._artistas = {ax: self.artistas_de(ax) for ax in self.ejes}

    # -- lazo principal -------------------------------------------------
    def correr(self, segundos=None):
        import matplotlib.pyplot as plt

        plt.ion()
        self.fig.show()
        self.reencuadrar()
        t0 = time.monotonic()
        periodo = 1.0 / self.fps
        try:
            while plt.fignum_exists(self.fig.number):
                if segundos is not None and time.monotonic() - t0 >= segundos:
                    break
                tic = time.monotonic()
                self.paso()
                resto = periodo - (time.monotonic() - tic)
                if resto > 0:
                    time.sleep(resto)          # sin plt.pause: fuerza un redibujo
                self.fig.canvas.flush_events()
        finally:
            plt.close(self.fig)

    def paso(self):
        from scipy import signal as sig

        x = self.fuente.ultimo
        if x is None:
            self.fig.canvas.flush_events()
            return
        _, P = sig.welch(x, fs=self.fs, nperseg=self.bins, return_onesided=False)
        pdb = 10 * np.log10(np.fft.fftshift(P) + 1e-12)

        if self._auto < 20:                     # autocalibrado del eje (1 s)
            self._auto += 1
            lo, hi = np.percentile(pdb, 2) - 4, pdb.max() + 4
            if lo < self.rango_db[0] or hi > self.rango_db[1]:
                self.rango_db = (min(lo, self.rango_db[0]),
                                 max(hi, self.rango_db[1]))
                self.ax_s.set_ylim(*self.rango_db)
                self.img.set_clim(*self.rango_db)
                self.reencuadrar()

        self.pdb = pdb
        self.linea.set_ydata(pdb)
        for g in self.glow:
            g.set_ydata(pdb)
        self.cascada[:-1] = self.cascada[1:]
        self.cascada[-1] = np.clip(pdb, *self.rango_db)
        self.img.set_data(self.cascada)
        self.p.actualizar(x, self.fs, time.monotonic())
        self.ax_s.set_title(f"{self._titulo_base}   {self.p.estado}",
                            fontsize=9, loc="left")
        self._dibujar()

    def _dibujar(self):
        if not self._blit:
            self.fig.canvas.draw()
            return
        if self.fig.canvas.get_width_height() != self._tam:
            self.reencuadrar()
        self.fig.canvas.restore_region(self._bg)
        for ax, lista in self._artistas.items():
            for a in lista:
                try:
                    ax.draw_artist(a)
                except Exception:
                    pass
        self.fig.canvas.blit(self.fig.bbox)
        self.fig.canvas.flush_events()

    # -- teclas ---------------------------------------------------------
    def _tecla(self, ev):
        if ev.key in ("s", "S"):
            rutas = self.p.guardar()
            for r in rutas:
                print(f"guardado: {r}")
        elif ev.key in ("a", "A"):
            self.alterna_audio()
        else:
            self.p.tecla(ev)

    def alterna_audio(self):
        """Silencia el audio o lo activa si la practica arranco sin el."""
        a = self.p.audio_vivo
        if a is None:
            a = AudioFM(self.fs)
            if a.activo:
                self.fuente.al_bloque(a.escribir)
                self.p.audio_vivo = a
                print("audio FM activado", file=sys.stderr)
            return
        if a.activo:
            a.cerrar()
            print("audio silenciado", file=sys.stderr)
        else:
            a = AudioFM(self.fs)
            if a.activo:
                self.fuente.al_bloque(a.escribir)
                self.p.audio_vivo = a


# --------------------------------------------------------------------------
# Arranque comun
# --------------------------------------------------------------------------

def parser(desc, freq=96.1e6, rate=comun.RATE_DEF, mas=None):
    p = argparse.ArgumentParser(
        description=desc, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("-f", "--freq", type=float, default=freq,
                   help="frecuencia central (Hz)")
    p.add_argument("-r", "--rate", type=float, default=rate,
                   help="sample rate / span (Hz)")
    p.add_argument("-g", "--gain", default="auto",
                   help="ganancia en dB o 'auto' (mayor sin recortar el ADC)")
    p.add_argument("-b", "--bw", type=float, default=0.6e6,
                   help="filtro IF del tuner (Hz, 0 = no tocar)")
    p.add_argument("--ppm", type=float, default=0.0,
                   help="correccion de frecuencia del cristal (ppm)")
    p.add_argument("--bin", type=int, default=1024, help="bins del FFT en vivo")
    p.add_argument("--historia", type=int, default=200, help="filas de la cascada")
    p.add_argument("--fps", type=float, default=10.0, help="refresco de la ventana")
    p.add_argument("--segundos", type=float, default=None,
                   help="cerrar solo tras N segundos (pruebas)")
    p.add_argument("--guardar", action="store_true",
                   help="guardar entregables al cerrar")
    p.add_argument("--audio", dest="audio", action="store_true",
                   help="demodular FM y reproducir audio")
    p.add_argument("--sin-audio", dest="audio", action="store_false",
                   help="silencio")
    p.add_argument("--sim", action="store_true",
                   help="fuente sintetica, sin dongle")
    p.set_defaults(audio=None)
    for flags, kw in (mas or []):
        p.add_argument(*((flags,) if isinstance(flags, str) else flags), **kw)
    return p


def limites(args):
    """Rango (lo, hi) del eje de potencia desde --rango.-90,-10."""
    r = getattr(args, "rango", None)
    if not r:
        return None
    lo, hi = (float(v) for v in r.split(","))
    return (lo, hi)


def correr(practica, args):
    fuente = audio = None
    try:
        try:
            sim = args.sim
            if args.sim:
                sim = practica.generador_sim(args.rate) or True
            fuente = Fuente(freq=args.freq, rate=args.rate, ganancia=args.gain,
                            bw=args.bw, ppm=args.ppm, sim=sim)
        except Exception as e:
            print(f"No se pudo abrir el SDR: {e}", file=sys.stderr)
            print("Reconecta el dongle y libera el driver DVB:  "
                  "sudo modprobe -r dvb_usb_rtl28xxu", file=sys.stderr)
            return 1
        if not fuente.esperar():
            print("No llegaron muestras del receptor.", file=sys.stderr)
            return 1
        usar_audio = args.audio if args.audio is not None else practica.audio
        if usar_audio:
            audio = AudioFM(fuente.fs)
        app = App(practica, fuente, audio, bins=args.bin, historia=args.historia,
                  fps=args.fps, rango_db=limites(args))
        app.correr(segundos=args.segundos)
    except KeyboardInterrupt:
        pass
    finally:
        if fuente is not None:
            fuente.cerrar()
        if audio is not None:
            audio.cerrar()
    if args.guardar:
        for r in practica.guardar():
            print(f"guardado: {r}")
    return 0
