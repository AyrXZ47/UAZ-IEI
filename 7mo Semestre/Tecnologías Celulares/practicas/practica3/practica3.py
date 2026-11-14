"""Practica 3: implementacion de un sistema DSSS y evaluacion de su BER.

Uso: python3 practica3.py
"""

import sys
from pathlib import Path

import numpy as np
from scipy import special, signal as sig

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE.parents[0] / "comun"))
from estilo_graficas import COLORES, guardar, guardar_json, preparar  # noqa: E402

M, K = 5, 2
N = 2**M - 1  # 31 chips por bit


def lfsr(m, k, n=None):
    n = n or 2**m - 1
    estado = [1] * m
    salida = np.empty(n, dtype=int)
    for i in range(n):
        salida[i] = estado[0]
        estado = estado[1:] + [estado[0] ^ estado[k]]
    return salida


def pn_bipolar():
    return 2 * lfsr(M, K) - 1


def dispersar(bits, codigo):
    return np.kron(2 * np.asarray(bits) - 1, codigo)


def desdispersar(rx, codigo, nbits):
    bloques = rx.reshape(nbits, len(codigo))
    return bloques @ codigo


def simular_ber(ebn0_db, codigo, nbits=200_000, rng=None):
    """Monte Carlo: chips +-1, ruido complejo de varianza N/EbN0 (Eb = N)."""
    rng = rng or np.random.default_rng(1234)
    ebn0 = 10 ** (ebn0_db / 10)
    bits = rng.integers(0, 2, nbits)
    tx = dispersar(bits, codigo)
    sigma2 = N / ebn0
    ruido = np.sqrt(sigma2 / 2) * (rng.standard_normal(tx.size)
                                   + 1j * rng.standard_normal(tx.size))
    rx = tx + ruido
    z = np.real(desdispersar(rx, codigo, nbits))
    return float(np.mean((z > 0).astype(int) != bits))


def main():
    import matplotlib.pyplot as plt

    figs, datos = preparar(BASE)
    codigo = pn_bipolar()
    rng = np.random.default_rng(2026)

    # --- Demostracion con 100 bits ---
    nb_demo = 100
    bits = rng.integers(0, 2, nb_demo)
    b = 2 * bits - 1
    tx = dispersar(bits, codigo)

    # Espectro de la senal de datos (cada bit repetido) y de la dispersa.
    datos_rect = np.repeat(b, N)
    f, p_datos = sig.welch(datos_rect, fs=1.0, nperseg=512, return_onesided=False)
    _, p_dsss = sig.welch(tx.astype(float), fs=1.0, nperseg=512,
                          return_onesided=False)
    orden = np.argsort(f)
    p_datos, p_dsss, f = p_datos[orden], p_dsss[orden], f[orden]

    # --- BER vs Eb/N0 ---
    snr_db = np.arange(0, 12, 2)
    ber = np.array([simular_ber(e, codigo, rng=rng) for e in snr_db])
    ber_teorica = 0.5 * special.erfc(np.sqrt(10 ** (snr_db / 10)))

    # --- Figuras ---
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 4.4), sharex=True)
    ax1.step(np.arange(2 * N), tx[: 2 * N], where="mid", color=COLORES[0])
    ax1.set_ylabel("Amplitud")
    ax1.set_title("Señal DSSS: dos bits dispersados con el código PN de 31 chips")
    ax2.plot(np.repeat(b[:2], N), color=COLORES[2], lw=2, label="datos")
    ax2.set_xlabel("Chip")
    ax2.set_ylabel("Amplitud")
    ax2.legend(loc="upper right")
    fig.tight_layout()
    guardar(fig, figs / "senal_dsss.png")

    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    ax.plot(f, 10 * np.log10(p_datos / p_datos.max() + 1e-20), lw=1.0,
            color=COLORES[2], label="datos (NRZ)")
    ax.plot(f, 10 * np.log10(p_dsss / p_dsss.max() + 1e-20), lw=0.8,
            color=COLORES[0], alpha=0.85, label="DSSS")
    ax.set_xlim(-0.5, 0.5)
    ax.set_ylim(-40, 3)
    ax.set_xlabel("Frecuencia normalizada ($f/F_s$)")
    ax.set_ylabel("PSD normalizada (dB)")
    ax.set_title("Ensanchamiento espectral por dispersión")
    ax.legend(loc="upper right")
    guardar(fig, figs / "espectro.png")

    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    ber_plot = np.where(ber > 0, ber, np.nan)
    ax.semilogy(snr_db, ber_plot, "o-", color=COLORES[0], label="DSSS simulado")
    ax.semilogy(snr_db, ber_teorica, "--", color=COLORES[1],
                label="BPSK teórico")
    ax.set_xlabel("$E_b/N_0$ (dB)")
    ax.set_ylabel("BER")
    ax.set_title("BER del sistema DSSS (31 chips/bit)")
    ax.grid(True, which="both")
    ax.legend()
    guardar(fig, figs / "ber.png")

    resultados = {
        "chips_por_bit": N,
        "bits_demo": nb_demo,
        "ganancia_procesamiento_db": float(10 * np.log10(N)),
        "ebn0_db": snr_db.tolist(),
        "ber": ber.tolist(),
        "ber_teorica": ber_teorica.tolist(),
        "ancho_relativo_datos": 1.0 / N,
        "ancho_relativo_dsss": 1.0,
    }
    guardar_json(resultados, datos / "resultados.json")

    print(f"DSSS con N={N} chips/bit, Gp={10*np.log10(N):.2f} dB")
    for e, b_, t in zip(snr_db, ber, ber_teorica):
        print(f"  Eb/N0={e:2d} dB: BER sim={b_:.5f}, teorica={t:.5f}")


if __name__ == "__main__":
    main()
