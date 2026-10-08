#!/usr/bin/env python3
"""Practica 8. Proyecto integrador: caracterizacion experimental de un canal inalambrico.

Orquesta la campana de medicion completa reutilizando las practicas 2 a 7 y
agrega sus resultados en un modelo integral del canal (perdidas por trayectoria,
shadowing, Rayleigh, Doppler, selectividad en frecuencia y capacidad).

Uso:
    python3 practica8.py --sim        # corre las practicas 2-7 en simulacion y agrega
    python3 practica8.py --real       # corre las practicas 2-7 con el transmisor real
    python3 practica8.py --selftest   # verifica la agregacion sin correr nada
"""
import argparse
import subprocess
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import comun  # noqa: E402

DIR = Path(__file__).resolve().parent
DATOS = DIR / "datos"
PRACTICAS = (2, 3, 4, 5, 6, 7)
ACTIVIDADES = {
    2: "Perdidas por trayectoria (n)",
    3: "Shadowing log-normal (sigma)",
    4: "Fading Rayleigh (% profundo)",
    5: "Efecto Doppler (fD, Tc)",
    6: "Selectividad en frecuencia (Bc)",
    7: "Capacidad de canal (C)",
}


def correr(sim):
    for n in PRACTICAS:
        script = DIR.parent / f"practica{n}" / f"practica{n}.py"
        orden = [sys.executable, str(script), "--no-show"]
        if sim:
            orden.insert(2, "--sim")
        print(f"\n=== Ejecutando practica {n} ({'simulacion' if sim else 'real'}) ===")
        subprocess.run(orden, cwd=script.parent, check=True)


def agregar():
    datos = {}
    for n in PRACTICAS:
        ruta = DIR.parent / f"practica{n}" / "datos" / "resultados.json"
        if not ruta.exists():
            raise SystemExit(f"falta {ruta}; corre primero la practica {n}")
        datos[n] = comun.cargar_json(ruta)
    return datos


def filas_resumen(datos):
    p2, p3, p4 = datos[2], datos[3], datos[4]
    p5, p6, p7 = datos[5], datos[6], datos[7]
    fds = ", ".join(f"{k}: {v['fD_estimado_Hz']:.2f} Hz" for k, v in p5["escenarios"].items())
    cap = ", ".join(f"{k}: {v['C_kbps']:.0f} kbps" for k, v in p7["escenarios"].items())
    return [
        ["2. Perdidas por trayectoria", f"n = {p2['n_estimado']:.2f}",
         f"R2 = {p2['r2']:.3f}, residuos {p2['desviacion_residuales_dB']:.2f} dB"],
        ["3. Shadowing", f"mu = {p3['mu']:.1f} dB, sigma = {p3['sigma']:.2f} dB",
         f"N = {p3['n']}, p normalidad = {p3['p_valor_normalidad']:.3f}"],
        ["4. Fading Rayleigh", f"sigma_R = {p4['sigma_rayleigh']:.3f}, profundo = {p4['porcentaje_profundo']:.1f} %",
         f"teorico {p4['porcentaje_teorico']:.1f} %, {p4['n_muestras']} muestras"],
        ["5. Efecto Doppler", fds,
         "Tc = 0.423 / fD"],
        ["6. Selectividad en frecuencia", f"Bc(0.5) LOS = {p6['LOS']['Bc_50_Hz']/1e3:.1f} kHz, "
         f"NLOS = {p6['NLOS']['Bc_50_Hz']/1e3:.1f} kHz",
         f"variacion espectral {p6['LOS']['variacion_espectral_dB']:.1f} / "
         f"{p6['NLOS']['variacion_espectral_dB']:.1f} dB"],
        ["7. Capacidad", cap, f"B = {p7['banda_Hz']/1e3:.0f} kHz"],
    ]


def resumen_markdown(datos):
    filas = [[ACTIVIDADES[n], *fila[1:]] for n, fila in
             zip(PRACTICAS, filas_resumen(datos))]
    return comun.tabla_markdown(["Actividad", "Resultado", "Detalle"], filas)


def selftest():
    sintetico = {
        2: {"n_estimado": 3.1, "r2": 0.99, "desviacion_residuales_dB": 1.4},
        3: {"mu": -50.0, "sigma": 6.0, "n": 50, "p_valor_normalidad": 0.5},
        4: {"sigma_rayleigh": 0.707, "porcentaje_profundo": 22.0,
            "porcentaje_teorico": 22.1, "n_muestras": 1000},
        5: {"escenarios": {"lento": {"fD_estimado_Hz": 3.0}}},
        6: {"LOS": {"Bc_50_Hz": 1e6, "variacion_espectral_dB": 1.0},
            "NLOS": {"Bc_50_Hz": 5e5, "variacion_espectral_dB": 6.0}},
        7: {"banda_Hz": 200e3, "escenarios": {"LOS": {"C_kbps": 1000.0}}},
    }
    tabla = resumen_markdown(sintetico)
    assert "n = 3.10" in tabla and "sigma = 6.00" in tabla and "1000 kbps" in tabla
    print("practica8 selftest OK")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--sim", action="store_true", help="corre 2-7 en simulacion y agrega")
    p.add_argument("--real", action="store_true", help="corre 2-7 con el transmisor real")
    p.add_argument("--selftest", action="store_true")
    args = p.parse_args()

    if args.selftest:
        selftest()
        return 0

    if args.sim or args.real:
        correr(sim=args.sim)

    datos = agregar()
    print("\n=== Modelo integral del canal ===\n")
    print(resumen_markdown(datos))
    comun.guardar_json(DATOS / "resumen.json", practicas=datos,
                       actividades=list(ACTIVIDADES.values()))
    print(f"\nresumen en {DATOS / 'resumen.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
