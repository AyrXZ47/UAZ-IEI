"""Practica 6: demodulacion de senales OFDM y curva BER.

Uso: python3 practica6.py
"""

import sys
from pathlib import Path

import numpy as np
from scipy import special

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE.parents[0] / "comun"))
from estilo_graficas import COLORES, guardar, guardar_json, preparar  # noqa: E402

NFFT = 64
NB = 4096


def modular_qpsk(bits):
    b = np.asarray(bits).reshape(-1, 2)
    return ((2 * b[:, 0] - 1) + 1j * (2 * b[:, 1] - 1)) / np.sqrt(2)


def demodular_qpsk(simbolos):
    bits = np.empty(2 * len(simbolos), dtype=int)
    bits[0::2] = np.real(simbolos) > 0
    bits[1::2] = np.imag(simbolos) > 0
    return bits


def transmitir(simbolos, nfft=NFFT):
    x = np.fft.ifft(simbolos.reshape(-1, nfft).T, axis=0) * np.sqrt(nfft)
    return x.flatten(order="F")


def recibir(rx, nfft=NFFT):
    y = np.fft.fft(rx.reshape(-1, nfft).T, axis=0) / np.sqrt(nfft)
    return y.flatten(order="F")


def main():
    import matplotlib.pyplot as plt

    figs, datos = preparar(BASE)
    rng = np.random.default_rng(6)

    # --- Un simbolo a 10 dB para la constelacion ---
    bits = rng.integers(0, 2, 4096)
    tx = transmitir(modular_qpsk(bits))
    ebn0 = 10 ** (10 / 10)
    sigma2 = 1 / (2 * ebn0)  # Es = 1, Eb = Es/2, N0 = Eb/EbN0
    rx = tx + np.sqrt(sigma2 / 2) * (rng.standard_normal(tx.size)
                                     + 1j * rng.standard_normal(tx.size))
    sym_rx = recibir(rx)
    sym_tx = modular_qpsk(bits)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.2))
    ax1.plot(sym_tx.real, sym_tx.imag, ".", color=COLORES[0], ms=3)
    ax1.set_title("Constelación transmitida")
    ax2.plot(sym_rx.real, sym_rx.imag, ".", color=COLORES[1], ms=3, alpha=0.7)
    ax2.set_title("Constelación recibida, $E_b/N_0=10$ dB")
    for ax in (ax1, ax2):
        ax.axhline(0, color=COLORES[5], lw=0.7)
        ax.axvline(0, color=COLORES[5], lw=0.7)
        ax.set_aspect("equal")
        ax.set_xlabel("I")
        ax.set_ylabel("Q")
    fig.tight_layout()
    guardar(fig, figs / "constelacion.png")

    # --- BER vs Eb/N0 con Monte Carlo ---
    snr_db = np.arange(0, 16, 2)
    ber = []
    for e in snr_db:
        g = 10 ** (e / 10)
        s2 = 1 / (2 * g)
        errores = total = 0
        for _ in range(50):  # 50 tramas de 4096 bits = 204 800 bits
            bits = rng.integers(0, 2, NB)
            tx = transmitir(modular_qpsk(bits))
            rx = tx + np.sqrt(s2 / 2) * (rng.standard_normal(tx.size)
                                         + 1j * rng.standard_normal(tx.size))
            hat = demodular_qpsk(recibir(rx))
            errores += int(np.sum(hat != bits))
            total += NB
        ber.append(errores / total)
    ber = np.array(ber)
    teorica = 0.5 * special.erfc(np.sqrt(10 ** (snr_db / 10)))

    fig, ax = plt.subplots(figsize=(6.6, 4.2))
    ax.semilogy(snr_db, np.where(ber > 0, ber, np.nan), "o-",
                color=COLORES[0], label="OFDM simulado")
    ax.semilogy(snr_db, teorica, "--", color=COLORES[1],
                label="QPSK teórico")
    ax.set_xlabel("$E_b/N_0$ (dB)")
    ax.set_ylabel("BER")
    ax.set_title("BER del sistema OFDM (64 subportadoras)")
    ax.grid(True, which="both")
    ax.legend()
    guardar(fig, figs / "ber.png")

    resultados = {
        "nfft": NFFT,
        "bits": NB,
        "ebn0_db": snr_db.tolist(),
        "ber": ber.tolist(),
        "ber_teorica": teorica.tolist(),
        "constelacion_snr_db": 10,
        "error_evm": float(np.sqrt(np.mean(np.abs(sym_rx - sym_tx) ** 2))),
    }
    guardar_json(resultados, datos / "resultados.json")

    print(f"OFDM {NFFT} subportadoras, {NB} bits por trama")
    for e, b_, t in zip(snr_db, ber, teorica):
        print(f"  Eb/N0={e:2d} dB: BER sim={b_:.3e}, teorica={t:.3e}")


if __name__ == "__main__":
    main()
