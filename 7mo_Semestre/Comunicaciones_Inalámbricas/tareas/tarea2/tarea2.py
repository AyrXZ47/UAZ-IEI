"""Tarea 2: capacidad de canal, codificacion y decodificacion.

Uso: python3 tarea2.py
"""

import json
import math
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import minimize, minimize_scalar
from scipy.special import erfc, i0e, logsumexp

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE.parents[0] / "comun"))
from estilo_graficas import COLORES, guardar, guardar_json, preparar  # noqa: E402

import matplotlib.pyplot as plt  # noqa: E402
import mplcyberpunk  # noqa: E402

plt.rcParams["figure.max_open_warning"] = 0
RNG = np.random.default_rng(7)
FIGS, DATOS = preparar(BASE)

# ------------------------------------------------------------------ utilidades


def qfunc(x):
    """Funcion Q(x) = P(N(0,1) > x)."""
    return 0.5 * erfc(np.asarray(x) / math.sqrt(2.0))


def hb(p):
    """Entropia binaria en bits.  Acepta escalares o arreglos."""
    p = np.clip(np.asarray(p, dtype=float), 0.0, 1.0)
    out = np.zeros_like(p)
    m = (p > 0) & (p < 1)
    out[m] = -p[m] * np.log2(p[m]) - (1 - p[m]) * np.log2(1 - p[m])
    return out


def hb_lista(p):
    """Entropia de una distribucion (ultimo eje) en bits."""
    p = np.asarray(p, dtype=float)
    out = np.zeros(p.shape[:-1])
    m = p > 0
    out = -np.sum(np.where(m, p * np.log2(np.where(m, p, 1)), 0), axis=-1)
    return out


def guardar_fig(fig, nombre, glow=True):
    """Guarda una figura con el estilo del repo y la deja abierta."""
    if glow:
        for ax in fig.axes:
            try:
                mplcyberpunk.add_glow_effects(ax)
            except Exception:
                pass
    return guardar(fig, FIGS / nombre, cerrar=False)


def dose(x):
    return 10 ** (np.asarray(x, dtype=float) / 10)


def sin_ceros(x):
    """Convierte BER=0 en NaN para no dibujar puntos fuera de escala."""
    x = np.asarray(x, dtype=float)
    return np.where(x > 0, x, np.nan)


# ---------------------------------------------------------------- 1. BSC
def problema1():
    p = np.linspace(0, 1, 501)
    C = 1 - hb(p)
    fig, ax = plt.subplots(figsize=(6.2, 3.4))
    ax.plot(p, C, color=COLORES[0], lw=2)
    ax.axvline(0.5, color=COLORES[1], ls="--", lw=1.2)
    ax.plot([0.5], [0], "o", color=COLORES[1], ms=7)
    ax.annotate("minimo en $p=1/2$\n$C=0$", xy=(0.5, 0), xytext=(0.58, 0.25),
                arrowprops=dict(arrowstyle="->", color=COLORES[1]),
                color=COLORES[1], fontsize=9)
    ax.set_xlabel("$p$")
    ax.set_ylabel("$C$ (bits/uso)")
    ax.set_title("Capacidad del canal simetrico binario")
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.02, 1.02)
    ax.grid(True, alpha=0.35)
    fig.tight_layout()
    guardar_fig(fig, "p01_bsc.png")
    return {"C_max": 1.0, "p_min": 0.5, "C_min": 0.0,
            "C_0.1": float(1 - hb(0.1)), "C_0.25": float(1 - hb(0.25))}


# --------------------------------------------------- 2. canal no simetrico
P2 = np.array([[0.6, 0.4], [0.2, 0.8]])


def i_problema2(p):
    px = np.array([1 - p, p])
    py = px @ P2
    return hb_lista(py) - px @ hb_lista(P2)


def problema2():
    p = np.linspace(0, 1, 1001)
    I = np.array([i_problema2(x) for x in p])
    res = minimize_scalar(lambda x: -i_problema2(x), bounds=(0, 1),
                          method="bounded")
    pmax, imax = float(res.x), float(-res.fun)
    fig, ax = plt.subplots(figsize=(6.2, 3.4))
    ax.plot(p, I, color=COLORES[0], lw=2)
    ax.plot([pmax], [imax], "o", color=COLORES[1], ms=7)
    ax.annotate(f"$p^*={pmax:.4f}$\n$I={imax:.4f}$ bits",
                xy=(pmax, imax), xytext=(pmax + 0.12, imax - 0.12),
                arrowprops=dict(arrowstyle="->", color=COLORES[1]),
                color=COLORES[1], fontsize=9)
    ax.set_xlabel("$p=P(X=1)$")
    ax.set_ylabel("$I(X:Y)$ (bits)")
    ax.set_title("Canal binario no simetrico")
    ax.grid(True, alpha=0.35)
    fig.tight_layout()
    guardar_fig(fig, "p02_no_simetrico.png")
    return {"p_optimo": pmax, "I_max": imax,
            "H_0": float(hb(0.4)), "H_1": float(hb(0.2))}


# ---------------------------------------------------------------- 3. canal Z
def i_canal_z(p, eps):
    py0 = 1 - p * (1 - eps)
    return hb(py0) - p * hb(eps)


def problema3():
    epsilons = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 0.9, 1]
    p = np.linspace(0, 1, 1001)
    fig, ax = plt.subplots(figsize=(7.0, 4.0))
    capacidades = {}
    for k, eps in enumerate(epsilons):
        I = np.array([i_canal_z(x, eps) for x in p])
        res = minimize_scalar(lambda x: -i_canal_z(x, eps), bounds=(0, 1),
                              method="bounded")
        C = float(-res.fun)
        p_opt = float(res.x)
        capacidades[f"eps_{eps:g}"] = {"C": C, "p_opt": p_opt}
        ax.plot(p, I, color=COLORES[k % len(COLORES)], lw=1.25,
                label=rf"$\epsilon={eps:g}$: $C={C:.3f}$")
    ax.set_xlabel("$p=P(X=1)$")
    ax.set_ylabel("$I(X:Y)$ (bits)")
    ax.set_title("Informacion mutua del canal Z")
    ax.legend(fontsize=7, ncol=2, loc="lower center")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    guardar_fig(fig, "p03_z.png")
    return capacidades


# ------------------------------------------- 4. entrada binaria, salida ternaria
P4 = np.array([[0.05, 0.20, 0.75], [0.10, 0.10, 0.80]])


def i_problema4(p):
    px = np.array([1 - p, p])
    py = px @ P4
    return hb_lista(py) - px @ hb_lista(P4)


def problema4():
    p = np.linspace(0, 1, 1001)
    I = np.array([i_problema4(x) for x in p])
    res = minimize_scalar(lambda x: -i_problema4(x), bounds=(0, 1),
                          method="bounded")
    pmax, imax = float(res.x), float(-res.fun)
    fig, ax = plt.subplots(figsize=(6.2, 3.4))
    ax.plot(p, I, color=COLORES[0], lw=2)
    ax.plot([pmax], [imax], "s", color=COLORES[1], ms=7)
    ax.annotate(f"$p^*={pmax:.4f}$\n$C={imax:.4f}$ bits",
                xy=(pmax, imax), xytext=(pmax + 0.12, imax * 0.55),
                arrowprops=dict(arrowstyle="->", color=COLORES[1]),
                color=COLORES[1], fontsize=9)
    ax.set_xlabel("$p=P(X=1)$")
    ax.set_ylabel("$I(X:Y)$ (bits)")
    ax.set_title("Canal binario con salida ternaria")
    ax.grid(True, alpha=0.35)
    fig.tight_layout()
    guardar_fig(fig, "p04_binario_ternario.png")
    return {"p_optimo": pmax, "C": imax}


# ------------------------------------------- 5. entrada ternaria, salida binaria
P5 = np.array([[0.05, 0.95], [0.80, 0.20], [0.10, 0.90]])


def i_problema5(p1, p2):
    px = np.array([1 - p1 - p2, p1, p2])
    if np.any(px < -1e-12):
        return -np.inf
    py = px @ P5
    return hb_lista(py) - px @ hb_lista(P5)


def problema5():
    n = 401
    p1 = np.linspace(0, 1, n)
    p2 = np.linspace(0, 1, n)
    P1, P2 = np.meshgrid(p1, p2)
    valido = P1 + P2 <= 1
    I = np.full_like(P1, np.nan)
    for i in range(n):
        for j in range(n):
            if valido[i, j]:
                I[i, j] = i_problema5(P1[i, j], P2[i, j])
    res = minimize(lambda x: -i_problema5(x[0], x[1]), x0=[0.3, 0.3],
                   method="SLSQP",
                   bounds=[(0, 1), (0, 1)],
                   constraints=[{"type": "ineq",
                                 "fun": lambda x: 1 - x[0] - x[1]}])
    p1opt, p2opt = float(res.x[0]), float(res.x[1])
    C = float(-res.fun)
    fig, ax = plt.subplots(figsize=(5.6, 4.4))
    cs = ax.contourf(P1, P2, I, levels=25, cmap="magma")
    fig.colorbar(cs, ax=ax, label="$I(X:Y)$ (bits)")
    ax.plot([p1opt], [p2opt], "*", color=COLORES[0], ms=15,
            markeredgecolor="white")
    ax.annotate(f"$p_1^*={p1opt:.3f}$\n$p_2^*={p2opt:.3f}$\n$C={C:.4f}$",
                xy=(p1opt, p2opt), xytext=(p1opt + 0.12, p2opt + 0.20),
                color="white", fontsize=9,
                arrowprops=dict(arrowstyle="->", color="white"))
    ax.set_xlabel("$p_1=P(X=1)$")
    ax.set_ylabel("$p_2=P(X=2)$")
    ax.set_title("Canal ternario con salida binaria")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    fig.tight_layout()
    guardar_fig(fig, "p05_ternario_binario.png", glow=False)
    return {"p1_optimo": p1opt, "p2_optimo": p2opt, "C": C,
            "p0_optimo": 1 - p1opt - p2opt}


# ------------------------------------------- 6. BSC con senalizacion ortogonal
def capacidad_bsc_desde_pe(pe):
    return 1 - hb(pe)


def problema6():
    ebn0_db = np.linspace(-2, 16, 400)
    g = dose(ebn0_db)
    pe = qfunc(np.sqrt(g))
    C = capacidad_bsc_desde_pe(pe)
    fig, ax = plt.subplots(figsize=(6.2, 3.4))
    ax.plot(ebn0_db, C, color=COLORES[0], lw=2)
    ax.axhline(1, color=COLORES[5], ls=":", lw=1)
    ax.set_xlabel("$E_b/N_0$ (dB)")
    ax.set_ylabel("$C$ (bits/uso)")
    ax.set_title("Capacidad con senalizacion ortogonal binaria")
    ax.grid(True, alpha=0.35)
    fig.tight_layout()
    guardar_fig(fig, "p06_ortogonal.png")
    return {"C_0dB": float(capacidad_bsc_desde_pe(qfunc(1))),
            "C_6dB": float(capacidad_bsc_desde_pe(qfunc(np.sqrt(dose(6))))),
            "C_10dB": float(capacidad_bsc_desde_pe(qfunc(np.sqrt(dose(10)))))}


# ------------------------------------------- 7. antipodal contra ortogonal
def capacidad_suave(mean_llr, var_llr):
    """C = 1 - E[log2(1+exp(-L))], con L=log p(y|0)/p(y|1) bajo X=0."""
    nodos, pesos = np.polynomial.hermite.hermgauss(120)
    L = mean_llr + math.sqrt(2 * var_llr) * nodos
    return 1 - np.sum(pesos * np.logaddexp(0, -L) / math.sqrt(math.pi)) / math.log(2)


def _cruce_05(eje, C):
    idx = np.argmin(np.abs(np.asarray(C) - 0.5))
    return float(np.asarray(eje)[idx])


def problema7():
    """Ilustrativo 3: capacidad AWGN binaria, antipodal contra ortogonal."""
    a_db = np.linspace(-10, 20, 500)
    a = 10 ** (a_db / 20)
    # Antipodal: L|0 ~ N(2a^2, 4a^2); ortogonal: L|0 ~ N(a^2, 2a^2)
    C_ant = np.array([capacidad_suave(2 * x ** 2, 4 * x ** 2) for x in a])
    C_ort = np.array([capacidad_suave(x ** 2, 2 * x ** 2) for x in a])
    fig, ax = plt.subplots(figsize=(6.4, 3.4))
    ax.plot(a_db, C_ant, color=COLORES[0], lw=2,
            label="antipodal (ilustrativo 3)")
    ax.plot(a_db, C_ort, color=COLORES[1], lw=2,
            label="ortogonal de igual energia")
    ax.axhline(0.5, color=COLORES[5], ls=":", lw=1)
    cruce_ant, cruce_ort = _cruce_05(a_db, C_ant), _cruce_05(a_db, C_ort)
    ax.plot([cruce_ant, cruce_ort], [0.5, 0.5], "o", color=COLORES[2], ms=5)
    ax.annotate(f"{cruce_ort - cruce_ant:.2f} dB",
                xy=(0.5 * (cruce_ant + cruce_ort), 0.53),
                color=COLORES[2], fontsize=9, ha="center")
    ax.set_xlabel("$A/\\sigma$ (dB)")
    ax.set_ylabel("$C$ (bits/uso)")
    ax.set_title("Capacidad AWGN binaria: antipodal contra ortogonal")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.35)
    fig.tight_layout()
    guardar_fig(fig, "p07_antipodal_ortogonal.png")
    return {"A_sigma_C0.5_antipodal_dB": cruce_ant,
            "A_sigma_C0.5_ortogonal_dB": cruce_ort,
            "penalizacion_dB": cruce_ort - cruce_ant}


# ------------------------------- 8. decision dura contra decision suave
def problema8():
    """Ilustrativo 4: capacidad con decision dura y suave, A/sigma."""
    a_db = np.linspace(-10, 18, 400)
    a = 10 ** (a_db / 20)
    C_ant_dura = capacidad_bsc_desde_pe(qfunc(a))
    C_ort_dura = capacidad_bsc_desde_pe(qfunc(a / math.sqrt(2)))
    C_ort_suave = np.array([capacidad_suave(x ** 2, 2 * x ** 2) for x in a])
    C_ant_suave = np.array([capacidad_suave(2 * x ** 2, 4 * x ** 2) for x in a])
    fig, ax = plt.subplots(figsize=(6.8, 3.8))
    ax.plot(a_db, C_ort_dura, "--", color=COLORES[0], lw=1.6,
            label="ortogonal, decision dura")
    ax.plot(a_db, C_ort_suave, color=COLORES[0], lw=2,
            label="ortogonal, decision suave")
    ax.plot(a_db, C_ant_dura, "--", color=COLORES[1], lw=1.6,
            label="antipodal, decision dura")
    ax.plot(a_db, C_ant_suave, color=COLORES[1], lw=2,
            label="antipodal, decision suave")
    ax.set_xlabel("$A/\\sigma$ (dB)")
    ax.set_ylabel("$C$ (bits/uso)")
    ax.set_title("Capacidad con decision dura y suave")
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.35)
    fig.tight_layout()
    guardar_fig(fig, "p08_decisiones.png")
    a6 = 10 ** (6 / 20)
    return {"C_ort_dura_6dB": float(capacidad_bsc_desde_pe(qfunc(a6 / math.sqrt(2)))),
            "C_ort_suave_6dB": float(capacidad_suave(a6 ** 2, 2 * a6 ** 2)),
            "C_ant_dura_6dB": float(capacidad_bsc_desde_pe(qfunc(a6))),
            "C_ant_suave_6dB": float(capacidad_suave(2 * a6 ** 2, 4 * a6 ** 2))}


# ------------------------- 9. ortogonal coherente contra no coherente
def problema9():
    ebn0_db = np.linspace(-2, 16, 400)
    g = dose(ebn0_db)
    p_coh = qfunc(np.sqrt(g))
    p_ncoh = 0.5 * np.exp(-g / 2)
    C_coh = capacidad_bsc_desde_pe(p_coh)
    C_ncoh = capacidad_bsc_desde_pe(p_ncoh)
    fig, ax = plt.subplots(figsize=(6.4, 3.4))
    ax.plot(ebn0_db, C_coh, color=COLORES[0], lw=2, label="coherente")
    ax.plot(ebn0_db, C_ncoh, color=COLORES[1], lw=2, label="no coherente")
    ax.set_xlabel("$E_b/N_0$ (dB)")
    ax.set_ylabel("$C$ (bits/uso)")
    ax.set_title("Ortogonal: deteccion coherente y no coherente")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.35)
    fig.tight_layout()
    guardar_fig(fig, "p09_coherente_no_coherente.png")
    return {"C_coh_10dB": float(capacidad_bsc_desde_pe(qfunc(np.sqrt(dose(10))))),
            "C_ncoh_10dB": float(capacidad_bsc_desde_pe(0.5 * np.exp(-dose(10) / 2)))}


# --------------------------------------------------- 10. codigos de Hamming
def hamming_matrices(m):
    """G sistematica (k x n) y H (m x n) para el codigo de Hamming."""
    n = 2 ** m - 1
    k = n - m
    ident = np.eye(m, dtype=int)
    unitarios = {1 << i for i in range(m)}
    columnas = [v for v in range(1, n + 1) if v not in unitarios]
    A = np.array([[(v >> i) & 1 for v in columnas] for i in range(m)],
                 dtype=int)
    H = np.concatenate([A, ident], axis=1) % 2
    G = np.concatenate([np.eye(k, dtype=int), A.T], axis=1) % 2
    return G, H


def tabla_lideres(H):
    """Lider de cada clase lateral indexado por el sindrome entero."""
    m, n = H.shape
    lideres = np.zeros((1 << m, n), dtype=int)
    pesos = np.full(1 << m, 99, dtype=int)
    for e in range(1 << n):
        vec = np.array([(e >> i) & 1 for i in range(n)], dtype=int)
        s = (H @ vec) % 2
        s_int = int(s @ (1 << np.arange(m)))
        w = int(vec.sum())
        if w < pesos[s_int]:
            pesos[s_int] = w
            lideres[s_int] = vec
    return lideres


def codificar_bloques(info, G):
    return (info @ G) % 2


def ber_hamming_dura(p, G, H, lideres):
    """BER exacta con decision dura y lideres de clase lateral."""
    n, k = H.shape[1], G.shape[0]
    ber = 0.0
    for e in range(1 << n):
        vec = np.array([(e >> i) & 1 for i in range(n)], dtype=int)
        s = (H @ vec) % 2
        s_int = int(s @ (1 << np.arange(H.shape[0])))
        ehat = lideres[s_int]
        errores = int(np.bitwise_xor(vec, ehat)[:k].sum())
        w = int(vec.sum())
        ber += p ** w * (1 - p) ** (n - w) * errores
    return ber / k


def decodificar_dura(R, H, lideres):
    m = H.shape[0]
    s = (R @ H.T) % 2
    s_int = s @ (1 << np.arange(m))
    return np.bitwise_xor(R, lideres[s_int])


def codewords(G):
    k, n = G.shape
    mensajes = np.array([[(i >> j) & 1 for j in range(k)]
                         for i in range(1 << k)], dtype=int)
    return (mensajes @ G) % 2


def decodificar_suave(L, C):
    """Decodificacion ML por correlacion con las palabras del codigo."""
    metricas = L @ (1 - 2 * C).T
    idx = np.argmax(metricas, axis=1)
    return C[idx]


def problema10():
    matrices = {}
    fig, axes = plt.subplots(2, 2, figsize=(8.4, 6.0))
    for ax, m in zip(axes.ravel(), [2, 3, 4, 5]):
        G, H = hamming_matrices(m)
        assert np.all((G @ H.T) % 2 == 0)
        n, k = H.shape[1], G.shape[0]
        matrices[f"m_{m}"] = {
            "n": n, "k": k, "tasa": k / n,
            "G": G.tolist(), "H": H.tolist(),
        }
        ax.pcolormesh(G, cmap="Greys", vmin=0, vmax=1,
                      edgecolors="#8d99ae", linewidth=0.35)
        ax.invert_yaxis()
        paso_x = max(1, G.shape[1] // 8)
        paso_y = max(1, G.shape[0] // 8)
        xt = np.arange(0, G.shape[1], paso_x)
        yt = np.arange(0, G.shape[0], paso_y)
        ax.set_xticks(xt + 0.5)
        ax.set_xticklabels(xt, fontsize=7)
        ax.set_yticks(yt + 0.5)
        ax.set_yticklabels(yt, fontsize=7)
        ax.set_title(rf"$m={m}$: $({n},{k})$")
        ax.set_xlabel("columna")
        ax.set_ylabel("fila")
    fig.suptitle("Matrices generadoras sistematicas de Hamming")
    fig.tight_layout()
    guardar_fig(fig, "p10_hamming.png", glow=False)
    return matrices


# --------------------------------------- 11. Hamming (15,11) con senalizacion ortogonal
def _cota_dura_bloque(p, k, dmin):
    """Cota (M-1)[4p(1-p)]^(dmin/2) de las notas."""
    return (2 ** k - 1) * (4 * p * (1 - p)) ** (dmin / 2)


def problema11():
    """Ilustrativo 10/11: Hamming (15,11) con decision dura."""
    k, n, dmin = 11, 15, 3
    R = k / n
    ebn0_db = np.linspace(0, 16, 161)
    g = dose(ebn0_db)
    p_ant = qfunc(np.sqrt(2 * R * g))
    p_coh = qfunc(np.sqrt(R * g))
    p_nc = 0.5 * np.exp(-R * g / 2)
    c_ant_raw = _cota_dura_bloque(p_ant, k, dmin)
    c_coh_raw = _cota_dura_bloque(p_coh, k, dmin)
    c_nc_raw = _cota_dura_bloque(p_nc, k, dmin)
    c_ant = np.minimum(c_ant_raw, 1.0)
    c_coh = np.minimum(c_coh_raw, 1.0)
    c_nc = np.minimum(c_nc_raw, 1.0)
    fig, ax = plt.subplots(figsize=(6.8, 3.8))
    ax.semilogy(ebn0_db, c_ant, color=COLORES[0], lw=2,
                label="antipodal (ilustrativo 10)")
    ax.semilogy(ebn0_db, c_coh, color=COLORES[1], lw=2,
                label="ortogonal coherente")
    ax.semilogy(ebn0_db, c_nc, color=COLORES[2], lw=2,
                label="ortogonal no coherente")
    ax.set_xlabel("$E_b/N_0$ (dB)")
    ax.set_ylabel("$P_e$ (cota de mensaje)")
    ax.set_title("Hamming (15,11) con decision dura")
    ax.set_ylim(1e-18, 1.15)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3, which="both")
    fig.tight_layout()
    guardar_fig(fig, "p11_hamming_ortogonal.png")
    idx = np.argmin(np.abs(ebn0_db - 10))
    return {"R": R, "cota_ant_10dB": float(c_ant_raw[idx]),
            "cota_coh_10dB": float(c_coh_raw[idx]),
            "cota_nc_10dB": float(c_nc_raw[idx])}


# --------------------------------------- 12. Monte Carlo Hamming (15,11) con BPSK
def simular_hamming_dura_15(ebn0_db, nbits=300000, rng=None):
    rng = rng or RNG
    G, H = hamming_matrices(4)
    lideres = tabla_lideres(H)
    R = G.shape[0] / H.shape[1]
    g = dose(ebn0_db)
    N0 = 1 / g
    sigma = math.sqrt(N0 / 2)
    nblocks = nbits // G.shape[0]
    info = rng.integers(0, 2, (nblocks, G.shape[0]))
    code = codificar_bloques(info, G)
    y = math.sqrt(R) * (1 - 2 * code) + \
        sigma * rng.standard_normal(code.shape)
    duros = (y < 0).astype(int)
    dec = decodificar_dura(duros, H, lideres)[:, :G.shape[0]]
    return float(np.sum(dec != info)) / (nblocks * G.shape[0])


def problema12():
    """Monte Carlo del ilustrativo 10: Hamming (15,11) antipodal y dura."""
    k, n, dmin = 11, 15, 3
    R = k / n
    ebn0_db = np.arange(0, 11, 1.0)
    mc = np.array([simular_hamming_dura_15(x) for x in ebn0_db])
    p = qfunc(np.sqrt(2 * R * dose(ebn0_db)))
    cota_raw = _cota_dura_bloque(p, k, dmin)
    cota = np.minimum(cota_raw, 1.0)
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.semilogy(ebn0_db, cota, color=COLORES[0], lw=2,
                label="cota (ilustrativo 10)")
    ax.semilogy(ebn0_db, sin_ceros(mc), "o", color=COLORES[1], ms=6,
                label="Monte Carlo")
    ax.set_xlabel("$E_b/N_0$ (dB)")
    ax.set_ylabel("BER")
    ax.set_title("Hamming (15,11), BPSK y decision dura")
    ax.set_ylim(1e-6, 1.15)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3, which="both")
    fig.tight_layout()
    guardar_fig(fig, "p12_hamming_mc.png")
    idx = np.argmin(np.abs(ebn0_db - 10))
    return {"mc": mc.tolist(), "cota": cota_raw.tolist(),
            "BER_10dB": float(mc[idx]), "cota_10dB": float(cota_raw[idx])}


# ------------------------------- 13. Hamming (15,11) con decision suave
def simular_hamming_suave_15(ebn0_db, tipo, nbits=30000, rng=None):
    """ML por correlacion para el Hamming (15,11)."""
    rng = rng or RNG
    G, H = hamming_matrices(4)
    C = codewords(G)
    R = G.shape[0] / H.shape[1]
    g = dose(ebn0_db)
    nblocks = nbits // G.shape[0]
    info = rng.integers(0, 2, (nblocks, G.shape[0]))
    code = codificar_bloques(info, G)
    if tipo == "antipodal":
        media, var = 4 * R * g, 8 * R * g
    else:
        media, var = 2 * R * g, 4 * R * g
    L = (1 - 2 * code) * media + math.sqrt(var) * \
        rng.standard_normal(code.shape)
    dec = decodificar_suave(L, C)[:, :G.shape[0]]
    return float(np.sum(dec != info)) / (nblocks * G.shape[0])


def problema13():
    """Ilustrativo 12 extendido a ortogonal coherente/no coherente."""
    k, n, dmin = 11, 15, 3
    M = 2 ** k - 1
    R = k / n
    ebn0_db = np.linspace(0, 16, 161)
    g = dose(ebn0_db)
    c_ant_raw = M * qfunc(np.sqrt(2 * dmin * R * g))
    c_coh_raw = M * qfunc(np.sqrt(dmin * R * g))
    c_nc_raw = M * 0.5 * np.exp(-dmin * R * g / 2)
    c_ant = np.minimum(c_ant_raw, 1.0)
    c_coh = np.minimum(c_coh_raw, 1.0)
    c_nc = np.minimum(c_nc_raw, 1.0)
    fig, ax = plt.subplots(figsize=(6.8, 3.8))
    ax.semilogy(ebn0_db, c_ant, color=COLORES[0], lw=2,
                label="antipodal, suave")
    ax.semilogy(ebn0_db, c_coh, color=COLORES[1], lw=2,
                label="ortogonal coherente, suave")
    ax.semilogy(ebn0_db, c_nc, color=COLORES[2], lw=2,
                label="ortogonal no coherente, suave")
    ax.set_xlabel("$E_b/N_0$ (dB)")
    ax.set_ylabel("$P_e$ (cota de mensaje)")
    ax.set_title("Hamming (15,11) con decision suave")
    ax.set_ylim(1e-18, 1.15)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3, which="both")
    fig.tight_layout()
    guardar_fig(fig, "p13_hamming_suave.png")
    idx = np.argmin(np.abs(ebn0_db - 10))
    return {"cota_ant_10dB": float(c_ant_raw[idx]),
            "cota_coh_10dB": float(c_coh_raw[idx]),
            "cota_nc_10dB": float(c_nc_raw[idx])}


def problema14():
    """Monte Carlo del ilustrativo 12: Hamming (15,11) con decision suave."""
    ebn0_db = np.array([0, 2, 4, 6, 8, 10], dtype=float)
    rng = np.random.default_rng(99)
    mc_ant = np.array([simular_hamming_suave_15(x, "antipodal", 30000, rng)
                       for x in ebn0_db])
    mc_ort = np.array([simular_hamming_suave_15(x, "ortogonal", 30000, rng)
                       for x in ebn0_db])
    k, n, dmin = 11, 15, 3
    M = 2 ** k - 1
    R = k / n
    g = dose(ebn0_db)
    c_ant_raw = M * qfunc(np.sqrt(2 * dmin * R * g))
    c_ort_raw = M * qfunc(np.sqrt(dmin * R * g))
    c_ant = np.minimum(c_ant_raw, 1.0)
    c_ort = np.minimum(c_ort_raw, 1.0)
    fig, ax = plt.subplots(figsize=(6.8, 3.8))
    ax.semilogy(ebn0_db, c_ant, color=COLORES[0], lw=1.4,
                label="cota antipodal")
    ax.semilogy(ebn0_db, c_ort, color=COLORES[1], lw=1.4,
                label="cota ortogonal")
    ax.semilogy(ebn0_db, sin_ceros(mc_ant), "o", color=COLORES[0], ms=6,
                label="MC antipodal")
    ax.semilogy(ebn0_db, sin_ceros(mc_ort), "s", color=COLORES[1], ms=6,
                label="MC ortogonal")
    ax.set_xlabel("$E_b/N_0$ (dB)")
    ax.set_ylabel("BER")
    ax.set_title("Monte Carlo de la decision suave (ilustrativo 12)")
    ax.set_ylim(1e-6, 1.15)
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3, which="both")
    fig.tight_layout()
    guardar_fig(fig, "p14_hamming_suave_mc.png")
    return {"ebn0_db": ebn0_db.tolist(),
            "mc_ant": mc_ant.tolist(), "mc_ort": mc_ort.tolist(),
            "cota_ant": c_ant_raw.tolist(), "cota_ort": c_ort_raw.tolist()}


# ------------------------------------------------ 15-20. convolucionales
G1, G2, K = 0b101, 0b111, 3


def _bits_gen(g, K):
    return [(g >> (K - 1 - i)) & 1 for i in range(K)]


def conv_trellis(g1=G1, g2=G2, K=K):
    """Trellis no recursivo: estado = K-1 bits previos (MSB primero)."""
    nstates = 1 << (K - 1)
    gen1, gen2 = _bits_gen(g1, K), _bits_gen(g2, K)
    trellis = []
    for s in range(nstates):
        estado = [(s >> (K - 2 - i)) & 1 for i in range(K - 1)]
        fila = []
        for u in (0, 1):
            reg = [u] + estado
            o1 = sum(a * b for a, b in zip(reg, gen1)) % 2
            o2 = sum(a * b for a, b in zip(reg, gen2)) % 2
            nuevo = [u] + estado[:-1]
            ns = sum(b << (K - 2 - i) for i, b in enumerate(nuevo))
            fila.append((ns, (o1, o2)))
        trellis.append(fila)
    return trellis


def conv_encode(bits, g1=G1, g2=G2, K=K):
    """Codificador convolucional rate 1/2, estado inicial cero."""
    trellis = conv_trellis(g1, g2, K)
    s = 0
    salida = []
    for u in bits:
        s, (o1, o2) = trellis[s][int(u)]
        salida.extend([o1, o2])
    return np.array(salida, dtype=int)


def viterbi(received, trellis, hard=True):
    """Viterbi para rate 1/2.  received: (T,2) bits o simbolos BPSK."""
    T = len(received)
    nstates = len(trellis)
    met = np.full(nstates, np.inf)
    met[0] = 0.0
    prev_s = np.zeros((T, nstates), dtype=int)
    prev_u = np.zeros((T, nstates), dtype=int)
    for t in range(T):
        nuevo = np.full(nstates, np.inf)
        for s in range(nstates):
            if not np.isfinite(met[s]):
                continue
            for u in (0, 1):
                ns, out = trellis[s][u]
                if hard:
                    costo = int(out[0] != received[t, 0]) + \
                        int(out[1] != received[t, 1])
                else:
                    costo = -sum(received[t, i] * (1 - 2 * out[i])
                                 for i in range(2))
                if met[s] + costo < nuevo[ns]:
                    nuevo[ns] = met[s] + costo
                    prev_s[t, ns] = s
                    prev_u[t, ns] = u
        met = nuevo
    s = int(np.argmin(met))
    bits = np.zeros(T, dtype=int)
    for t in range(T - 1, -1, -1):
        bits[t] = prev_u[t, s]
        s = prev_s[t, s]
    return bits, float(np.min(met))


def _pares(bits):
    return np.asarray(bits).reshape(-1, 2)


def problema15():
    entrada = np.array([int(c) for c in "110010101010010111101011111010"])
    salida = conv_encode(entrada)
    fig, axes = plt.subplots(3, 1, figsize=(8.0, 4.2), sharex=True)
    axes[0].step(np.arange(len(entrada)), entrada, where="post",
                 color=COLORES[0], lw=1.4)
    axes[0].set_ylabel("$u_n$")
    axes[0].set_ylim(-0.2, 1.2)
    axes[1].step(np.arange(0, len(salida), 2), salida[0::2], where="post",
                 color=COLORES[1], lw=1.4)
    axes[1].set_ylabel("$o_{1,n}$")
    axes[1].set_ylim(-0.2, 1.2)
    axes[2].step(np.arange(0, len(salida), 2), salida[1::2], where="post",
                 color=COLORES[2], lw=1.4)
    axes[2].set_ylabel("$o_{2,n}$")
    axes[2].set_ylim(-0.2, 1.2)
    axes[2].set_xlabel("$n$")
    fig.suptitle("Codificador convolucional de la Figura 18")
    fig.tight_layout()
    guardar_fig(fig, "p15_convolucional.png")
    return {"entrada": "".join(map(str, entrada)),
            "salida": "".join(map(str, salida)),
            "longitud_entrada": int(len(entrada)),
            "longitud_salida": int(len(salida)),
            "generadores": {"g1": format(G1, "03b"), "g2": format(G2, "03b")}}


def cnv_encd(g, k0, input_bits):
    """Codificador convolucional de las notas (equivalente a cnv_encd.m).

    g es la matriz generadora n0 x (k0*L); las filas son g1,...,gn0.
    Agrega (L-1)*k0 ceros al final para regresar al estado cero.
    """
    g = np.asarray(g, dtype=int)
    inp = list(map(int, input_bits))
    if len(inp) % k0:
        inp += [0] * (k0 - len(inp) % k0)
    n = len(inp) // k0
    l = g.shape[1] // k0
    n0 = g.shape[0]
    u = [0] * ((l - 1) * k0) + inp + [0] * ((l - 1) * k0)
    u1 = u[l * k0 - 1::-1]
    for i in range(1, n + l - 1):
        start = (i + l) * k0 - 1
        stop = i * k0
        u1 += u[start:stop - 1:-1]
    uu = np.array(u1).reshape((l * k0, n + l - 1), order="F")
    salida = (g @ uu) % 2
    return salida.flatten(order="F").astype(int)


def problema16():
    G = np.array([[1, 0, 1, 1],
                  [0, 1, 1, 0],
                  [1, 1, 0, 1],
                  [1, 1, 1, 1]], dtype=int)
    entrada = np.array([int(c) for c in "110010101010010111101011111010"])
    salida1 = cnv_encd(G, 1, entrada)
    salida2 = cnv_encd(G, 2, entrada)
    fig, axes = plt.subplots(1, 3, figsize=(10.6, 3.2))
    axes[0].imshow(G, cmap="Greys", vmin=0, vmax=1, aspect="auto")
    axes[0].set_title("Matriz $G$")
    axes[0].set_xticks(range(4))
    axes[0].set_yticks(range(4))
    axes[0].set_xlabel("salida")
    axes[0].set_ylabel("coeficiente / entrada")
    axes[1].step(np.arange(60), salida1[:60], where="post",
                 color=COLORES[0], lw=1.1)
    axes[1].set_title(f"$k=1$: primeros 60 de {len(salida1)} bits")
    axes[1].set_xlabel("bit de salida")
    axes[1].set_ylim(-0.2, 1.2)
    axes[2].step(np.arange(60), salida2[:60], where="post",
                 color=COLORES[1], lw=1.1)
    axes[2].set_title(f"$k=2$: primeros 60 de {len(salida2)} bits")
    axes[2].set_xlabel("bit de salida")
    axes[2].set_ylim(-0.2, 1.2)
    fig.suptitle("Codigo del problema 16")
    fig.tight_layout()
    guardar_fig(fig, "p16_convolucional_g.png")
    return {"entrada": "".join(map(str, entrada)),
            "salida_k1": "".join(map(str, salida1)),
            "salida_k2": "".join(map(str, salida2)),
            "n_k1": int(len(salida1)), "n_k2": int(len(salida2))}


def problema17():
    entrada = np.array([int(c) for c in "110010101010010111101011111010"])
    codificada = conv_encode(entrada)
    trellis = conv_trellis()
    casos = {
        "sin errores": np.zeros_like(codificada),
        "primeros 6": np.r_[np.ones(6, dtype=int),
                            np.zeros(len(codificada) - 6, dtype=int)],
        "ultimos 6": np.r_[np.zeros(len(codificada) - 6, dtype=int),
                           np.ones(6, dtype=int)],
        "3 + 3": np.r_[np.ones(3, dtype=int),
                       np.zeros(len(codificada) - 6, dtype=int),
                       np.ones(3, dtype=int)],
    }
    resultados, errores = {}, {}
    for nombre, e in casos.items():
        recibida = np.bitwise_xor(codificada, e)
        dec, metrica = viterbi(_pares(recibida), trellis, hard=True)
        nerr = int(np.sum(dec != entrada))
        resultados[nombre] = {
            "errores": nerr,
            "metrica": metrica,
            "decodificada": "".join(map(str, dec)),
        }
        errores[nombre] = nerr
    fig, ax = plt.subplots(figsize=(6.6, 3.4))
    ax.bar(range(len(errores)), list(errores.values()),
           color=[COLORES[0], COLORES[1], COLORES[2], COLORES[3]])
    ax.set_xticks(range(len(errores)))
    ax.set_xticklabels(list(errores), fontsize=8)
    ax.set_ylabel("bits erroneos")
    ax.set_title("Viterbi con metrica de Hamming (30 bits de informacion)")
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    guardar_fig(fig, "p17_viterbi.png")
    return resultados


def problema18():
    rng = np.random.default_rng(21)
    trellis = conv_trellis()
    nbits = 1000
    probabilidades = [0.01, 0.05, 0.1, 0.2]
    resultados = {}
    for p in probabilidades:
        bers = []
        for _ in range(30):
            info = rng.integers(0, 2, nbits)
            cod = conv_encode(info)
            error = (rng.random(len(cod)) < p).astype(int)
            recibida = np.bitwise_xor(cod, error)
            dec, _ = viterbi(_pares(recibida), trellis, hard=True)
            bers.append(float(np.mean(dec != info)))
        resultados[f"p_{p:g}"] = {
            "media": float(np.mean(bers)),
            "std": float(np.std(bers)),
            "bers": bers,
        }
    fig, ax = plt.subplots(figsize=(6.4, 3.5))
    x = np.array(probabilidades)
    y = np.array([resultados[f"p_{p:g}"]["media"] for p in x])
    e = np.array([resultados[f"p_{p:g}"]["std"] for p in x])
    ax.errorbar(x, y, yerr=e, fmt="o-", color=COLORES[0], ms=6,
                capsize=3, label="Viterbi (30 corridas)")
    ax.semilogy(x, x, "--", color=COLORES[1], lw=1.2,
                label="sin codificar ($p$)")
    ax.set_xlabel("$p$ del canal binario simetrico")
    ax.set_ylabel("BER")
    ax.set_title("Codigo convolucional (5,7): 1000 bits")
    ax.set_ylim(1e-5, 1)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3, which="both")
    fig.tight_layout()
    guardar_fig(fig, "p18_viterbi_errores.png")
    return resultados


def _enumerador(g1=G1, g2=G2, K=K, L=14):
    """Cota truncada: enumera bloques terminados de L bits."""
    k = L - (K - 1)
    A = {}
    for i in range(1 << k):
        info = np.array([(i >> j) & 1 for j in range(k)], dtype=int)
        cod = conv_encode(np.r_[info, np.zeros(K - 1, dtype=int)], g1, g2, K)
        d = int(cod.sum())
        w = int(info.sum())
        if d:
            A[(w, d)] = A.get((w, d), 0) + 1
    return A, k, 2 * L


def _cota_suave(A, k, n, g):
    R = k / n
    total = 0.0
    for (w, d), cuenta in A.items():
        total += w * cuenta * qfunc(math.sqrt(2 * d * R * g))
    return total / k


def _cota_dura(A, k, n, p):
    total = 0.0
    for (w, d), cuenta in A.items():
        cola = 0.0
        for i in range((d + 1) // 2, d + 1):
            cola += math.comb(d, i) * p ** i * (1 - p) ** (d - i)
        total += w * cuenta * cola
    return total / k


def simular_conv(ebn0_db, hard, nbits=200000, rng=None):
    rng = rng or RNG
    trellis = conv_trellis()
    g = dose(ebn0_db)
    N0 = 1 / g
    sigma = math.sqrt(N0 / 2)
    info = rng.integers(0, 2, nbits)
    # termina con K-1 ceros para que el decodificador cierre en estado 0
    info_t = np.r_[info, np.zeros(K - 1, dtype=int)]
    cod = conv_encode(info_t)
    amp = math.sqrt(0.5)  # R = 1/2, Eb = 1
    simbolos = amp * (1 - 2 * cod)
    y = simbolos + sigma * rng.standard_normal(len(cod))
    if hard:
        recibida = _pares((y < 0).astype(int))
        dec, _ = viterbi(recibida, trellis, hard=True)
    else:
        dec, _ = viterbi(_pares(y), trellis, hard=False)
    return float(np.mean(dec[:nbits] != info))


def problema19():
    ebn0_db = np.arange(3, 10, 1.0)
    rng = np.random.default_rng(2026)
    hard = np.array([simular_conv(x, True, 500000, rng) for x in ebn0_db])
    suave = np.array([simular_conv(x, False, 500000, rng) for x in ebn0_db])
    A, k, n = _enumerador(L=14)
    g = dose(ebn0_db)
    p = qfunc(np.sqrt(2 * (k / n) * g))
    cota_s = np.array([_cota_suave(A, k, n, x) for x in g])
    cota_d = np.array([_cota_dura(A, k, n, x) for x in p])
    sin_cod = qfunc(np.sqrt(2 * g))
    fig, ax = plt.subplots(figsize=(6.8, 3.8))
    ax.semilogy(ebn0_db, sin_ceros(hard), "o", color=COLORES[0], ms=6,
                label="duro (MC)")
    ax.semilogy(ebn0_db, sin_ceros(suave), "s", color=COLORES[1], ms=6,
                label="suave (MC)")
    ax.semilogy(ebn0_db, cota_d, "--", color=COLORES[0], lw=1.2,
                label="cota dura (truncada)")
    ax.semilogy(ebn0_db, cota_s, "--", color=COLORES[1], lw=1.2,
                label="cota suave (truncada)")
    ax.semilogy(ebn0_db, sin_cod, ":", color=COLORES[5], lw=1.2,
                label="BPSK sin codificar")
    ax.set_xlabel("$E_b/N_0$ (dB)")
    ax.set_ylabel("BER")
    ax.set_title("Codigo convolucional (5,7) con Viterbi")
    ax.set_ylim(1e-6, 1)
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3, which="both")
    fig.tight_layout()
    guardar_fig(fig, "p19_convolucional_ber.png")
    return {"duro": hard.tolist(), "suave": suave.tolist(),
            "cota_duro": cota_d.tolist(), "cota_suave": cota_s.tolist(),
            "pesos": {f"{w}_{d}": v for (w, d), v in A.items()}}


def problema20():
    recibida = np.array([int(c) for c in
                         "02020110202112002220110101020220111112"])
    if len(recibida) % 2:
        recibida = recibida[:-1]
    logP = np.log(np.array([[0.90, 0.01, 0.09],
                            [0.01, 0.90, 0.09]]))
    trellis = conv_trellis()
    T = len(recibida) // 2
    met = np.full(len(trellis), np.inf)
    met[0] = 0.0
    prev_s = np.zeros((T, len(trellis)), dtype=int)
    prev_u = np.zeros((T, len(trellis)), dtype=int)
    for t in range(T):
        y1, y2 = recibida[2 * t], recibida[2 * t + 1]
        nuevo = np.full(len(trellis), np.inf)
        for s in range(len(trellis)):
            if not np.isfinite(met[s]):
                continue
            for u in (0, 1):
                ns, out = trellis[s][u]
                costo = -(logP[out[0], y1] + logP[out[1], y2])
                if met[s] + costo < nuevo[ns]:
                    nuevo[ns] = met[s] + costo
                    prev_s[t, ns] = s
                    prev_u[t, ns] = u
        met = nuevo
    s = int(np.argmin(met))
    bits = np.zeros(T, dtype=int)
    for t in range(T - 1, -1, -1):
        bits[t] = prev_u[t, s]
        s = prev_s[t, s]
    fig, axes = plt.subplots(2, 1, figsize=(8.0, 4.0), sharex=True)
    axes[0].step(np.arange(len(recibida)), recibida, where="post",
                 color=COLORES[0], lw=1.4)
    axes[0].set_ylabel("simbolo $y$")
    axes[0].set_ylim(-0.2, 2.2)
    axes[0].set_title("Recibida por el canal de 3 salidas")
    axes[1].step(np.arange(len(bits)), bits, where="post",
                 color=COLORES[1], lw=1.4)
    axes[1].set_ylabel("bit decodificado")
    axes[1].set_xlabel("$n$")
    axes[1].set_ylim(-0.2, 1.2)
    axes[1].set_title("Salida de Viterbi")
    for ax in axes:
        ax.grid(True, alpha=0.3)
    fig.tight_layout()
    guardar_fig(fig, "p20_viterbi_canal.png")
    return {"recibida": "".join(map(str, recibida)),
            "decodificada": "".join(map(str, bits)),
            "metrica": float(np.min(met)),
            "longitud": int(len(recibida))}


# ------------------------------------------- 21. max* de la ecuacion (80)
def maxstar(a, b):
    """max*(a,b) = max(a,b) + ln(1+exp(-|a-b|)) de la Ecuacion (80)."""
    return np.maximum(a, b) + np.log1p(np.exp(-np.abs(a - b)))


def problema21():
    rng = np.random.default_rng(5)
    a = rng.normal(0, 5, 20000)
    b = rng.normal(0, 5, 20000)
    c = rng.normal(0, 5, 20000)
    exacto2 = np.logaddexp(a, b)
    exacto3 = np.logaddexp(np.logaddexp(a, b), c)
    err2 = float(np.max(np.abs(maxstar(a, b) - exacto2)))
    err3 = float(np.max(np.abs(maxstar(maxstar(a, b), c) - exacto3)))
    err_asoc = float(np.max(np.abs(maxstar(maxstar(a, b), c) -
                                maxstar(a, maxstar(b, c)))))
    # error de la aproximacion max* ~ max
    delta = np.linspace(0, 10, 400)
    error_aprox = np.log1p(np.exp(-delta))
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.6))
    x = np.linspace(-6, 6, 400)
    axes[0].plot(x, maxstar(x, 0.0), color=COLORES[0], lw=2,
                 label=r"$\max^*(x,0)$")
    axes[0].plot(x, np.maximum(x, 0.0), "--", color=COLORES[1], lw=1.4,
                 label=r"$\max(x,0)$")
    axes[0].set_xlabel("$x$")
    axes[0].set_title(r"$\max^*(x,0)$ y su version aproximada")
    axes[0].legend(fontsize=8)
    axes[0].grid(True, alpha=0.3)
    axes[1].plot(delta, error_aprox, color=COLORES[2], lw=2)
    axes[1].set_xlabel(r"$|x-y|$")
    axes[1].set_ylabel(r"$\max^*-\max$")
    axes[1].set_title("Error de la aproximacion (maximo $\\ln 2$)")
    axes[1].grid(True, alpha=0.3)
    fig.tight_layout()
    guardar_fig(fig, "p21_identidades.png")
    return {"error_maxstar2": err2, "error_maxstar3": err3,
            "error_asociatividad": err_asoc,
            "error_maximo_aproximacion": float(np.log(2))}


# ------------------------------------------------- 22. entrelazador aleatorio
def entrelazador(N, seed=11):
    rng = np.random.default_rng(seed)
    perm = rng.permutation(N)
    return np.vstack([np.arange(1, N + 1), perm + 1])


def problema22():
    N = 2000
    matriz = entrelazador(N)
    assert np.array_equal(np.sort(matriz[1]), np.arange(1, N + 1))
    desplazamiento = matriz[1] - matriz[0]
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.6))
    axes[0].plot(matriz[0], matriz[1], ".", color=COLORES[0], ms=1.5,
                 alpha=0.6)
    axes[0].plot([1, N], [1, N], "--", color=COLORES[5], lw=1)
    axes[0].set_xlabel("posicion original")
    axes[0].set_ylabel("posicion entrelazada")
    axes[0].set_title(f"Entrelazador pseudoaleatorio, $N={N}$")
    axes[0].grid(True, alpha=0.3)
    axes[1].hist(desplazamiento, bins=60, color=COLORES[1], alpha=0.8)
    axes[1].set_xlabel("desplazamiento $\\pi(i)-i$")
    axes[1].set_ylabel("cuenta")
    axes[1].set_title("Distribucion del desplazamiento")
    axes[1].grid(True, alpha=0.3)
    fig.tight_layout()
    guardar_fig(fig, "p22_entrelazador.png")
    return {"N": N, "primeras_20_columnas": matriz[:, :20].tolist(),
            "desplazamiento_medio": float(desplazamiento.mean()),
            "desplazamiento_max": int(np.max(np.abs(desplazamiento)))}


# ----------------------------------------------------- 23. turbo codificador
def rsc_trellis():
    """Trellis de 8 estados del RSCC 5/7 de las notas (Figura 24)."""
    trellis = []
    for s in range(8):
        r1, r2, r3 = (s >> 2) & 1, (s >> 1) & 1, s & 1
        fila = []
        for u in (0, 1):
            r1t = (r3 + r2 + u) % 2
            ns = (r1t << 2) | (r1 << 1) | r2
            fila.append((ns, (u, (r1t + r2) % 2)))
        trellis.append(fila)
    return trellis


def rsc_encode(bits):
    """RSCC 5/7 exacto de las notas: r1'=u+r2+r3, c2=r1'+r2."""
    r1 = r2 = r3 = 0
    salida = []
    for u in np.asarray(bits, dtype=int):
        r1t = (r3 + r2 + u) % 2
        r3, r2, r1 = r2, r1, r1t
        salida.append((u, (r1 + r3) % 2))
    return np.array(salida, dtype=int)


def turbo_encode(bits, perm):
    bits = np.asarray(bits, dtype=int)
    c1 = rsc_encode(bits)
    c2 = rsc_encode(bits[perm])
    return np.column_stack([c1[:, 0], c1[:, 1], c2[:, 1]])


def problema23():
    rng = np.random.default_rng(13)
    N = 2000
    bits = rng.integers(0, 2, N)
    perm = rng.permutation(N)
    cod = turbo_encode(bits, perm)
    assert np.array_equal(cod[:, 0], bits)
    fig, axes = plt.subplots(3, 1, figsize=(8.0, 4.4), sharex=True)
    for ax, y, etiqueta, color in zip(
            axes, [cod[:, 0], cod[:, 1], cod[:, 2]],
            ["sistematico $u$", "paridad $p_1$", "paridad $p_2$"],
            [COLORES[0], COLORES[1], COLORES[2]]):
        ax.step(np.arange(80), y[:80], where="post", color=color, lw=1.3)
        ax.set_ylabel(etiqueta)
        ax.set_ylim(-0.2, 1.2)
    axes[-1].set_xlabel("$n$")
    fig.suptitle("Turbo codificador con RSC (5,7) y entrelazador aleatorio")
    fig.tight_layout()
    guardar_fig(fig, "p23_turbo_encoder.png")
    return {"N": N, "tasa": 1 / 3,
            "primeros_30": {
                "u": "".join(map(str, cod[:30, 0])),
                "p1": "".join(map(str, cod[:30, 1])),
                "p2": "".join(map(str, cod[:30, 2])),
            },
            "entrelazador_primeros_20": (perm[:20] + 1).tolist()}


# ------------------------------------------------------ 24. turbo decodificador
def bcjr_siso(Ls, Lp, La, trellis):
    """Decodificador SISO BCJR en el dominio logaritmico."""
    N = len(Ls)
    ns = len(trellis)
    gamma = np.empty((N, ns, 2))
    for t in range(N):
        for s in range(ns):
            for u in (0, 1):
                _, (su, p) = trellis[s][u]
                gamma[t, s, u] = 0.5 * (Ls[t] + La[t]) * (1 - 2 * su) + \
                    0.5 * Lp[t] * (1 - 2 * p)
    alpha = np.full((N + 1, ns), -np.inf)
    alpha[0, :] = 0.0
    for t in range(N):
        for s in range(ns):
            if not np.isfinite(alpha[t, s]):
                continue
            for u in (0, 1):
                nsiguiente, _ = trellis[s][u]
                alpha[t + 1, nsiguiente] = np.logaddexp(
                    alpha[t + 1, nsiguiente], alpha[t, s] + gamma[t, s, u])
        m = np.max(alpha[t + 1])
        if np.isfinite(m):
            alpha[t + 1] -= m
    beta = np.full((N + 1, ns), -np.inf)
    beta[N, :] = 0.0
    for t in range(N - 1, -1, -1):
        for s in range(ns):
            for u in (0, 1):
                nsiguiente, _ = trellis[s][u]
                beta[t, s] = np.logaddexp(
                    beta[t, s], gamma[t, s, u] + beta[t + 1, nsiguiente])
        m = np.max(beta[t])
        if np.isfinite(m):
            beta[t] -= m
    Lpost = np.zeros(N)
    for t in range(N):
        term0 = []
        term1 = []
        for s in range(ns):
            ns0, _ = trellis[s][0]
            ns1, _ = trellis[s][1]
            term0.append(alpha[t, s] + gamma[t, s, 0] + beta[t + 1, ns0])
            term1.append(alpha[t, s] + gamma[t, s, 1] + beta[t + 1, ns1])
        Lpost[t] = logsumexp(term0) - logsumexp(term1)
    Le = Lpost - Ls - La
    return Lpost, np.clip(Le, -30, 30)


def turbo_decode(Ls, Lp1, Lp2, perm, trellis, iteraciones=5):
    N = len(Ls)
    La1 = np.zeros(N)
    La2 = np.zeros(N)
    Lpost1 = np.zeros(N)
    for _ in range(iteraciones):
        Lpost1, Le1 = bcjr_siso(Ls, Lp1, La1, trellis)
        La2 = Le1[perm]
        _, Le2 = bcjr_siso(Ls[perm], Lp2, La2, trellis)
        La1 = np.empty(N)
        La1[perm] = Le2
    return (Lpost1 < 0).astype(int), Lpost1


def simular_turbo(ebn0_db, iteraciones=5, N=500, nblocks=5, rng=None):
    rng = rng or RNG
    trellis = rsc_trellis()
    g = dose(ebn0_db)
    N0 = 1 / g
    sigma = math.sqrt(N0 / 2)
    amp = math.sqrt(1 / 3)
    errores = 0
    total = 0
    for _ in range(nblocks):
        bits = rng.integers(0, 2, N)
        perm = rng.permutation(N)
        cod = turbo_encode(bits, perm)
        y = amp * (1 - 2 * cod) + sigma * rng.standard_normal(cod.shape)
        L = 2 * amp * y / sigma ** 2
        dec, _ = turbo_decode(L[:, 0], L[:, 1], L[:, 2], perm, trellis,
                              iteraciones)
        errores += int(np.sum(dec != bits))
        total += N
    return errores / total


def problema24():
    ebn0_db = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
    rng = np.random.default_rng(2026)
    it1 = np.array([simular_turbo(x, 1, N=1000, nblocks=10, rng=rng)
                    for x in ebn0_db])
    it5 = np.array([simular_turbo(x, 5, N=1000, nblocks=10, rng=rng)
                    for x in ebn0_db])
    iteraciones = np.arange(1, 8)
    ber_iter = np.array([simular_turbo(2.0, int(k), N=800, nblocks=8, rng=rng)
                         for k in iteraciones])
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.6))
    axes[0].semilogy(ebn0_db, sin_ceros(it1), "o-", color=COLORES[0], ms=5,
                     label="1 iteracion")
    axes[0].semilogy(ebn0_db, sin_ceros(it5), "s-", color=COLORES[1], ms=5,
                     label="5 iteraciones")
    axes[0].set_xlabel("$E_b/N_0$ (dB)")
    axes[0].set_ylabel("BER")
    axes[0].set_title("Turbo codigo RSC (5,7), $N=500$")
    axes[0].set_ylim(1e-4, 1)
    axes[0].legend(fontsize=8)
    axes[0].grid(True, alpha=0.3, which="both")
    axes[1].semilogy(iteraciones, sin_ceros(ber_iter), "o-", color=COLORES[2], ms=5)
    axes[1].set_xlabel("iteraciones")
    axes[1].set_ylabel("BER")
    axes[1].set_title("Convergencia a $E_b/N_0=2$ dB")
    axes[1].set_ylim(1e-4, 1)
    axes[1].grid(True, alpha=0.3, which="both")
    fig.tight_layout()
    guardar_fig(fig, "p24_turbo_decoder.png")
    return {"ebn0_db": ebn0_db.tolist(), "ber_1it": it1.tolist(),
            "ber_5it": it5.tolist(),
            "iteraciones": iteraciones.tolist(),
            "ber_por_iteracion": ber_iter.tolist()}


# ------------------------------------------------------------- 25-26. LDPC
H_LDPC = np.array([[1, 1, 0, 1, 0, 0],
                   [0, 1, 1, 0, 1, 0],
                   [1, 0, 0, 0, 1, 1],
                   [0, 0, 1, 1, 0, 1]], dtype=int)


def gf2_sistematica(H):
    """G sistematica a partir de H por eliminacion gaussiana en GF(2)."""
    Hr = H.copy() % 2
    m, n = Hr.shape
    pivotes, fila = [], 0
    for col in range(n):
        idx = np.where(Hr[fila:, col] == 1)[0]
        if len(idx) == 0:
            continue
        i = fila + idx[0]
        Hr[[fila, i]] = Hr[[i, fila]]
        for r in range(m):
            if r != fila and Hr[r, col] == 1:
                Hr[r] ^= Hr[fila]
        pivotes.append(col)
        fila += 1
        if fila == m:
            break
    libres = [c for c in range(n) if c not in pivotes]
    G = np.zeros((len(libres), n), dtype=int)
    for j, fc in enumerate(libres):
        G[j, fc] = 1
        for i, pc in enumerate(pivotes):
            G[j, pc] = Hr[i, fc]
    return G % 2, Hr, pivotes, libres


def codigos_h(H):
    n = H.shape[1]
    C = []
    for i in range(1 << n):
        c = np.array([(i >> j) & 1 for j in range(n)], dtype=int)
        if np.all((H @ c) % 2 == 0):
            C.append(c)
    return np.array(C)


def bit_flipping(r, H, max_iter=20):
    r = r.copy()
    for it in range(max_iter):
        s = (H @ r) % 2
        if not np.any(s):
            return r, it, True
        unsat = H.T @ s
        m = int(np.max(unsat))
        if m == 0:
            break
        idx = np.flatnonzero(unsat == m)
        r[idx[0]] ^= 1
    return r, max_iter, False


def sum_product(Lch, H, max_iter=20):
    m, n = H.shape
    checks = [[v for v in range(n) if H[c, v]] for c in range(m)]
    vars_ = [[c for c in range(m) if H[c, v]] for v in range(n)]
    M_vc = {(v, c): float(Lch[v]) for c in range(m) for v in checks[c]}
    M_cv = {(c, v): 0.0 for c in range(m) for v in checks[c]}
    for it in range(max_iter):
        for c in range(m):
            for v in checks[c]:
                prod = 1.0
                for v2 in checks[c]:
                    if v2 != v:
                        prod *= math.tanh(M_vc[(v2, c)] / 2)
                prod = min(max(prod, -1 + 1e-12), 1 - 1e-12)
                M_cv[(c, v)] = 2 * math.atanh(prod)
        for v in range(n):
            for c in vars_[v]:
                M_vc[(v, c)] = Lch[v] + sum(
                    M_cv[(c2, v)] for c2 in vars_[v] if c2 != c)
                M_vc[(v, c)] = min(max(M_vc[(v, c)], -30), 30)
        Lpost = np.array([Lch[v] + sum(M_cv[(c, v)] for c in vars_[v])
                          for v in range(n)])
        dec = (Lpost < 0).astype(int)
        if not np.any((H @ dec) % 2):
            return dec, it + 1, True
    return dec, max_iter, False


def problema25():
    G, Hr, pivotes, libres = gf2_sistematica(H_LDPC)
    assert np.all((G @ H_LDPC.T) % 2 == 0)
    C = codigos_h(H_LDPC)
    dmin = int(min(c.sum() for c in C if c.sum() > 0))
    rng = np.random.default_rng(31)
    ps = np.array([0.01, 0.02, 0.05, 0.08, 0.10, 0.15])
    bers, iters = [], []
    for p in ps:
        err = 0
        total = 0
        its = []
        for _ in range(20000):
            msg = rng.integers(0, 2, G.shape[0])
            cod = (msg @ G) % 2
            r = np.bitwise_xor(cod, (rng.random(len(cod)) < p).astype(int))
            dec, it, ok = bit_flipping(r, H_LDPC)
            info = dec[libres]
            err += int(np.sum(info != msg))
            total += len(msg)
            its.append(it)
        bers.append(err / total)
        iters.append(float(np.mean(its)))
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.6))
    axes[0].semilogy(ps, bers, "o-", color=COLORES[0], ms=5,
                     label="bit-flipping")
    axes[0].semilogy(ps, ps, "--", color=COLORES[1], lw=1.2,
                     label="sin codificar")
    axes[0].set_xlabel("$p$ del BSC")
    axes[0].set_ylabel("BER")
    axes[0].set_title("LDPC (6,3): volteo de bit")
    axes[0].set_ylim(1e-4, 1)
    axes[0].legend(fontsize=8)
    axes[0].grid(True, alpha=0.3, which="both")
    axes[1].plot(ps, iters, "o-", color=COLORES[2], ms=5)
    axes[1].set_xlabel("$p$ del BSC")
    axes[1].set_ylabel("iteraciones medias")
    axes[1].set_title("Convergencia del volteo de bit")
    axes[1].grid(True, alpha=0.3)
    fig.tight_layout()
    guardar_fig(fig, "p25_bit_flipping.png")
    return {"G": G.tolist(), "columnas_libres": libres,
            "d_min": dmin, "p": ps.tolist(), "ber": bers,
            "iteraciones_medias": iters}


def problema26():
    G, Hr, pivotes, libres = gf2_sistematica(H_LDPC)
    rng = np.random.default_rng(41)
    ebn0_db = np.array([0, 1, 2, 3, 4, 5, 6], dtype=float)
    R = G.shape[0] / H_LDPC.shape[1]
    ber_sp, ber_bf, ber_sc = [], [], []
    for db in ebn0_db:
        g = dose(db)
        N0 = 1 / g
        sigma = math.sqrt(N0 / 2)
        amp = math.sqrt(R)
        err_sp = err_bf = err_sc = 0
        total = 0
        for _ in range(12000):
            msg = rng.integers(0, 2, G.shape[0])
            cod = (msg @ G) % 2
            y = amp * (1 - 2 * cod) + sigma * rng.standard_normal(len(cod))
            Lch = 2 * amp * y / sigma ** 2
            dec_sp, _, _ = sum_product(Lch, H_LDPC)
            duros = (y < 0).astype(int)
            dec_bf, _, _ = bit_flipping(duros, H_LDPC)
            err_sp += int(np.sum(dec_sp[libres] != msg))
            err_bf += int(np.sum(dec_bf[libres] != msg))
            err_sc += int(np.sum(duros[libres] != msg))
            total += len(msg)
        ber_sp.append(err_sp / total)
        ber_bf.append(err_bf / total)
        ber_sc.append(err_sc / total)
    iteraciones = np.arange(1, 11)
    ber_iter = []
    for k in iteraciones:
        g = dose(3.0)
        N0 = 1 / g
        sigma = math.sqrt(N0 / 2)
        amp = math.sqrt(R)
        err = 0
        total = 0
        for _ in range(8000):
            msg = rng.integers(0, 2, G.shape[0])
            cod = (msg @ G) % 2
            y = amp * (1 - 2 * cod) + sigma * rng.standard_normal(len(cod))
            Lch = 2 * amp * y / sigma ** 2
            dec, _, _ = sum_product(Lch, H_LDPC, int(k))
            err += int(np.sum(dec[libres] != msg))
            total += len(msg)
        ber_iter.append(err / total)
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.6))
    axes[0].semilogy(ebn0_db, ber_sp, "o-", color=COLORES[0], ms=5,
                     label="suma-producto")
    axes[0].semilogy(ebn0_db, ber_bf, "s-", color=COLORES[1], ms=5,
                     label="volteo de bit")
    axes[0].semilogy(ebn0_db, ber_sc, ":", color=COLORES[5], lw=1.2,
                     label="sin codificar")
    axes[0].set_xlabel("$E_b/N_0$ (dB)")
    axes[0].set_ylabel("BER")
    axes[0].set_title("LDPC (6,3): suma-producto")
    axes[0].set_ylim(1e-4, 1)
    axes[0].legend(fontsize=8)
    axes[0].grid(True, alpha=0.3, which="both")
    axes[1].semilogy(iteraciones, ber_iter, "o-", color=COLORES[2], ms=5)
    axes[1].set_xlabel("iteraciones")
    axes[1].set_ylabel("BER")
    axes[1].set_title("Convergencia a $E_b/N_0=3$ dB")
    axes[1].set_ylim(1e-4, 1)
    axes[1].grid(True, alpha=0.3, which="both")
    fig.tight_layout()
    guardar_fig(fig, "p26_sum_product.png")
    return {"ebn0_db": ebn0_db.tolist(), "suma_producto": ber_sp,
            "volteo_bit": ber_bf, "sin_codificar": ber_sc,
            "iteraciones": iteraciones.tolist(),
            "ber_por_iteracion": ber_iter}


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
        "problema8": problema8(),
        "problema9": problema9(),
        "problema10": problema10(),
        "problema11": problema11(),
        "problema12": problema12(),
        "problema13": problema13(),
        "problema14": problema14(),
        "problema15": problema15(),
        "problema16": problema16(),
        "problema17": problema17(),
        "problema18": problema18(),
        "problema19": problema19(),
        "problema20": problema20(),
        "problema21": problema21(),
        "problema22": problema22(),
        "problema23": problema23(),
        "problema24": problema24(),
        "problema25": problema25(),
        "problema26": problema26(),
    }
    guardar_json(resultados, DATOS / "resultados.json")
    print(json.dumps(resultados, indent=1, ensure_ascii=False))
    if plt.get_fignums():
        plt.show()
        plt.close("all")


if __name__ == "__main__":
    main()
