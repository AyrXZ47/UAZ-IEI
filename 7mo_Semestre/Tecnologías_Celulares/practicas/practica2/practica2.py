"""Practica 2: generacion y analisis de secuencias pseudoaleatorias (PN).

Genera secuencias de longitud maxima con LFSR, verifica periodo y balance, y
calcula autocorrelacion y correlacion cruzada.

Uso: python3 practica2.py
"""

import sys
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE.parents[0] / "comun"))
from estilo_graficas import COLORES, guardar, guardar_json, preparar  # noqa: E402

# Trinomios primitivos x^m + x^k + 1.
POLINOMIOS = {4: 1, 5: 2, 6: 1, 7: 3}


def lfsr(m, k, n=None, estado_inicial=None):
    """LFSR de Fibonacci: s[n+m] = s[n] + s[n+k] (mod 2)."""
    n = n or 2**m - 1
    estado = list(estado_inicial or [1] * m)
    salida = np.empty(n, dtype=int)
    for i in range(n):
        salida[i] = estado[0]
        retro = estado[0] ^ estado[k]
        estado = estado[1:] + [retro]
    return salida


def bipolar(x):
    return 2 * np.asarray(x) - 1


def autocorrelacion(x):
    """Autocorrelacion lineal normalizada (equivalente a xcorr(x,'coeff'))."""
    r = np.correlate(x, x, mode="full")
    return r / np.max(np.abs(r))


def autocorrelacion_periodica(x):
    """Autocorrelacion circular normalizada de una secuencia periodica."""
    n = len(x)
    r = np.fft.ifft(np.abs(np.fft.fft(x)) ** 2).real
    r = np.concatenate((r[-(n // 2):], r[: n // 2 + 1]))
    return r / r[n // 2]


def correlacion_cruzada(x, y):
    r = np.correlate(x, y, mode="full")
    return r / np.sqrt(np.sum(x**2) * np.sum(y**2))


def medir_periodo(seq):
    """Primer periodo de la secuencia (posicion donde se repite el estado inicial)."""
    m = len(seq)
    for p in range(1, m + 1):
        if np.array_equal(seq[:m - p], seq[p:]):
            return p
    return m


def main():
    import matplotlib.pyplot as plt

    figs, datos = preparar(BASE)
    c = COLORES

    # Secuencia principal: m=5, polinomio x^5 + x^2 + 1.
    m, k = 5, POLINOMIOS[5]
    pn = lfsr(m, k)
    xb = bipolar(pn)
    unos, ceros = int(pn.sum()), int(len(pn) - pn.sum())

    # Segunda secuencia para correlacion cruzada: x^5 + x^4 + 1.
    pn2 = lfsr(5, 4)
    yb = bipolar(pn2)

    r_auto = autocorrelacion(xb)
    r_per = autocorrelacion_periodica(xb)
    r_cruz = correlacion_cruzada(xb, yb)
    n = len(xb)

    # Longitudes para m = 4..7.
    tabla = []
    for mm, kk in POLINOMIOS.items():
        s = lfsr(mm, kk)
        tabla.append({
            "m": mm,
            "polinomio": f"x^{mm} + x^{kk} + 1",
            "longitud_teorica": 2**mm - 1,
            "longitud_observada": medir_periodo(s),
            "unos": int(s.sum()),
            "ceros": int(len(s) - s.sum()),
        })
    # --- Figura 1: secuencia y version bipolar ---
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 4.4), sharex=True)
    ax1.stem(np.arange(n), pn, basefmt=" ", linefmt=c[0], markerfmt="o")
    ax1.set_ylabel("Valor binario")
    ax1.set_title("Secuencia PN de longitud 31 (m = 5)")
    ax2.stem(np.arange(n), xb, basefmt=" ", linefmt=c[1], markerfmt="s")
    ax2.set_xlabel("Índice del chip")
    ax2.set_ylabel("Valor bipolar")
    ax2.set_yticks([-1, 0, 1])
    fig.tight_layout()
    guardar(fig, figs / "secuencia.png")

    # --- Figura 2: histograma bipolar ---
    fig, ax = plt.subplots(figsize=(5.6, 3.6))
    ax.bar([-1, 1], [ceros, unos], width=0.55, color=[c[1], c[0]])
    for x, v in zip([-1, 1], [ceros, unos]):
        ax.text(x, v + 0.3, str(v), ha="center")
    ax.set_xticks([-1, 1])
    ax.set_ylim(0, max(unos, ceros) + 3)
    ax.set_xlabel("Valor bipolar")
    ax.set_ylabel("Frecuencia")
    ax.set_title("Balance de la secuencia PN (31 chips)")
    guardar(fig, figs / "histograma.png")

    # --- Figura 3: autocorrelacion lineal y periodica ---
    retardos = np.arange(-n + 1, n)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 4.8), sharex=True)
    ax1.stem(retardos, r_auto, basefmt=" ", linefmt=c[0], markerfmt="o")
    ax1.set_ylabel("$R(\\tau)$")
    ax1.set_title("Autocorrelación lineal normalizada")
    ax2.stem(np.arange(-(n // 2), n // 2 + 1), r_per, basefmt=" ",
             linefmt=c[1], markerfmt="s")
    ax2.axhline(-1 / n, color=c[2], ls="--", lw=1,
                label=f"$-1/N = {-1/n:.4f}$")
    ax2.set_xlabel("Retardo $\\tau$ (chips)")
    ax2.set_ylabel("$R(\\tau)$")
    ax2.set_title("Autocorrelación periódica")
    ax2.legend(loc="lower right")
    fig.tight_layout()
    guardar(fig, figs / "autocorrelacion.png")

    # --- Figura 4: correlacion cruzada ---
    fig, ax = plt.subplots(figsize=(8, 3.6))
    ax.stem(np.arange(-n + 1, n), r_cruz, basefmt=" ",
            linefmt=c[4], markerfmt="o")
    ax.set_xlabel("Retardo $\\tau$ (chips)")
    ax.set_ylabel("$R_{xy}(\\tau)$")
    ax.set_title("Correlación cruzada entre $x^5+x^2+1$ y $x^5+x^4+1$")
    fig.tight_layout()
    guardar(fig, figs / "correlacion_cruzada.png")

    resultados = {
        "m": m,
        "polinomio": f"x^{m} + x^{k} + 1",
        "longitud": n,
        "unos": unos,
        "ceros": ceros,
        "autocorrelacion_pico": float(r_per[len(r_per) // 2]),
        "autocorrelacion_secundaria": float(-1 / n),
        "autocorrelacion_lineal_pico": float(np.max(r_auto)),
        "correlacion_cruzada_max": float(np.max(np.abs(r_cruz))),
        "correlacion_cruzada_media": float(np.mean(np.abs(r_cruz))),
        "tabla_longitudes": tabla,
        "balance_teorico": {"unos": 2 ** (m - 1), "ceros": 2 ** (m - 1) - 1},
        "periodo_observado": medir_periodo(pn),
    }
    guardar_json(resultados, datos / "resultados.json")

    print(f"PN m={m} ({resultados['polinomio']}): N={n}, unos={unos}, ceros={ceros}")
    print(f"Autocorrelacion: pico=1, secundaria={-1/n:.4f}, "
          f"max cruzada={resultados['correlacion_cruzada_max']:.4f}")
    for t in tabla:
        print(f"  m={t['m']}: teorica={t['longitud_teorica']}, "
              f"observada={t['longitud_observada']}, "
              f"unos={t['unos']}, ceros={t['ceros']}")


if __name__ == "__main__":
    main()
