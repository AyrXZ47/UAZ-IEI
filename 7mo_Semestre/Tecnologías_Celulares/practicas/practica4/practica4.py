"""Practica 4: sistema FHSS frente a interferencia de banda parcial.

Uso: python3 practica4.py
"""

import sys
from pathlib import Path

import numpy as np
from scipy import special

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE.parents[0] / "comun"))
from estilo_graficas import COLORES, guardar, guardar_json, preparar  # noqa: E402

CANALES = 8
CANAL_JAM = 4


def ber_teorica(ai):
    """BPSK con ruido real de desviacion AI: Q(1/AI)."""
    return 0.5 * special.erfc(1.0 / (ai * np.sqrt(2)))


def simular(ai, nbits=200_000, rng=None):
    """FHSS: solo 1/8 de los simbolos cae en el canal interferido."""
    rng = rng or np.random.default_rng(7)
    bits = rng.integers(0, 2, nbits)
    b = 2 * bits - 1
    hops = rng.integers(1, CANALES + 1, nbits)
    afectados = hops == CANAL_JAM
    rx = b.astype(float).copy()
    rx[afectados] += ai * rng.standard_normal(afectados.sum())
    ber_fhss = float(np.mean((rx > 0).astype(int) != bits))

    # Sistema convencional: siempre transmite en el canal interferido.
    rx_conv = b + ai * rng.standard_normal(nbits)
    ber_conv = float(np.mean((rx_conv > 0).astype(int) != bits))
    return ber_fhss, ber_conv, float(np.mean(afectados))


def main():
    import matplotlib.pyplot as plt

    figs, datos = preparar(BASE)
    rng = np.random.default_rng(2026)

    # --- Demostracion con 200 bits ---
    nb = 200
    bits = rng.integers(0, 2, nb)
    b = 2 * bits - 1
    hops = rng.integers(1, CANALES + 1, nb)
    afectados = hops == CANAL_JAM

    ai_demo = 8.0
    rx = b.astype(float).copy()
    rx[afectados] += ai_demo * rng.standard_normal(afectados.sum())

    fig, ax = plt.subplots(figsize=(8, 3.6))
    ax.step(np.arange(1, nb + 1), hops, where="post", color=COLORES[0])
    ax.scatter(np.arange(1, nb + 1)[afectados], hops[afectados],
               color=COLORES[1], zorder=3, s=18, label="canal interferido")
    ax.set_yticks(range(1, CANALES + 1))
    ax.set_xlabel("Símbolo")
    ax.set_ylabel("Canal")
    ax.set_title("Secuencia de salto FHSS (M = 8)")
    ax.legend(loc="upper right")
    guardar(fig, figs / "saltos.png")

    fig, ax = plt.subplots(figsize=(8, 4.0))
    ax.scatter(np.arange(1, nb + 1), hops, c=np.where(b > 0, COLORES[0], COLORES[3]),
               s=14, marker="s")
    ax.axhspan(CANAL_JAM - 0.4, CANAL_JAM + 0.4, color=COLORES[1], alpha=0.15)
    ax.text(nb * 0.99, CANAL_JAM + 0.55, "interferencia", ha="right",
            fontsize=8, color=COLORES[1])
    ax.set_yticks(range(1, CANALES + 1))
    ax.set_xlabel("Símbolo")
    ax.set_ylabel("Canal")
    ax.set_title("Tiempo--frecuencia: cada símbolo salta a un canal distinto")
    guardar(fig, figs / "tiempo_frecuencia.png")

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 4.6), sharex=True)
    ax1.plot(b, color=COLORES[2], lw=1.2, label="transmitido")
    ax1.set_ylabel("Amplitud")
    ax1.legend(loc="upper right")
    ax1.set_title(f"Señal recibida con AI = {ai_demo:.0f} en el canal {CANAL_JAM}")
    ax2.plot(rx, ".", color=COLORES[0], ms=4, label="recibido")
    ax2.scatter(np.arange(nb)[afectados], rx[afectados], color=COLORES[1],
                s=16, zorder=3, label="afectado")
    ax2.set_xlabel("Símbolo")
    ax2.set_ylabel("Amplitud")
    ax2.legend(loc="upper right")
    fig.tight_layout()
    guardar(fig, figs / "senal_interferida.png")

    # --- BER vs amplitud de interferencia ---
    niveles = np.array([2, 4, 6, 8, 10])
    fhss, conv, teorica = [], [], []
    for ai in niveles:
        bf, bc, _ = simular(ai, rng=rng)
        fhss.append(bf)
        conv.append(bc)
        teorica.append(ber_teorica(ai) / CANALES)

    fig, ax = plt.subplots(figsize=(6.6, 4.2))
    ax.plot(niveles, fhss, "o-", color=COLORES[0], label="FHSS (M = 8)")
    ax.plot(niveles, conv, "s-", color=COLORES[1], label="convencional")
    ax.plot(niveles, teorica, "--", color=COLORES[3], label="teórica FHSS")
    ax.set_xlabel("Amplitud de interferencia $A_I$")
    ax.set_ylabel("BER")
    ax.set_yscale("log")
    ax.set_title("Desempeño frente a interferencia de banda parcial")
    ax.grid(True, which="both")
    ax.legend()
    guardar(fig, figs / "ber.png")

    resultados = {
        "canales": CANALES,
        "canal_interferido": CANAL_JAM,
        "bits_demo": nb,
        "fraccion_afectada": float(np.mean(afectados)),
        "ai_demo": ai_demo,
        "niveles_ai": niveles.tolist(),
        "ber_fhss": fhss,
        "ber_convencional": conv,
        "ber_teorica_fhss": teorica,
    }
    guardar_json(resultados, datos / "resultados.json")

    print(f"FHSS M={CANALES}, canal interferido={CANAL_JAM}, "
          f"fraccion afectada={np.mean(afectados):.3f}")
    for ai, bf, bc in zip(niveles, fhss, conv):
        print(f"  AI={ai:2d}: BER FHSS={bf:.4f}, convencional={bc:.4f}")


if __name__ == "__main__":
    main()
