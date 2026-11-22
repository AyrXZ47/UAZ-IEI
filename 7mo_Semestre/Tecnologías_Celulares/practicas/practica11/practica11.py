"""Practica 11: codigo espacio-tiempo de Alamouti 2x1 vs SISO Rayleigh.

Uso: python3 practica11.py
"""

import sys
from pathlib import Path

import numpy as np
from scipy import integrate, special, stats

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE.parents[0] / "comun"))
from estilo_graficas import COLORES, guardar, guardar_json, preparar  # noqa: E402

NB = 200_000


def rayleigh(rng, n):
    return (rng.standard_normal(n) + 1j * rng.standard_normal(n)) / np.sqrt(2)


def ruido(rng, n, var):
    return np.sqrt(var / 2) * (rng.standard_normal(n) + 1j * rng.standard_normal(n))


def simular_alamouti(ebn0_db, rng, nbits=NB):
    """2 antenas Tx, 1 Rx, potencia total unitaria (cada antena s/sqrt(2))."""
    n0 = 1 / 10 ** (ebn0_db / 10)
    bits = rng.integers(0, 2, nbits)
    s = 2.0 * bits - 1
    s1, s2 = s[0::2], s[1::2]
    npares = len(s1)

    h1, h2 = rayleigh(rng, npares), rayleigh(rng, npares)
    r1 = (h1 * s1 + h2 * s2) / np.sqrt(2) + ruido(rng, npares, n0)
    r2 = (-h1 * np.conj(s2) + h2 * np.conj(s1)) / np.sqrt(2) + ruido(rng, npares, n0)

    ganancia = (np.abs(h1) ** 2 + np.abs(h2) ** 2) / np.sqrt(2)
    s1_hat = (np.conj(h1) * r1 + h2 * np.conj(r2)) / ganancia
    s2_hat = (np.conj(h2) * r1 - h1 * np.conj(r2)) / ganancia

    hat = np.empty(nbits, dtype=int)
    hat[0::2] = np.real(s1_hat) > 0
    hat[1::2] = np.real(s2_hat) > 0
    return float(np.mean(hat != bits)), s1_hat


def simular_siso(ebn0_db, rng, nbits=NB):
    n0 = 1 / 10 ** (ebn0_db / 10)
    bits = rng.integers(0, 2, nbits)
    s = 2.0 * bits - 1
    h = rayleigh(rng, nbits)
    r = h * s + ruido(rng, nbits, n0)
    return float(np.mean((np.real(np.conj(h) * r) > 0).astype(int) != bits))


def ber_siso_teorica(ebn0_db):
    g = 10 ** (ebn0_db / 10)
    return 0.5 * (1 - np.sqrt(g / (1 + g)))


def ber_alamouti_teorica(ebn0_db):
    """Promedio sobre la distribucion Gamma del SNR combinado (2 ramas)."""
    g = 10 ** (ebn0_db / 10)
    f = lambda x: 0.5 * special.erfc(np.sqrt(x)) * stats.gamma.pdf(x, 2, scale=g / 2)
    return integrate.quad(f, 0, np.inf)[0]


def main():
    import matplotlib.pyplot as plt

    figs, datos = preparar(BASE)
    rng = np.random.default_rng(11)

    snr_db = np.arange(0, 21, 2)
    ber_alamouti, ber_siso = [], []
    s1_ejemplo = None
    for e in snr_db:
        ba, s1h = simular_alamouti(e, rng)
        ber_alamouti.append(ba)
        ber_siso.append(simular_siso(e, rng))
        if e == 10:
            s1_ejemplo = s1h
    ber_alamouti = np.array(ber_alamouti)
    ber_siso = np.array(ber_siso)
    teorica_siso = np.array([ber_siso_teorica(e) for e in snr_db])
    teorica_alamouti = np.array([ber_alamouti_teorica(e) for e in snr_db])

    fig, ax = plt.subplots(figsize=(6.8, 4.2))
    ax.semilogy(snr_db, ber_siso, "o-", color=COLORES[1], label="SISO simulado")
    ax.semilogy(snr_db, ber_alamouti, "s-", color=COLORES[0], label="Alamouti simulado")
    ax.semilogy(snr_db, teorica_siso, "--", color=COLORES[1], alpha=0.6,
                label="SISO teórico")
    ax.semilogy(snr_db, teorica_alamouti, ":", color=COLORES[0], alpha=0.8,
                label="Alamouti teórico")
    ax.set_xlabel("$E_b/N_0$ (dB)")
    ax.set_ylabel("BER")
    ax.set_title("Ganancia de diversidad: SISO vs Alamouti 2x1")
    ax.grid(True, which="both")
    ax.legend()
    guardar(fig, figs / "ber.png")

    fig, ax = plt.subplots(figsize=(4.8, 4.2))
    ax.plot(np.real(s1_ejemplo), np.imag(s1_ejemplo), ".", color=COLORES[0],
            ms=3, alpha=0.6)
    ax.axvline(0, color=COLORES[5], lw=0.7)
    ax.set_xlim(-2, 2)
    ax.set_xlabel("I")
    ax.set_ylabel("Q")
    ax.set_title("$s_1$ detectado a $E_b/N_0=10$ dB")
    guardar(fig, figs / "constelacion.png")

    # Ganancia a BER = 1e-3 por interpolacion logaritmica.
    def cruce(ber, objetivo=1e-2):
        ber = np.asarray(ber)
        idx = np.where(ber <= objetivo)[0]
        if not len(idx):
            return None
        i = idx[0]
        if i == 0:
            return float(snr_db[0])
        x0, x1 = snr_db[i - 1], snr_db[i]
        y0, y1 = np.log10(ber[i - 1]), np.log10(ber[i])
        return float(x0 + (np.log10(objetivo) - y0) * (x1 - x0) / (y1 - y0))

    resultados = {
        "bits": NB,
        "snr_db": snr_db.tolist(),
        "ber_alamouti": ber_alamouti.tolist(),
        "ber_siso": ber_siso.tolist(),
        "teorica_siso": teorica_siso.tolist(),
        "teorica_alamouti": teorica_alamouti.tolist(),
        "snr_ber_1e2_siso": cruce(ber_siso),
        "snr_ber_1e2_alamouti": cruce(ber_alamouti),
        "snr_ber_1e3_siso": cruce(ber_siso, 1e-3),
        "snr_ber_1e3_alamouti": cruce(ber_alamouti, 1e-3),
        "ber_10db_siso": float(ber_siso[5]),
        "ber_10db_alamouti": float(ber_alamouti[5]),
    }
    guardar_json(resultados, datos / "resultados.json")

    for e, bs, ba in zip(snr_db, ber_siso, ber_alamouti):
        print(f"  Eb/N0={e:2d} dB: SISO={bs:.5f}, Alamouti={ba:.5f}")
    print(f"BER=1e-2: SISO en {resultados['snr_ber_1e2_siso']} dB, "
          f"Alamouti en {resultados['snr_ber_1e2_alamouti']} dB")
    siso = resultados['snr_ber_1e3_siso']
    print(f"BER=1e-3: SISO " + (f"en {siso:.2f} dB" if siso else "no alcanza")
          + f", Alamouti en {resultados['snr_ber_1e3_alamouti']:.2f} dB")


if __name__ == "__main__":
    main()
