#!/usr/bin/env python3
"""Practica 2. Medicion experimental de perdidas por trayectoria (path loss).

Una sola ventana en vivo: espectro y cascada del canal, mas la curva de
potencia contra distancia y sus residuales actualizandose con cada medicion.
El modelo  P(d) = P0 - 10*n*log10(d/d0) + X_sigma  se ajusta por minimos
cuadrados en cuanto hay dos distancias medidas.

Procedimiento:
    1. Deja el transmisor fijo y lleva el receptor a la distancia 1.
    2. Pulsa la tecla de esa distancia (1..6) para seleccionarla.
    3. Pulsa ESPACIO para registrar una medicion; repite 10 veces por distancia.
    4. Pulsa s para guardar figuras, CSV y JSON del reporte.

Uso:
    python3 practica2.py                          # transmisor en 433.9 MHz
    python3 practica2.py -f 915e6 --distancias 1,2,5,10
    python3 practica2.py --sim                    # demo automatica, sin dongle
    python3 practica2.py --selftest               # verifica el ajuste sin dongle
Teclas:  1..6 distancia   ESPACIO medir   r reiniciar   s guardar   q salir
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

P0_SIM = -40.0        # potencia recibida a 1 m en la simulacion (dB)
N_REAL_SIM = 3.2      # exponente de perdidas del entorno simulado
SIGMA_SIM = 4.0       # desviacion del shadowing log-normal (dB)


def simular(distancias, nmed, p0=P0_SIM, n_real=N_REAL_SIM, sigma=SIGMA_SIM, seed=0):
    """Potencia por bloque en dB: modelo logaritmico + shadowing log-normal."""
    rng = np.random.default_rng(seed)
    d = np.asarray(distancias, float)
    return p0 - 10.0 * n_real * np.log10(d)[:, None] + rng.normal(0.0, sigma, (d.size, nmed))


def ajustar(distancias, Pr_dB):
    """Ajuste lineal de Pr(dB) contra log10(d); n = -pendiente/10."""
    x = np.log10(np.asarray(distancias, float))
    p = np.polyfit(x, Pr_dB, 1)
    Pr_aj = np.polyval(p, x)
    res = Pr_dB - Pr_aj
    r2 = 1.0 - np.sum(res ** 2) / np.sum((Pr_dB - Pr_dB.mean()) ** 2)
    return {"pendiente": float(p[0]), "intercepto": float(p[1]), "n": -p[0] / 10.0,
            "r2": float(r2), "residuales": res, "sigma_res": float(res.std()),
            "Pr_ajuste": Pr_aj}


def guardar_csv(distancias, M_lin):
    DATOS.mkdir(parents=True, exist_ok=True)
    filas = ["distancia_m,bloque,potencia_lineal,potencia_dB"]
    for i, d in enumerate(distancias):
        for k, pl in enumerate(M_lin[i], 1):
            filas.append(f"{d:g},{k},{pl:.6e},{10 * np.log10(pl):.3f}")
    (DATOS / "mediciones.csv").write_text("\n".join(filas) + "\n")


def fig_pathloss(distancias, Pr_dB, aj, ruta):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(9, 5))
    dd = np.logspace(np.log10(min(distancias)), np.log10(max(distancias)), 100)
    ax.semilogx(dd, aj["intercepto"] + aj["pendiente"] * np.log10(dd), "-",
                label=f"Ajuste: n = {aj['n']:.2f}, R² = {aj['r2']:.3f}")
    ax.semilogx(distancias, Pr_dB, "o", ms=7, label="Mediciones")
    ax.set_xlabel("Distancia (m)")
    ax.set_ylabel("Potencia recibida (dB)")
    ax.set_title("Pérdidas por trayectoria")
    ax.grid(True, which="both", alpha=0.3)
    ax.legend()
    return comun.guardar_fig(fig, ruta, False)


def fig_residuales(distancias, res, sigma, ruta):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.axhline(sigma, color="C3", ls="--", lw=1, label=f"+σ = {sigma:.2f} dB")
    ax.axhline(-sigma, color="C3", ls="--", lw=1, label=f"−σ = {sigma:.2f} dB")
    ax.axhline(0.0, color="C7", lw=1)
    ax.semilogx(distancias, res, "o", ms=7, label="Residuales")
    ax.set_xlabel("Distancia (m)")
    ax.set_ylabel("Residual (dB)")
    ax.set_title("Residuales del ajuste (Pr − ajuste)")
    ax.grid(True, which="both", alpha=0.3)
    ax.legend()
    return comun.guardar_fig(fig, ruta, False)


class P2(vivo.Practica):
    titulo = "Practica 2 - perdidas por trayectoria"
    filas = 2
    alto = [2.2, 1.3, 2.0, 1.5]

    def __init__(self, args):
        super().__init__(args)
        self.d = np.array([float(v) for v in args.distancias.split(",") if v.strip()])
        if self.d.size == 0:
            raise SystemExit("--distancias vacio")
        self.M = {float(dd): [] for dd in self.d}
        self.sel = 0
        self.aj = None
        self.ax_pl = self.ax_res = None
        self.l_pts = self.l_aj = self.l_res = None
        self._demo = 0

    # -- paneles ---------------------------------------------------------
    def ejes(self, fig, gs, inicio):
        self.ax_pl = fig.add_subplot(gs[inicio])
        self.ax_pl.set_xlabel("Distancia (m)")
        self.ax_pl.set_ylabel("P (dBFS)")
        self.ax_pl.set_title("Perdidas por trayectoria", fontsize=9, loc="left")
        self.ax_pl.grid(True, which="both", alpha=0.25)
        self.l_pts, = self.ax_pl.semilogx([], [], "o", ms=8, label="Mediciones")
        self.l_aj, = self.ax_pl.semilogx([], [], "-", lw=1.6, label="Ajuste LS")
        self.ax_pl.legend(fontsize=7, loc="upper right")

        self.ax_res = fig.add_subplot(gs[inicio + 1], sharex=self.ax_pl)
        self.ax_res.set_xlabel("Distancia (m)")
        self.ax_res.set_ylabel("Residual (dB)")
        self.ax_res.grid(True, which="both", alpha=0.25)
        self.l_res, = self.ax_res.semilogx([], [], "o-", ms=5, lw=0.8)
        self._acomodar()
        return [self.ax_pl, self.ax_res]

    # -- mediciones ------------------------------------------------------
    def medias(self):
        """Distancias medidas, media en dB y cantidad de mediciones."""
        ds = [dd for dd in self.d if self.M[float(dd)]]
        if not ds:
            return np.array([]), np.array([]), 0
        pr = np.array([np.mean(self.M[float(dd)]) for dd in ds])
        return np.array(ds), pr, sum(len(self.M[float(dd)]) for dd in ds)

    def registrar(self, pot_db):
        self.M[float(self.d[self.sel])].append(float(pot_db))
        self._actualizar_ajuste()

    def _acomodar(self):
        ds, pr, _ = self.medias()
        if ds.size >= 2:
            self.ax_pl.set_xlim(ds.min() * 0.8, ds.max() * 1.25)
            lo, hi = min(pr.min(), pr.min() - 6), pr.max() + 6
            self.ax_pl.set_ylim(lo, hi)
            self.ax_res.set_ylim(-(hi - lo) / 3, (hi - lo) / 3)
        elif ds.size == 1:
            self.ax_pl.set_xlim(ds[0] * 0.8, ds[0] * 1.25)
            self.ax_pl.set_ylim(pr[0] - 10, pr[0] + 10)
            self.ax_res.set_ylim(-4, 4)

    def _actualizar_ajuste(self):
        ds, pr, ntot = self.medias()
        self.l_pts.set_data(ds, pr)
        if ds.size >= 2:
            self.aj = ajustar(ds, pr)
            dd = np.logspace(np.log10(ds.min()), np.log10(ds.max()), 50)
            self.l_aj.set_data(dd, self.aj["intercepto"] + self.aj["pendiente"] * np.log10(dd))
            self.l_res.set_data(ds, self.aj["residuales"])
        self._acomodar()
        self.estado = (f"| d = {self.d[self.sel]:g} m   medidas {ntot:3d}   "
                       + (f"n = {self.aj['n']:.2f}  R2 = {self.aj['r2']:.3f}"
                          if self.aj else "n = -- (mide 2 distancias)"))
        if self.app is not None:
            self.app.reencuadrar()

    # -- lazo ------------------------------------------------------------
    def actualizar(self, x, fs, t):
        if self.args.sim and self.cada(0.6):      # demo: recorre las distancias
            pot = float(simular(self.d, 1, seed=self._demo)[self.sel, 0])
            self._demo += 1
            self.registrar(pot)
            self.sel = (self.sel + 1) % self.d.size
        elif not self.args.sim:
            self.estado = (f"| d = {self.d[self.sel]:g} m   "
                           f"P {comun.potencia_dbfs(x):6.2f} dBFS   "
                           + (f"n = {self.aj['n']:.2f}  R2 = {self.aj['r2']:.3f}"
                              if self.aj else "n = --"))

    def tecla(self, ev):
        if ev.key == " ":
            if self.args.sim:
                self.registrar(float(simular(self.d, 1, seed=self._demo)[self.sel, 0]))
                self._demo += 1
            else:
                self.registrar(comun.potencia_dbfs(self.app.fuente.ultimo))
        elif ev.key.isdigit() and 1 <= int(ev.key) <= self.d.size:
            self.sel = int(ev.key) - 1
            self._actualizar_ajuste()
        elif ev.key in ("r", "R"):
            self.M = {float(dd): [] for dd in self.d}
            self.aj = None
            for l in (self.l_pts, self.l_aj, self.l_res):
                l.set_data([], [])
            self._actualizar_ajuste()

    def ayuda(self):
        return "1..6 distancia   ESPACIO medir   r reiniciar"

    # -- entregables -----------------------------------------------------
    def guardar(self):
        ds, pr, _ = self.medias()
        if ds.size < 2:
            print("faltan mediciones: mide al menos 2 distancias")
            return []
        M_lin = [10 ** (np.array(self.M[float(dd)]) / 10) for dd in ds]
        aj = ajustar(ds, pr)
        guardar_csv(ds, M_lin)
        rutas = [fig_pathloss(ds, pr, aj, FIGS / "pathloss.png"),
                 fig_residuales(ds, aj["residuales"], aj["sigma_res"], FIGS / "residuales.png")]
        rutas.append(comun.guardar_json(
            DATOS / "resultados.json", distancias=[float(v) for v in ds],
            potencias_dB=[float(v) for v in pr], n_estimado=aj["n"],
            intercepto=aj["intercepto"], r2=aj["r2"],
            desviacion_residuales_dB=aj["sigma_res"],
            modo="simulacion" if self.args.sim else "real"))
        filas = [(f"{dd:g}", f"{p:.2f}", f"σ = {np.std(self.M[float(dd)]):.2f} dB")
                 for dd, p in zip(ds, pr)]
        print(comun.tabla_markdown(["Distancia (m)", "Potencia (dB)", "Observaciones"], filas))
        print(f"Exponente de perdidas : n = {aj['n']:.3f}")
        print(f"Intercepto (d0 = 1 m) : {aj['intercepto']:.2f} dB")
        print(f"Coeficiente R2        : {aj['r2']:.4f}")
        return rutas


def selftest():
    d = np.array([1.0, 2.0, 5.0, 10.0, 15.0, 20.0])
    Pr_dB = simular(d, 10, p0=-40.0, n_real=3.0, sigma=4.0).mean(axis=1)
    aj = ajustar(d, Pr_dB)
    assert abs(aj["n"] - 3.0) < 0.6, aj["n"]
    print("practica2 selftest OK")


def main(argv=None):
    args = vivo.parser(
        __doc__, freq=433.9e6,
        mas=[("--distancias", dict(default="1,2,5,10,15,20")),
             ("--selftest", dict(action="store_true"))]).parse_args(argv)
    if args.selftest:
        selftest()
        return 0
    return vivo.correr(P2(args), args)


if __name__ == "__main__":
    sys.exit(main())
