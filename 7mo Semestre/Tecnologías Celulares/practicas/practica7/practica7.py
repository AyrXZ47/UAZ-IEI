"""Practica 7: prefijo ciclico frente a la dispersion del canal.

El manual propone h=[1 0.6 0.3], pero con tres taps adyacentes la ISI afecta solo
2 de 64 muestras y el efecto del prefijo es marginal. Para que el experimento
muestre el fenomeno se usa un canal con la misma energia y retardos en 0, 5 y 12
muestras (dentro del CP de 16).

Uso: python3 practica7.py
"""

import sys
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE.parents[0] / "comun"))
from estilo_graficas import COLORES, guardar, guardar_json, preparar  # noqa: E402

NFFT = 64
NCP = 16
NB = 4096
H_NOMINAL = np.array([1.0, 0.6, 0.3])
H_DISPERSIVO = np.zeros(13)
H_DISPERSIVO[[0, 5, 12]] = [1.0, 0.6, 0.3]


def modular_qpsk(bits):
    b = np.asarray(bits).reshape(-1, 2)
    return ((2 * b[:, 0] - 1) + 1j * (2 * b[:, 1] - 1)) / np.sqrt(2)


def demodular_qpsk(simbolos):
    bits = np.empty(2 * len(simbolos), dtype=int)
    bits[0::2] = np.real(simbolos) > 0
    bits[1::2] = np.imag(simbolos) > 0
    return bits


def cadena_ofdm(bits):
    return np.fft.ifft(modular_qpsk(bits).reshape(-1, NFFT).T, axis=0) * np.sqrt(NFFT)


def transmitir_sin_cp(x, h):
    tx = x.flatten(order="F")
    return tx, np.convolve(tx, h)[: tx.size]


def transmitir_con_cp(x, h, ncp=NCP):
    tx = np.vstack((x[-ncp:], x)).flatten(order="F")
    return tx, np.convolve(tx, h)[: tx.size]


def ecualizar(simbolos, h):
    return simbolos / (np.fft.fft(h, NFFT) / np.sqrt(NFFT))[:, None]


def recibir_sin_cp(rx, h, ecualizar_si=True):
    y = np.fft.fft(rx.reshape(-1, NFFT).T, axis=0) / np.sqrt(NFFT)
    if ecualizar_si:
        y = ecualizar(y, h)
    return y.flatten(order="F")


def recibir_con_cp(rx, h, ncp=NCP):
    bloques = rx.reshape(-1, NFFT + ncp).T
    y = np.fft.fft(bloques[ncp:], axis=0) / np.sqrt(NFFT)
    return ecualizar(y, h).flatten(order="F")


def ber_punto(ebn0_db, rng, modo, h, nbits=NB, tramas=30):
    """modo: 'sin' (sin CP + ZF), 'sin_eq' (sin CP ni ecualizacion), 'con'."""
    s2 = 1 / (2 * 10 ** (ebn0_db / 10))
    errores = total = 0
    for _ in range(tramas):
        bits = rng.integers(0, 2, nbits)
        x = cadena_ofdm(bits)
        if modo == "con":
            _, rx = transmitir_con_cp(x, h)
            rx = rx + np.sqrt(s2 / 2) * (rng.standard_normal(rx.size)
                                         + 1j * rng.standard_normal(rx.size))
            hat = demodular_qpsk(recibir_con_cp(rx, h))
        else:
            _, rx = transmitir_sin_cp(x, h)
            rx = rx + np.sqrt(s2 / 2) * (rng.standard_normal(rx.size)
                                         + 1j * rng.standard_normal(rx.size))
            hat = demodular_qpsk(recibir_sin_cp(rx, h, modo == "sin"))
        errores += int(np.sum(hat != bits))
        total += nbits
    return errores / total


def main():
    import matplotlib.pyplot as plt

    figs, datos = preparar(BASE)
    rng = np.random.default_rng(7)

    # --- Canal ---
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 3.4))
    ax1.stem(np.arange(len(H_NOMINAL)), H_NOMINAL, basefmt=" ",
             linefmt=COLORES[2], markerfmt="o")
    ax1.set_title("Canal del manual (3 taps adyacentes)")
    ax1.set_xlabel("Retardo (muestras)")
    ax1.set_ylabel("$h[l]$")
    ax2.stem(np.arange(len(H_DISPERSIVO)), H_DISPERSIVO, basefmt=" ",
             linefmt=COLORES[0], markerfmt="o")
    ax2.set_title("Canal dispersivo usado (retardos 0, 5 y 12)")
    ax2.set_xlabel("Retardo (muestras)")
    fig.tight_layout()
    guardar(fig, figs / "canal.png")

    # --- Comparacion temporal: ISI en el borde de bloque ---
    bits = rng.integers(0, 2, NB)
    x = cadena_ofdm(bits)
    _, rx_sin = transmitir_sin_cp(x, H_DISPERSIVO)
    _, rx_con = transmitir_con_cp(x, H_DISPERSIVO)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 4.8), sharex=True)
    ax1.plot(np.real(rx_sin[: 2 * NFFT]), color=COLORES[1], lw=1.0)
    ax1.axvspan(0, 12, color=COLORES[1], alpha=0.20)
    ax1.axvspan(NFFT, NFFT + 12, color=COLORES[1], alpha=0.20)
    ax1.set_title("Sin prefijo cíclico: el símbolo anterior invade 12 muestras de cada bloque")
    ax1.set_ylabel("Parte real")
    ax2.plot(np.real(rx_con[: 2 * NFFT]), color=COLORES[0], lw=1.0)
    ax2.set_title("Con prefijo cíclico de 16 muestras")
    ax2.set_xlabel("Muestra")
    ax2.set_ylabel("Parte real")
    fig.tight_layout()
    guardar(fig, figs / "tiempo_isi.png")

    # --- Constelaciones a 15 dB ---
    snr_c = 15
    s2 = 1 / (2 * 10 ** (snr_c / 10))
    bits = rng.integers(0, 2, NB)
    x = cadena_ofdm(bits)
    _, rx_sin = transmitir_sin_cp(x, H_DISPERSIVO)
    rx_sin = rx_sin + np.sqrt(s2 / 2) * (rng.standard_normal(rx_sin.size)
                                         + 1j * rng.standard_normal(rx_sin.size))
    sym_sin = recibir_sin_cp(rx_sin, H_DISPERSIVO)
    _, rx_con = transmitir_con_cp(x, H_DISPERSIVO)
    rx_con = rx_con + np.sqrt(s2 / 2) * (rng.standard_normal(rx_con.size)
                                         + 1j * rng.standard_normal(rx_con.size))
    sym_con = recibir_con_cp(rx_con, H_DISPERSIVO)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.2), sharey=True)
    ax1.plot(sym_sin.real, sym_sin.imag, ".", color=COLORES[1], ms=3, alpha=0.6)
    ax1.set_title("Sin prefijo cíclico, $E_b/N_0=15$ dB")
    ax2.plot(sym_con.real, sym_con.imag, ".", color=COLORES[3], ms=3, alpha=0.6)
    ax2.set_title("Con prefijo cíclico, $E_b/N_0=15$ dB")
    for ax in (ax1, ax2):
        ax.axhline(0, color=COLORES[5], lw=0.7)
        ax.axvline(0, color=COLORES[5], lw=0.7)
        ax.set_aspect("equal")
        ax.set_xlabel("I")
    ax1.set_ylabel("Q")
    fig.tight_layout()
    guardar(fig, figs / "constelaciones.png")

    # --- Curvas BER sobre el canal dispersivo ---
    snr_db = np.arange(0, 22, 2)
    ber_sin = np.array([ber_punto(e, rng, "sin", H_DISPERSIVO) for e in snr_db])
    ber_con = np.array([ber_punto(e, rng, "con", H_DISPERSIVO) for e in snr_db])

    fig, ax = plt.subplots(figsize=(6.8, 4.2))
    ax.semilogy(snr_db, np.where(ber_sin > 0, ber_sin, np.nan), "o-",
                color=COLORES[1], label="sin prefijo")
    ax.semilogy(snr_db, np.where(ber_con > 0, ber_con, np.nan), "s-",
                color=COLORES[3], label="con prefijo (16)")
    ax.set_xlabel("$E_b/N_0$ (dB)")
    ax.set_ylabel("BER")
    ax.set_title("BER con y sin prefijo cíclico, canal dispersivo")
    ax.grid(True, which="both")
    ax.legend()
    guardar(fig, figs / "ber.png")

    # --- Casos de referencia a 15 dB ---
    ber_nominal_sin = ber_punto(15, rng, "sin", H_NOMINAL)
    ber_nominal_con = ber_punto(15, rng, "con", H_NOMINAL)
    ber_sin_eq = ber_punto(15, rng, "sin_eq", H_DISPERSIVO)
    h_largo = np.zeros(21)
    h_largo[[0, 20]] = [1.0, 0.6]
    ber_insuf = ber_punto(20, rng, "con", h_largo)

    idx = int(np.argmin(np.abs(snr_db - 14)))
    resultados = {
        "nfft": NFFT,
        "ncp": NCP,
        "canal_nominal": H_NOMINAL.tolist(),
        "canal_dispersivo": H_DISPERSIVO.tolist(),
        "bits": NB,
        "ebn0_db": snr_db.tolist(),
        "ber_sin_cp": ber_sin.tolist(),
        "ber_con_cp": ber_con.tolist(),
        "ber_sin_cp_14db": float(ber_sin[idx]),
        "ber_con_cp_14db": float(ber_con[idx]),
        "ber_sin_cp_sin_ecualizar_15db": float(ber_sin_eq),
        "ber_nominal_sin_cp_15db": float(ber_nominal_sin),
        "ber_nominal_con_cp_15db": float(ber_nominal_con),
        "ber_cp_insuficiente_20db": float(ber_insuf),
    }
    guardar_json(resultados, datos / "resultados.json")

    print(f"CP={NCP}, canal dispersivo={np.flatnonzero(H_DISPERSIVO)}")
    for e, bs, bc in zip(snr_db, ber_sin, ber_con):
        print(f"  Eb/N0={e:2d} dB: BER sin CP={bs:.5f}, con CP={bc:.6f}")
    print(f"Canal nominal 15 dB: sin CP={ber_nominal_sin:.5f}, "
          f"con CP={ber_nominal_con:.6f}")
    print(f"Sin CP y sin ecualizar: {ber_sin_eq:.4f}")
    print(f"Prefijo insuficiente (eco en 20): {ber_insuf:.4f}")


if __name__ == "__main__":
    main()
