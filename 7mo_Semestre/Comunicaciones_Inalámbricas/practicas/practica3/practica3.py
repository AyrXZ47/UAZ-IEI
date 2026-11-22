#!/usr/bin/env python3
"""Practica 3. Caracterizacion experimental del shadowing log-normal.

Una sola ventana en vivo: espectro y cascada del canal, la serie de potencias
medidas y su histograma con el ajuste gaussiano, todo actualizandose con cada
medicion.  Se estima mu, sigma sigma del shadowing y la normalidad (Shapiro-Wilk).

Procedimiento:
    1. Deja el transmisor fijo a ~10 m y conserva esa distancia.
    2. Pulsa ESPACIO en cada posicion nueva (pasillo, pared, puerta, con gente).
    3. Pulsa s para guardar figuras, CSV y JSON del reporte.

Uso:
    python3 practica3.py                       # 433.9 MHz, distancia 10 m
    python3 practica3.py -d 15 -f 915e6        # otra distancia / frecuencia
    python3 practica3.py --sim                 # demo automatica, sin dongle
    python3 practica3.py --selftest            # verifica el analisis sin dongle
Teclas:  ESPACIO medir   r reiniciar   s guardar   q salir
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


def medir_sim(nmed, mu=-50.0, sigma=6.0, seed=0):
    return np.random.default_rng(seed).normal(mu, sigma, nmed)


def analizar(Pr):
    from scipy import stats

    n = Pr.size
    mu, sigma = float(np.mean(Pr)), float(np.std(Pr, ddof=1))
    mu_fit, sigma_fit = (float(v) for v in stats.norm.fit(Pr))
    p = float(stats.shapiro(Pr).pvalue) if n >= 3 else float("nan")
    se = sigma / np.sqrt(2 * (n - 1)) if n > 1 else float("nan")
    return {"mu": mu, "sigma": sigma, "mu_fit": mu_fit, "sigma_fit": sigma_fit,
            "p_valor_normalidad": p,
            "sigma_ic95": [sigma - 1.96 * se, sigma + 1.96 * se]}


def entorno_de(sigma):
    for lim, nombre in ((4, "espacio libre"), (6, "interior con poca obstruccion"),
                        (8, "exterior urbano"), (12, "interior de oficinas")):
        if sigma <= lim:
            return nombre
    return "entorno industrial"


def fig_variacion(Pr, ruta):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(np.arange(1, Pr.size + 1), Pr, "o-", ms=4)
    ax.set_xlabel("Medición")
    ax.set_ylabel("Potencia (dB)")
    ax.set_title("Variación de potencia recibida")
    ax.grid(alpha=0.3)
    return comun.guardar_fig(fig, ruta, False)


def fig_histograma(Pr, mu_fit, sigma_fit, ruta):
    import matplotlib.pyplot as plt
    from scipy import stats

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.hist(Pr, bins=10, density=True, alpha=0.7, label="Mediciones")
    x = np.linspace(Pr.min() - sigma_fit, Pr.max() + sigma_fit, 200)
    ax.plot(x, stats.norm.pdf(x, mu_fit, sigma_fit), lw=2, label="Ajuste gaussiano")
    ax.set_xlabel("Potencia (dB)")
    ax.set_ylabel("Densidad")
    ax.set_title("Modelo gaussiano del shadowing")
    ax.grid(alpha=0.3)
    ax.legend()
    return comun.guardar_fig(fig, ruta, False)


class P3(vivo.Practica):
    titulo = "Practica 3 - shadowing log-normal"
    filas = 2
    alto = [2.2, 1.3, 1.8, 1.9]

    def __init__(self, args):
        super().__init__(args)
        self.distancia = float(args.distancia)
        self.nmax = int(args.nmed)
        self.Pr = []
        self.res = None
        self.ax_serie = self.ax_hist = None
        self.l_serie = self.l_hist = self.l_pdf = None
        self._demo = 0

    def ejes(self, fig, gs, inicio):
        self.ax_serie = fig.add_subplot(gs[inicio])
        self.ax_serie.set_xlabel("Medicion")
        self.ax_serie.set_ylabel("P (dBFS)")
        self.ax_serie.set_title(f"Potencia recibida a {self.distancia:g} m",
                                fontsize=9, loc="left")
        self.ax_serie.grid(alpha=0.25)
        self.ax_serie.set_xlim(1, max(10, self.nmax))
        self.l_serie, = self.ax_serie.plot([], [], "o-", ms=4, lw=0.9)

        self.ax_hist = fig.add_subplot(gs[inicio + 1])
        self.ax_hist.set_xlabel("Potencia (dBFS)")
        self.ax_hist.set_ylabel("Densidad")
        self.ax_hist.set_title("Histograma y ajuste gaussiano (shadowing)",
                               fontsize=9, loc="left")
        self.ax_hist.grid(alpha=0.25)
        self.l_hist, = self.ax_hist.plot([], [], drawstyle="steps-mid", lw=1.2,
                                         label="Mediciones")
        self.l_pdf, = self.ax_hist.plot([], [], lw=1.8, label="N(mu, sigma)")
        self.ax_hist.legend(fontsize=7, loc="upper right")
        return [self.ax_serie, self.ax_hist]

    def registrar(self, pot_db):
        if len(self.Pr) < 2000:
            self.Pr.append(float(pot_db))
        self._refrescar()

    def _refrescar(self):
        from scipy import stats

        Pr = np.array(self.Pr)
        self.l_serie.set_data(np.arange(1, Pr.size + 1), Pr)
        if Pr.size >= 3:
            self.res = analizar(Pr)
            lo, hi = Pr.min() - 1, Pr.max() + 1
            dens, bordes = np.histogram(Pr, bins=10, range=(lo, hi), density=True)
            self.l_hist.set_data((bordes[:-1] + bordes[1:]) / 2, dens)
            x = np.linspace(lo, hi, 200)
            self.l_pdf.set_data(x, stats.norm.pdf(x, self.res["mu_fit"],
                                                  self.res["sigma_fit"]))
            self.ax_hist.set_xlim(lo, hi)
            self.ax_hist.set_ylim(0, max(dens.max(), 1e-3) * 1.35)
            self.ax_serie.set_xlim(1, max(10, Pr.size + 1))
            self.ax_serie.set_ylim(Pr.min() - 4, Pr.max() + 4)
            self.estado = (f"| N {Pr.size:3d}   mu {self.res['mu']:6.2f} dB   "
                           f"sigma {self.res['sigma']:5.2f} dB   "
                           f"p {self.res['p_valor_normalidad']:.2f}")
        else:
            self.estado = f"| N {Pr.size:3d}   (necesita 3 mediciones)"
        if self.app is not None:
            self.app.reencuadrar()

    def actualizar(self, x, fs, t):
        if self.args.sim and self.cada(0.5) and len(self.Pr) < self.nmax:
            self.registrar(medir_sim(1, seed=self._demo)[0])
            self._demo += 1
        elif not self.args.sim:
            extra = (f"   mu {self.res['mu']:.1f} dB" if self.res else "")
            self.estado = (f"| N {len(self.Pr):3d}   "
                           f"P {comun.potencia_dbfs(x):6.2f} dBFS{extra}")

    def tecla(self, ev):
        if ev.key == " ":
            if self.args.sim:
                self.registrar(medir_sim(1, seed=self._demo)[0])
                self._demo += 1
            else:
                self.registrar(comun.potencia_dbfs(self.app.fuente.ultimo))
        elif ev.key in ("r", "R"):
            self.Pr, self.res = [], None
            for l in (self.l_serie, self.l_hist, self.l_pdf):
                l.set_data([], [])
            self._refrescar()

    def ayuda(self):
        return "ESPACIO medir   r reiniciar"

    def guardar(self):
        Pr = np.array(self.Pr)
        if Pr.size < 3:
            print("faltan mediciones: usa ESPACIO al menos 3 veces")
            return []
        res = analizar(Pr)
        DATOS.mkdir(parents=True, exist_ok=True)
        np.savetxt(DATOS / "mediciones.csv", np.c_[np.arange(1, Pr.size + 1), Pr],
                   delimiter=",", header="indice,potencia_dB", comments="",
                   fmt=["%d", "%.4f"])
        rutas = [fig_variacion(Pr, FIGS / "variacion.png"),
                 fig_histograma(Pr, res["mu_fit"], res["sigma_fit"],
                                FIGS / "histograma.png")]
        rutas.append(comun.guardar_json(
            DATOS / "resultados.json", n=int(Pr.size), distancia=self.distancia,
            mu=res["mu"], sigma=res["sigma"], mu_fit=res["mu_fit"],
            sigma_fit=res["sigma_fit"], p_valor_normalidad=res["p_valor_normalidad"],
            sigma_ic95=res["sigma_ic95"],
            modo="simulacion" if self.args.sim else "real"))
        print(f"Prueba de normalidad (Shapiro-Wilk): p = "
              f"{res['p_valor_normalidad']:.4f}")
        print(f"IC 95 % aprox. para sigma: [{res['sigma_ic95'][0]:.2f}, "
              f"{res['sigma_ic95'][1]:.2f}] dB")
        print(comun.tabla_markdown(["Parámetro", "Valor"], [
            ["Media µ (dB)", f"{res['mu']:.2f}"],
            ["Desviación σ (dB)", f"{res['sigma']:.2f}"],
            ["N mediciones", int(Pr.size)],
            ["Entorno", entorno_de(res["sigma"])]]))
        return rutas


def selftest():
    Pr = medir_sim(5000, seed=1)
    mu, sigma = np.mean(Pr), np.std(Pr, ddof=1)
    assert abs(sigma - 6) < 1.5, sigma
    assert abs(mu + 50) < 2, mu
    print("practica3 selftest OK")


def main(argv=None):
    args = vivo.parser(
        __doc__, freq=433.9e6,
        mas=[(("-d", "--distancia"), dict(type=float, default=10.0)),
             (("-n", "--nmed"), dict(type=int, default=50,
                                     help="mediciones de la demo --sim")),
             ("--selftest", dict(action="store_true"))]).parse_args(argv)
    if args.selftest:
        selftest()
        return 0
    return vivo.correr(P3(args), args)


if __name__ == "__main__":
    sys.exit(main())
