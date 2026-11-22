"""Practica 12: caracterizacion experimental de una red LTE (captura sintetica).

Genera capturas IQ de una portadora LTE de 10 MHz y otra de 5 MHz en la banda de
850 MHz para tres ubicaciones con distinta atenuacion y multitrayectoria, y estima
potencia, SNR, ancho de banda y capacidad.

Uso: python3 practica12.py
"""

import sys
from pathlib import Path

import numpy as np
from scipy import signal as sig

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE.parents[0] / "comun"))
from estilo_graficas import COLORES, guardar, guardar_json, preparar  # noqa: E402

FS = 15.36e6          # frecuencia de muestreo LTE (1024 FFT, 15 kHz por subportadora)
NFFT = 1024
N = 262144
FC = 881e6
PORTADORAS = [(-3.0e6, 600, -30.0), (4.5e6, 300, -38.0)]  # offset, subportadoras, potencia

UBICACIONES = {
    "Exterior": {"potencias": (-30.0, -38.0), "retardos": [0, 1, 3],
                 "ganancias": [1.0, 0.15, 0.06]},
    "Laboratorio": {"potencias": (-48.0, -56.0), "retardos": [0, 4, 9],
                    "ganancias": [1.0, 0.45, 0.20]},
    "Pasillo": {"potencias": (-55.0, -63.0), "retardos": [0, 7, 15],
                "ganancias": [1.0, 0.60, 0.35]},
}
PISO_RUIDO = -72.0


def qpsk(rng, n):
    return ((2 * rng.integers(0, 2, n) - 1)
            + 1j * (2 * rng.integers(0, 2, n) - 1)) / np.sqrt(2)


def portadora_ofdm(n, fs, offset, nsub, rng):
    """OFDM con 15 kHz por subportadora, normalizado a potencia unitaria."""
    bloques = []
    while sum(len(b) for b in bloques) < n:
        x = np.zeros(NFFT, dtype=complex)
        idx = (np.arange(nsub) - nsub // 2) % NFFT
        x[idx] = qpsk(rng, nsub)
        bloques.append(np.fft.ifft(x) * NFFT / np.sqrt(nsub))
    base = np.concatenate(bloques)[:n]
    t = np.arange(n) / fs
    return base * np.exp(1j * 2 * np.pi * offset * t)


def filtrar_banda(x, offset, ancho, transicion=0.15e6):
    """Filtro de banda con flancos de coseno alzado (rechaza emision fuera de banda)."""
    X = np.fft.fft(x)
    f = np.fft.fftfreq(len(x), 1 / FS)
    d = np.abs(f - offset)
    mascara = np.where(d <= ancho / 2, 1.0,
                       np.where(d >= ancho / 2 + transicion, 0.0,
                                0.5 * (1 + np.cos(np.pi * (d - ancho / 2) / transicion))))
    return np.fft.ifft(X * mascara)


def canal_multitrayectoria(x, retardos, ganancias):
    h = np.zeros(max(retardos) + 1)
    h[retardos] = ganancias
    h /= np.sqrt(np.sum(np.abs(h) ** 2))
    return np.convolve(x, h)[: len(x)]


def generar(ubicacion, rng):
    x = (rng.standard_normal(N) + 1j * rng.standard_normal(N)) / np.sqrt(2)
    x *= 10 ** (PISO_RUIDO / 20)
    for (offset, nsub, _), pot in zip(PORTADORAS, ubicacion["potencias"]):
        c = portadora_ofdm(N, FS, offset, nsub, rng)
        c = filtrar_banda(c, offset, nsub * 15e3)
        x += c * 10 ** (pot / 20)
    x = canal_multitrayectoria(x, ubicacion["retardos"], ubicacion["ganancias"])
    x += (rng.standard_normal(N) + 1j * rng.standard_normal(N)) / np.sqrt(2) \
        * 10 ** (PISO_RUIDO / 20)
    return x


def psd(x, nperseg=4096):
    f, p = sig.welch(x, fs=FS, nperseg=nperseg, noverlap=nperseg // 2,
                     return_onesided=False, detrend=False, scaling="density")
    orden = np.argsort(f)
    return f[orden], p[orden]


def analizar(x):
    f, p = psd(x)
    p_db = 10 * np.log10(p + 1e-30)
    piso = float(np.percentile(p_db, 5))
    encima = p_db > piso + 8
    regiones, inicio = [], None
    for k, activo in enumerate(np.append(encima, False)):
        if activo and inicio is None:
            inicio = k
        elif not activo and inicio is not None:
            if f[k - 1] - f[inicio] >= 0.5e6:
                regiones.append((inicio, k - 1))
            inicio = None

    portadoras = []
    for a, b in regiones:
        fr, pr = f[a:b + 1], 10 ** (p_db[a:b + 1] / 10)
        acum = np.cumsum(pr) / np.sum(pr)
        i99 = np.searchsorted(acum, [0.005, 0.995])
        centro = float(np.sum(fr * pr) / np.sum(pr))
        portadoras.append({
            "centro_mhz": centro / 1e6,
            "centro_mhz_abs": FC / 1e6 + centro / 1e6,
            "ancho_mhz": float((fr[i99[1]] - fr[i99[0]]) / 1e6),
            "potencia_dbfs": float(10 * np.log10(np.sum(pr) * (fr[1] - fr[0]))),
        })

    dentro = p_db > piso + 8
    ruido_lineal = 10 ** (piso / 10) * np.sum(dentro)
    senal_lineal = np.sum(10 ** (p_db[dentro] / 10)) - ruido_lineal
    snr = float(10 * np.log10(max(senal_lineal, 1e-30) / ruido_lineal))
    # Ancho de banda ocupado al 99 % de extremo a extremo (incluye guardas internas).
    activos = np.flatnonzero(encima)
    a, b = activos[0], activos[-1]
    fr, pr = f[a:b + 1], 10 ** (p_db[a:b + 1] / 10)
    acum = np.cumsum(pr) / np.sum(pr)
    i99 = np.searchsorted(acum, [0.005, 0.995])
    ancho_total = fr[i99[1]] - fr[i99[0]]
    capacidad = ancho_total * np.log2(1 + 10 ** (snr / 10)) / 1e6

    return {
        "potencia_dbfs": float(10 * np.log10(np.mean(np.abs(x) ** 2))),
        "piso_ruido_dbfs_hz": piso,
        "snr_db": snr,
        "ancho_total_mhz": ancho_total / 1e6,
        "capacidad_mbps": float(capacidad),
        "portadoras": portadoras,
        "f": f, "p_db": p_db,
    }


def main():
    import matplotlib.pyplot as plt

    figs, datos = preparar(BASE)
    resumen = {}
    for i, (nombre, ubicacion) in enumerate(UBICACIONES.items()):
        rng = np.random.default_rng(100 + i)
        x = generar(ubicacion, rng)
        r = analizar(x)
        r["x"] = x
        resumen[nombre] = r

    # --- Espectros ---
    fig, ejes = plt.subplots(2, 2, figsize=(11, 6.0))
    for ax, (nombre, r) in zip(ejes.ravel(), resumen.items()):
        f_mhz = (FC + r["f"]) / 1e6
        ax.plot(f_mhz, r["p_db"], lw=0.6, color=COLORES[0])
        ax.axhline(r["piso_ruido_dbfs_hz"], color=COLORES[5], ls="--", lw=0.8)
        for c in r["portadoras"]:
            ax.axvspan(c["centro_mhz"] - c["ancho_mhz"] / 2 + FC / 1e6,
                       c["centro_mhz"] + c["ancho_mhz"] / 2 + FC / 1e6,
                       color=COLORES[1], alpha=0.12)
        ax.set_title(nombre, fontsize=10)
        ax.set_xlabel("MHz", fontsize=8)
        ax.set_ylabel("dBFS/Hz", fontsize=8)
        ax.tick_params(labelsize=7)
    ejes.ravel()[-1].axis("off")
    fig.suptitle("Espectros LTE en tres ubicaciones (capturas sintéticas)", fontsize=11)
    fig.tight_layout()
    guardar(fig, figs / "espectros.png")

    # --- Espectrogramas ---
    fig, ejes = plt.subplots(3, 1, figsize=(9, 6.4), sharex=True)
    for ax, (nombre, r) in zip(ejes, resumen.items()):
        f, t, s = sig.spectrogram(r["x"], fs=FS, nperseg=1024, noverlap=768,
                                  return_onesided=False, mode="psd", detrend=False)
        orden = np.argsort(f)
        s_db = 10 * np.log10(s[orden] + 1e-30)
        mesh = ax.pcolormesh(t * 1e3, (FC + f[orden]) / 1e6, s_db, shading="auto",
                             cmap="magma", vmin=np.percentile(s_db, 5),
                             vmax=s_db.max())
        ax.set_ylabel("Frecuencia (MHz)")
        ax.set_title(nombre, fontsize=9)
        ax.grid(False)
        fig.colorbar(mesh, ax=ax, label="dBFS/Hz")
    ejes[-1].set_xlabel("Tiempo (ms)")
    fig.suptitle("Espectrogramas de las tres ubicaciones", fontsize=11)
    fig.tight_layout()
    guardar(fig, figs / "espectrogramas.png")

    # --- Comparacion de potencia y SNR ---
    nombres = list(resumen)
    potencias = [resumen[n]["potencia_dbfs"] for n in nombres]
    snrs = [resumen[n]["snr_db"] for n in nombres]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 3.6))
    ax1.bar(nombres, potencias, color=COLORES[0])
    ax1.set_ylabel("Potencia recibida (dBFS)")
    ax1.set_title("Potencia total")
    ax2.bar(nombres, snrs, color=COLORES[1])
    ax2.set_ylabel("SNR en banda (dB)")
    ax2.set_title("Relación señal a ruido")
    fig.tight_layout()
    guardar(fig, figs / "comparacion.png")

    # --- Estructura OFDM: detalle espectral y forma de onda ---
    r = resumen["Exterior"]
    f_fino, p_fino = psd(r["x"], nperseg=16384)
    f_mhz = (FC + f_fino) / 1e6
    ventana = (f_mhz > FC / 1e6 - 7) & (f_mhz < FC / 1e6 + 1)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8.4, 5.0))
    ax1.plot(f_mhz[ventana], 10 * np.log10(p_fino[ventana] + 1e-30),
             lw=0.6, color=COLORES[0])
    ax1.set_ylabel("dBFS/Hz")
    ax1.set_title("Detalle de la portadora de 10 MHz: forma espectral de OFDM")
    ax2.plot(np.real(r["x"][: 4 * NFFT]), lw=0.7, color=COLORES[2])
    ax2.set_xlabel("Muestra")
    ax2.set_ylabel("Parte real")
    ax2.set_title("Forma de onda OFDM en el tiempo")
    fig.tight_layout()
    guardar(fig, figs / "estructura_ofdm.png")

    resultados = {
        "fc_mhz": FC / 1e6,
        "fs_mhz": FS / 1e6,
        "muestras": N,
        "receptor": "captura sintética (RTL-SDR no conectado)",
        "ubicaciones": {
            n: {k: v for k, v in r.items() if k not in ("f", "p_db", "x")}
            for n, r in resumen.items()
        },
    }
    guardar_json(resultados, datos / "resultados.json")

    for n, r in resumen.items():
        print(f"{n:12s} P={r['potencia_dbfs']:6.2f} dBFS, "
              f"SNR={r['snr_db']:5.1f} dB, BW={r['ancho_total_mhz']:.2f} MHz, "
              f"C={r['capacidad_mbps']:.1f} Mbps")
        for c in r["portadoras"]:
            print(f"    portadora {c['centro_mhz_abs']:8.3f} MHz, BW={c['ancho_mhz']:.2f} MHz")


if __name__ == "__main__":
    main()
