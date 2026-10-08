#!/usr/bin/env python3
"""Practica 1. Introduccion al RTL-SDR y analisis espectral de senales inalambricas.

Captura muestras IQ de una estacion FM comercial y obtiene:
  - componentes I y Q en el tiempo
  - potencia promedio recibida
  - espectro (FFT)
  - espectrograma
  - frecuencia central y ancho de banda observados

Uso:
    python3 practica1.py                       # captura real en 96.5 MHz
    python3 practica1.py -f 93.3e6 -n 65536    # otra estacion / otra longitud
    python3 practica1.py --sim                 # datos sinteticos (sin dongle)
    python3 practica1.py --selftest            # verifica el analisis sin dongle
    python3 practica1.py --no-show             # solo guarda figuras
"""
import argparse
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import comun  # noqa: E402

DIR = Path(__file__).resolve().parent
FIGS, DATOS = DIR / "figs", DIR / "datos"


def fm_sintetica(fs, n, f0=30e3, dev=75e3, snr_db=25.0, seed=0):
    """Estacion FM sintetica (audio de banda limitada) para pruebas sin antena."""
    from scipy.signal import firwin, lfilter

    rng = np.random.default_rng(seed)
    audio = lfilter(firwin(129, 15e3, fs=fs), 1.0, rng.standard_normal(n))
    audio /= np.sqrt(np.mean(audio ** 2))
    audio = np.tanh(audio)                    # audio tipo radiodifusion (RMS/pico ~0.6)
    audio /= np.max(np.abs(audio))            # desviacion pico = dev
    t = np.arange(n) / fs
    fase = 2 * np.pi * f0 * t + 2 * np.pi * dev * np.cumsum(audio) / fs
    x = np.exp(1j * fase)
    ruido = (rng.standard_normal(n) + 1j * rng.standard_normal(n)) / np.sqrt(2)
    x = x + ruido * 10 ** (-snr_db / 20)
    return x.astype(np.complex64)


def centro_y_ancho(f, P, umbral_db=3.0, fraccion=0.99):
    """Frecuencia central y ancho de banda (99% de potencia) de la senal.

    Primero busca la region contigua sobre el piso de ruido + umbral_db alrededor
    del maximo; dentro de ella calcula el ancho con el `fraccion` de la potencia
    en exceso sobre el piso.
    """
    pdb = 10 * np.log10(P + 1e-20)
    piso = np.median(pdb)
    sobre = pdb > piso + umbral_db
    i = int(np.argmax(pdb))
    i0 = i1 = i
    while i0 > 0 and sobre[i0 - 1]:
        i0 -= 1
    while i1 < pdb.size - 1 and sobre[i1 + 1]:
        i1 += 1
    fr, Pr = f[i0:i1 + 1], P[i0:i1 + 1]
    exc = np.maximum(Pr - 10 ** (piso / 10), 0.0)
    if exc.sum() <= 0:
        return 0.0, 0.0
    cdf = np.cumsum(exc) / exc.sum()
    lo = np.searchsorted(cdf, (1 - fraccion) / 2)
    hi = np.searchsorted(cdf, 1 - (1 - fraccion) / 2)
    centro = float(np.average(fr, weights=exc))
    ancho = float(fr[min(hi, fr.size - 1)] - fr[lo])
    return centro, ancho


def analizar(x, fs):
    """Metricas de la captura: potencia, centro y ancho de banda."""
    n = x.size
    fw, Pw = comun.espectro(x, fs, nperseg=4096)   # PSD promediada (robusta)
    centro, ancho = centro_y_ancho(fw, Pw)
    X = np.fft.fftshift(np.fft.fft(x))
    f = np.linspace(-fs / 2, fs / 2, n)
    return {
        "n_muestras": int(n),
        "potencia_dbfs": float(comun.potencia_dbfs(x)),
        "offset_centro_Hz": centro,
        "ancho_banda_Hz": ancho,
        "f": f,
        "PSD_dB": 20 * np.log10(np.abs(X) + 1e-20),
    }


def fig_iq(x, fs, ruta):
    import matplotlib.pyplot as plt

    n = min(4096, x.size)
    t = np.arange(n) / fs * 1e3
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(9, 5.5), sharex=True)
    a1.plot(t, x.real[:n], lw=0.8)
    a1.set_ylabel("I[n]"); a1.set_title("Componente I"); a1.grid(alpha=0.3)
    a2.plot(t, x.imag[:n], lw=0.8, color="C1")
    a2.set_ylabel("Q[n]"); a2.set_title("Componente Q"); a2.grid(alpha=0.3)
    a2.set_xlabel("Tiempo (ms)")
    fig.suptitle("Muestras IQ de la estacion FM")
    fig.tight_layout()
    return comun.guardar_fig(fig, ruta, MOSTRAR)


def fig_espectro(f, psd_db, freq, ruta):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot((freq + f) / 1e6, psd_db, lw=0.7)
    ax.set_xlabel("Frecuencia (MHz)")
    ax.set_ylabel("Magnitud (dB)")
    ax.set_title("Espectro de la senal (FFT)")
    ax.grid(alpha=0.3)
    return comun.guardar_fig(fig, ruta, MOSTRAR)


def fig_espectrograma(x, fs, freq, ruta):
    import matplotlib.pyplot as plt
    from scipy import signal as sig

    f, t, S = sig.spectrogram(x, fs=fs, window="hamming", nperseg=1024,
                              noverlap=512, nfft=1024, return_onesided=False,
                              detrend=False, mode="psd")
    S = np.fft.fftshift(S, axes=0)
    f = np.fft.fftshift(f)
    fig, ax = plt.subplots(figsize=(9, 5))
    m = ax.pcolormesh(t * 1e3, (freq + f) / 1e6, 10 * np.log10(S + 1e-20),
                      shading="auto", cmap="viridis")
    ax.set_xlabel("Tiempo (ms)")
    ax.set_ylabel("Frecuencia (MHz)")
    ax.set_title("Espectrograma")
    fig.colorbar(m, ax=ax, label="PSD (dB)")
    return comun.guardar_fig(fig, ruta, MOSTRAR)


def reporte_consola(res, freq):
    print(f"Frecuencia sintonizada : {freq/1e6:.3f} MHz")
    print(f"Muestras               : {res['n_muestras']}")
    print(f"Potencia promedio      : {res['potencia_dbfs']:.2f} dBFS")
    print(f"Frecuencia central obs.: {(freq + res['offset_centro_Hz'])/1e6:.4f} MHz "
          f"(offset {res['offset_centro_Hz']/1e3:+.1f} kHz)")
    print(f"Ancho de banda (99%)   : {res['ancho_banda_Hz']/1e3:.1f} kHz")


def selftest():
    fs, n = 2.4e6, 1 << 18
    x = fm_sintetica(fs, n, f0=30e3)
    res = analizar(x, fs)
    assert abs(res["offset_centro_Hz"] - 30e3) < 8e3, res["offset_centro_Hz"]
    assert 100e3 < res["ancho_banda_Hz"] < 350e3, res["ancho_banda_Hz"]
    p = comun.potencia_dbfs(x)
    assert -30 < p < 5, p
    print("practica1 selftest OK")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("-f", "--freq", type=float, default=96.5e6)
    p.add_argument("-n", type=int, default=1 << 17, help="muestras a capturar")
    p.add_argument("-r", "--rate", type=float, default=comun.RATE_DEF)
    p.add_argument("-g", "--gain", default="auto")
    p.add_argument("-b", "--bw", type=float, default=2.4e6, help="filtro IF del tuner")
    p.add_argument("--sim", action="store_true")
    p.add_argument("--no-show", action="store_true")
    p.add_argument("--selftest", action="store_true")
    args = p.parse_args()
    global MOSTRAR
    MOSTRAR = not args.no_show

    if args.selftest:
        selftest()
        return 0

    if args.sim:
        x = fm_sintetica(args.rate, args.n, f0=30e3)
        print("modo simulacion: estacion FM sintetica a +30 kHz")
    else:
        info = comun.info_dispositivo()
        print(f"Dispositivo: RTL2832U / {info['tuner']}  "
              f"({info['frecuencia_min_Hz']/1e6:.0f}-{info['frecuencia_max_Hz']/1e6:.0f} MHz)")
        x = comun.capturar(args.freq, n=args.n, rate=args.rate,
                           ganancia=args.gain, bw=args.bw)
        np.save(DATOS / "iq.npy", x)
        print(f"capturadas {x.size} muestras a {args.freq/1e6:.3f} MHz")

    res = analizar(x, args.rate)
    reporte_consola(res, args.freq)
    fig_iq(x, args.rate, FIGS / "iq_temporal.png")
    fig_espectro(res["f"], res["PSD_dB"], args.freq, FIGS / "espectro.png")
    fig_espectrograma(x, args.rate, args.freq, FIGS / "espectrograma.png")
    comun.guardar_json(DATOS / "resultados.json", frecuencia_Hz=args.freq,
                       n_muestras=res["n_muestras"],
                       potencia_dbfs=res["potencia_dbfs"],
                       offset_centro_Hz=res["offset_centro_Hz"],
                       ancho_banda_Hz=res["ancho_banda_Hz"])
    print(f"figuras en {FIGS}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
