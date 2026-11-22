"""Practica 9: capacidad de canales MIMO Rayleigh.

Uso: python3 practica9.py
"""

import sys
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE.parents[0] / "comun"))
from estilo_graficas import COLORES, guardar, guardar_json, preparar  # noqa: E402

SNR_DB = np.arange(0, 31, 5)
REALIZACIONES = 1000


def canal(nr, nt, rng):
    return (rng.standard_normal((nr, nt)) + 1j * rng.standard_normal((nr, nt))) / np.sqrt(2)


def capacidad(h, rho):
    nr, nt = h.shape
    if nt == 1 and nr == 1:
        return float(np.log2(1 + rho * abs(h[0, 0]) ** 2))
    return float(np.real(np.log2(np.linalg.det(
        np.eye(nr) + (rho / nt) * h @ h.conj().T))))


def main():
    import matplotlib.pyplot as plt

    figs, datos = preparar(BASE)
    rng = np.random.default_rng(9)

    configs = [(1, 1), (2, 2), (4, 4)]
    curvas = {}
    for nt, nr in configs:
        medias = []
        for snr in SNR_DB:
            rho = 10 ** (snr / 10)
            vals = [capacidad(canal(nr, nt, rng), rho) for _ in range(REALIZACIONES)]
            medias.append(float(np.mean(vals)))
        curvas[f"{nt}x{nr}"] = medias

    fig, ax = plt.subplots(figsize=(7.0, 4.2))
    for (nombre, vals), color, marca in zip(curvas.items(), COLORES, ["o", "s", "^"]):
        ax.plot(SNR_DB, vals, marca + "-", color=color, label=f"MIMO {nombre}" if nombre != "1x1" else "SISO 1x1")
    ax.set_xlabel("SNR (dB)")
    ax.set_ylabel("Capacidad (bps/Hz)")
    ax.set_title("Capacidad ergódica de canales Rayleigh")
    ax.legend()
    guardar(fig, figs / "capacidad.png")

    # --- Distribucion de valores singulares ---
    fig, ejes = plt.subplots(1, 2, figsize=(9, 3.8), sharey=True)
    for ax, (nt, nr) in zip(ejes, [(2, 2), (4, 4)]):
        sv = np.concatenate([np.linalg.svd(canal(nr, nt, rng), compute_uv=False)
                             for _ in range(1000)])
        ax.hist(sv, bins=40, color=COLORES[0] if nt == 2 else COLORES[1],
                alpha=0.85, density=True)
        ax.set_title(f"Valores singulares, {nt}x{nr}")
        ax.set_xlabel("$\\sigma_i$")
    ejes[0].set_ylabel("Densidad")
    fig.tight_layout()
    guardar(fig, figs / "valores_singulares.png")

    # --- Ejemplo de matriz y sus valores singulares a 10 dB ---
    h2 = canal(2, 2, rng)
    sv2 = np.linalg.svd(h2, compute_uv=False)

    resultados = {
        "snr_db": SNR_DB.tolist(),
        "realizaciones": REALIZACIONES,
        "capacidad": curvas,
        "ejemplo_2x2": {
            "H_real": h2.real.tolist(),
            "H_imag": h2.imag.tolist(),
            "valores_singulares": sv2.tolist(),
        },
        "capacidad_10db": {k: float(v[2]) for k, v in curvas.items()},
        "ganancia_4x4_sobre_siso_10db": float(curvas["4x4"][2] / curvas["1x1"][2]),
    }
    guardar_json(resultados, datos / "resultados.json")

    for nombre, vals in curvas.items():
        print(f"  {nombre}: " + ", ".join(f"{v:.2f}" for v in vals))
    print(f"Valores singulares del ejemplo 2x2: {sv2}")


if __name__ == "__main__":
    main()
