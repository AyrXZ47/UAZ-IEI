#!/usr/bin/env python3
"""Practica 4. Caracterizacion experimental del desvanecimiento Rayleigh.

Captura muestras IQ y analiza la envolvente normalizada de la senal recibida:
  - envolvente en el tiempo (decimada) y desvanecimientos profundos
  - histograma de amplitudes y ajuste de una distribucion Rayleigh
  - porcentaje de muestras bajo un umbral (fading profundo)

Uso:
    python3 practica4.py                       # captura real en 433.9 MHz (caminar con el receptor)
    python3 practica4.py -f 915e6 --dur 5      # otra frecuencia / duracion
    python3 practica4.py --sim                 # datos sinteticos (sin dongle)
    python3 practica4.py --selftest            # verifica el analisis sin dongle
    python3 practica4.py --no-show             # solo guarda figuras
"""
import argparse
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import comun  # noqa: E402

DIR = Path(__file__).resolve().parent
FIGS, DATOS = DIR / "figs", DIR / "datos"
MOSTRAR = True


def rayleigh_sim(fs, n, fd=10.0, los=0.0, seed=0):
    """Desvanecimiento Rayleigh con correlacion temporal (fd = Doppler maximo)."""
    from scipy.signal import firwin, lfilter

    rng = np.random.default_rng(seed)
    fs_f = 100.0 * fd   # ponytail: 129 taps a fs no resuelven 10 Hz; sintetizar a 100*fd
    m = int(np.ceil(n * fs_f / fs))
    h = firwin(129, fd, fs=fs_f)
    a = lfilter(h, 1.0, (rng.standard_normal(m) + 1j * rng.standard_normal(m)) / np.sqrt(2))
    a /= np.sqrt(np.mean(np.abs(a) ** 2))
    if los:
        a = a + los
    t = np.linspace(0, m - 1, n)
    return (np.interp(t, np.arange(m), a.real)
            + 1j * np.interp(t, np.arange(m), a.imag)).astype(np.complex64)


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

    paso = 100
    rd, x = r[::paso], np.arange(0, r.size, paso)
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(x, rd, lw=0.6)
    ax.axhline(umbral, color="C3", ls="--", lw=1.5, label=f"Umbral = {umbral}")
    ax.set_xlabel("Muestra")
    ax.set_ylabel("Amplitud")
    ax.set_title("Envolvente de la señal recibida")
    ax.grid(alpha=0.3)
    ax.legend()
    return comun.guardar_fig(fig, ruta, MOSTRAR)


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
    return comun.guardar_fig(fig, ruta, MOSTRAR)


def selftest():
    from scipy.stats import rayleigh

    r = rayleigh.rvs(scale=1 / np.sqrt(2), size=200000, random_state=0)
    r = r / np.sqrt(np.mean(r ** 2))
    pct = 100.0 * np.mean(r < 0.5)
    sigma = float(rayleigh.fit(r, floc=0)[1])
    assert 18.0 < pct < 26.0, pct
    assert abs(sigma - 1 / np.sqrt(2)) < 0.05, sigma
    print("practica4 selftest OK")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("-f", "--freq", type=float, default=433.9e6)
    p.add_argument("--dur", type=float, default=2.0, help="segundos de captura")
    p.add_argument("-r", "--rate", type=float, default=comun.RATE_DEF)
    p.add_argument("--umbral", type=float, default=0.5)
    p.add_argument("-g", "--gain", default="auto")
    p.add_argument("--fd", type=float, default=10.0, help="Doppler maximo simulado (Hz)")
    p.add_argument("--los", type=float, default=0.0, help="componente LOS simulada")
    p.add_argument("--sim", action="store_true")
    p.add_argument("--no-show", action="store_true")
    p.add_argument("--selftest", action="store_true")
    args = p.parse_args()
    global MOSTRAR
    MOSTRAR = not args.no_show

    if args.selftest:
        selftest()
        return 0

    n = int(args.dur * args.rate)
    if args.sim:
        x = rayleigh_sim(args.rate, n, fd=args.fd, los=args.los)
        modo = "simulacion"
        print(f"modo simulacion: Rayleigh con fd={args.fd:g} Hz, LOS={args.los:g}, {n} muestras")
    else:
        print("mueva el receptor (camine) durante la captura para excitar el desvanecimiento")
        x = comun.capturar(args.freq, n=n, rate=args.rate, ganancia=args.gain)
        modo = "real"
        print(f"capturadas {x.size} muestras a {args.freq/1e6:.3f} MHz")

    r = np.abs(x)
    r = r / np.sqrt(np.mean(r ** 2))
    res = analizar(r, args.umbral)

    print(comun.tabla_markdown(
        ["Frecuencia de operación", "Cantidad de muestras", "Media de amplitud",
         "Desviación estándar", "Porcentaje de fading profundo"],
        [[f"{args.freq/1e6:.3f} MHz", r.size, f"{res['media']:.4f}",
          f"{res['std']:.4f}", f"{res['porcentaje_profundo']:.2f} %"]]))
    print(f"sigma Rayleigh ajustado : {res['sigma']:.4f}")
    print(f"fading profundo teorico : {res['porcentaje_teorico']:.2f} %")

    fig_envolvente(r, args.umbral, FIGS / "envolvente.png")
    fig_histograma(r, res["sigma"], FIGS / "histograma_rayleigh.png")
    comun.guardar_json(DATOS / "resultados.json", frecuencia=args.freq,
                       n_muestras=int(r.size), media=res["media"], std=res["std"],
                       sigma_rayleigh=res["sigma"], umbral=args.umbral,
                       porcentaje_profundo=res["porcentaje_profundo"],
                       porcentaje_teorico=res["porcentaje_teorico"], modo=modo)
    print(f"figuras en {FIGS}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
