"""Practica 8: relacion de potencia pico a promedio (PAPR) en OFDM.

Uso: python3 practica8.py
"""

import sys
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE.parents[0] / "comun"))
from estilo_graficas import COLORES, guardar, guardar_json, preparar  # noqa: E402

NFFTS = [16, 32, 64, 128, 256]
REALIZACIONES = 3000


def simbolo_qpsk(rng, n):
    return ((2 * rng.integers(0, 2, n) - 1)
            + 1j * (2 * rng.integers(0, 2, n) - 1)) / np.sqrt(2)


def senal_ofdm(rng, nfft):
    x = np.fft.ifft(simbolo_qpsk(rng, nfft)) * np.sqrt(nfft)
    return x


def papr_db(x):
    p = np.abs(x) ** 2
    return float(10 * np.log10(np.max(p) / np.mean(p)))


def main():
    import matplotlib.pyplot as plt

    figs, datos = preparar(BASE)
    rng = np.random.default_rng(8)

    # --- PAPR por numero de subportadoras ---
    tabla = []
    muestras = {}
    for nfft in NFFTS:
        vals = np.array([papr_db(senal_ofdm(rng, nfft))
                         for _ in range(REALIZACIONES)])
        muestras[nfft] = vals
        tabla.append({"nfft": nfft, "papr_medio_db": float(vals.mean()),
                      "papr_std_db": float(vals.std()),
                      "papr_max_db": float(vals.max())})

    # --- Potencia instantanea de un simbolo de 64 ---
    x = senal_ofdm(rng, 64)
    p = np.abs(x) ** 2
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 4.6), sharex=True)
    ax1.plot(np.real(x), color=COLORES[0], lw=1.0)
    ax1.set_ylabel("Parte real")
    ax1.set_title("Símbolo OFDM de 64 subportadoras: picos de amplitud")
    ax2.plot(p, color=COLORES[2], lw=1.0)
    ax2.axhline(p.mean(), color=COLORES[3], ls="--", lw=1,
                label=f"potencia media = {p.mean():.2f}")
    ax2.set_xlabel("Muestra")
    ax2.set_ylabel("$|x[n]|^2$")
    ax2.legend(loc="upper right")
    fig.tight_layout()
    guardar(fig, figs / "potencia_instantanea.png")

    # --- PAPR vs Nfft ---
    medias = np.array([t["papr_medio_db"] for t in tabla])
    stds = np.array([t["papr_std_db"] for t in tabla])
    fig, ax = plt.subplots(figsize=(6.6, 4.0))
    ax.errorbar(NFFTS, medias, yerr=stds, fmt="o-", capsize=4,
                color=COLORES[0], label="media $\\pm$ desviación")
    ax.set_xscale("log", base=2)
    ax.set_xticks(NFFTS)
    ax.set_xticklabels([str(n) for n in NFFTS])
    ax.set_xlabel("Número de subportadoras $N_{\\mathrm{FFT}}$")
    ax.set_ylabel("PAPR (dB)")
    ax.set_title("PAPR media en función del número de subportadoras")
    ax.legend()
    guardar(fig, figs / "papr_vs_nfft.png")

    # --- CCDF para 64, 128 y 256 ---
    umbrales = np.arange(0, 15.01, 0.1)
    fig, ax = plt.subplots(figsize=(6.6, 4.2))
    for nfft, color in zip([64, 128, 256], COLORES[:3]):
        vals = muestras[nfft]
        ccdf = np.array([np.mean(vals > u) for u in umbrales])
        ax.semilogy(umbrales, ccdf, lw=1.8, color=color,
                    label=f"$N_{{\\mathrm{{FFT}}}}={nfft}$")
    ax.set_xlabel("PAPR (dB)")
    ax.set_ylabel("CCDF")
    ax.set_title("Distribución complementaria acumulada de la PAPR")
    ax.grid(True, which="both")
    ax.legend()
    guardar(fig, figs / "ccdf.png")

    ccdf = {n: [float(np.mean(muestras[n] > u)) for u in umbrales] for n in (64, 128, 256)}
    papr_1pc = {n: float(umbrales[np.argmax(np.array(c) <= 0.01)])
                for n, c in ccdf.items()}
    resultados = {
        "realizaciones": REALIZACIONES,
        "tabla": tabla,
        "umbrales": umbrales.tolist(),
        "ccdf": ccdf,
        "papr_1pc_db": papr_1pc,
    }
    guardar_json(resultados, datos / "resultados.json")

    for t in tabla:
        print(f"  Nfft={t['nfft']:3d}: PAPR medio={t['papr_medio_db']:.2f} dB "
              f"(std {t['papr_std_db']:.2f}, max {t['papr_max_db']:.2f})")
    print(f"PAPR del simbolo de 64 subportadoras: {papr_db(x):.2f} dB")


if __name__ == "__main__":
    main()
