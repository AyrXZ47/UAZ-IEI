#!/usr/bin/env python3
"""Practica 3. Caracterizacion experimental del shadowing log-normal.

Mide la potencia recibida Pr(k) = 10*log10(mean(|data|^2)) en Nmed posiciones
independientes a distancia fija (10 m recomendados), estima la media mu y la
desviacion sigma del shadowing, ajusta una normal y verifica su normalidad.

Uso:
    python3 practica3.py                       # 50 mediciones reales a 433.9 MHz
    python3 practica3.py -f 433.9e6 -d 10 -n 50 --frame 4096 --pausa 1
    python3 practica3.py --sim                 # datos sinteticos (sin dongle)
    python3 practica3.py --selftest            # verifica el analisis sin dongle
    python3 practica3.py --no-show             # solo guarda figuras
"""
import argparse
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import comun  # noqa: E402

DIR = Path(__file__).resolve().parent
FIGS, DATOS = DIR / "figs", DIR / "datos"


def medir_real(nmed, frame, freq, ganancia, pausa):
    print("Mueva la antena/receptor entre mediciones (pasillo, interior de oficina,")
    print("paredes, puertas, con y sin personas), conservando ~10 m al transmisor.")
    Pr = np.empty(nmed)
    for k in range(nmed):
        Pr[k] = comun.potencia_dbfs(comun.capturar(freq, n=frame, ganancia=ganancia))
        if (k + 1) % 10 == 0 or k == nmed - 1:
            print(f"  medicion {k + 1:3d}/{nmed}: {Pr[k]:7.2f} dB")
        if k < nmed - 1:
            time.sleep(pausa)
    return Pr


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
    return comun.guardar_fig(fig, ruta, MOSTRAR)


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
    return comun.guardar_fig(fig, ruta, MOSTRAR)


def selftest():
    Pr = medir_sim(5000, seed=1)
    mu, sigma = np.mean(Pr), np.std(Pr, ddof=1)
    assert abs(sigma - 6) < 1.5, sigma
    assert abs(mu + 50) < 2, mu
    print("practica3 selftest OK")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("-f", "--freq", type=float, default=433.9e6)
    p.add_argument("-d", "--distancia", type=float, default=10.0)
    p.add_argument("-n", "--nmed", type=int, default=50)
    p.add_argument("--frame", type=int, default=4096, help="muestras por medicion")
    p.add_argument("--pausa", type=float, default=1.0, help="segundos entre mediciones")
    p.add_argument("-g", "--gain", default="auto")
    p.add_argument("--sim", action="store_true")
    p.add_argument("--no-show", action="store_true")
    p.add_argument("--selftest", action="store_true")
    args = p.parse_args()
    global MOSTRAR
    MOSTRAR = not args.no_show

    if args.selftest:
        selftest()
        return 0

    DATOS.mkdir(parents=True, exist_ok=True)
    if args.sim:
        Pr = medir_sim(args.nmed)
        modo = "simulacion"
        print(f"modo simulacion: {args.nmed} muestras N(-50, 6) dB")
    else:
        Pr = medir_real(args.nmed, args.frame, args.freq, args.gain, args.pausa)
        modo = "real"
    np.savetxt(DATOS / "mediciones.csv", np.c_[np.arange(1, Pr.size + 1), Pr],
               delimiter=",", header="indice,potencia_dB", comments="",
               fmt=["%d", "%.4f"])

    res = analizar(Pr)
    comun.guardar_json(DATOS / "resultados.json", n=int(Pr.size),
                       distancia=args.distancia, mu=res["mu"], sigma=res["sigma"],
                       mu_fit=res["mu_fit"], sigma_fit=res["sigma_fit"],
                       p_valor_normalidad=res["p_valor_normalidad"],
                       sigma_ic95=res["sigma_ic95"], modo=modo)
    fig_variacion(Pr, FIGS / "variacion.png")
    fig_histograma(Pr, res["mu_fit"], res["sigma_fit"], FIGS / "histograma.png")

    print(f"\nPrueba de normalidad (Shapiro-Wilk): p = {res['p_valor_normalidad']:.4f}")
    print(f"IC 95 % aprox. para sigma: [{res['sigma_ic95'][0]:.2f}, "
          f"{res['sigma_ic95'][1]:.2f}] dB")
    print(comun.tabla_markdown(["Parámetro", "Valor"], [
        ["Media µ (dB)", f"{res['mu']:.2f}"],
        ["Desviación σ (dB)", f"{res['sigma']:.2f}"],
        ["N mediciones", int(Pr.size)],
        ["Entorno", entorno_de(res["sigma"])]]))
    print(f"\nfiguras en {FIGS}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
