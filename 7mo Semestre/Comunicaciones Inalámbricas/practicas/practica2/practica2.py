#!/usr/bin/env python3
"""Practica 2. Medicion experimental de perdidas por trayectoria (path loss).

Captura la potencia recibida a varias distancias con el RTL-SDR y ajusta el
modelo logaritmico  P(d) = P0 - 10*n*log10(d/d0) + X_sigma  por minimos
cuadrados para estimar el exponente de perdidas n del entorno.

Uso:
    python3 practica2.py                          # medicion real a 433.9 MHz
    python3 practica2.py -f 915e6 --distancias 1,2,5,10
    python3 practica2.py --sim                    # datos sinteticos (sin dongle)
    python3 practica2.py --selftest               # verifica ajuste sin dongle
    python3 practica2.py --no-show                # solo guarda figuras
"""
import argparse
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import comun  # noqa: E402

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


def medir_real(distancias, freq, frame, nmed, gain):
    """Captura nmed bloques de `frame` muestras a cada distancia; potencia lineal P(k)."""
    P = np.empty((len(distancias), nmed))
    for i, d in enumerate(distancias):
        input(f"Transmisor a {d:g} m — Enter para capturar {nmed} bloques de {frame} muestras...")
        for k in range(nmed):
            x = comun.capturar(freq, n=frame, ganancia=gain)
            P[i, k] = np.mean(np.abs(x) ** 2)
        print(f"  {d:g} m: {10 * np.log10(P[i].mean()):.2f} dB")
    return P


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
    return comun.guardar_fig(fig, ruta, MOSTRAR)


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
    return comun.guardar_fig(fig, ruta, MOSTRAR)


def reporte(distancias, Pr_dB, M_dB, aj, modo):
    filas = [(f"{d:g}", f"{pr:.2f}", f"σ = {s:.2f} dB")
             for d, pr, s in zip(distancias, Pr_dB, M_dB.std(axis=1))]
    print(comun.tabla_markdown(["Distancia (m)", "Potencia (dB)", "Observaciones"], filas))
    print(f"\nModo                    : {modo}")
    print(f"Exponente de pérdidas   : n = {aj['n']:.3f}")
    print(f"Intercepto (d0 = 1 m)   : {aj['intercepto']:.2f} dB")
    print(f"Coeficiente R²          : {aj['r2']:.4f}")
    print(f"Desv. de residuales     : {aj['sigma_res']:.2f} dB")


def selftest():
    d = np.array([1.0, 2.0, 5.0, 10.0, 15.0, 20.0])
    Pr_dB = simular(d, 10, p0=-40.0, n_real=3.0, sigma=4.0).mean(axis=1)
    aj = ajustar(d, Pr_dB)
    assert abs(aj["n"] - 3.0) < 0.6, aj["n"]
    print("practica2 selftest OK")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("-f", "--freq", type=float, default=433.9e6)
    p.add_argument("--distancias", default="1,2,5,10,15,20")
    p.add_argument("--nmed", type=int, default=10, help="bloques por distancia")
    p.add_argument("--frame", type=int, default=4096, help="muestras por bloque")
    p.add_argument("--gain", default="auto")
    p.add_argument("--sim", action="store_true")
    p.add_argument("--selftest", action="store_true")
    p.add_argument("--no-show", action="store_true")
    args = p.parse_args()
    global MOSTRAR
    MOSTRAR = not args.no_show

    if args.selftest:
        selftest()
        return 0

    d = np.array([float(v) for v in args.distancias.split(",") if v.strip()])
    if args.sim:
        modo = "simulacion"
        M_dB = simular(d, args.nmed)
        M_lin = 10.0 ** (M_dB / 10.0)
        Pr_dB = M_dB.mean(axis=1)
        print(f"Modo simulación: P0 = {P0_SIM:g} dB a 1 m, "
              f"n_real = {N_REAL_SIM}, σ = {SIGMA_SIM:g} dB "
              f"({args.nmed} bloques por distancia)")
    else:
        modo = "real"
        print(f"Frecuencia del transmisor: {args.freq / 1e6:.3f} MHz")
        M_lin = medir_real(d, args.freq, args.frame, args.nmed, args.gain)
        M_dB = 10.0 * np.log10(M_lin)
        Pr_dB = 10.0 * np.log10(M_lin.mean(axis=1))

    aj = ajustar(d, Pr_dB)
    guardar_csv(d, M_lin)
    fig_pathloss(d, Pr_dB, aj, FIGS / "pathloss.png")
    fig_residuales(d, aj["residuales"], aj["sigma_res"], FIGS / "residuales.png")
    comun.guardar_json(DATOS / "resultados.json",
                       distancias=[float(v) for v in d],
                       potencias_dB=[float(v) for v in Pr_dB],
                       n_estimado=aj["n"], intercepto=aj["intercepto"], r2=aj["r2"],
                       desviacion_residuales_dB=aj["sigma_res"], modo=modo)
    reporte(d, Pr_dB, M_dB, aj, modo)
    print(f"\nfiguras en {FIGS}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
