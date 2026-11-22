"""Practica 1: exploracion de redes celulares con RTL-SDR y MATLAB/Python.

Genera una captura IQ de una banda celular (modo sintetico, etiquetado como tal),
calcula espectro, PSD y espectrograma, y estima frecuencia central, ancho de banda
y potencia de cada portadora detectada.

Uso:
    python3 practica1.py                # banda de 850 MHz + tabla de bandas
    python3 practica1.py --fs 2.4e6     # ancho de ventana del receptor real
"""

import argparse
import sys
from pathlib import Path

import numpy as np
from scipy import signal as sig

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE.parents[0] / "comun"))
from estilo_graficas import COLORES, guardar, guardar_json, preparar  # noqa: E402

# Banda -> centro de sintonia y portadoras LTE (offset MHz, ancho MHz, potencia dBFS).
BANDAS = {
    "700 MHz": {"fc": 740e6, "portadoras": [(-7.0, 5, -44.0), (4.0, 5, -38.0)]},
    "850 MHz": {"fc": 881e6, "portadoras": [(-4.0, 10, -28.0), (6.0, 5, -42.0)]},
    "1900 MHz": {"fc": 1950e6, "portadoras": [(-4.0, 10, -40.0), (6.0, 5, -34.0)]},
    "AWS 2100 MHz": {"fc": 2140e6, "portadoras": [(-7.0, 5, -39.0), (3.0, 10, -31.0)]},
    "2600 MHz": {"fc": 2650e6, "portadoras": [(-4.0, 10, -46.0), (6.0, 5, -37.0)]},
}
PISO_RUIDO_DBFS = -72.0


def ruido_banda(n, fs, offset, ancho, rng, transicion=0.2e6):
    """Ruido complejo gaussiano filtrado a una banda de ancho `ancho`."""
    X = rng.standard_normal(n) + 1j * rng.standard_normal(n)
    f = np.fft.fftfreq(n, 1 / fs)
    d = np.abs(f - offset)
    mascara = np.clip((ancho / 2 + transicion - d) / transicion, 0.0, 1.0)
    y = np.fft.ifft(X * mascara)
    y /= np.sqrt(np.mean(np.abs(y) ** 2))
    return y


def generar_captura(fc, fs, n, portadoras, piso=PISO_RUIDO_DBFS, semilla=7):
    """Captura IQ sintetica: piso de ruido + portadoras OFDM + tonos espurios."""
    rng = np.random.default_rng(semilla)
    x = (rng.standard_normal(n) + 1j * rng.standard_normal(n)) / np.sqrt(2)
    x *= 10 ** (piso / 20)

    for offset_mhz, ancho_mhz, potencia in portadoras:
        offset, ancho = offset_mhz * 1e6, ancho_mhz * 1e6
        c = ruido_banda(n, fs, offset, ancho, rng)
        x += c * 10 ** (potencia / 20)

    # Espurios de banda angosta (otros servicios presentes en el entorno).
    t = np.arange(n) / fs
    x += 10 ** (-78 / 20) * np.exp(1j * 2 * np.pi * 1.7e6 * t)
    x += 10 ** (-84 / 20) * np.exp(1j * 2 * np.pi * (-3.9e6) * t + 0.7)
    return x


def psd(x, fs, nperseg=4096):
    """PSD unilateral desplazada al centro (dBFS/Hz) con metodo de Welch."""
    f, p = sig.welch(x, fs=fs, nperseg=nperseg, noverlap=nperseg // 2,
                     return_onesided=False, detrend=False, scaling="density")
    orden = np.argsort(f)
    return f[orden], p[orden]


def detectar_portadoras(f, p_db, umbral_db=8.0, ancho_min=0.4e6):
    """Regiones por encima del piso de ruido, con sus parametros espectrales."""
    piso = float(np.percentile(p_db, 10))
    encima = p_db > piso + umbral_db
    regiones, inicio = [], None
    for k, activo in enumerate(np.append(encima, False)):
        if activo and inicio is None:
            inicio = k
        elif not activo and inicio is not None:
            if f[k - 1] - f[inicio] >= ancho_min:
                regiones.append((inicio, k - 1))
            inicio = None

    detectadas = []
    for a, b in regiones:
        fr, pr = f[a:b + 1], 10 ** (p_db[a:b + 1] / 10)
        acumulada = np.cumsum(pr) / np.sum(pr)
        i99 = np.searchsorted(acumulada, np.array([0.005, 0.995]))
        ancho = fr[i99[1]] - fr[i99[0]]
        centro = float(np.sum(fr * pr) / np.sum(pr))
        potencia = float(10 * np.log10(np.sum(pr) * (fr[1] - fr[0])))
        detectadas.append({"centro_mhz": centro / 1e6, "ancho_mhz": ancho / 1e6,
                           "potencia_dbfs": potencia})
    return piso, detectadas


def analizar(x, fs, fc):
    f, p = psd(x, fs)
    p_db = 10 * np.log10(p + 1e-30)
    piso, portadoras = detectar_portadoras(f, p_db)
    for c in portadoras:
        c["centro_mhz_abs"] = fc / 1e6 + c["centro_mhz"]
    ruido = float(np.percentile(p_db, 10))
    pico = float(np.max(p_db))
    potencia = float(10 * np.log10(np.mean(np.abs(x) ** 2)))
    return {
        "fs_mhz": fs / 1e6,
        "muestras": len(x),
        "duracion_ms": 1e3 * len(x) / fs,
        "potencia_dbfs": potencia,
        "piso_ruido_dbfs_hz": float(ruido),
        "pico_dbfs_hz": pico,
        "snr_db": pico - float(ruido),
        "portadoras": portadoras,
        "f": f,
        "p_db": p_db,
    }


def figura_iq(x, fs, figs, fc):
    import matplotlib.pyplot as plt

    n = 400
    t = np.arange(n) / fs * 1e6
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 4.2), sharex=True)
    ax1.plot(t, x.real[:n], lw=0.9, label="I")
    ax1.plot(t, x.imag[:n], lw=0.9, label="Q")
    ax1.set_ylabel("Amplitud")
    ax1.legend(loc="upper right", ncols=2)
    ax1.set_title(f"Componentes I y Q ({fc/1e6:.1f} MHz, {fs/1e6:.0f} MSPS)")
    ax2.plot(t, np.abs(x[:n]), lw=0.9, color=COLORES[2], label="|x|")
    ax2.set_xlabel("Tiempo (µs)")
    ax2.set_ylabel("Envolvente")
    ax2.legend(loc="upper right")
    fig.tight_layout()
    return guardar(fig, figs / "iq_temporal.png")


def figura_espectro(r, figs):
    import matplotlib.pyplot as plt

    f_mhz = (r["fc"] + r["f"]) / 1e6
    fig, ax = plt.subplots(figsize=(8, 4.2))
    ax.plot(f_mhz, r["p_db"], lw=0.7, color=COLORES[0])
    ax.axhline(r["piso_ruido_dbfs_hz"], color=COLORES[5], ls="--", lw=0.9,
               label=f"piso de ruido ({r['piso_ruido_dbfs_hz']:.1f} dBFS/Hz)")
    for c in r["portadoras"]:
        ax.axvspan(c["centro_mhz_abs"] - c["ancho_mhz"] / 2,
                   c["centro_mhz_abs"] + c["ancho_mhz"] / 2,
                   color=COLORES[1], alpha=0.12)
        ax.annotate(f"{c['ancho_mhz']:.1f} MHz\n{c['potencia_dbfs']:.1f} dBFS",
                    (c["centro_mhz_abs"], np.max(r["p_db"])),
                    textcoords="offset points", xytext=(0, 6),
                    ha="center", va="bottom", fontsize=8, color=COLORES[1])
    ax.set_xlabel("Frecuencia (MHz)")
    ax.set_ylabel("Densidad espectral (dBFS/Hz)")
    ax.set_title(f"Espectro observado, sintonía {r['fc']/1e6:.1f} MHz")
    ax.set_ylim(np.percentile(r["p_db"], 1) - 8, np.max(r["p_db"]) + 14)
    ax.legend(loc="lower right")
    return guardar(fig, figs / "espectro.png")


def figura_espectrograma(x, fs, figs):
    import matplotlib.pyplot as plt

    f, t, s = sig.spectrogram(x, fs=fs, window="hann", nperseg=1024,
                              noverlap=768, nfft=1024, return_onesided=False,
                              mode="psd", detrend=False)
    orden = np.argsort(f)
    s_db = 10 * np.log10(s[orden] + 1e-30)
    fig, ax = plt.subplots(figsize=(8, 4.0))
    mesh = ax.pcolormesh(t * 1e3, f[orden] / 1e6, s_db, shading="auto",
                         cmap="magma", vmin=np.percentile(s_db, 10), vmax=s_db.max())
    fig.colorbar(mesh, ax=ax, label="dBFS/Hz")
    ax.set_xlabel("Tiempo (ms)")
    ax.set_ylabel("Frecuencia relativa (MHz)")
    ax.set_title("Espectrograma de la captura")
    ax.grid(False)
    return guardar(fig, figs / "espectrograma.png")


def figura_bandas(resumen, figs):
    import matplotlib.pyplot as plt

    fig, ejes = plt.subplots(2, 3, figsize=(11, 5.6))
    for ax, (nombre, r) in zip(ejes.ravel(), resumen.items()):
        f_mhz = (r["fc"] + r["f"]) / 1e6
        ax.plot(f_mhz, r["p_db"], lw=0.6, color=COLORES[0])
        ax.set_title(nombre, fontsize=9)
        ax.set_xlabel("MHz", fontsize=8)
        ax.set_ylabel("dBFS/Hz", fontsize=8)
        ax.tick_params(labelsize=7)
        for c in r["portadoras"]:
            ax.axvspan(c["centro_mhz_abs"] - c["ancho_mhz"] / 2,
                       c["centro_mhz_abs"] + c["ancho_mhz"] / 2,
                       color=COLORES[1], alpha=0.15)
        if not r["portadoras"]:
            ax.text(0.5, 0.5, "sin portadoras", transform=ax.transAxes,
                    ha="center", color=COLORES[5])
    ejes.ravel()[-1].axis("off")
    fig.suptitle("Exploración de bandas celulares (capturas sintéticas)", fontsize=11)
    fig.tight_layout()
    return guardar(fig, figs / "bandas.png")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--fs", type=float, default=20e6,
                    help="frecuencia de muestreo en Hz (RTL-SDR: 2.4e6)")
    ap.add_argument("--muestras", type=int, default=262144)
    args = ap.parse_args()
    figs, datos = preparar(BASE)

    # 1) Banda principal de trabajo: 850 MHz.
    cfg = BANDAS["850 MHz"]
    x = generar_captura(cfg["fc"], args.fs, args.muestras, cfg["portadoras"])
    r = analizar(x, args.fs, cfg["fc"])
    r["fc"] = cfg["fc"]

    # 2) Exploracion del resto de bandas con la misma cadena de analisis.
    resumen = {}
    for nombre, banda in BANDAS.items():
        xx = generar_captura(banda["fc"], args.fs, args.muestras,
                             banda["portadoras"], semilla=11)
        rr = analizar(xx, args.fs, banda["fc"])
        rr["fc"] = banda["fc"]
        resumen[nombre] = rr

    figura_iq(x, args.fs, figs, cfg["fc"])
    figura_espectro(r, figs)
    figura_espectrograma(x, args.fs, figs)
    figura_bandas(resumen, figs)

    resultados = {
        "receptor": "RTL-SDR (captura sintética; el equipo no estaba conectado)",
        "fs_mhz": args.fs / 1e6,
        "muestras": args.muestras,
        "fc_mhz": cfg["fc"] / 1e6,
        "potencia_dbfs": r["potencia_dbfs"],
        "piso_ruido_dbfs_hz": r["piso_ruido_dbfs_hz"],
        "snr_db": r["snr_db"],
        "portadoras": r["portadoras"],
        "bandas": {
            n: {"fc_mhz": rr["fc"] / 1e6,
                "piso_ruido_dbfs_hz": rr["piso_ruido_dbfs_hz"],
                "portadoras": rr["portadoras"]}
            for n, rr in resumen.items()
        },
    }
    guardar_json(resultados, datos / "resultados.json")

    print(f"Banda 850 MHz @ {cfg['fc']/1e6:.1f} MHz, Fs={args.fs/1e6:.1f} MSPS, "
          f"N={args.muestras}")
    print(f"  potencia={r['potencia_dbfs']:.2f} dBFS, piso={r['piso_ruido_dbfs_hz']:.1f} "
          f"dBFS/Hz, SNR={r['snr_db']:.1f} dB")
    for c in r["portadoras"]:
        print(f"  portadora {c['centro_mhz']:.3f} MHz, BW={c['ancho_mhz']:.2f} MHz, "
              f"P={c['potencia_dbfs']:.1f} dBFS")
    print("\nExploracion de bandas:")
    for n, rr in resumen.items():
        print(f"  {n:14s} {rr['fc']/1e6:7.1f} MHz -> {len(rr['portadoras'])} portadoras")


if __name__ == "__main__":
    main()
