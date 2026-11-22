"""Tarea 3: OFDM. Genera las figuras y los numeros del reporte.

Uso: python3 tarea3.py
"""

import json
import sys
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE.parents[1] / "practicas" / "comun"))
from estilo_graficas import COLORES, guardar, guardar_json, preparar  # noqa: E402

import matplotlib.pyplot as plt  # noqa: E402

RNG = np.random.default_rng(3)
FIGS, DATOS = preparar(BASE)

FS = 200          # muestras por periodo de simbolo para la PAPR
REALIZACIONES = 1000


# ----------------------------------------------------------------- utilidades
def qpsk(n, rng):
    """n simbolos 4-PSK de energia unitaria."""
    return ((2 * rng.integers(0, 2, n) - 1)
            + 1j * (2 * rng.integers(0, 2, n) - 1)) / np.sqrt(2)


def qam16(n, rng):
    """n simbolos 16-QAM de la constelacion {-3,-1,1,3} + j{-3,-1,1,3}."""
    b = 2 * rng.integers(0, 2, (n, 4)) - 1
    return (2 * b[:, 0] + b[:, 1]) + 1j * (2 * b[:, 2] + b[:, 3])


def papr_db(x):
    p = np.abs(x) ** 2
    return 10 * np.log10(np.max(p) / np.mean(p))


def ccdf(valores, umbrales):
    return np.array([np.mean(valores > u) for u in umbrales])


# ------------------------------------------------------- 1. OFDM con 16-QAM
def problema1():
    K, N, T = 5, 10, 100
    X_info = qam16(4, RNG)
    X = np.concatenate(([0], X_info, [0], np.conj(X_info[::-1])))

    t = np.arange(T + 1)
    k = np.arange(N)
    x_t = np.exp(1j * 2 * np.pi * np.outer(t, k) / T) @ (X / np.sqrt(N))
    xn = np.fft.ifft(X) * np.sqrt(N)

    muestras = np.arange(N) * T / N
    error = np.max(np.abs(x_t[muestras.astype(int)].real - xn.real))
    X_rec = np.fft.fft(xn) / np.sqrt(N)

    fig, ax = plt.subplots(figsize=(7.2, 3.8))
    ax.plot(t, x_t.real, color=COLORES[0], lw=1.6, label="$x(t)$")
    ax.plot(muestras, xn.real, "o", color=COLORES[1], ms=5,
            label="muestras IDFT $x_n$")
    ax.set_xlabel("$t$")
    ax.set_ylabel("$x(t)$")
    ax.set_title("Señal OFDM con 4 símbolos 16-QAM ($N=10$)")
    ax.legend(loc="upper right")
    guardar(fig, FIGS / "p1_senal.png")

    return {"N": N, "K": K, "error_muestras": float(error),
            "error_simbolos": float(np.max(np.abs(X_rec - X))),
            "X": [f"{v.real:+.0f}{v.imag:+.0f}j" for v in X_info]}


# ------------------------------------------- 2. OFDM 4-PSK con FFT (K = 16)
def problema2():
    K = 16
    X = qpsk(K, RNG)
    x = np.fft.ifft(X) * np.sqrt(K)
    X_rec = np.fft.fft(x) / np.sqrt(K)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.2, 3.6))
    ax1.plot(x.real, "o-", color=COLORES[0], ms=4, lw=1.0, label="Re")
    ax1.plot(x.imag, "s-", color=COLORES[1], ms=4, lw=1.0, label="Im")
    ax1.set_xlabel("$n$")
    ax1.set_ylabel("$x_n$")
    ax1.set_title("Símbolo OFDM ($K=16$)")
    ax1.legend(loc="upper right")

    ax2.plot(X_rec.real, X_rec.imag, "o", color=COLORES[3], ms=7,
             label="recuperado")
    ax2.set_xlim(-1.4, 1.4)
    ax2.set_ylim(-1.4, 1.4)
    ax2.set_aspect("equal")
    ax2.set_xlabel("Re")
    ax2.set_ylabel("Im")
    ax2.set_title("Constelación 4-PSK recuperada")
    ax2.legend(loc="upper right")
    fig.tight_layout()
    guardar(fig, FIGS / "p2_simbolo.png")

    return {"K": K, "error_fft": float(np.max(np.abs(X_rec - X)))}


# ------------------------------------------------- 3. efecto del ruido aditivo
def problema3():
    K = 16
    varianzas = [1.0, 2.0, 4.0]
    X = qpsk(K, RNG)
    x = np.fft.ifft(X) * np.sqrt(K)

    ideal = np.array([1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j]) / np.sqrt(2)
    fig, axes = plt.subplots(1, 3, figsize=(9.2, 3.3))
    resultados = []
    for ax, var in zip(axes, varianzas):
        r = x + np.sqrt(var / 2) * (RNG.standard_normal(K)
                                    + 1j * RNG.standard_normal(K))
        Y = np.fft.fft(r) / np.sqrt(K)
        detect = (np.where(Y.real >= 0, 1, -1)
                  + 1j * np.where(Y.imag >= 0, 1, -1)) / np.sqrt(2)
        errores = int(np.sum(detect != X))

        ax.plot(ideal.real, ideal.imag, "x", color=COLORES[5],
                ms=9, mew=2, label="ideal")
        ax.plot(Y.real, Y.imag, "o", color=COLORES[1], ms=6,
                label="recibido")
        ax.set_xlim(-2.6, 2.6)
        ax.set_ylim(-2.6, 2.6)
        ax.set_aspect("equal")
        ax.set_title(rf"$\sigma^2={var:g}$: {errores} errores")
        ax.set_xlabel("Re")
        if ax is axes[0]:
            ax.set_ylabel("Im")
            ax.legend(loc="upper right", fontsize=8)
        resultados.append({"varianza": var, "errores": errores})
    fig.tight_layout()
    guardar(fig, FIGS / "p3_ruido.png")

    # curva Monte Carlo de simbolos en error
    nsim = 4000
    serie = []
    Xs = qpsk(nsim, RNG)
    xs = np.fft.ifft(Xs.reshape(-1, K).T, axis=0) * np.sqrt(K)
    for var in [0.25, 0.5, 1, 2, 4]:
        rx = xs + np.sqrt(var / 2) * (RNG.standard_normal(xs.shape)
                                      + 1j * RNG.standard_normal(xs.shape))
        Y = np.fft.fft(rx, axis=0) / np.sqrt(K)
        d = (np.where(Y.real >= 0, 1, -1)
             + 1j * np.where(Y.imag >= 0, 1, -1)) / np.sqrt(2)
        serie.append({"varianza": var,
                      "ser": float(np.mean(d != Xs.reshape(-1, K).T))})
    return {"una_realizacion": resultados, "monte_carlo": serie}


# ----------------------------------------------------- 4. espectro de x(t)
def problema4():
    K, T = 16, 1.0
    X = qpsk(K, RNG)
    f = np.linspace(-2, K + 1, 6000)
    k = np.arange(K)

    # X(f) = sqrt(T) * suma Xk exp(-j pi (fT-k)) sinc(fT-k)
    S = (np.exp(-1j * np.pi * (f[:, None] - k))
         * np.sinc(f[:, None] - k)) @ X
    Xf = np.sqrt(T) * S
    magnitud = 20 * np.log10(np.abs(Xf) + 1e-12)

    # verificacion: FFT con relleno de ceros (interpola el espectro)
    M, NFFT = 1024, 16384
    m = np.arange(M)
    x_fine = np.exp(1j * 2 * np.pi * np.outer(m / M, k)) @ (X / np.sqrt(T))
    X_fft = np.fft.fftshift(np.fft.fft(x_fine, NFFT)) * (T / M)
    f_fft = np.fft.fftshift(np.fft.fftfreq(NFFT, T / M))

    fig, ax = plt.subplots(figsize=(7.4, 3.8))
    ax.plot(f_fft, 20 * np.log10(np.abs(X_fft) + 1e-12), ":",
            color=COLORES[1], lw=2, label="FFT sobremuestreada")
    ax.plot(f, magnitud, color=COLORES[0], lw=1.2, label="analítica")
    ax.set_xlim(-1, K + 0.5)
    ax.set_ylim(-60, 8)
    ax.set_xlabel("$fT$")
    ax.set_ylabel("$|X(f)|$ (dB)")
    ax.set_title("Espectro de la señal OFDM con $K=16$")
    ax.legend(loc="upper right")
    guardar(fig, FIGS / "p4_espectro.png")

    return {"pico_db": float(np.max(magnitud))}


# ---------------------------------------------------------------- 5. PAPR
def simbolo_papr(K, rng, fases=None):
    t = np.arange(FS) / FS
    k = np.arange(1, K)
    theta = np.pi / 2 * rng.integers(0, 4, K - 1)
    if fases is None:
        x = np.cos(2 * np.pi * np.outer(t, k) + theta).sum(axis=1)
    else:
        x = np.cos(2 * np.pi * np.outer(t, k) + theta + fases).sum(axis=1)
    return x


def problema5():
    K = 16
    vals = np.array([papr_db(simbolo_papr(K, RNG))
                     for _ in range(REALIZACIONES)])
    umbrales = np.arange(3, 12.01, 0.1)
    c = ccdf(vals, umbrales)

    fig, ax = plt.subplots(figsize=(6.8, 3.8))
    ax.semilogy(umbrales, c, color=COLORES[0], lw=1.8)
    ax.set_xlabel("PAPR (dB)")
    ax.set_ylabel("CCDF")
    ax.set_title(f"CCDF de la PAPR con $K={K}$ y 4-PSK")
    guardar(fig, FIGS / "p5_papr.png")

    return {"K": K, "media_db": float(vals.mean()),
            "std_db": float(vals.std()), "max_db": float(vals.max()),
            "pct1_db": float(umbrales[np.argmax(c <= 0.01)])}


# ------------------------------------------------- 6. recorte de picos
def recortar(x, umbral_db):
    """Limita la amplitud hasta que la PAPR quede en el umbral."""
    y = x.copy()
    umbral = 10 ** (umbral_db / 10)
    for _ in range(200):
        pav = np.mean(y ** 2)                 # potencia media de la señal recortada
        A = np.sqrt(umbral * pav)
        y = np.where(np.abs(y) > A, np.sign(y) * A, y)
        if np.max(y ** 2) / np.mean(y ** 2) <= umbral * (1 + 1e-9):
            break
    return y


def problema6():
    K = 16
    base = [simbolo_papr(K, RNG) for _ in range(REALIZACIONES)]
    papr_base = np.array([papr_db(x) for x in base])
    umbrales = np.arange(2, 12.01, 0.1)

    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(9.2, 3.7))
    ax.semilogy(umbrales, ccdf(papr_base, umbrales), color=COLORES[5],
                lw=1.8, label="sin recortar")
    resumen = []
    for umbral, color in [(4.0, COLORES[1]), (6.0, COLORES[3])]:
        salida = [recortar(x, umbral) for x in base]
        papr_sal = np.array([papr_db(x) for x in salida])
        dist = np.array([np.sum((a - b) ** 2) / FS for a, b in zip(base, salida)])
        evm = np.sqrt(dist / np.mean(np.array([np.mean(x ** 2) for x in base])))
        ax.semilogy(umbrales, ccdf(papr_sal, umbrales), color=color, lw=1.8,
                    label=f"recortada a {umbral:.0f} dB")
        resumen.append({"umbral_db": umbral,
                        "papr_medio_db": float(papr_sal.mean()),
                        "papr_max_db": float(papr_sal.max()),
                        "evm_medio": float(evm.mean())})
    ax.set_xlabel("PAPR (dB)")
    ax.set_ylabel("CCDF")
    ax.set_title("PAPR antes y después del recorte")
    ax.legend(loc="upper right")

    t = np.arange(FS) / FS
    x0 = base[0]
    ax2.plot(t, x0, color=COLORES[5], lw=1.2, label="original")
    ax2.plot(t, recortar(x0, 4.0), color=COLORES[1], lw=1.2,
             label="recortada a 4 dB")
    ax2.set_xlabel("$t/T$")
    ax2.set_ylabel("$x(t)$")
    ax2.set_title("Un símbolo antes y después del recorte")
    ax2.legend(loc="upper right")
    fig.tight_layout()
    guardar(fig, FIGS / "p6_recorte.png")

    return {"papr_medio_db": float(papr_base.mean()),
            "umbrales": resumen}


# ------------------------------------------------- 7. SLM con K = 8
def problema7():
    K, M = 8, 4
    t = np.arange(FS) / FS
    k = np.arange(1, K)
    base, slm = [], []
    for _ in range(REALIZACIONES):
        theta = np.pi / 2 * RNG.integers(0, 4, K - 1)
        x0 = np.cos(2 * np.pi * np.outer(t, k) + theta).sum(axis=1)
        phi = 2 * np.pi * RNG.random((M, K - 1))
        x = np.cos(2 * np.pi * np.outer(t, k) + theta + phi[:, None, :]).sum(axis=2)
        base.append(papr_db(x0))
        slm.append(min(papr_db(xm) for xm in x))

    base = np.array(base)
    slm = np.array(slm)
    umbrales = np.arange(2, 12.01, 0.1)

    fig, ax = plt.subplots(figsize=(6.8, 3.8))
    ax.semilogy(umbrales, ccdf(base, umbrales), color=COLORES[5],
                lw=1.8, label="sin SLM")
    ax.semilogy(umbrales, ccdf(slm, umbrales), color=COLORES[4], lw=1.8,
                label=f"SLM, $M={M}$")
    ax.set_xlabel("PAPR (dB)")
    ax.set_ylabel("CCDF")
    ax.set_title(f"Reducción de PAPR por fase aleatoria ($K={K}$)")
    ax.legend(loc="upper right")
    guardar(fig, FIGS / "p7_slm.png")

    return {"K": K, "M": M,
            "media_sin_db": float(base.mean()),
            "media_con_db": float(slm.mean()),
            "mejora_db": float(base.mean() - slm.mean())}


# --------------------------------------------------------------------- main
def main():
    resultados = {
        "problema1": problema1(),
        "problema2": problema2(),
        "problema3": problema3(),
        "problema4": problema4(),
        "problema5": problema5(),
        "problema6": problema6(),
        "problema7": problema7(),
    }
    guardar_json(resultados, DATOS / "resultados.json")
    print(json.dumps(resultados, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
