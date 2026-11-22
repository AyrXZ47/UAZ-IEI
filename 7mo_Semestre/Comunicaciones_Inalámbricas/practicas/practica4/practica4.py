#!/usr/bin/env python3
"""Practica 4. Caracterizacion experimental del desvanecimiento Rayleigh.

Una sola ventana en vivo: espectro y cascada del canal, la envolvente
normalizada de los ultimos segundos y su histograma con el ajuste Rayleigh.
Mientras caminas ves el desvanecimiento en tiempo real; ESPACIO lo congela.

Procedimiento:
    1. Deja el transmisor fijo y camina con el receptor (paredes, puertas, muebles).
    2. Observa las caidas de la envolvente y el porcentaje de fading profundo.
    3. Pulsa ESPACIO cuando la ventana capturada te sirva como medicion.
    4. Pulsa s para guardar figuras y JSON del reporte.

Uso:
    python3 practica4.py                       # 433.9 MHz, ventana de 2 s
    python3 practica4.py -f 915e6 --dur 5 --umbral 0.5
    python3 practica4.py --sim                 # Rayleigh sintetico con fd=10 Hz
    python3 practica4.py --selftest            # verifica el analisis sin dongle
Teclas:  ESPACIO fijar/descongelar   r reiniciar   s guardar   q salir
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


def analizar(r, umbral):
    """Media, desviacion, sigma Rayleigh y porcentaje de fading profundo."""
    from scipy.stats import rayleigh

    sigma = float(rayleigh.fit(r, floc=0)[1])
    pct = 100.0 * np.mean(r < umbral)
    pct_teo = 100.0 * (1.0 - np.exp(-umbral ** 2 / (2 * sigma ** 2)))
    return {"media": float(np.mean(r)), "std": float(np.std(r)), "sigma": sigma,
            "porcentaje_profundo": float(pct), "porcentaje_teorico": float(pct_teo)}


def fig_envolvente(r, umbral, ruta):
    import matplotlib.pyplot as plt

    paso = max(1, r.size // 4000)
    rd, x = r[::paso], np.arange(0, r.size, paso)
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(x, rd, lw=0.6)
    ax.axhline(umbral, color="C3", ls="--", lw=1.5, label=f"Umbral = {umbral}")
    ax.set_xlabel("Muestra")
    ax.set_ylabel("Amplitud")
    ax.set_title("Envolvente de la señal recibida")
    ax.grid(alpha=0.3)
    ax.legend()
    return comun.guardar_fig(fig, ruta, False)


def fig_histograma(r, sigma, ruta):
    import matplotlib.pyplot as plt
    from scipy.stats import rayleigh

    x = np.linspace(0, np.max(r), 200)
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.hist(r, bins=100, density=True, alpha=0.6, label="Experimental")
    ax.plot(x, rayleigh.pdf(x, scale=sigma), lw=2, label="Modelo Rayleigh")
    ax.set_xlabel("Amplitud")
    ax.set_ylabel("Densidad")
    ax.set_title("Ajuste Rayleigh")
    ax.grid(alpha=0.3)
    ax.legend()
    return comun.guardar_fig(fig, ruta, False)


class P4(vivo.Practica):
    titulo = "Practica 4 - desvanecimiento Rayleigh"
    filas = 2
    alto = [2.0, 1.2, 1.9, 1.9]

    def __init__(self, args):
        super().__init__(args)
        self.dur = float(args.dur)
        self.umbral = float(args.umbral)
        self.dec = max(1, int(round(args.rate / 2400.0)))
        self.bloques = []
        self.total = 0
        self.fijado = False
        self.res = None
        self.ax_env = self.ax_hist = None
        self.l_env = self.l_hist = self.l_pdf = None

    # -- fuente sintetica ------------------------------------------------
    def generador_sim(self, rate):
        return vivo.rayleigh_sim(rate, fd=self.args.fd, los=self.args.los)

    # -- paneles ---------------------------------------------------------
    def ejes(self, fig, gs, inicio):
        self.ax_env = fig.add_subplot(gs[inicio])
        self.ax_env.set_title("Envolvente normalizada (ventana movil)",
                             fontsize=9, loc="left")
        self.ax_env.set_xlabel("Tiempo (s)")
        self.ax_env.set_ylabel("|x| / rms")
        self.ax_env.grid(alpha=0.25)
        self.ax_env.set_ylim(0, 3)
        self.umbral_linea = self.ax_env.axhline(self.umbral, color="#ff2975",
                                                ls="--", lw=1.0)
        self.l_env, = self.ax_env.plot([], [], lw=0.7, color="#00e5ff")

        self.ax_hist = fig.add_subplot(gs[inicio + 1])
        self.ax_hist.set_title("Histograma y ajuste Rayleigh", fontsize=9, loc="left")
        self.ax_hist.set_xlabel("Amplitud")
        self.ax_hist.set_ylabel("Densidad")
        self.ax_hist.grid(alpha=0.25)
        self.ax_hist.set_xlim(0, 3)
        self.l_hist, = self.ax_hist.plot([], [], drawstyle="steps-mid", lw=1.1,
                                         label="Experimental")
        self.l_pdf, = self.ax_hist.plot([], [], lw=1.8, label="Rayleigh")
        self.ax_hist.legend(fontsize=7, loc="upper right")
        return [self.ax_env, self.ax_hist]

    @property
    def fs(self):
        return self.app.fs if self.app is not None else self.args.rate

    # -- acumulacion -----------------------------------------------------
    def _acumular(self, x):
        r = np.abs(x)[::self.dec]
        self.bloques.append(r)
        self.total += r.size
        tope = int(self.dur * self.fs / self.dec)
        while self.bloques and self.total - self.bloques[0].size >= tope:
            self.total -= self.bloques.pop(0).size

    def ventana(self):
        if not self.bloques:
            return np.zeros(1)
        r = np.concatenate(self.bloques)
        return r / np.sqrt(np.mean(r ** 2) + 1e-20)

    def _refrescar(self):
        from scipy.stats import rayleigh

        r = self.ventana()
        self.res = analizar(r, self.umbral)
        paso = max(1, r.size // 3000)
        t = np.arange(0, r.size, paso) * self.dec / self.fs
        self.l_env.set_data(t, r[::paso])
        self.ax_env.set_xlim(0, max(t[-1] if t.size else 1.0, 0.1))
        lo, hi = 0.0, min(max(3.0, float(r.max()) * 1.1), 6.0)
        dens, bordes = np.histogram(np.clip(r, 0, hi), bins=40, range=(lo, hi),
                                    density=True)
        self.l_hist.set_data((bordes[:-1] + bordes[1:]) / 2, dens)
        x = np.linspace(0, hi, 200)
        self.l_pdf.set_data(x, rayleigh.pdf(x, scale=self.res["sigma"]))
        self.ax_hist.set_xlim(lo, hi)
        self.ax_hist.set_ylim(0, max(dens.max(), 1e-3) * 1.35)
        self.estado = (f"| {'FIJADO ' if self.fijado else ''}N {r.size:6d}   "
                       f"sigma {self.res['sigma']:.3f}   "
                       f"profundo {self.res['porcentaje_profundo']:5.2f} %   "
                       f"teorico {self.res['porcentaje_teorico']:5.2f} %")
        if self.app is not None:
            self.app.reencuadrar()

    # -- lazo ------------------------------------------------------------
    def actualizar(self, x, fs, t):
        if not self.fijado:
            self._acumular(x)
            if self.cada(0.35):
                self._refrescar()

    def tecla(self, ev):
        if ev.key == " ":
            self.fijado = not self.fijado
            self._refrescar()
        elif ev.key in ("r", "R"):
            self.bloques, self.total, self.fijado = [], 0, False
            for l in (self.l_env, self.l_hist, self.l_pdf):
                l.set_data([], [])

    def ayuda(self):
        return "ESPACIO fijar/descongelar   r reiniciar"

    # -- entregables -----------------------------------------------------
    def guardar(self):
        r = self.ventana()
        if r.size < 1000:
            print("ventana demasiado corta: espera unos segundos")
            return []
        res = analizar(r, self.umbral)
        rutas = [fig_envolvente(r, self.umbral, FIGS / "envolvente.png"),
                 fig_histograma(r, res["sigma"], FIGS / "histograma_rayleigh.png")]
        rutas.append(comun.guardar_json(
            DATOS / "resultados.json", frecuencia=self.freq, n_muestras=int(r.size),
            media=res["media"], std=res["std"], sigma_rayleigh=res["sigma"],
            umbral=self.umbral, porcentaje_profundo=res["porcentaje_profundo"],
            porcentaje_teorico=res["porcentaje_teorico"],
            modo="simulacion" if self.args.sim else "real"))
        print(comun.tabla_markdown(
            ["Frecuencia", "Muestras", "Media", "Desviación", "Fading profundo"],
            [[f"{self.freq/1e6:.3f} MHz", r.size, f"{res['media']:.4f}",
              f"{res['std']:.4f}", f"{res['porcentaje_profundo']:.2f} %"]]))
        print(f"sigma Rayleigh ajustado : {res['sigma']:.4f}")
        print(f"fading profundo teorico : {res['porcentaje_teorico']:.2f} %")
        return rutas


def selftest():
    from scipy.stats import rayleigh

    r = rayleigh.rvs(scale=1 / np.sqrt(2), size=200000, random_state=0)
    r = r / np.sqrt(np.mean(r ** 2))
    pct = 100.0 * np.mean(r < 0.5)
    sigma = float(rayleigh.fit(r, floc=0)[1])
    assert 18.0 < pct < 26.0, pct
    assert abs(sigma - 1 / np.sqrt(2)) < 0.05, sigma
    print("practica4 selftest OK")


def main(argv=None):
    args = vivo.parser(
        __doc__, freq=433.9e6,
        mas=[("--dur", dict(type=float, default=2.0,
                            help="ventana movil de analisis (s)")),
             ("--umbral", dict(type=float, default=0.5,
                               help="umbral de desvanecimiento profundo")),
             ("--fd", dict(type=float, default=10.0,
                           help="Doppler maximo de la simulacion (Hz)")),
             ("--los", dict(type=float, default=0.0,
                            help="componente LOS de la simulacion")),
             ("--selftest", dict(action="store_true"))]).parse_args(argv)
    if args.selftest:
        selftest()
        return 0
    return vivo.correr(P4(args), args)


if __name__ == "__main__":
    sys.exit(main())
