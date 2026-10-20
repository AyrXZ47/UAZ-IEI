#!/usr/bin/env python3
"""Practica 5. Efecto Doppler y tiempo de coherencia.

Una sola ventana en vivo: espectro y cascada del canal CW, la envolvente del
ultimo tramo y su espectro Doppler, con la estimacion de fD y del tiempo de
coherencia Tc = 0.423/fD en el titulo.

Procedimiento:
    1. Deja el transmisor fijo y elige el escenario con 1, 2 o 3.
    2. Camina como indica el escenario mientras observas el espectro Doppler.
    3. Pulsa ESPACIO para fijar la medicion de ese escenario.
    4. Pulsa s para guardar las figuras y el JSON del reporte.

Uso:
    python3 practica5.py                       # 3 escenarios, 5 s de ventana
    python3 practica5.py --dur 8 -r 240e3
    python3 practica5.py --sim                 # demo automatica, sin dongle
    python3 practica5.py --selftest            # verifica el estimador sin dongle
Teclas:  1 estatico   2 lento   3 rapido   ESPACIO medir   r reiniciar   s guardar
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
FS_ENV = 240.0            # tasa de la envolvente (Hz)
FD_ESC = {
    "estatico": (0.2, "Receptor estatico: permanece quieto con el receptor en la mano"),
    "lento": (3.0, "Movimiento lento: camina despacio y sosten el paso"),
    "rapido": (12.0, "Movimiento rapido: camina rapido y sosten el paso"),
}
NOMBRES = list(FD_ESC)


def simular(fd, rate, dur, semilla=42):
    """IQ sintetico de una fuente CW con desvanecimiento de espectro plano +-fd."""
    gen = vivo.ruido_plano(rate, fd=fd, semilla=semilla)
    n = int(dur * rate)
    partes, resto = [], n
    while resto > 0:
        x = gen(min(resto, 1 << 17))
        partes.append(x)
        resto -= x.size
    return (np.concatenate(partes) * np.exp(1j * np.pi / 4)).astype(np.complex64)


def _psd(x, fs, nperseg, noverlap=None, nfft=None, detrend=False):
    """PSD de Welch centrada (f en Hz, un solo lado del espectro original)."""
    from scipy.signal import welch

    nperseg = min(nperseg, x.size)
    f, P = welch(x, fs=fs, nperseg=nperseg,
                 noverlap=nperseg // 2 if noverlap is None else min(noverlap, nperseg - 1),
                 nfft=nfft or nperseg, return_onesided=False, detrend=detrend)
    return np.fft.fftshift(f), np.fft.fftshift(P)


def _ancho_3db(f, P, k=9):
    """Semi-ancho a -3 dB de la PSD normalizada a su maximo (suavizada, k bins)."""
    P = np.convolve(P, np.ones(k) / k, mode="same")
    m = f >= 0
    fp, Pp = f[m], P[m]
    i0 = int(np.argmax(Pp))
    Pdb = 10 * np.log10(Pp / Pp[i0] + 1e-30)
    i = int(np.argmax(Pdb[i0:] < -3)) + i0
    if i == i0:
        return float(fp[-1] - fp[i0])
    return float(fp[i - 1] + (fp[i] - fp[i - 1]) * (-3 - Pdb[i - 1]) / (Pdb[i] - Pdb[i - 1]))


def _sigma(f, P):
    """Ancho RMS (desviacion estandar) de la PSD bilateral.

    Se descuenta el piso de ruido (mediana de la PSD) antes de integrar: sin eso
    el termino f^2 del piso domina la integral y el ancho medido salta entre
    analisis consecutivos de la misma senal.
    """
    P = np.maximum(P - np.median(P), 0.0)
    m0 = P.sum()
    return float(np.sqrt((f ** 2 * P).sum() / m0)) if m0 > 0 else 0.0


def analizar(x, fs):
    """Espectro Doppler de la envolvente y estimacion de fD y Tc.

    Criterio de estimacion: para un espectro Doppler plano de ancho fD, la PSD
    de las fluctuaciones de la envolvente es su autoconvolucion (triangular),
    de varianza sigma^2 = 2 fD^2 / 3.  Por eso se usa fD = sqrt(3/2) * sigma
    (ancho RMS, descontando el piso de ruido), mas estable que el cruce puntual
    de -3 dB con registros cortos.
    """
    from scipy.signal import resample_poly

    L = max(1, int(round(fs / FS_ENV)))
    xd = resample_poly(x, 1, L)
    fsd = fs / L
    r = np.abs(xd)
    f_env, P_env = _psd(r - r.mean(), fsd, 1024, nfft=8192)
    f_iq, P_iq = _psd(xd, fsd, 1024, nfft=8192)
    f_man, P_man = _psd(x, fs, 4096, 2048, 4096)          # metodo del manual
    sigma = _sigma(f_env, P_env)
    fd = float(np.sqrt(1.5) * sigma)
    return {
        "fD_estimado_Hz": fd,
        "Tc_s": 0.423 / fd if fd > 0 else float("inf"),
        "ancho_PSD_Hz": sigma,
        "ancho_3dB_Hz": _ancho_3db(f_env, P_env),
        "ancho_manual_Hz": _ancho_3db(f_man, P_man),
        "n_muestras": int(x.size),
        "t": np.arange(r.size) / fsd,
        "r": r,
        "f_env": f_env,
        "P_env_norm": P_env / P_env.max(),
        "f_iq": f_iq,
        "P_iq_norm": P_iq / P_iq.max(),
    }


def fig_envolventes(res, ruta):
    import matplotlib.pyplot as plt

    ejes = np.atleast_1d(plt.subplots(len(res), 1, figsize=(9, 2.6 * len(res)),
                                      sharex=True)[1])
    for ax, (nombre, d) in zip(ejes, res.items()):
        ax.plot(d["t"], d["r"], lw=0.7)
        ax.set_ylabel("|x(t)|")
        ax.set_title(f"{nombre.capitalize()}: fD ≈ {d['fD_estimado_Hz']:.2f} Hz, "
                     f"Tc ≈ {d['Tc_s']:.3f} s")
        ax.grid(alpha=0.3)
    ejes[-1].set_xlabel("Tiempo (s)")
    ejes[0].figure.suptitle("Variación temporal de la envolvente")
    ejes[0].figure.tight_layout()
    return comun.guardar_fig(ejes[0].figure, ruta, False)


def fig_doppler(res, ruta):
    import matplotlib.pyplot as plt

    ejes = np.atleast_1d(plt.subplots(len(res), 1, figsize=(9, 2.8 * len(res)))[1])
    for ax, (nombre, d) in zip(ejes, res.items()):
        ax.plot(d["f_env"], 10 * np.log10(d["P_env_norm"] + 1e-30), lw=0.7,
                label="PSD envolvente")
        ax.plot(d["f_iq"], 10 * np.log10(d["P_iq_norm"] + 1e-30), lw=0.7,
                ls="--", alpha=0.8, label="PSD IQ (canal)")
        ax.axhline(-3, color="C3", ls="--", lw=0.8, label="-3 dB")
        ax.axvline(d["fD_estimado_Hz"], color="C2", ls=":", lw=1.0,
                   label=f"fD ≈ {d['fD_estimado_Hz']:.2f} Hz")
        limite = 3 * max(d["ancho_PSD_Hz"], 2.0)
        ax.set_xlim(-limite, limite)
        ax.set_ylim(-30, 3)
        ax.set_ylabel("PSD (dB)")
        ax.set_title(f"Espectro Doppler: {nombre}")
        ax.grid(alpha=0.3)
        ax.legend(loc="upper right", fontsize=8)
    ejes[-1].set_xlabel("Frecuencia (Hz)")
    ejes[0].figure.suptitle("Espectro Doppler de la envolvente (normalizado)")
    ejes[0].figure.tight_layout()
    return comun.guardar_fig(ejes[0].figure, ruta, False)


class P5(vivo.Practica):
    titulo = "Practica 5 - Doppler y tiempo de coherencia"
    filas = 2
    alto = [2.0, 1.2, 1.7, 2.0]

    def __init__(self, args):
        super().__init__(args)
        self.dur = float(args.dur)
        self.bloques = []
        self.total = 0
        self.sel = 1                       # arranca en "lento"
        self.res = {}                      # escenario -> resultado fijado
        self.actual = None
        self.ax_env = self.ax_dop = None
        self.l_env = self.l_dop = None
        self._t0 = 0.0

    # -- fuente sintetica ------------------------------------------------
    def generador_sim(self, rate):
        gen = vivo.ruido_plano(rate, fd=FD_ESC[NOMBRES[self.sel]][0])
        estado = {"gen": gen, "esc": NOMBRES[self.sel]}

        def bloque(n):
            if estado["esc"] != NOMBRES[self.sel]:      # cambio de escenario
                estado["gen"] = vivo.ruido_plano(
                    rate, fd=FD_ESC[NOMBRES[self.sel]][0])
                estado["esc"] = NOMBRES[self.sel]
            return (estado["gen"](n) * np.exp(1j * np.pi / 4)).astype(np.complex64)

        return bloque

    @property
    def escenario(self):
        return NOMBRES[self.sel]

    # -- paneles ---------------------------------------------------------
    def ejes(self, fig, gs, inicio):
        self.ax_env = fig.add_subplot(gs[inicio])
        self.ax_env.set_title("Envolvente del canal (ventana movil)",
                              fontsize=9, loc="left")
        self.ax_env.set_xlabel("Tiempo (s)")
        self.ax_env.set_ylabel("|x(t)|")
        self.ax_env.grid(alpha=0.25)
        self.l_env, = self.ax_env.plot([], [], lw=0.7, color="#00e5ff")

        self.ax_dop = fig.add_subplot(gs[inicio + 1])
        self.ax_dop.set_title("Espectro Doppler de la envolvente",
                              fontsize=9, loc="left")
        self.ax_dop.set_xlabel("Frecuencia (Hz)")
        self.ax_dop.set_ylabel("PSD (dB)")
        self.ax_dop.grid(alpha=0.25)
        self.l_dop, = self.ax_dop.plot([], [], lw=0.9, color="#00e5ff",
                                       label="PSD envolvente")
        self.l_iq, = self.ax_dop.plot([], [], lw=0.7, ls="--", color="#ff2975",
                                      label="PSD IQ")
        self.v_fd = self.ax_dop.axvline(0.0, color="#00ff9f", ls=":", lw=1.0)
        self.ax_dop.legend(fontsize=7, loc="upper right")
        return [self.ax_env, self.ax_dop]

    # -- acumulacion y analisis ------------------------------------------
    def _acumular(self, x):
        self.bloques.append(x)
        self.total += x.size
        tope = int(self.dur * self.app.fs)
        while self.bloques and self.total - self.bloques[0].size >= tope:
            self.total -= self.bloques.pop(0).size

    def ventana(self):
        if not self.bloques:
            return np.zeros(2, np.complex64)
        return np.concatenate(self.bloques)[-int(self.dur * self.app.fs):]

    def _analizar_ventana(self):
        x = self.ventana()
        if x.size < 4096:
            return None
        return analizar(x, self.app.fs)

    def _pintar(self, res):
        self.actual = res
        self.l_env.set_data(res["t"], res["r"])
        self.ax_env.set_xlim(0, max(res["t"][-1] if res["t"].size else 1.0, 0.1))
        self.ax_env.set_ylim(0, max(1.5, float(res["r"].max()) * 1.1))
        db = 10 * np.log10(res["P_env_norm"] + 1e-30)
        lim = 3 * max(res["ancho_PSD_Hz"], 2.0)
        self.l_dop.set_data(res["f_env"], db)
        self.l_iq.set_data(res["f_iq"], 10 * np.log10(res["P_iq_norm"] + 1e-30))
        self.ax_dop.set_xlim(-lim, lim)
        self.ax_dop.set_ylim(-30, 3)
        self.v_fd.set_xdata([res["fD_estimado_Hz"]] * 2)
        self.estado = (f"| {self.escenario:8s} fD {res['fD_estimado_Hz']:5.2f} Hz   "
                       f"Tc {res['Tc_s']:.3f} s   "
                       f"medidos {','.join(self.res) or '--'}")
        self.app.reencuadrar()

    def actualizar(self, x, fs, t):
        self._acumular(x)
        if self.cada(1.0):
            res = self._analizar_ventana()
            if res is not None:
                self._pintar(res)

    def tecla(self, ev):
        if ev.key in ("1", "2", "3") and int(ev.key) <= len(NOMBRES):
            self.sel = int(ev.key) - 1
            self.bloques, self.total = [], 0
            self.estado = f"| {self.escenario}: cambia el escenario y camina"
        elif ev.key == " ":
            res = self._analizar_ventana()
            if res is not None:
                self.res[self.escenario] = res
                self._pintar(res)
        elif ev.key in ("r", "R"):
            self.res, self.bloques, self.total = {}, [], 0
            for l in (self.l_env, self.l_dop, self.l_iq):
                l.set_data([], [])

    def ayuda(self):
        return "1 estatico  2 lento  3 rapido  ESPACIO medir"

    # -- entregables -----------------------------------------------------
    def guardar(self):
        res = dict(self.res)
        if self.actual is not None:
            res.setdefault(self.escenario, self.actual)
        if not res:
            print("sin mediciones: pulsa ESPACIO en cada escenario")
            return []
        rutas = [fig_envolventes(res, FIGS / "envolventes.png"),
                 fig_doppler(res, FIGS / "doppler.png")]
        rutas.append(comun.guardar_json(
            DATOS / "resultados.json",
            modo="simulacion" if self.args.sim else "real",
            frecuencia_Hz=self.freq, rate_Hz=self.app.fs, dur_s=self.dur,
            escenarios={n: {k: v for k, v in d.items()
                            if not isinstance(v, np.ndarray)}
                        for n, d in res.items()}))
        filas = [[n.capitalize(), f"{d['fD_estimado_Hz']:.2f}",
                  f"{d['Tc_s']:.3f}", f"{d['ancho_PSD_Hz']:.2f}"]
                 for n, d in res.items()]
        print(comun.tabla_markdown(["Escenario", "fD (Hz)", "Tc (s)",
                                    "Ancho PSD (Hz)"], filas))
        manual = ", ".join(f"{n}: {d['ancho_manual_Hz']:.1f}" for n, d in res.items())
        print(f"PSD IQ a fs (metodo del manual): ancho a -3 dB = {manual} Hz; "
              f"resolucion {self.app.fs / 4096:.1f} Hz, insuficiente para fD de "
              f"pocos Hz; el espectro Doppler se calcula sobre la envolvente "
              f"decimada a {FS_ENV:.0f} Hz")
        return rutas


def selftest():
    x = simular(3.0, 240e3, 5.0)
    fd = analizar(x, 240e3)["fD_estimado_Hz"]
    assert 1.5 < fd < 6.0, fd
    print("practica5 selftest OK")


def main(argv=None):
    args = vivo.parser(
        __doc__, freq=433.9e6, rate=240e3,
        mas=[("--dur", dict(type=float, default=5.0,
                            help="ventana movil de analisis (s)")),
             ("--selftest", dict(action="store_true"))]).parse_args(argv)
    if args.selftest:
        selftest()
        return 0
    return vivo.correr(P5(args), args)


if __name__ == "__main__":
    sys.exit(main())
