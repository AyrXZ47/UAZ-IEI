"""Tarea 4: sistemas de antena multiple. Genera figuras y numeros.

Uso: python3 tarea4.py
"""

import json
import sys
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE.parents[1] / "practicas" / "comun"))
from estilo_graficas import COLORES, guardar, guardar_json, preparar  # noqa: E402

import matplotlib.pyplot as plt  # noqa: E402

RNG = np.random.default_rng(4)
FIGS, DATOS = preparar(BASE)

SNR_DB = np.arange(0, 30.01, 0.5)
SNR = 10 ** (SNR_DB / 10)


# ------------------------------------------------------------------ canales
def canal_rayleigh(nr, nt, rng, tam=None):
    """Matriz de canal CN(0,1); tam opcional para varias realizaciones."""
    forma = (nr, nt) if tam is None else (nr, nt, tam)
    return (rng.standard_normal(forma) + 1j * rng.standard_normal(forma)) / np.sqrt(2)


# ------------------------------------------------- 1 y 12: matriz de canal
def problema1():
    H = canal_rayleigh(3, 4, RNG)
    return {"NR": 3, "NT": 4, "shape": list(H.shape),
            "media_re": float(H.real.mean()), "var_media": float(np.mean(np.abs(H) ** 2))}


# ------------------------------------------- 2: detectores ML, MMSE e ICD
def simular_detectores(nt, nr, detector, ebn0_db, max_err=100, max_sim=400000):
    N0 = 10 ** (-ebn0_db / 10)
    S = np.array([[1, 1, -1, -1], [1, -1, 1, -1]], dtype=complex)[:nt, :]
    errores = total = 0
    B = 4000
    while errores < max_err and total < max_sim:
        H = (RNG.standard_normal((nr, nt, B))
             + 1j * RNG.standard_normal((nr, nt, B))) / np.sqrt(2 * nr)
        s = 2 * (RNG.random((nt, B)) < 0.5) - 1
        n = np.sqrt(N0 / 2) * (RNG.standard_normal((nr, B))
                               + 1j * RNG.standard_normal((nr, B)))
        y = np.einsum("mnb,nb->mb", H, s) + n

        if detector == "ML":
            cod = np.einsum("mnb,nj->mjb", H, S)
            d = np.sum(np.abs(y[:, None, :] - cod) ** 2, axis=0)
            s_h = S[:, np.argmin(d, axis=0)]
        elif detector == "MMSE":
            Hh = H.conj().transpose(1, 0, 2)          # nt x nr x B
            G = np.einsum("mib,mjb->ijb", H.conj(), H) + N0 * np.eye(nt)[:, :, None]
            W = np.linalg.solve(G.transpose(2, 0, 1), Hh.transpose(2, 0, 1))
            s_h = np.einsum("bin,nb->ib", W, y)
        else:  # ICD (pseudoinversa)
            W = np.linalg.pinv(H.transpose(2, 0, 1))
            s_h = np.einsum("bin,nb->ib", W, y)

        s_h = np.where(s_h.real >= 0, 1, -1)
        errores += int(np.sum(s_h != s))
        total += nt * B
    return errores / total


def simular_mrc(nr, ebn0_db, max_err=2000, max_sim=200000):
    """Referencia (1, NR) con BPSK: combinador de relacion maxima."""
    N0 = 10 ** (-ebn0_db / 10)
    err = tot = 0
    while err < max_err and tot < max_sim:
        B = 5000
        h = (RNG.standard_normal((nr, B)) + 1j * RNG.standard_normal((nr, B))) / np.sqrt(2 * nr)
        s = 2 * (RNG.random(B) < 0.5) - 1
        n = np.sqrt(N0 / 2) * (RNG.standard_normal((nr, B)) + 1j * RNG.standard_normal((nr, B)))
        y = h * s + n
        s_h = np.where(np.real(np.sum(h.conj() * y, axis=0)) >= 0, 1, -1)
        err += int(np.sum(s_h != s))
        tot += B
    return err / tot


def problema2():
    ebn0 = np.arange(0, 31, 5)
    datos = {}
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.8), sharey=True)
    for ax, nr in zip(axes, [2, 3]):
        curvas = {}
        for det, color in [("ML", COLORES[0]), ("MMSE", COLORES[1]), ("ICD", COLORES[3])]:
            vals = np.array([simular_detectores(2, nr, det, e) for e in ebn0])
            curvas[det] = vals.tolist()
            ax.semilogy(ebn0, np.where(vals > 0, vals, np.nan), "o-", color=color,
                        ms=4, lw=1.4, label=det)
        mrc = np.array([simular_mrc(nr, e) for e in ebn0])
        curvas["MRC"] = mrc.tolist()
        ax.semilogy(ebn0, np.where(mrc > 0, mrc, np.nan), "k--", lw=1.2,
                    label=f"MRC (1,{nr})")
        ax.set_xlabel("$E_b/N_0$ (dB)")
        ax.set_title(f"$N_T=2$, $N_R={nr}$")
        ax.legend(loc="lower left", fontsize=8)
        datos[f"2x{nr}"] = curvas
    axes[0].set_ylabel("BER")
    fig.tight_layout()
    guardar(fig, FIGS / "p2_detectores.png")
    return datos


# ------------------------------------------------ 3 y 4: capacidad fija
def capacidad(h, snr, nt):
    lam = np.linalg.eigvalsh(h @ h.conj().T)
    return np.sum(np.log2(1 + snr[:, None] * lam / nt), axis=1), lam


def problema3y4():
    H2 = np.array([[2, 0.3], [0.5, 1.2]])
    H3 = np.array([[2, 0.5, 0.3], [0.5, 2, 0.4], [0.3, 0.4, 1.5]])
    c2, l2 = capacidad(H2, SNR, 2)
    c3, l3 = capacidad(H3, SNR, 3)

    fig, ax = plt.subplots(figsize=(6.8, 3.8))
    ax.plot(SNR_DB, c2, color=COLORES[0], lw=1.8, label="$2\\times2$")
    ax.plot(SNR_DB, c3, color=COLORES[1], lw=1.8, label="$3\\times3$")
    ax.set_xlabel("SNR (dB)")
    ax.set_ylabel("Capacidad (bps/Hz)")
    ax.set_title("Capacidad de canales MIMO con matriz fija")
    ax.legend(loc="upper left")
    guardar(fig, FIGS / "p34_capacidad_fija.png")

    return {"H2": {"lambda": l2.tolist(), "C20db": float(np.interp(20, SNR_DB, c2))},
            "H3": {"lambda": l3.tolist(), "C20db": float(np.interp(20, SNR_DB, c3))}}


# -------------------------------------- 5, 6 y 7: capacidad ergodica
def cap_ergodica(nt, nr, snr, rng, realizaciones=2000):
    H = canal_rayleigh(nr, nt, rng, realizaciones)
    lam = np.linalg.eigvalsh(np.einsum("mnb,mjb->bnj", H.conj(), H))  # R x nt
    c = np.sum(np.log2(1 + snr[:, None, None] * lam[None, :, :] / nt), axis=2)
    return c.mean(axis=1)


def problema5a7():
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.4))
    rng = np.random.default_rng(17)
    datos = {}

    for nr, color in zip([1, 3, 5, 7], COLORES):
        c = cap_ergodica(1, nr, SNR, rng)
        axes[0].plot(SNR_DB, c, color=color, lw=1.6, label=f"$N_R={nr}$")
        datos[f"simo_{nr}"] = float(np.interp(20, SNR_DB, c))
    axes[0].set_title("SIMO")

    for nt, color in zip([1, 3, 5, 7], COLORES):
        c = cap_ergodica(nt, 1, SNR, rng)
        axes[1].plot(SNR_DB, c, color=color, lw=1.6, label=f"$N_T={nt}$")
        datos[f"miso_{nt}"] = float(np.interp(20, SNR_DB, c))
    axes[1].set_title("MISO")

    for nt, color in zip([3, 5], COLORES):
        c = cap_ergodica(nt, nt, SNR, rng)
        axes[2].plot(SNR_DB, c, color=color, lw=1.6, label=f"${nt}\\times{nt}$")
        datos[f"mimo_{nt}"] = float(np.interp(20, SNR_DB, c))
    axes[2].set_title("MIMO")

    for ax in axes:
        ax.set_xlabel("SNR (dB)")
        ax.legend(loc="upper left", fontsize=8)
    axes[0].set_ylabel("Capacidad (bps/Hz)")
    fig.tight_layout()
    guardar(fig, FIGS / "p567_capacidad.png")
    return datos


# ----------------------------------------------------- 8 y 13: Alamouti
def qpsk(n, rng):
    return ((2 * rng.integers(0, 2, n) - 1) + 1j * (2 * rng.integers(0, 2, n) - 1)) / np.sqrt(2)


def simular_alamouti(nr, snr_db, rng, iteraciones=30000):
    snr = 10 ** (snr_db / 10)
    # Es = 1, N0 = Es/SNR
    N0 = 1 / snr
    err_sim = err_bit = tot_sim = 0
    for _ in range(iteraciones // 2000):
        B = 2000
        s = qpsk((2, B), rng)
        H = canal_rayleigh(nr, 2, rng, B)
        n = np.sqrt(N0 / 2) * (rng.standard_normal((nr, 2, B))
                               + 1j * rng.standard_normal((nr, 2, B)))
        y1 = H[:, 0, :] * s[0] + H[:, 1, :] * s[1] + n[:, 0, :]
        y2 = -H[:, 0, :] * np.conj(s[1]) + H[:, 1, :] * np.conj(s[0]) + n[:, 1, :]
        s1 = np.sum(np.conj(H[:, 0, :]) * y1 + H[:, 1, :] * np.conj(y2), axis=0)
        s2 = np.sum(np.conj(H[:, 1, :]) * y1 - H[:, 0, :] * np.conj(y2), axis=0)

        # deteccion QPSK
        def detectar(v):
            return (np.where(v.real >= 0, 1, -1) + 1j * np.where(v.imag >= 0, 1, -1)) / np.sqrt(2)

        s_h = np.array([detectar(s1), detectar(s2)])
        err_sim += int(np.sum(s_h != s))
        err_bit += int(np.sum(s_h.real != s.real)) + int(np.sum(s_h.imag != s.imag))
        tot_sim += 2 * B
    return err_sim / tot_sim, err_bit / (2 * tot_sim)


def simular_siso(snr_db, rng, iteraciones=200000):
    snr = 10 ** (snr_db / 10)
    N0 = 1 / snr
    err = tot = 0
    for _ in range(iteraciones // 5000):
        B = 5000
        s = qpsk(B, rng)
        h = (rng.standard_normal(B) + 1j * rng.standard_normal(B)) / np.sqrt(2)
        n = np.sqrt(N0 / 2) * (rng.standard_normal(B) + 1j * rng.standard_normal(B))
        y = h * s + n
        s_h = (np.where((np.conj(h) * y).real >= 0, 1, -1)
               + 1j * np.where((np.conj(h) * y).imag >= 0, 1, -1)) / np.sqrt(2)
        err += int(np.sum(s_h != s))
        tot += B
    return err / tot


def problema8y13():
    rng = np.random.default_rng(23)
    snr_db = np.arange(0, 21, 2)
    res_2x1, res_2x2 = [], []
    for e in snr_db:
        res_2x1.append(simular_alamouti(1, e, rng, 40000))
        res_2x2.append(simular_alamouti(2, e, rng, 40000))
    ser_2x1 = np.array([r[0] for r in res_2x1])
    ser_2x2 = np.array([r[0] for r in res_2x2])
    ber_2x2 = np.array([r[1] for r in res_2x2])
    ser_siso = np.array([simular_siso(s, rng) for s in snr_db])

    fig, ax = plt.subplots(figsize=(6.8, 3.8))
    ax.semilogy(snr_db, np.where(ser_siso > 0, ser_siso, np.nan), "-", color=COLORES[5],
                lw=1.4, label="SISO (sin diversidad)")
    ax.semilogy(snr_db, np.where(ser_2x1 > 0, ser_2x1, np.nan), "o-", color=COLORES[0],
                ms=4, lw=1.6, label="Alamouti $2\\times1$")
    ax.semilogy(snr_db, np.where(ser_2x2 > 0, ser_2x2, np.nan), "s-", color=COLORES[1],
                ms=4, lw=1.6, label="Alamouti $2\\times2$")
    ax.set_xlabel("$E_s/N_0$ (dB)")
    ax.set_ylabel("SER")
    ax.set_title("Código de Alamouti con QPSK")
    ax.legend(loc="lower left")
    guardar(fig, FIGS / "p8_alamouti.png")

    return {"ser_2x1": ser_2x1.tolist(), "ser_2x2": ser_2x2.tolist(),
            "ber_2x2": ber_2x2.tolist(), "snr_db": snr_db.tolist(),
            "ser_2x1_20db": float(ser_2x1[-1]), "ser_2x2_20db": float(ser_2x2[-1])}


# ------------------------------- 9, 10, 11 y 14: verificacion algebraica
def problema9a14():
    rng = np.random.default_rng(9)
    s = (rng.standard_normal(3) + 1j * rng.standard_normal(3))
    G = np.array([[s[0], s[1], s[2], 0],
                  [-np.conj(s[1]), np.conj(s[0]), 0, s[2]],
                  [np.conj(s[2]), 0, -np.conj(s[0]), s[1]],
                  [0, np.conj(s[2]), -np.conj(s[1]), -s[0]]])
    norma = np.sum(np.abs(s) ** 2)
    error_g = np.max(np.abs(G.conj().T @ G - norma * np.eye(4)))

    # detector ML del codigo de 4 antenas sobre 4^3 = 64 tripletas 4-PSK
    const = np.array([1, 1j, -1, -1j]) / np.sqrt(2)
    aciertos = 0
    for _ in range(500):
        h = (rng.standard_normal(4) + 1j * rng.standard_normal(4)) / np.sqrt(2)
        sym = rng.integers(0, 4, 3)
        sv = const[sym]
        Gt = np.array([[sv[0], sv[1], sv[2], 0],
                       [-np.conj(sv[1]), np.conj(sv[0]), 0, sv[2]],
                       [np.conj(sv[2]), 0, -np.conj(sv[0]), sv[1]],
                       [0, np.conj(sv[2]), -np.conj(sv[1]), -sv[0]]])
        y = Gt @ h + 0.1 * (rng.standard_normal(4) + 1j * rng.standard_normal(4))
        mejor, idx = 1e9, None
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    s2 = const[[i, j, k]]
                    Gc = np.array([[s2[0], s2[1], s2[2], 0],
                                   [-np.conj(s2[1]), np.conj(s2[0]), 0, s2[2]],
                                   [np.conj(s2[2]), 0, -np.conj(s2[0]), s2[1]],
                                   [0, np.conj(s2[2]), -np.conj(s2[1]), -s2[0]]])
                    d = np.sum(np.abs(y - Gc @ h) ** 2)
                    if d < mejor:
                        mejor, idx = d, (i, j, k)
        aciertos += int(idx == tuple(sym))
    error_ml = 1 - aciertos / 500

    h3 = (rng.standard_normal(3) + 1j * rng.standard_normal(3)) / np.sqrt(2)
    H31 = np.array([[h3[0], h3[1], h3[2]],
                    [np.conj(h3[1]), -np.conj(h3[0]), 0],
                    [-np.conj(h3[2]), 0, np.conj(h3[0])],
                    [0, -np.conj(h3[2]), np.conj(h3[1])]])
    error_h31 = np.max(np.abs(H31.conj().T @ H31 - np.sum(np.abs(h3) ** 2) * np.eye(3)))

    # (2,2) Alamouti: diversidad 4
    H = canal_rayleigh(2, 2, rng)
    Heq = np.array([[H[0, 0], H[0, 1]],
                    [np.conj(H[0, 1]), -np.conj(H[0, 0])],
                    [H[1, 0], H[1, 1]],
                    [np.conj(H[1, 1]), -np.conj(H[1, 0])]])
    error_22 = np.max(np.abs(Heq.conj().T @ Heq - np.sum(np.abs(H) ** 2) * np.eye(2)))

    return {"error_G": float(error_g), "error_ml_4x1": float(error_ml),
            "error_H31": float(error_h31), "error_alamouti2x2": float(error_22)}


# ---------------------------------------------------- 15: trellis 8 estados
def tabla_trellis():
    """Tabla de la Figura 1: (estado, entrada) -> (estado siguiente, salidas)."""
    s1 = [0, 1, 2, 3, 2, 3, 0, 1]
    tabla = {}
    for st in range(8):
        for x in range(4):
            nxt = (st + x) % 8
            s2 = (x + 2 * (nxt >= 4)) % 4
            tabla[(st, x)] = (nxt, s1[nxt], s2)
    return tabla


def problema15():
    tabla = tabla_trellis()
    rng = np.random.default_rng(15)
    entrada = rng.integers(0, 4, 10)
    st = 0
    ant1, ant2 = [], []
    for x in entrada:
        st, a, b = tabla[(st, int(x))]
        ant1.append(a)
        ant2.append(b)
    return {"entrada": entrada.tolist(), "antena1": ant1, "antena2": ant2,
            "tabla": {f"{k[0]}-{k[1]}": v for k, v in tabla.items()}}


# --------------------------------------------------------------------- main
def main():
    resultados = {
        "problema1": problema1(),
        "problema2": problema2(),
        "problema3_4": problema3y4(),
        "problema5_7": problema5a7(),
        "problema8_13": problema8y13(),
        "problema9_14": problema9a14(),
        "problema15": problema15(),
    }
    guardar_json(resultados, DATOS / "resultados.json")
    print(json.dumps(resultados, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
