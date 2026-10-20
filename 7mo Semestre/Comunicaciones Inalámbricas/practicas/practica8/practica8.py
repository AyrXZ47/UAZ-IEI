#!/usr/bin/env python3
"""Practica 8. Proyecto integrador: caracterizacion experimental de un canal.

Agrega los resultados de las practicas 2 a 7 (cada una guardo su
`datos/resultados.json` con la tecla `s`) en un modelo integral del canal:
perdidas por trayectoria, shadowing, Rayleigh, Doppler, selectividad en
frecuencia y capacidad.

Uso:
    python3 practica8.py               # agrega lo medido en las practicas 2-7
    python3 practica8.py --sim         # mismo resumen con datos sinteticos (demo)
    python3 practica8.py --selftest    # verifica la agregacion sin correr nada
"""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))
for _n in range(2, 8):                      # cada practica vive en su carpeta
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / f"practica{_n}"))
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


def ruta_datos(n):
    return DIR.parent / f"practica{n}" / "datos" / "resultados.json"


def agregar():
    """Carga el JSON que dejo cada practica 2-7."""
    datos = {}
    for n in PRACTICAS:
        ruta = ruta_datos(n)
        if not ruta.exists():
            raise SystemExit(f"falta {ruta}; corre la practica {n} y guarda con `s`")
        datos[n] = comun.cargar_json(ruta)
    return datos


def _escalares(d):
    """Copia un dict de resultados sin los arreglos (para el JSON)."""
    return {k: v for k, v in d.items() if not isinstance(v, np.ndarray)}


def datos_sim():
    """Seis resultados sinteticos con los simuladores de cada practica."""
    import practica2 as p2
    import practica3 as p3
    import practica4 as p4
    import practica5 as p5
    import practica6 as p6
    import practica7 as p7

    d = np.array([1.0, 2.0, 5.0, 10.0, 15.0, 20.0])
    aj = p2.ajustar(d, p2.simular(d, 10).mean(axis=1))
    r3 = p3.analizar(p3.medir_sim(50, seed=1))
    r4 = np.random.default_rng(0).rayleigh(1 / np.sqrt(2), 20000)
    r4 = p4.analizar(r4 / np.sqrt(np.mean(r4 ** 2)), 0.5)
    r5 = p5.analizar(p5.simular(3.0, 240e3, 5.0), 240e3)
    r6 = {esc: p6.analizar(x, 2.4e6)
          for esc, x in p6.capturar_sim(2.4e6, 1 << 20, seed=0).items()}
    r7 = {}
    for i, esc in enumerate(p7.SNR_SIM_DB):
        r7[esc] = p7.estimar(*p7.captura_sim(1 << 17, p7.SNR_SIM_DB[esc], seed=i),
                             200e3)
    return {
        2: {"n_estimado": aj["n"], "r2": aj["r2"],
            "desviacion_residuales_dB": aj["sigma_res"]},
        3: {"mu": r3["mu"], "sigma": r3["sigma"], "n": 50,
            "p_valor_normalidad": r3["p_valor_normalidad"]},
        4: {"sigma_rayleigh": r4["sigma"],
            "porcentaje_profundo": r4["porcentaje_profundo"],
            "porcentaje_teorico": r4["porcentaje_teorico"],
            "n_muestras": 20000},
        5: {"escenarios": {"lento": _escalares(r5)}},
        6: {esc: _escalares(r) for esc, r in r6.items()},
        7: {"banda_Hz": 200e3,
            "escenarios": {esc: _escalares(r) for esc, r in r7.items()}},
    }


def filas_resumen(datos):
    p2, p3, p4 = datos[2], datos[3], datos[4]
    p5, p6, p7 = datos[5], datos[6], datos[7]
    fds = ", ".join(f"{k}: {v['fD_estimado_Hz']:.2f} Hz"
                    for k, v in p5["escenarios"].items())
    cap = ", ".join(f"{k}: {v['C_kbps']:.0f} kbps"
                    for k, v in p7["escenarios"].items())
    return [
        ["2. Perdidas por trayectoria", f"n = {p2['n_estimado']:.2f}",
         f"R2 = {p2['r2']:.3f}, residuos {p2['desviacion_residuales_dB']:.2f} dB"],
        ["3. Shadowing", f"mu = {p3['mu']:.1f} dB, sigma = {p3['sigma']:.2f} dB",
         f"N = {p3['n']}, p normalidad = {p3['p_valor_normalidad']:.3f}"],
        ["4. Fading Rayleigh",
         f"sigma_R = {p4['sigma_rayleigh']:.3f}, "
         f"profundo = {p4['porcentaje_profundo']:.1f} %",
         f"teorico {p4['porcentaje_teorico']:.1f} %, {p4['n_muestras']} muestras"],
        ["5. Efecto Doppler", fds, "Tc = 0.423 / fD"],
        ["6. Selectividad en frecuencia",
         f"Bc(0.5) LOS = {p6['LOS']['Bc_50_Hz']/1e3:.1f} kHz, "
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


def main(argv=None):
    import argparse

    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--sim", action="store_true",
                   help="resumen con datos sinteticos, sin leer las mediciones")
    p.add_argument("--selftest", action="store_true")
    args = p.parse_args(argv)

    if args.selftest:
        selftest()
        return 0

    datos = datos_sim() if args.sim else agregar()
    print("=== Modelo integral del canal ===\n")
    print(resumen_markdown(datos))
    ruta = comun.guardar_json(DATOS / "resumen.json", practicas=datos,
                              actividades=list(ACTIVIDADES.values()),
                              modo="simulacion" if args.sim else "real")
    print(f"\nresumen en {ruta}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
