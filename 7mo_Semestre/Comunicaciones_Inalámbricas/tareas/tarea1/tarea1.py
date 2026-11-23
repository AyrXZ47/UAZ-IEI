"""Tarea 1: transmision por canales inalambricos.

Uso: python3 tarea1.py
"""

import json
import sys
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE.parents[0] / "comun"))
from estilo_graficas import COLORES, guardar, guardar_json, preparar  # noqa: E402

import matplotlib.pyplot as plt  # noqa: E402

RNG = np.random.default_rng(1)
FIGS, DATOS = preparar(BASE)

SNR_DB = np.arange(0, 25.01, 1)
SNR = 10 ** (SNR_DB / 10)


def rayleigh(n, rng, sigma=1.0):
    """Amplitud Rayleigh con parametro sigma (E[a^2]=2 sigma^2)."""
    return sigma * np.sqrt(-2 * np.log(rng.random(n)))


def complejo_awgn(n, rng, varianza):
    return np.sqrt(varianza / 2) * (rng.standard_normal(n) + 1j * rng.standard_normal(n))


# ---------------------------------------------------------------- 1. Rayleigh
def problema1():
    sigmas = [1.0, 5.0, 10.0]
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.2))
    datos = {}
    for ax, s in zip(axes, sigmas):
        r = rayleigh(2000, RNG, s)
        x = np.linspace(0, 4 * s, 400)
        pdf = x / s ** 2 * np.exp(-x ** 2 / (2 * s ** 2))
        ax.hist(r, bins=30, density=True, color=COLORES[0], alpha=0.55,
                edgecolor=COLORES[5], label="histograma")
        ax.plot(x, pdf, color=COLORES[1], lw=1.8, label="PDF Rayleigh")
        ax.set_title(rf"$\sigma^2={s:g}$")
        ax.set_xlabel("$r$")
        ax.set_ylabel("densidad")
        ax.legend(fontsize=8)
        datos[f"sigma2_{s:g}"] = {"media_muestral": float(r.mean()),
                                  "teorica": float(s * np.sqrt(np.pi / 2))}
    fig.tight_layout()
    guardar(fig, FIGS / "p1_rayleigh.png", cerrar=False)
    return datos


# ------------------------------------------------- 2. taps con filtro de un polo
def taps_un_polo(p, N=1000, rng=None):
    rng = rng or RNG
    w = complejo_awgn(N, rng, 1.0)
    c = np.zeros(N, dtype=complex)
    for n in range(N):
        c[n] = p * c[n - 1] + (1 - p) * w[n] if n else (1 - p) * w[n]
    return c


def autocorr(x, m=60):
    x = x - x.mean()
    r = np.array([np.vdot(x[:len(x) - k], x[k:]).real / (len(x) - k)
                  for k in range(m)])
    return r / r[0]


def problema2():
    fig, axes = plt.subplots(2, 2, figsize=(9.2, 6.2))
    datos = {}
    for p, color in [(0.9, COLORES[0]), (0.99, COLORES[1])]:
        c = taps_un_polo(p)
        axes[0, 0].plot(c.real, color=color, lw=0.9, label=f"$p={p}$")
        axes[0, 1].plot(np.abs(c), color=color, lw=0.9, label=f"$p={p}$")
        axes[1, 0].plot(autocorr(c), color=color, lw=1.4, label=f"$p={p}$")

        from scipy.signal import welch
        f, Pxx = welch(c, nperseg=256, return_onesided=False, detrend=False)
        f, Pxx = np.fft.fftshift(f), np.fft.fftshift(Pxx)
        axes[1, 1].plot(f, 10 * np.log10(Pxx / Pxx.max()), ":",
                        color=color, lw=1.2)
        S = np.abs((1 - p) / (1 - p * np.exp(-2j * np.pi * f))) ** 2
        axes[1, 1].plot(f, 10 * np.log10(S / S.max()), color=color, lw=1.4,
                        label=f"$p={p}$")
        datos[f"p_{p}"] = {"varianza": float(np.var(c)),
                           "rho1": float(autocorr(c)[1])}

    axes[0, 0].set_title("Parte real")
    axes[0, 1].set_title("$|c_n|$")
    axes[1, 0].set_title("Autocorrelación")
    axes[1, 1].set_title("PSD normalizada (dB)")
    axes[0, 0].set_xlabel("$n$")
    axes[0, 1].set_xlabel("$n$")
    axes[1, 0].set_xlabel("retardo")
    axes[1, 1].set_xlabel("$f$ (ciclos/muestra)")
    for ax in axes.ravel():
        ax.legend(fontsize=8)
    fig.tight_layout()
    guardar(fig, FIGS / "p2_taps.png", cerrar=False)
    return datos


# ----------------------------------------------------------- 3. Jakes
def problema3():
    v_kmh, fc = 200.0, 1e9
    c = 3e8
    v = v_kmh / 3.6
    fm = v * fc / c
    f = np.linspace(-0.999 * fm, 0.999 * fm, 2000)
    S = 1 / (np.pi * fm * np.sqrt(1 - (f / fm) ** 2))

    fig, ax = plt.subplots(figsize=(6.8, 3.6))
    ax.plot(f, S, color=COLORES[0], lw=1.8)
    ax.set_xlabel("$f$ (Hz)")
    ax.set_ylabel("$S(f)$")
    ax.set_title(f"Espectro Doppler de Jakes ($f_m={fm:.1f}$ Hz)")
    guardar(fig, FIGS / "p3_jakes.png", cerrar=False)
    return {"fm_hz": fm, "v_ms": v}


# ------------------------------------------- 4, 5 y 6: binarias en Rayleigh
def ber_ortogonal_no_coherente(snr_db, nbits=200000):
    """D=1, detector de ley cuadrada."""
    rho = 10 ** (snr_db / 10)
    N0 = 1 / rho
    err = 0
    for _ in range(nbits // 5000):
        c = (RNG.standard_normal(5000) + 1j * RNG.standard_normal(5000)) / np.sqrt(2)
        n1 = complejo_awgn(5000, RNG, N0)
        n2 = complejo_awgn(5000, RNG, N0)
        R1 = np.abs(c + n1) ** 2
        R2 = np.abs(n2) ** 2
        err += int(np.sum(R2 > R1))
    return err / nbits


def ber_ook(snr_db, nbits=200000):
    rho = 10 ** (snr_db / 10)
    N0 = 1 / rho
    err = 0
    for _ in range(nbits // 5000):
        c = (RNG.standard_normal(5000) + 1j * RNG.standard_normal(5000)) / np.sqrt(2)
        n = complejo_awgn(5000, RNG, N0)
        bit = RNG.integers(0, 2, 5000)
        y = c * bit + n
        # umbral ML con CSI: Re(c* y) > |c|^2/2
        dec = (np.conj(c) * y).real > 0.5 * np.abs(c) ** 2
        err += int(np.sum(dec != bit))
    return err / nbits


def ber_ortogonal_diversidad(snr_db, D=3, nbits=100000):
    """D ramas independientes, combinacion de ley cuadrada."""
    rho = 10 ** (snr_db / 10)          # SNR por rama
    N0 = 1 / rho
    err = 0
    for _ in range(nbits // 5000):
        R1 = np.zeros(5000)
        R2 = np.zeros(5000)
        for _d in range(D):
            c = (RNG.standard_normal(5000) + 1j * RNG.standard_normal(5000)) / np.sqrt(2)
            R1 += np.abs(c + complejo_awgn(5000, RNG, N0)) ** 2
            R2 += np.abs(complejo_awgn(5000, RNG, N0)) ** 2
        err += int(np.sum(R2 > R1))
    return err / nbits


def problema4a6():
    rho = SNR
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 3.3))
    datos = {}

    mc = np.array([ber_ortogonal_no_coherente(s) for s in SNR_DB])
    axes[0].semilogy(SNR_DB, mc, "o", color=COLORES[0], ms=4, label="Monte Carlo")
    axes[0].semilogy(SNR_DB, 1 / (2 + rho), color=COLORES[1], lw=1.6, label="$1/(2+\\bar\\rho_b)$")
    axes[0].set_title("Ortogonal no coherente")
    datos["ortogonal_nc"] = mc.tolist()

    mc = np.array([ber_ook(s) for s in SNR_DB])
    axes[1].semilogy(SNR_DB, mc, "s", color=COLORES[0], ms=4, label="Monte Carlo")
    axes[1].semilogy(SNR_DB, 0.5 * (1 - np.sqrt(rho / (rho + 4))),
                     color=COLORES[1], lw=1.6, label="teoría")
    axes[1].set_title("OOK coherente")
    datos["ook"] = mc.tolist()

    mc = np.array([ber_ortogonal_diversidad(s - 10 * np.log10(3), 3) for s in SNR_DB])
    rho_rama = rho / 3
    K3 = 10
    axes[2].semilogy(SNR_DB, mc, "^", color=COLORES[0], ms=4, label="Monte Carlo")
    axes[2].semilogy(SNR_DB, K3 / rho_rama ** 3, color=COLORES[1], lw=1.6,
                     label="$10/\\bar\\rho^3$")
    axes[2].set_title("Diversidad $D=3$")
    datos["ortogonal_d3"] = mc.tolist()

    for ax in axes:
        ax.set_xlabel("$\\bar\\rho_b$ (dB)")
        ax.set_ylim([1e-5, 1])
        ax.legend(fontsize=8)
    axes[0].set_ylabel("BER")
    fig.tight_layout()
    guardar(fig, FIGS / "p456_binarias.png", cerrar=False)
    return datos


# ------------------------------------------------- 7 y 8: Rake de dos rayos
def ber_rake(snr_db, potencias, nbits=200000):
    """Rake de 2 rayos, senales ortogonales, deteccion coherente."""
    rho = 10 ** (snr_db / 10)      # SNR por rama (con E|c|^2 = 1 total)
    N0 = 1 / rho
    err = 0
    for _ in range(nbits // 5000):
        c1 = np.sqrt(potencias[0] / 2) * (RNG.standard_normal(5000)
                                          + 1j * RNG.standard_normal(5000))
        c2 = np.sqrt(potencias[1] / 2) * (RNG.standard_normal(5000)
                                          + 1j * RNG.standard_normal(5000))
        bit = RNG.integers(0, 2, 5000).astype(float)
        s1, s2 = bit, 1 - bit
        # correladores de las dos senales ortogonales en cada rayo
        z1 = (np.conj(c1) * (c1 * s1 + complejo_awgn(5000, RNG, N0))
              + np.conj(c2) * (c2 * s1 + complejo_awgn(5000, RNG, N0)))
        z2 = (np.conj(c1) * (c1 * s2 + complejo_awgn(5000, RNG, N0))
              + np.conj(c2) * (c2 * s2 + complejo_awgn(5000, RNG, N0)))
        dec = z1.real > z2.real
        err += int(np.sum(dec != bit))
    return err / nbits


def problema7y8():
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.4))
    datos = {}
    K2 = 3

    mc = np.array([ber_rake(s - 10 * np.log10(2), [1, 1]) for s in SNR_DB])
    rho = SNR
    axes[0].semilogy(SNR_DB, mc, "o", color=COLORES[0], ms=4, label="Monte Carlo")
    axes[0].semilogy(SNR_DB, K2 / rho ** 2, color=COLORES[1], lw=1.6,
                     label="$3/\\bar\\rho_b^2$")
    axes[0].set_title("Dos rayos iguales")
    datos["rake_iguales"] = mc.tolist()

    p = [2 / 3, 1 / 3]
    mc = np.array([ber_rake(s, p) for s in SNR_DB])
    axes[1].semilogy(SNR_DB, mc, "s", color=COLORES[0], ms=4, label="Monte Carlo")
    axes[1].semilogy(SNR_DB, K2 / (4 * rho ** 2 * p[0] * p[1]),
                     color=COLORES[1], lw=1.6, label="$27/(8\\bar\\rho_b^2)$")
    axes[1].set_title("Primera trayectoria al doble de potencia")
    datos["rake_desiguales"] = mc.tolist()

    for ax in axes:
        ax.set_xlabel("$\\bar\\rho_b$ (dB)")
        ax.set_ylabel("BER")
        ax.set_ylim([1e-4, 1])
        ax.legend(fontsize=8)
    fig.tight_layout()
    guardar(fig, FIGS / "p78_rake.png", cerrar=False)
    return datos


# ------------------------------------------------------------- 9: OFDM
def problema9():
    W, Tm, Bd = 800e3, 10e-6, 10.0
    T = 10 * Tm                     # perdida del CP <= 10%
    df = 1 / T
    N = W / df
    return {"W_Hz": W, "Tm_s": Tm, "Bd_Hz": Bd, "T_s": T, "df_Hz": df,
            "N_subcanales": N, "Tct_s": 1 / Bd, "Bcb_Hz": 1 / Tm,
            "diversidad_max": int(W * Tm), "Rs_simbolos_s": N / T}


# --------------------------------------------------------------------- main
def main():
    resultados = {
        "problema1": problema1(),
        "problema2": problema2(),
        "problema3": problema3(),
        "problema4_6": problema4a6(),
        "problema7_8": problema7y8(),
        "problema9": problema9(),
    }
    guardar_json(resultados, DATOS / "resultados.json")
    print(json.dumps(resultados, indent=1, ensure_ascii=False))
    if plt.get_fignums():
        plt.show()
        plt.close("all")


if __name__ == "__main__":
    main()
