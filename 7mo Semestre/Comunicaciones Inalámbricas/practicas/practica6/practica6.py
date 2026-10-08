#!/usr/bin/env python3
"""Práctica 6. Caracterización experimental de canales selectivos en frecuencia.

Captura muestras IQ en un entorno interior (escenarios LOS y NLOS), estima la
PSD normalizada de cada escenario, calcula la función de correlación en
frecuencia y estima el ancho de banda de coherencia con los umbrales 0.9 y 0.5.

Uso:
    python3 practica6.py                 # dos capturas reales (LOS y NLOS)
    python3 practica6.py --sim           # canal de 2 rayos simulado
    python3 practica6.py --selftest      # verifica el análisis sin dongle
    python3 practica6.py --no-show       # solo guarda figuras
"""
import argparse
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import comun  # noqa: E402

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
    return comun.guardar_fig(fig, ruta, MOSTRAR)


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
    return comun.guardar_fig(fig, ruta, MOSTRAR)


def selftest():
    fs, n = comun.RATE_DEF, 1 << 20
    res = {esc: analizar(x, fs) for esc, x in capturar_sim(fs, n, seed=0).items()}
    assert res["NLOS"]["Bc_50_Hz"] < res["LOS"]["Bc_50_Hz"], \
        (res["LOS"]["Bc_50_Hz"], res["NLOS"]["Bc_50_Hz"])
    assert 100e3 < res["NLOS"]["Bc_50_Hz"] < 2e6, res["NLOS"]["Bc_50_Hz"]
    print("practica6 selftest OK")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("-f", "--freq", type=float, default=433.9e6)
    p.add_argument("-r", "--rate", type=float, default=comun.RATE_DEF)
    p.add_argument("-n", "--n", type=int, default=262144)
    p.add_argument("-g", "--gain", default="auto")
    p.add_argument("--sim", action="store_true")
    p.add_argument("--selftest", action="store_true")
    p.add_argument("--no-show", action="store_true")
    args = p.parse_args()
    global MOSTRAR
    MOSTRAR = not args.no_show

    if args.selftest:
        selftest()
        return 0

    if args.sim:
        print("modo simulación: canal de 2 rayos (LOS y NLOS)")
        capturas = capturar_sim(args.rate, args.n)
    else:
        info = comun.info_dispositivo()
        print(f"Dispositivo: RTL2832U / {info['tuner']}")
        capturas = {}
        for esc, desc in (("LOS", "en línea de vista directa"),
                          ("NLOS", "con obstáculos (sin línea de vista)")):
            input(f"[{esc}] Coloca el receptor {desc} y pulsa ENTER para capturar... ")
            capturas[esc] = comun.capturar(args.freq, n=args.n, rate=args.rate,
                                           ganancia=args.gain)
            print(f"  {esc}: {capturas[esc].size} muestras a {args.freq/1e6:.3f} MHz")

    res = {esc: analizar(x, args.rate) for esc, x in capturas.items()}
    filas = [[esc, f"{r['potencia_dB']:.2f}", f"{r['variacion_espectral_dB']:.2f}",
              f"{r['Bc_90_Hz']/1e3:.1f} kHz", f"{r['Bc_50_Hz']/1e3:.1f} kHz"]
             for esc, r in res.items()]
    print(comun.tabla_markdown(["Escenario", "Potencia (dB)",
                                "Variación espectral (dB)", "Bc 0.9", "Bc 0.5"], filas))

    fig_psd(res, FIGS / "psd_los_nlos.png")
    fig_correlacion(res, FIGS / "correlacion.png")
    comun.guardar_json(DATOS / "resultados.json",
                       **{esc: {k: r[k] for k in ("potencia_dB",
                                                  "variacion_espectral_dB",
                                                  "Bc_90_Hz", "Bc_50_Hz")}
                          for esc, r in res.items()})
    print(f"figuras en {FIGS}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
