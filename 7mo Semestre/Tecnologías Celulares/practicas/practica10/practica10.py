"""Practica 10: detectores ZF y MMSE para un sistema MIMO 2x2.

Uso: python3 practica10.py
"""

import sys
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE.parents[0] / "comun"))
from estilo_graficas import COLORES, guardar, guardar_json, preparar  # noqa: E402

NT = NR = 2
NB = 10_000
REALIZACIONES = 500


def canal(rng):
    return (rng.standard_normal((NR, NT)) + 1j * rng.standard_normal((NR, NT))) / np.sqrt(2)


def simular(ebn0_db, rng):
    rho = 10 ** (ebn0_db / 10)
    sigma = np.sqrt(1 / rho)
    err_zf = err_mmse = total = 0
    for _ in range(REALIZACIONES):
        bits = rng.integers(0, 2, (NT, NB))
        x = 2.0 * bits - 1
        h = canal(rng)
        y = h @ x
        y = y + sigma * (rng.standard_normal(y.shape)
                         + 1j * rng.standard_normal(y.shape)) / np.sqrt(2)

        w_zf = np.linalg.inv(h.conj().T @ h) @ h.conj().T
        w_mmse = np.linalg.inv(h.conj().T @ h + (1 / rho) * np.eye(NT)) @ h.conj().T

        err_zf += int(np.sum((np.real(w_zf @ y) > 0).astype(int) != bits))
        err_mmse += int(np.sum((np.real(w_mmse @ y) > 0).astype(int) != bits))
        total += 2 * NB
    return err_zf / total, err_mmse / total


def main():
    import matplotlib.pyplot as plt

    figs, datos = preparar(BASE)
    rng = np.random.default_rng(10)

    snr_db = np.arange(0, 21, 2)
    ber_zf, ber_mmse = [], []
    for snr in snr_db:
        bz, bm = simular(snr, rng)
        ber_zf.append(bz)
        ber_mmse.append(bm)

    fig, ax = plt.subplots(figsize=(6.8, 4.2))
    ax.semilogy(snr_db, np.where(np.array(ber_zf) > 0, ber_zf, np.nan), "o-",
                color=COLORES[1], label="ZF")
    ax.semilogy(snr_db, np.where(np.array(ber_mmse) > 0, ber_mmse, np.nan), "s-",
                color=COLORES[0], label="MMSE")
    ax.set_xlabel("$E_b/N_0$ (dB)")
    ax.set_ylabel("BER")
    ax.set_title("Comparación de detectores lineales MIMO 2x2")
    ax.grid(True, which="both")
    ax.legend()
    guardar(fig, figs / "ber.png")

    # --- Constelaciones a 10 dB ---
    rho = 10 ** (10 / 10)
    sigma = np.sqrt(1 / rho)
    h = canal(rng)
    bits = rng.integers(0, 2, (NT, 2000))
    x = 2.0 * bits - 1
    y = h @ x + sigma * (rng.standard_normal((NR, 2000))
                         + 1j * rng.standard_normal((NR, 2000))) / np.sqrt(2)
    w_zf = np.linalg.inv(h.conj().T @ h) @ h.conj().T
    w_mmse = np.linalg.inv(h.conj().T @ h + (1 / rho) * np.eye(NT)) @ h.conj().T

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 3.8), sharey=True)
    ax1.plot((w_zf @ y)[0].real, (w_zf @ y)[0].imag, ".", color=COLORES[1],
             ms=3, alpha=0.6)
    ax1.set_title("ZF, $E_b/N_0=10$ dB")
    ax2.plot((w_mmse @ y)[0].real, (w_mmse @ y)[0].imag, ".", color=COLORES[0],
             ms=3, alpha=0.6)
    ax2.set_title("MMSE, $E_b/N_0=10$ dB")
    for ax in (ax1, ax2):
        ax.set_xlabel("I")
        ax.set_xlim(-2.5, 2.5)
        ax.axvline(0, color=COLORES[5], lw=0.7)
    ax1.set_ylabel("Q")
    fig.tight_layout()
    guardar(fig, figs / "constelaciones.png")

    resultados = {
        "nt": NT,
        "nr": NR,
        "bits_por_realizacion": NB,
        "realizaciones": REALIZACIONES,
        "snr_db": snr_db.tolist(),
        "ber_zf": ber_zf,
        "ber_mmse": ber_mmse,
        "ber_zf_10db": float(ber_zf[5]),
        "ber_mmse_10db": float(ber_mmse[5]),
        "mejora_10db": float(ber_zf[5] / ber_mmse[5]) if ber_mmse[5] else None,
    }
    guardar_json(resultados, datos / "resultados.json")

    for e, bz, bm in zip(snr_db, ber_zf, ber_mmse):
        print(f"  Eb/N0={e:2d} dB: ZF={bz:.5f}, MMSE={bm:.5f}")
    print(f"A 10 dB: ZF={ber_zf[5]:.5f}, MMSE={ber_mmse[5]:.5f}")


if __name__ == "__main__":
    main()
