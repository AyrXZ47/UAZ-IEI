"""Practica 5: generacion de una senal OFDM con IFFT.

Uso: python3 practica5.py
"""

import sys
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE.parents[0] / "comun"))
from estilo_graficas import COLORES, guardar, guardar_json, preparar  # noqa: E402

NFFT = 64
NBITS = 1024


def modular_qpsk(bits):
    b = np.asarray(bits).reshape(-1, 2)
    return ((2 * b[:, 0] - 1) + 1j * (2 * b[:, 1] - 1)) / np.sqrt(2)


def generar_ofdm(simbolos, nfft=NFFT):
    """Cada columna de X es un simbolo OFDM; devuelve tx serializado."""
    x = np.fft.ifft(simbolos.reshape(-1, nfft).T, axis=0) * np.sqrt(nfft)
    return x.flatten(order="F"), x


def main():
    import matplotlib.pyplot as plt
    from scipy import signal as sig

    figs, datos = preparar(BASE)
    rng = np.random.default_rng(5)

    bits = rng.integers(0, 2, NBITS)
    sym = modular_qpsk(bits)
    tx, x = generar_ofdm(sym)
    nsym = x.shape[1]
    n = np.arange(NFFT)

    # --- Figura 1: senal OFDM en el tiempo ---
    fig, ax = plt.subplots(figsize=(8, 3.8))
    ax.plot(np.real(tx[: 4 * NFFT]), lw=0.9, color=COLORES[0])
    for k in range(5):
        ax.axvline(k * NFFT, color=COLORES[5], ls=":", lw=0.8)
    ax.set_xlabel("Muestra")
    ax.set_ylabel("Parte real")
    ax.set_title("Señal OFDM (4 símbolos, 64 subportadoras)")
    guardar(fig, figs / "senal_ofdm.png")

    # --- Figura 2: constelacion QPSK ---
    fig, ax = plt.subplots(figsize=(4.8, 4.4))
    ax.plot(sym.real, sym.imag, ".", color=COLORES[1], ms=4)
    ax.axhline(0, color=COLORES[5], lw=0.8)
    ax.axvline(0, color=COLORES[5], lw=0.8)
    ax.set_aspect("equal")
    ax.set_xlabel("I")
    ax.set_ylabel("Q")
    ax.set_title("Constelación QPSK")
    guardar(fig, figs / "constelacion.png")

    # --- Figura 3: espectro OFDM ---
    f, p = sig.welch(tx, fs=1.0, nperseg=512, return_onesided=False)
    orden = np.argsort(f)
    fig, ax = plt.subplots(figsize=(7.2, 3.8))
    ax.plot(f[orden], 10 * np.log10(p[orden] / p.max() + 1e-20),
            color=COLORES[0], lw=1.0)
    ax.set_xlim(-0.5, 0.5)
    ax.set_ylim(-45, 3)
    ax.set_xlabel("Frecuencia normalizada ($f/F_s$)")
    ax.set_ylabel("PSD normalizada (dB)")
    ax.set_title("Espectro de la señal OFDM")
    guardar(fig, figs / "espectro.png")

    # --- Figura 4: subportadoras del primer simbolo ---
    fig, ax = plt.subplots(figsize=(7.2, 3.6))
    ax.stem(np.arange(NFFT), np.abs(x[:, 0]), basefmt=" ",
            linefmt=COLORES[2], markerfmt="o")
    ax.set_xlabel("Subportadora")
    ax.set_ylabel("|$X_k$|")
    ax.set_title("Magnitud de las 64 subportadoras del primer símbolo")
    guardar(fig, figs / "subportadoras.png")

    # --- Figura 5: ortogonalidad ---
    s5 = np.exp(1j * 2 * np.pi * 5 * n / NFFT)
    s6 = np.exp(1j * 2 * np.pi * 6 * n / NFFT)
    producto = np.sum(s5 * np.conj(s6))
    productos = np.array([np.sum(np.exp(1j * 2 * np.pi * k * n / NFFT)
                                 * np.conj(s5)) for k in range(NFFT)])

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 4.8))
    ax1.plot(n, s5.real, "-o", ms=3, color=COLORES[0], label="k = 5")
    ax1.plot(n, s6.real, "-s", ms=3, color=COLORES[1], label="k = 6")
    ax1.set_xlabel("Muestra")
    ax1.set_ylabel("Parte real")
    ax1.set_title("Dos subportadoras consecutivas en un símbolo OFDM")
    ax1.legend(loc="upper right", ncols=2)
    ax2.bar(np.arange(NFFT), np.abs(productos), color=COLORES[3])
    ax2.set_xlabel("Subportadora $k$")
    ax2.set_ylabel("$|\\langle s_k, s_5\\rangle|$")
    ax2.set_title("Producto interno: solo la subportadora 5 es distinta de cero")
    fig.tight_layout()
    guardar(fig, figs / "ortogonalidad.png")

    papr = 10 * np.log10(np.max(np.abs(tx) ** 2) / np.mean(np.abs(tx) ** 2))
    resultados = {
        "nfft": NFFT,
        "bits": NBITS,
        "simbolos_qpsk": int(len(sym)),
        "simbolos_ofdm": int(nsym),
        "muestras_tx": int(tx.size),
        "potencia_media": float(np.mean(np.abs(tx) ** 2)),
        "producto_5_6": float(np.abs(producto)),
        "max_producto_fuera_diagonal": float(np.max(np.abs(np.delete(productos, 5)))),
        "papr_db": float(papr),
    }
    guardar_json(resultados, datos / "resultados.json")

    print(f"OFDM: {len(sym)} simbolos QPSK -> {nsym} simbolos OFDM de {NFFT}")
    print(f"Producto interno <s5,s6> = {np.abs(producto):.3e}")
    print(f"Maximo producto fuera de la diagonal = "
          f"{resultados['max_producto_fuera_diagonal']:.3e}")
    print(f"Potencia media de tx = {resultados['potencia_media']:.4f}, "
          f"PAPR = {papr:.2f} dB")


if __name__ == "__main__":
    main()
