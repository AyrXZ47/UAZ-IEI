#!/usr/bin/env python3
"""Practica 6. Caracterizacion experimental de canales selectivos en frecuencia.

Una sola ventana en vivo: espectro y cascada del canal, la PSD normalizada de
cada escenario capturado y su funcion de correlacion en frecuencia con los
umbrales 0.9 y 0.5. Captura el escenario LOS o NLOS en un entorno interior y
compara el ancho de banda de coherencia entre ambos.

Procedimiento:
    1. Pulsa 1 para el escenario LOS o 2 para el NLOS.
    2. Pulsa ESPACIO para capturar los ultimos `--n` IQ y analizarlos.
    3. Repite con el otro escenario; ambas curvas quedan superpuestas.
    4. Pulsa s para guardar figuras y JSON del reporte.

Uso:
    python3 practica6.py                     # capturas reales LOS y NLOS
    python3 practica6.py -f 915e6 -n 524288  # otra frecuencia y captura mas larga
    python3 practica6.py --sim               # canal de 2 rayos, sin dongle
    python3 practica6.py --selftest          # verifica el analisis sin dongle
Teclas:  1 LOS   2 NLOS   ESPACIO capturar   r reiniciar   s guardar   q salir
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
NPERSEG = 4096
LOS = {"tau": 0.05e-6, "a": 0.5}
NLOS = {"tau": 0.5e-6, "a": 0.9}
PHI_LOS = 3 * np.pi / 4


def simular(fs, n, tau, a, phi=None, snr_db=25.0, seed=None):
    """Señal de banda ancha (ruido blanco complejo) tras un canal de 2 rayos.

    h = [1, a·e^{jφ}] con retardo τ; como τ puede ser menor que 1/fs, el canal
    se aplica en frecuencia (H(f) = 1 + a·e^{j(φ-2πfτ)}), no con dos taps.
    """
    rng = np.random.default_rng(seed)
    if phi is None:
        phi = rng.uniform(0, 2 * np.pi)
    x = (rng.standard_normal(n) + 1j * rng.standard_normal(n)) / np.sqrt(2)
    f = np.fft.fftfreq(n, 1 / fs)
    H = 1 + a * np.exp(1j * (phi - 2 * np.pi * f * tau))
    y = np.fft.ifft(np.fft.fft(x) * H)
    ruido = np.sqrt(1 + a ** 2) * 10 ** (-snr_db / 20)
    y += ruido * (rng.standard_normal(n) + 1j * rng.standard_normal(n)) / np.sqrt(2)
    return y.astype(np.complex64)


def capturar_sim(fs, n, seed=None):
    """Escenarios simulados LOS (φ fija) y NLOS (φ aleatoria)."""
    return {"LOS": simular(fs, n, LOS["tau"], LOS["a"], phi=PHI_LOS, seed=seed),
            "NLOS": simular(fs, n, NLOS["tau"], NLOS["a"], seed=seed)}


def ancho_coherencia(R, lags, umbral):
    """Ancho (Hz) de la región contigua alrededor de lag 0 con R > umbral."""
    c = R.size // 2
    sobre = R > umbral
    i = j = c
    while i > 0 and sobre[i - 1]:
        i -= 1
    while j < R.size - 1 and sobre[j + 1]:
        j += 1
    return float(lags[j] - lags[i])


def analizar(x, fs):
    """PSD normalizada, correlación en frecuencia y métricas del escenario."""
    from scipy import signal as sig

    f, P = comun.espectro(x, fs, nperseg=NPERSEG)
    psd = P / P.max()
    psd_db = 10 * np.log10(psd + 1e-20)
    v = psd - psd.mean()
    R = sig.correlate(v, v, "full")
    R = R / R.max()
    lags = sig.correlation_lags(v.size, v.size, "full") * (f[1] - f[0])
    return {
        "f": f,
        "psd_db": psd_db,
        "R": R,
        "lags_Hz": lags,
        "potencia_dB": float(comun.potencia_dbfs(x)),
        "variacion_espectral_dB": float(np.std(psd_db)),
        "Bc_90_Hz": ancho_coherencia(R, lags, 0.9),
        "Bc_50_Hz": ancho_coherencia(R, lags, 0.5),
    }


def fig_psd(res, ruta):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(9, 5))
    for esc, r in res.items():
        ax.plot(r["f"] / 1e6, r["psd_db"], lw=0.7, label=esc)
    ax.set_xlabel("Frecuencia (MHz)")
    ax.set_ylabel("PSD normalizada (dB)")
    ax.set_title("Respuesta espectral del canal")
    ax.legend()
    ax.grid(alpha=0.3)
    return comun.guardar_fig(fig, ruta, False)


def fig_correlacion(res, ruta):
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5), sharey=True)
    for ax, (esc, r) in zip(axes, res.items()):
        b50 = r["Bc_50_Hz"]
        ax.plot(r["lags_Hz"] / 1e3, r["R"], lw=0.8, label="Correlación")
        ax.axhline(0.9, color="C1", ls="--", lw=0.8, label="Umbral 0.9")
        ax.axhline(0.5, color="C2", ls="--", lw=0.8, label="Umbral 0.5")
        ax.axvspan(-b50 / 2e3, b50 / 2e3, color="C2", alpha=0.12)
        ax.text(0, 0.15, f"Bc(0.9) = {r['Bc_90_Hz']/1e3:.1f} kHz\n"
                         f"Bc(0.5) = {b50/1e3:.1f} kHz",
                ha="center", fontsize=9)
        ax.set_title(esc)
        ax.set_xlabel("Lag de frecuencia (kHz)")
        ax.grid(alpha=0.3)
    axes[0].set_ylabel("Correlación normalizada")
    axes[0].legend(loc="upper right", fontsize=8)
    fig.suptitle("Función de correlación en frecuencia")
    fig.tight_layout()
    return comun.guardar_fig(fig, ruta, False)


class P6(vivo.Practica):
    titulo = "Practica 6 - canales selectivos"
    filas = 2
    alto = [2.2, 1.6, 1.7, 1.7]

    def __init__(self, args):
        super().__init__(args)
        self.n = int(args.n)
        self.bloques = []
        self.total = 0
        self.escenario = "LOS"
        self.res = {}
        self.ax_psd = self.ax_corr = None
        self.lineas_psd = {}
        self.lineas_corr = {}
        self._demo = 0
        self.estado = self._texto()

    # -- paneles ---------------------------------------------------------
    def ejes(self, fig, gs, inicio):
        self.ax_psd = fig.add_subplot(gs[inicio])
        self.ax_psd.set_title("PSD normalizada del canal", fontsize=9, loc="left")
        self.ax_psd.set_xlabel("Frecuencia (MHz)")
        self.ax_psd.set_ylabel("PSD (dB)")
        self.ax_psd.grid(alpha=0.25)
        for esc in ("LOS", "NLOS"):
            self.lineas_psd[esc], = self.ax_psd.plot([], [], lw=0.7, label=esc)
        self.ax_psd.legend(fontsize=7, loc="upper right")

        self.ax_corr = fig.add_subplot(gs[inicio + 1])
        self.ax_corr.set_title("Correlación en frecuencia", fontsize=9, loc="left")
        self.ax_corr.set_xlabel("Lag de frecuencia (kHz)")
        self.ax_corr.set_ylabel("R normalizada")
        self.ax_corr.grid(alpha=0.25)
        self.ax_corr.set_ylim(-0.2, 1.05)
        self.ax_corr.axhline(0.9, color="#ff2975", ls="--", lw=0.8,
                             label="Umbral 0.9")
        self.ax_corr.axhline(0.5, color="#00e5ff", ls="--", lw=0.8,
                             label="Umbral 0.5")
        for esc in ("LOS", "NLOS"):
            self.lineas_corr[esc], = self.ax_corr.plot([], [], lw=0.8, label=esc)
        self.ax_corr.legend(fontsize=7, loc="upper right")
        return [self.ax_psd, self.ax_corr]

    # -- acumulacion y captura ------------------------------------------
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

    def _texto(self):
        partes = []
        for esc in ("LOS", "NLOS"):
            r = self.res.get(esc)
            if r is None:
                continue
            partes.append(f"{esc} P {r['potencia_dB']:.1f} dB "
                          f"var {r['variacion_espectral_dB']:.1f} dB "
                          f"Bc90 {r['Bc_90_Hz']/1e3:.1f} kHz "
                          f"Bc50 {r['Bc_50_Hz']/1e3:.1f} kHz")
        return f"| esc {self.escenario}  " + (" | ".join(partes) or "sin capturas")

    def _reencuadrar(self):
        if self.res:
            ys = [r["psd_db"] for r in self.res.values()]
            self.ax_psd.set_ylim(min(y.min() for y in ys) - 3,
                                 max(y.max() for y in ys) + 3)
            b50 = max(r["Bc_50_Hz"] for r in self.res.values())
            medio = max(2.0 * b50, 5e3) / 1e3
            self.ax_corr.set_xlim(-medio, medio)
        self.estado = self._texto()
        if self.app is not None:
            self.app.reencuadrar()

    def _medir(self, esc, x):
        r = analizar(x, self.app.fs)
        self.res[esc] = r
        self.lineas_psd[esc].set_data(r["f"] / 1e6, r["psd_db"])
        self.lineas_corr[esc].set_data(r["lags_Hz"] / 1e3, r["R"])
        self._reencuadrar()

    # -- lazo ------------------------------------------------------------
    def actualizar(self, x, fs, t):
        self._acumular(x)
        if self.args.sim and self.cada(2.0):
            esc = "LOS" if self._demo % 2 == 0 else "NLOS"
            self._medir(esc, capturar_sim(fs, self.n, seed=self._demo)[esc])
            self._demo += 1

    def tecla(self, ev):
        if ev.key == "1":
            self.escenario = "LOS"
            self.estado = self._texto()
        elif ev.key == "2":
            self.escenario = "NLOS"
            self.estado = self._texto()
        elif ev.key == " ":
            if self.args.sim:
                x = capturar_sim(self.app.fs, self.n, seed=self._demo)[self.escenario]
                self._demo += 1
            else:
                x = self.captura()
            self._medir(self.escenario, x)
        elif ev.key in ("r", "R"):
            self.res = {}
            for l in list(self.lineas_psd.values()) + list(self.lineas_corr.values()):
                l.set_data([], [])
            self._reencuadrar()

    def ayuda(self):
        return "1 LOS   2 NLOS   ESPACIO capturar   r reiniciar"

    # -- entregables -----------------------------------------------------
    def guardar(self):
        if not self.res:
            print("sin capturas: pulsa ESPACIO en al menos un escenario")
            return []
        rutas = [fig_psd(self.res, FIGS / "psd_los_nlos.png"),
                 fig_correlacion(self.res, FIGS / "correlacion.png")]
        rutas.append(comun.guardar_json(
            DATOS / "resultados.json",
            **{esc: {k: r[k] for k in ("potencia_dB", "variacion_espectral_dB",
                                       "Bc_90_Hz", "Bc_50_Hz")}
               for esc, r in self.res.items()},
            modo="simulacion" if self.args.sim else "real"))
        filas = [[esc, f"{r['potencia_dB']:.2f}",
                  f"{r['variacion_espectral_dB']:.2f}",
                  f"{r['Bc_90_Hz']/1e3:.1f} kHz", f"{r['Bc_50_Hz']/1e3:.1f} kHz"]
                 for esc, r in self.res.items()]
        print(comun.tabla_markdown(["Escenario", "Potencia (dB)",
                                    "Variación espectral (dB)", "Bc 0.9", "Bc 0.5"],
                                   filas))
        return rutas


def selftest():
    fs, n = comun.RATE_DEF, 1 << 20
    res = {esc: analizar(x, fs) for esc, x in capturar_sim(fs, n, seed=0).items()}
    assert res["NLOS"]["Bc_50_Hz"] < res["LOS"]["Bc_50_Hz"], \
        (res["LOS"]["Bc_50_Hz"], res["NLOS"]["Bc_50_Hz"])
    assert 100e3 < res["NLOS"]["Bc_50_Hz"] < 2e6, res["NLOS"]["Bc_50_Hz"]
    print("practica6 selftest OK")


def main(argv=None):
    args = vivo.parser(
        __doc__, freq=433.9e6,
        mas=[(("-n", "--n"), dict(type=int, default=262144,
                                  help="muestras IQ por captura")),
             ("--selftest", dict(action="store_true"))]).parse_args(argv)
    if args.selftest:
        selftest()
        return 0
    return vivo.correr(P6(args), args)


if __name__ == "__main__":
    sys.exit(main())
