#!/usr/bin/env python3
"""Practica 7. Estimacion experimental de la capacidad de canal (Shannon-Hartley).

Por cada escenario (LOS, interior con obstaculos, distancia maxima) captura la
senal en la frecuencia de interes y el ruido en un canal cercano vacio, estima
Ps, Pn y la SNR y calcula la capacidad C = B*log2(1+SNR).

Uso:
    python3 practica7.py --sim                 # verificacion sin dongle
    python3 practica7.py                       # captura real (confirmacion por escenario)
    python3 practica7.py --selftest            # autochequeo del estimador de SNR
    python3 practica7.py --no-show             # solo guarda figuras
"""
import argparse
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import comun  # noqa: E402

DIR = Path(__file__).resolve().parent
FIGS, DATOS = DIR / "figs", DIR / "datos"

SNR_SIM_DB = {"LOS": 20.0, "NLOS": 12.0, "lejano": 5.0}


def potencia_media(x):
    """Ps = mean(abs(data).^2) del manual."""
    return float(np.mean(np.abs(x) ** 2))


def estimar(x, x_ruido, B):
    """Ps, Pn, SNR y capacidad de Shannon a partir de una captura y ruido."""
    Ps, Pn = potencia_media(x), potencia_media(x_ruido)
    snr = Ps / Pn
    C = B * np.log2(1 + snr)
    return {"Ps_dB": 10 * np.log10(Ps), "Pn_dB": 10 * np.log10(Pn),
            "SNR_dB": 10 * np.log10(snr), "C_bps": float(C), "C_kbps": float(C / 1e3)}


def captura_sim(n, snr_db, seed=0):
    """BPSK de potencia unitaria + ruido complejo gaussiano y captura de solo ruido."""
    rng = np.random.default_rng(seed)
    s = (2.0 * rng.integers(0, 2, n) - 1.0).astype(np.complex64)
    escala = np.float32(np.sqrt(10 ** (-snr_db / 10) / 2))
    ruido = lambda: (rng.standard_normal(n) + 1j * rng.standard_normal(n)).astype(np.complex64) * escala
    return (s + ruido()).astype(np.complex64), ruido()


def capturar_escenario(esc, args):
    input(f"[{esc}] Ubique la antena en el escenario y presione Enter para capturar... ")
    x = comun.capturar(args.freq, n=args.n, rate=args.rate, ganancia=args.gain)
    xr = comun.capturar(args.freq + args.fnoise, n=args.n, rate=args.rate, ganancia=args.gain)
    return x, xr


def fig_shannon(resultados, B, ruta):
    import matplotlib.pyplot as plt

    snr_db = np.linspace(-10, 30, 401)
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(snr_db, np.log2(1 + 10 ** (snr_db / 10)), lw=2, label="Curva teórica")
    for esc, r in resultados.items():
        c_bhz = r["C_bps"] / B
        ax.plot([r["SNR_dB"]] * 2, [0, c_bhz], "--", lw=1)
        ax.plot(r["SNR_dB"], c_bhz, "o",
                label=f"{esc}: {r['SNR_dB']:.1f} dB, {r['C_kbps']:.1f} kbps")
    ax.set_xlabel("SNR (dB)")
    ax.set_ylabel("Capacidad espectral C/B (bps/Hz)")
    ax.set_title("Capacidad de Shannon por escenario")
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)
    return comun.guardar_fig(fig, ruta, MOSTRAR)


def fig_potencias(resultados, ruta):
    import matplotlib.pyplot as plt

    escs = list(resultados)
    pos = np.arange(len(escs))
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(pos - 0.2, [resultados[e]["Ps_dB"] for e in escs], 0.4, label="Señal (Ps)")
    ax.bar(pos + 0.2, [resultados[e]["Pn_dB"] for e in escs], 0.4, label="Ruido (Pn)")
    ax.set_xticks(pos, escs)
    ax.set_ylabel("Potencia (dB)")
    ax.set_title("Potencia de señal y ruido por escenario")
    ax.grid(alpha=0.3, axis="y")
    ax.legend()
    return comun.guardar_fig(fig, ruta, MOSTRAR)


def reporte(resultados):
    filas = [(esc, f"{r['Ps_dB']:.2f}", f"{r['Pn_dB']:.2f}",
              f"{r['SNR_dB']:.2f}", f"{r['C_kbps']:.2f}")
             for esc, r in resultados.items()]
    print(comun.tabla_markdown(
        ["Escenario", "Potencia señal (dB)", "Potencia ruido (dB)", "SNR (dB)", "Capacidad (kbps)"],
        filas))
    for esc, r in resultados.items():
        print(f"{esc}: C = {r['C_kbps']:.2f} kbps = {r['C_bps'] / 1e6:.4f} Mbps")


def selftest():
    x, xr = captura_sim(1 << 18, 15.0, seed=7)
    est = estimar(x, xr, 200e3)
    assert abs(est["SNR_dB"] - 15.0) < 1.5, est["SNR_dB"]
    print("practica7 selftest OK")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("-f", "--freq", type=float, default=433.9e6, help="frecuencia de la señal")
    p.add_argument("--fnoise", type=float, default=1e6, help="offset del canal de ruido")
    p.add_argument("--escenarios", default="LOS,NLOS,lejano")
    p.add_argument("--n", type=int, default=262144)
    p.add_argument("-r", "--rate", type=float, default=comun.RATE_DEF)
    p.add_argument("-B", "--banda", type=float, default=200e3)
    p.add_argument("-g", "--gain", default="auto")
    p.add_argument("--sim", action="store_true")
    p.add_argument("--no-show", action="store_true")
    p.add_argument("--selftest", action="store_true")
    args = p.parse_args()
    global MOSTRAR
    MOSTRAR = not args.no_show

    if args.selftest:
        selftest()
        return 0

    if not args.sim:
        info = comun.info_dispositivo()
        print(f"Dispositivo: RTL2832U / {info['tuner']}  "
              f"({info['frecuencia_min_Hz'] / 1e6:.0f}-{info['frecuencia_max_Hz'] / 1e6:.0f} MHz)")

    resultados = {}
    for i, esc in enumerate(e.strip() for e in args.escenarios.split(",") if e.strip()):
        if args.sim:
            snr = SNR_SIM_DB.get(esc, 10.0)
            x, xr = captura_sim(args.n, snr, seed=i)
            print(f"modo simulación: {esc} con SNR conocida de {snr:.0f} dB")
        else:
            x, xr = capturar_escenario(esc, args)
        resultados[esc] = estimar(x, xr, args.banda)

    reporte(resultados)
    fig_shannon(resultados, args.banda, FIGS / "shannon.png")
    fig_potencias(resultados, FIGS / "potencias.png")
    comun.guardar_json(DATOS / "resultados.json", frecuencia_Hz=args.freq,
                       offset_ruido_Hz=args.fnoise, banda_Hz=args.banda,
                       modo="sim" if args.sim else "real", escenarios=resultados)
    print(f"figuras en {FIGS}, datos en {DATOS / 'resultados.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
