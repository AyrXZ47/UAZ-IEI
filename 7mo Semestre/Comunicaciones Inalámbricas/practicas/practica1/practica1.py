#!/usr/bin/env python3
"""Practica 1. Introduccion al RTL-SDR y analisis espectral de senales inalambricas.

Una sola ventana en vivo (espectro, cascada e I/Q), audio FM sonando al mismo
tiempo y los entregables del reporte guardados con la tecla `s`:
  - componentes I y Q en el tiempo
  - potencia promedio recibida
  - espectro (FFT) y frecuencia central / ancho de banda observados
  - espectrograma

Uso:
    python3 practica1.py                       # estacion FM en 106.5 MHz
    python3 practica1.py -f 93.3e6             # otra estacion
    python3 practica1.py --sin-audio           # solo analisis en vivo
    python3 practica1.py --sim                 # sin dongle (FM sintetica)
    python3 practica1.py --selftest            # verifica el analisis sin dongle
Teclas:  s guardar entregables   q cerrar
"""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun  # noqa: E402
import vivo  # noqa: E402

DIR = Path(__file__).resolve().parent
FIGS, DATOS = DIR / "figs", DIR / "datos"
N_LIVE = 1024          # muestras de I/Q dibujadas en vivo


def centro_y_ancho(f, P, umbral_db=3.0, fraccion=0.99):
    """Frecuencia central y ancho de banda (99% de potencia) de la senal.

    Primero busca la region contigua sobre el piso de ruido + umbral_db alrededor
    del maximo; dentro de ella calcula el ancho con el `fraccion` de la potencia
    en exceso sobre el piso.
    """
    pdb = 10 * np.log10(P + 1e-20)
    piso = np.median(pdb)
    sobre = pdb > piso + umbral_db
    i = int(np.argmax(pdb))
    i0 = i1 = i
    while i0 > 0 and sobre[i0 - 1]:
        i0 -= 1
    while i1 < pdb.size - 1 and sobre[i1 + 1]:
        i1 += 1
    fr, Pr = f[i0:i1 + 1], P[i0:i1 + 1]
    exc = np.maximum(Pr - 10 ** (piso / 10), 0.0)
    if exc.sum() <= 0:
        return 0.0, 0.0
    cdf = np.cumsum(exc) / exc.sum()
    lo = np.searchsorted(cdf, (1 - fraccion) / 2)
    hi = np.searchsorted(cdf, 1 - (1 - fraccion) / 2)
    centro = float(np.average(fr, weights=exc))
    ancho = float(fr[min(hi, fr.size - 1)] - fr[lo])
    return centro, ancho


def analizar(x, fs):
    """Metricas de la captura: potencia, centro y ancho de banda."""
    n = x.size
    fw, Pw = comun.espectro(x, fs, nperseg=4096)   # PSD promediada (robusta)
    centro, ancho = centro_y_ancho(fw, Pw)
    X = np.fft.fftshift(np.fft.fft(x))
    f = np.linspace(-fs / 2, fs / 2, n)
    return {
        "n_muestras": int(n),
        "potencia_dbfs": float(comun.potencia_dbfs(x)),
        "offset_centro_Hz": centro,
        "ancho_banda_Hz": ancho,
        "f": f,
        "PSD_dB": 20 * np.log10(np.abs(X) + 1e-20),
    }


def fig_iq(x, fs, ruta):
    import matplotlib.pyplot as plt

    n = min(4096, x.size)
    t = np.arange(n) / fs * 1e3
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(9, 5.5), sharex=True)
    a1.plot(t, x.real[:n], lw=0.8)
    a1.set_ylabel("I[n]"); a1.set_title("Componente I"); a1.grid(alpha=0.3)
    a2.plot(t, x.imag[:n], lw=0.8, color="C1")
    a2.set_ylabel("Q[n]"); a2.set_title("Componente Q"); a2.grid(alpha=0.3)
    a2.set_xlabel("Tiempo (ms)")
    fig.suptitle("Muestras IQ de la estacion FM")
    fig.tight_layout()
    return comun.guardar_fig(fig, ruta, False)


def fig_espectro(f, psd_db, freq, ruta):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot((freq + f) / 1e6, psd_db, lw=0.7)
    ax.set_xlabel("Frecuencia (MHz)")
    ax.set_ylabel("Magnitud (dB)")
    ax.set_title("Espectro de la senal (FFT)")
    ax.grid(alpha=0.3)
    return comun.guardar_fig(fig, ruta, False)


def fig_espectrograma(x, fs, freq, ruta):
    import matplotlib.pyplot as plt
    from scipy import signal as sig

    f, t, S = sig.spectrogram(x, fs=fs, window="hamming", nperseg=1024,
                              noverlap=512, nfft=1024, return_onesided=False,
                              detrend=False, mode="psd")
    S = np.fft.fftshift(S, axes=0)
    f = np.fft.fftshift(f)
    fig, ax = plt.subplots(figsize=(9, 5))
    m = ax.pcolormesh(t * 1e3, (freq + f) / 1e6, 10 * np.log10(S + 1e-20),
                      shading="auto", cmap="viridis")
    ax.set_xlabel("Tiempo (ms)")
    ax.set_ylabel("Frecuencia (MHz)")
    ax.set_title("Espectrograma")
    fig.colorbar(m, ax=ax, label="PSD (dB)")
    return comun.guardar_fig(fig, ruta, False)


class P1(vivo.Practica):
    titulo = "Practica 1 - analisis espectral"
    filas = 1
    alto = [2.2, 1.6, 1.7]
    audio = True                 # es una estacion FM: aqui si se escucha

    def __init__(self, args):
        super().__init__(args)
        self.n = int(args.muestras)
        self.bloques = []
        self.total = 0
        self.ax_t = None
        self.lineas = []

    def ejes(self, fig, gs, inicio):
        self.ax_t = fig.add_subplot(gs[inicio])
        self.ax_t.set_xlim(0, N_LIVE)
        self.ax_t.set_ylim(-1.1, 1.1)
        self.ax_t.set_ylabel("IQ")
        self.ax_t.set_xlabel("Muestra (ventana en vivo)")
        self.ax_t.grid(alpha=0.25)
        self.lineas = [self.ax_t.plot(np.zeros(N_LIVE), lw=0.8, color="#00e5ff")[0],
                       self.ax_t.plot(np.zeros(N_LIVE), lw=0.8, color="#ff2975")[0]]
        self.ax_t.legend(["I", "Q"], loc="upper right", fontsize=8)
        return [self.ax_t]

    def _acumular(self, x):
        self.bloques.append(x)
        self.total += x.size
        while self.bloques and self.total - self.bloques[0].size >= self.n:
            self.total -= self.bloques.pop(0).size

    def captura(self):
        """Ultimas `n` muestras continuas (lo que va al reporte)."""
        if not self.bloques:
            return np.zeros(self.n, np.complex64)
        return np.concatenate(self.bloques)[-self.n:]

    def actualizar(self, x, fs, t):
        self._acumular(x)
        i, q = x.real[:N_LIVE], x.imag[:N_LIVE]
        if i.size < N_LIVE:                     # ultimo bloque incompleto
            i, q = np.resize(i, N_LIVE), np.resize(q, N_LIVE)
        self.lineas[0].set_ydata(i)
        self.lineas[1].set_ydata(q)
        app = self.app
        pdb = app.pdb if app is not None else None
        if pdb is not None:
            centro, ancho = centro_y_ancho(app.f_mhz * 1e6, 10 ** (pdb / 10))
            pot = float(np.mean(np.abs(x) ** 2))
            self.estado = (f"| P {10*np.log10(pot + 1e-20):5.1f} dBFS  "
                           f"fc {(self.freq + centro)/1e6:8.4f} MHz  "
                           f"B99 {ancho/1e3:5.1f} kHz")

    def ayuda(self):
        return ""

    def guardar(self):
        x = self.captura()
        res = analizar(x, self.app.fs)
        rutas = [
            fig_iq(x, self.app.fs, FIGS / "iq_temporal.png"),
            fig_espectro(res["f"], res["PSD_dB"], self.freq, FIGS / "espectro.png"),
            fig_espectrograma(x, self.app.fs, self.freq, FIGS / "espectrograma.png"),
        ]
        np.save(DATOS / "iq.npy", x)
        rutas.append(comun.guardar_json(
            DATOS / "resultados.json", frecuencia_Hz=self.freq,
            n_muestras=res["n_muestras"], potencia_dbfs=res["potencia_dbfs"],
            offset_centro_Hz=res["offset_centro_Hz"],
            ancho_banda_Hz=res["ancho_banda_Hz"]))
        print(f"Frecuencia sintonizada : {self.freq/1e6:.3f} MHz")
        print(f"Muestras               : {res['n_muestras']}")
        print(f"Potencia promedio      : {res['potencia_dbfs']:.2f} dBFS")
        print(f"Frecuencia central obs.: "
              f"{(self.freq + res['offset_centro_Hz'])/1e6:.4f} MHz "
              f"(offset {res['offset_centro_Hz']/1e3:+.1f} kHz)")
        print(f"Ancho de banda (99%)   : {res['ancho_banda_Hz']/1e3:.1f} kHz")
        return rutas


def selftest():
    fs, n = 2.4e6, 1 << 18
    x = vivo.fm_sintetica(fs, n, f0=30e3)
    res = analizar(x, fs)
    assert abs(res["offset_centro_Hz"] - 30e3) < 8e3, res["offset_centro_Hz"]
    assert 100e3 < res["ancho_banda_Hz"] < 350e3, res["ancho_banda_Hz"]
    p = comun.potencia_dbfs(x)
    assert -30 < p < 5, p
    # la cadena de audio del motor debe seguir demodulando el tono de prueba
    fs_a, fm, dev = 2.4e6, 1000.0, 75e3
    t = np.arange(int(fs_a)) / fs_a
    y = np.exp(2j * np.pi * (100e3 * t + dev / fm * np.sin(2 * np.pi * fm * t)))
    proc, out = vivo.make_audio(240e3, 5)
    ch = vivo.make_channelizer(fs_a, 10)(y.astype(np.complex64))
    a = proc(vivo.fm_demod(ch)).astype(np.float32) / 32767
    F = np.abs(np.fft.rfft(a * np.hanning(a.size)))
    fr = np.fft.rfftfreq(a.size, 1 / out)
    assert abs(fr[np.argmax(F)] - fm) < 20, fr[np.argmax(F)]
    assert 0.05 < np.sqrt(np.mean(a ** 2)) < 1.0
    print("practica1 selftest OK")


def main(argv=None):
    args = vivo.parser(
        __doc__, freq=106.5e6,
        mas=[(("-n", "--muestras"), dict(type=int, default=1 << 17,
                                        help="muestras del reporte guardado")),
             ("--selftest", dict(action="store_true"))]).parse_args(argv)
    if args.selftest:
        selftest()
        return 0
    return vivo.correr(P1(args), args)


if __name__ == "__main__":
    sys.exit(main())
