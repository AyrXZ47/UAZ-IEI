"""Utilidades compartidas de las practicas de Comunicaciones Inalambricas.

Captura IQ del RTL-SDR (lectura asincrona, sin perder muestras) y graficas con
el estilo obligatorio del repo (mplcyberpunk).
"""
import json
import sys
import threading
import time
from pathlib import Path

import numpy as np

RATE_DEF = 2.4e6
BW_IF_DEF = 0.6e6
RAIZ = Path(__file__).resolve().parent


def bytes_a_iq(raw):
    """Convierte el buffer crudo uint8 del RTL-SDR a complejos en [-1, 1)."""
    a = np.frombuffer(raw, dtype=np.uint8).astype(np.float32)
    iq = a.view(np.complex64)
    iq *= np.float32(1.0 / 127.5)
    iq -= np.complex64(1.0 + 1.0j)
    return iq


def fijar_ganancia(sdr, ganancia="auto"):
    """Fija la ganancia.  'auto' elige la mayor que no recorte el ADC."""
    if ganancia != "auto":
        sdr.gain = float(ganancia)
        return sdr.get_gain()
    for g in sorted((g for g in sdr.valid_gains_db if g > 0), reverse=True):
        sdr.gain = g
        x = sdr.read_samples(65536)
        clip = np.mean((np.abs(x.real) > 0.98) | (np.abs(x.imag) > 0.98))
        if clip < 0.001:
            break
    return sdr.get_gain()


def info_dispositivo():
    """Equivalente a sdrinfo('RTL-SDR'): datos del dongle conectado."""
    from rtlsdr import RtlSdr

    sdr = RtlSdr()
    info = {
        "fabricante": "RTL2832U",
        "ganancias_dB": sdr.valid_gains_db,
        "frecuencia_min_Hz": 24e6,
        "frecuencia_max_Hz": 1766e6,
        "rate_actual_Hz": sdr.get_sample_rate(),
    }
    try:
        from rtlsdr.librtlsdr import librtlsdr

        info["tuner"] = "R820T" if librtlsdr.rtlsdr_get_tuner_type(sdr.dev_p) == 5 else "otro"
    except Exception:
        info["tuner"] = "desconocido"
    sdr.close()
    return info


def capturar(freq, n=262144, rate=RATE_DEF, ganancia="auto", bw=BW_IF_DEF, ppm=0.0):
    """Captura n muestras IQ a la frecuencia dada (lectura asincrona).

    Devuelve un arreglo complex64.  Lanza RuntimeError si no hay dongle.
    """
    from rtlsdr import RtlSdr

    sdr = RtlSdr()
    sdr.sample_rate = rate
    sdr.center_freq = freq
    if ppm:
        sdr.freq_correction = int(ppm)
    if bw:
        try:
            sdr.set_bandwidth(bw)
        except Exception:
            pass
    fijar_ganancia(sdr, ganancia)

    partes, listo = [], threading.Event()
    total = [0]

    def cb(raw, ctx):
        x = bytes_a_iq(raw)
        partes.append(x)
        total[0] += x.size
        if total[0] >= n:
            listo.set()

    def leer():
        try:
            sdr.read_bytes_async(cb, 2 * min(n, 65536))
        except Exception:
            pass

    hilo = threading.Thread(target=leer, daemon=True)
    hilo.start()
    listo.wait(timeout=n / rate * 3 + 5)
    sdr.cancel_read_async()
    hilo.join(timeout=2)
    sdr.close()
    if total[0] < n:
        raise RuntimeError(f"solo se capturaron {total[0]} de {n} muestras")
    return np.concatenate(partes)[:n].astype(np.complex64)


def potencia_dbfs(x):
    """Potencia promedio de las muestras IQ en dBFS (0 dB = escala completa)."""
    return 10.0 * np.log10(np.mean(np.abs(x) ** 2) + 1e-20)


def espectro(x, fs, nperseg=4096):
    """PSD de Welch centrada (f en Hz, P en densidad de potencia)."""
    from scipy import signal as sig

    f, P = sig.welch(x, fs=fs, nperseg=nperseg, return_onesided=False)
    return np.fft.fftshift(f), np.fft.fftshift(P)


def guardar_fig(fig, ruta, mostrar=True):
    """Aplica el glow obligatorio del repo, guarda el PNG y cierra."""
    import mplcyberpunk
    from matplotlib import pyplot as plt

    for ax in fig.axes:
        mplcyberpunk.add_glow_effects(ax)
    ruta = Path(ruta)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(ruta, dpi=150, bbox_inches="tight")
    if mostrar:
        plt.show()
    plt.close(fig)
    return ruta


def guardar_json(ruta, **datos):
    ruta = Path(ruta)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(json.dumps(datos, indent=2, ensure_ascii=False))
    return ruta


def cargar_json(ruta):
    return json.loads(Path(ruta).read_text())


def tabla_markdown(cabeceras, filas):
    lineas = ["| " + " | ".join(str(c) for c in cabeceras) + " |",
              "|" + "|".join("---" for _ in cabeceras) + "|"]
    for fila in filas:
        lineas.append("| " + " | ".join(str(c) for c in fila) + " |")
    return "\n".join(lineas)


def _autochequeo():
    iq = bytes_a_iq(np.array([255, 255, 0, 0, 128, 128], np.uint8))
    assert np.allclose(iq[:2], [1 + 1j, -1 - 1j])
    assert np.allclose(iq[2], [0.0039 + 0.0039j], atol=1e-3)
    assert abs(potencia_dbfs(np.ones(100, np.complex64)) - 0) < 1e-6
    print("comun.py autochequeo OK")


if __name__ == "__main__":
    _autochequeo()
