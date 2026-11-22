#!/usr/bin/env python3
"""Escaneo rapido de una banda con el RTL-SDR: donde hay senales de verdad.

Barre la banda en pasos de `paso` Hz, mide el pico de cada canal y lo compara
con el piso de ruido, y lista los candidatos ordenados por potencia.  Sirve para
elegir a que frecuencia apuntar las practicas (o comprobar si la senal que
estas viendo es un transmisor cercano o una emisora real).

Uso:
    python3 escaner.py                       # banda FM comercial (87.5-108 MHz)
    python3 escaner.py -i 430e6 -f 440e6     # banda ISM de 433 MHz
    python3 escaner.py -p 100e3 -n 8         # paso fino, top 8
"""
import argparse
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun  # noqa: E402


def escanear(ini, fin, paso, rate, ganancia, muestras):
    """Pico y piso de ruido (dBFS) de cada canal del barrido."""
    from rtlsdr import RtlSdr
    from scipy import signal as sig

    try:
        sdr = RtlSdr()
    except Exception as e:
        raise SystemExit(f"No se pudo abrir el SDR ({e}). ¿Está ocupado por otra "
                         f"practica abierta? Cierra esa ventana y reintenta.")
    sdr.sample_rate = rate
    try:
        sdr.set_bandwidth(min(rate, 1.0e6))
    except Exception:
        pass
    comun.fijar_ganancia(sdr, ganancia)
    filas = []
    try:
        for f0 in np.arange(ini, fin + paso / 2, paso):
            sdr.center_freq = f0
            x = sdr.read_samples(muestras)
            fr, P = sig.welch(x, fs=rate, nperseg=min(4096, muestras),
                              return_onesided=False)
            fr, P = np.fft.fftshift(fr), np.fft.fftshift(P)
            pdb = 10 * np.log10(P + 1e-20)
            canal = np.abs(fr) <= paso / 2
            pico = float(pdb[canal].max())
            piso = float(np.median(pdb[~canal]))
            filas.append((float(f0), pico, pico - piso))
    finally:
        sdr.close()
    return filas


def main(argv=None):
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("-i", "--ini", type=float, default=87.5e6, help="inicio (Hz)")
    p.add_argument("-f", "--fin", type=float, default=108.5e6, help="fin (Hz)")
    p.add_argument("-p", "--paso", type=float, default=0.5e6, help="paso (Hz)")
    p.add_argument("-r", "--rate", type=float, default=comun.RATE_DEF)
    p.add_argument("-n", "--top", type=int, default=12)
    p.add_argument("-g", "--gain", default="auto")
    p.add_argument("--muestras", type=int, default=1 << 16)
    args = p.parse_args(argv)

    filas = escanear(args.ini, args.fin, args.paso, args.rate, args.gain,
                     args.muestras)
    filas.sort(key=lambda r: -r[1])
    print(f"{'MHz':>9} {'pico dBFS':>10} {'sobre piso':>11}")
    for f, pico, sobre in filas[:args.top]:
        marca = "  <-- candidato" if sobre > 10 else ""
        print(f"{f/1e6:9.2f} {pico:10.1f} {sobre:11.1f}{marca}")
    if all(s <= 10 for _, _, s in filas):
        print("\nNada destaca sobre el ruido en esta banda.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
