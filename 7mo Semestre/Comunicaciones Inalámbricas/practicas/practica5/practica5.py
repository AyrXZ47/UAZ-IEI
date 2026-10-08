#!/usr/bin/env python3
"""Practica 5. Efecto Doppler y tiempo de coherencia.

Mide la envolvente de una fuente CW en tres escenarios de movilidad del
receptor (estatico, caminando lento, caminando rapido), estima la frecuencia
Doppler maxima fD a partir del espectro Doppler de la envolvente y calcula el
tiempo de coherencia Tc = 0.423 / fD.

Uso:
    python3 practica5.py                       # captura real, 3 escenarios
    python3 practica5.py --sim                 # datos sinteticos (sin dongle)
    python3 practica5.py --selftest            # verifica el estimador sin dongle
    python3 practica5.py --no-show             # solo guarda figuras
"""
import argparse
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import comun  # noqa: E402

DIR = Path(__file__).resolve().parent
FIGS, DATOS = DIR / "figs", DIR / "datos"
MOSTRAR = True
FS_ENV = 240.0            # tasa de la envolvente generada en simulacion (Hz)
TAPS = 257                # taps del FIR pasa-bajos de la simulacion
FD_ESC = {
    "estatico": (0.2, "Receptor estatico: permanece quieto con el receptor en la mano"),
    "lento": (3.0, "Movimiento lento: camina despacio y sosten el paso durante la captura"),
    "rapido": (12.0, "Movimiento rapido: camina rapido y sosten el paso durante la captura"),
}
SEMILLA = 42


def _interpolar(x, L):
    """Interpolacion en banda base por relleno de ceros espectral (factor L)."""
    m = x.size
    X = np.fft.fft(x)
    Y = np.zeros(m * L, dtype=complex)
    if m % 2:
        Y[:m // 2 + 1] = X[:m // 2 + 1]
        Y[-(m // 2):] = X[-(m // 2):]
    else:
        Y[:m // 2] = X[:m // 2]
        Y[-(m // 2 - 1):] = X[-(m // 2 - 1):]
    return np.fft.ifft(Y) * L


def simular(fd, fs, dur, semilla=SEMILLA):
    """IQ sintetico de una fuente CW con desvanecimiento Rayleigh de ancho fd.

    El ruido gaussiano complejo se filtra con un FIR pasa-bajos de 257 taps a la
    tasa de la envolvente (FS_ENV): a fs=240 kHz un FIR de 257 taps solo puede
    tener una banda de transicion de ~1.5 kHz, tres ordenes de magnitud mayor
    que fD.  La envolvente de banda base se interpola despues a fs.
    """
    from scipy.signal import firwin, lfilter

    n = int(dur * fs)
    L = max(1, int(round(fs / FS_ENV)))
    m = int(np.ceil(n / L)) + TAPS
    rng = np.random.default_rng(semilla)
    w = (rng.standard_normal(m) + 1j * rng.standard_normal(m)) / np.sqrt(2)
    h = lfilter(firwin(TAPS, fd, fs=fs / L), 1.0, w)[TAPS:][:int(np.ceil(n / L))]
    h /= np.sqrt(np.mean(np.abs(h) ** 2))
    return (_interpolar(h, L)[:n] * np.exp(1j * np.pi / 4)).astype(np.complex64)


def _psd(x, fs, nperseg, noverlap=None, nfft=None, detrend=False):
    """PSD de Welch centrada (f en Hz, un solo lado del espectro original)."""
    from scipy.signal import welch

    nperseg = min(nperseg, x.size)
    f, P = welch(x, fs=fs, nperseg=nperseg,
                 noverlap=nperseg // 2 if noverlap is None else min(noverlap, nperseg - 1),
                 nfft=nfft or nperseg, return_onesided=False, detrend=detrend)
    return np.fft.fftshift(f), np.fft.fftshift(P)


def _ancho_3db(f, P, k=9):
    """Semi-ancho a -3 dB de la PSD normalizada a su maximo.

    Al remover la media, el bin exacto de DC queda anulado; la referencia es el
    maximo de la PSD, que en el espectro ideal cae en DC.  Se suaviza (media
    movil de k bins) porque un periodograma de 5 s tiene pocos grados de
    libertad.  Se devuelve el primer cruce hacia frecuencias crecientes.
    """
    P = np.convolve(P, np.ones(k) / k, mode="same")
    m = f >= 0
    fp, Pp = f[m], P[m]
    i0 = int(np.argmax(Pp))
    Pdb = 10 * np.log10(Pp / Pp[i0] + 1e-30)
    i = int(np.argmax(Pdb[i0:] < -3)) + i0
    if i == i0:
        return float(fp[-1] - fp[i0])
    return float(fp[i - 1] + (fp[i] - fp[i - 1]) * (-3 - Pdb[i - 1]) / (Pdb[i] - Pdb[i - 1]))


def _sigma(f, P):
    """Ancho RMS (desviacion estandar) de la PSD bilateral."""
    P = np.maximum(P, 0.0)
    m0 = P.sum()
    return float(np.sqrt((f ** 2 * P).sum() / m0)) if m0 > 0 else 0.0


def analizar(x, fs):
    """Espectro Doppler de la envolvente y estimacion de fD y Tc.

    Criterio de estimacion: para un espectro Doppler plano de ancho fD, la PSD
    de las fluctuaciones de la envolvente es su autoconvolucion (triangular),
    de varianza sigma^2 = 2 fD^2 / 3.  Por eso se usa fD = sqrt(3/2) * sigma
    (ancho RMS), mas estable que el cruce puntual de -3 dB con registros cortos.
    'ancho_PSD_Hz' es sigma (ancho RMS medido) y 'ancho_3dB_Hz' el cruce crudo.
    """
    from scipy.signal import resample_poly

    L = max(1, int(round(fs / FS_ENV)))
    xd = resample_poly(x, 1, L)
    fsd = fs / L
    r = np.abs(xd)
    f_env, P_env = _psd(r - r.mean(), fsd, 1024, nfft=8192)
    f_iq, P_iq = _psd(xd, fsd, 1024, nfft=8192)
    f_man, P_man = _psd(x, fs, 4096, 2048, 4096)          # metodo del manual
    sigma = _sigma(f_env, P_env)
    fd = float(np.sqrt(1.5) * sigma)
    return {
        "fD_estimado_Hz": fd,
        "Tc_s": 0.423 / fd if fd > 0 else float("inf"),
        "ancho_PSD_Hz": sigma,
        "ancho_3dB_Hz": _ancho_3db(f_env, P_env),
        "ancho_manual_Hz": _ancho_3db(f_man, P_man),
        "n_muestras": int(x.size),
        "t": np.arange(r.size) / fsd,
        "r": r,
        "f_env": f_env,
        "P_env_norm": P_env / P_env.max(),
        "f_iq": f_iq,
        "P_iq_norm": P_iq / P_iq.max(),
    }


def _confirmar(indicacion):
    try:
        respuesta = input(f"{indicacion}\n¿Iniciar captura? [s/N] ").strip().lower()
    except EOFError:
        raise SystemExit("el modo real requiere confirmacion interactiva; usa --sim o --selftest")
    return respuesta in ("s", "si", "sí", "y")


def reporte_consola(res, freq, rate, dur, modo):
    print(f"Modo        : {modo}")
    print(f"Frecuencia  : {freq / 1e6:.3f} MHz")
    print(f"Sample rate : {rate / 1e3:.1f} kHz")
    print(f"Duracion    : {dur:.1f} s por escenario")
    filas = [[n.capitalize(), f"{d['fD_estimado_Hz']:.2f}",
              f"{d['Tc_s']:.3f}", f"{d['ancho_PSD_Hz']:.2f}"] for n, d in res.items()]
    print(comun.tabla_markdown(["Escenario", "fD (Hz)", "Tc (s)", "Ancho PSD (Hz)"], filas))
    manual = ", ".join(f"{n}: {d['ancho_manual_Hz']:.1f}" for n, d in res.items())
    print(f"PSD IQ a fs (metodo del manual): ancho a -3 dB = {manual} Hz; "
          f"resolucion {rate / 4096:.1f} Hz, insuficiente para fD de pocos Hz; "
          f"el espectro Doppler se calcula sobre la envolvente decimada a {FS_ENV:.0f} Hz")


def fig_envolventes(res, ruta):
    import matplotlib.pyplot as plt

    ejes = np.atleast_1d(plt.subplots(len(res), 1, figsize=(9, 2.6 * len(res)),
                                      sharex=True)[1])
    for ax, (nombre, d) in zip(ejes, res.items()):
        ax.plot(d["t"], d["r"], lw=0.7)
        ax.set_ylabel("|x(t)|")
        ax.set_title(f"{nombre.capitalize()}: fD ≈ {d['fD_estimado_Hz']:.2f} Hz, "
                     f"Tc ≈ {d['Tc_s']:.3f} s")
        ax.grid(alpha=0.3)
    ejes[-1].set_xlabel("Tiempo (s)")
    ejes[0].figure.suptitle("Variación temporal de la envolvente")
    ejes[0].figure.tight_layout()
    return comun.guardar_fig(ejes[0].figure, ruta, MOSTRAR)


def fig_doppler(res, ruta):
    import matplotlib.pyplot as plt

    ejes = np.atleast_1d(plt.subplots(len(res), 1, figsize=(9, 2.8 * len(res)))[1])
    for ax, (nombre, d) in zip(ejes, res.items()):
        ax.plot(d["f_env"], 10 * np.log10(d["P_env_norm"] + 1e-30), lw=0.7,
                label="PSD envolvente")
        ax.plot(d["f_iq"], 10 * np.log10(d["P_iq_norm"] + 1e-30), lw=0.7,
                ls="--", alpha=0.8, label="PSD IQ (canal)")
        ax.axhline(-3, color="C3", ls="--", lw=0.8, label="-3 dB")
        ax.axvline(d["fD_estimado_Hz"], color="C2", ls=":", lw=1.0,
                   label=f"fD ≈ {d['fD_estimado_Hz']:.2f} Hz")
        limite = 3 * max(d["ancho_PSD_Hz"], 2.0)
        ax.set_xlim(-limite, limite)
        ax.set_ylim(-30, 3)
        ax.set_ylabel("PSD (dB)")
        ax.set_title(f"Espectro Doppler: {nombre}")
        ax.grid(alpha=0.3)
        ax.legend(loc="upper right", fontsize=8)
    ejes[-1].set_xlabel("Frecuencia (Hz)")
    ejes[0].figure.suptitle("Espectro Doppler de la envolvente (normalizado)")
    ejes[0].figure.tight_layout()
    return comun.guardar_fig(ejes[0].figure, ruta, MOSTRAR)


def selftest():
    x = simular(3.0, 240e3, 5.0)
    fd = analizar(x, 240e3)["fD_estimado_Hz"]
    assert 1.5 < fd < 6.0, fd
    print("practica5 selftest OK")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("-f", "--freq", type=float, default=433.9e6)
    p.add_argument("-r", "--rate", type=float, default=240e3)
    p.add_argument("--dur", type=float, default=5.0, help="segundos por escenario")
    p.add_argument("--escenarios", default="estatico,lento,rapido")
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

    nombres = [s.strip() for s in args.escenarios.split(",") if s.strip()]
    desconocidos = [s for s in nombres if s not in FD_ESC]
    if desconocidos:
        raise SystemExit(f"escenarios desconocidos: {desconocidos}; usa {list(FD_ESC)}")

    n = int(args.dur * args.rate)
    res = {}
    for nombre in nombres:
        fd_teo, indicacion = FD_ESC[nombre]
        if args.sim:
            x = simular(fd_teo, args.rate, args.dur)
        else:
            if not _confirmar(indicacion):
                print(f"escenario '{nombre}' omitido")
                continue
            print(f"capturando {args.dur:.1f} s ({n} muestras) a {args.freq / 1e6:.3f} MHz ...")
            x = comun.capturar(args.freq, n=n, rate=args.rate, ganancia=args.gain)
        res[nombre] = analizar(x, args.rate)
        res[nombre]["fD_teorico_Hz"] = fd_teo

    if not res:
        raise SystemExit("no se midio ningun escenario")

    reporte_consola(res, args.freq, args.rate, args.dur,
                    "simulacion" if args.sim else "real")
    fig_envolventes(res, FIGS / "envolventes.png")
    fig_doppler(res, FIGS / "doppler.png")
    comun.guardar_json(DATOS / "resultados.json",
                       modo="simulacion" if args.sim else "real",
                       frecuencia_Hz=args.freq, rate_Hz=args.rate, dur_s=args.dur,
                       escenarios={n: {k: v for k, v in d.items()
                                       if not isinstance(v, np.ndarray)}
                                   for n, d in res.items()})
    print(f"figuras en {FIGS}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
