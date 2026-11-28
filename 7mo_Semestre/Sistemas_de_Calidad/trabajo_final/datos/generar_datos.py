#!/usr/bin/env python3
"""Genera la base simulada, el diagrama de Pareto y el libro de Excel.

El ejercicio reproduce el instrumento descrito en el reporte: una encuesta de
respuesta múltiple aplicada a 250 alumnos del Campus Siglo XXI. Los conteos se
fijan por diseño (semilla fija) para que el reporte, el CSV y el libro de Excel
sean consistentes entre sí.

Salidas (relativas a la carpeta trabajo_final/):
    datos/encuesta.csv     microdatos, una fila por alumno
    datos/pareto.csv       tabla resumen ordenada
    figuras/pareto.pdf     figura vectorial para LaTeX
    figuras/pareto.png     vista previa
    pareto.xlsx            libro con datos, FODA y gráfico nativo de Excel
"""

from __future__ import annotations

import csv
import random
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import xlsxwriter

BASE = Path(__file__).resolve().parent.parent
DATOS = BASE / "datos"
FIGURAS = BASE / "figuras"
DATOS.mkdir(exist_ok=True)
FIGURAS.mkdir(exist_ok=True)

SEMILLA = 20261127
ALUMNOS = 250

# clave, texto para el reporte, etiqueta corta, menciones
DEBILIDADES = [
    ("D1", "Iluminación insuficiente en accesos, andadores y estacionamientos",
     "Iluminación", 190),
    ("D2", "Ausencia de vigilancia en los accesos peatonales en horas pico",
     "Vigilancia accesos", 132),
    ("D3", "Calles aledañas con banquetas rotas, poda excesiva y lotes baldíos",
     "Calles y baldíos", 168),
    ("D4", "Falta de control de acceso vehicular e identificación de conductores",
     "Control vehicular", 92),
    ("D5", "Poca presencia de seguridad en la salida del turno vespertino",
     "Turno vespertino", 150),
    ("D6", "Cámaras mal ubicadas o fuera de servicio que dejan puntos ciegos",
     "Cámaras", 118),
    ("D7", "Transporte público insuficiente y paradas alejadas o sin iluminación",
     "Transporte", 104),
    ("D8", "Falta de señalización y de rutas peatonales seguras",
     "Señalización", 80),
    ("D9", "Comunicación deficiente de los protocolos de emergencia",
     "Protocolos", 68),
    ("D10", "Puentes peatonales y pasos a desnivel inexistentes o en mal estado",
     "Puentes", 56),
    ("D11", "Estacionamientos sin delimitación, numeración ni control",
     "Estacionamientos", 44),
    ("D12", "Ausencia de programas de acompañamiento entre alumnos",
     "Acompañamiento", 34),
    ("D13", "Coordinación débil con la policía municipal y estatal",
     "Coordinación", 24),
    ("D14", "Mobiliario urbano vandalizado y sin mantenimiento",
     "Mobiliario", 16),
    ("D15", "Falta de intendencia y vigilancia en los últimos minutos de la jornada",
     "Intendencia", 9),
]

AREAS = ["Ciencias de la Salud", "Ingeniería", "Ciencias Básicas", "Posgrado"]
AREAS_PESOS = [0.52, 0.31, 0.12, 0.05]

# Sesgo por turno: la salida del vespertino ocurre de noche, así que estas
# debilidades se perciben con más frecuencia en ese turno. El total de
# menciones no cambia; solo se reparte entre turnos.
SESGO = {
    "D1": {"Vespertino": 1.18, "Matutino": 0.98},  # iluminación
    "D5": {"Vespertino": 1.60, "Matutino": 0.80},   # seguridad al salir
    "D7": {"Vespertino": 1.25, "Matutino": 0.92},   # transporte
}


def generar_microdatos() -> list[dict]:
    rng = random.Random(SEMILLA)
    n = ALUMNOS

    alumnos = []
    for i in range(1, n + 1):
        area = rng.choices(AREAS, weights=AREAS_PESOS, k=1)[0]
        turno = "Vespertino" if rng.random() < 0.46 else "Matutino"
        alumnos.append({
            "id": i,
            "sexo": "M" if rng.random() < 0.48 else "F",
            "turno": turno,
            "semestre": rng.choice([1, 3, 5, 7, 9]),
            "area": area,
            "marcas": [0] * len(DEBILIDADES),
        })

    # Asigna exactamente las menciones objetivo. Si la debilidad tiene sesgo
    # por turno, se reparte el total entre turnos y se baraja dentro de cada
    # grupo; si no, se baraja la lista completa de alumnos.
    for j, (clave, _, _, menciones) in enumerate(DEBILIDADES):
        sesgo = SESGO.get(clave)
        if not sesgo:
            orden = list(range(n))
            rng.shuffle(orden)
            for i in orden[:menciones]:
                alumnos[i]["marcas"][j] = 1
            continue

        grupos = {}
        for i, a in enumerate(alumnos):
            grupos.setdefault(a["turno"], []).append(i)

        pesos = {t: sesgo.get(t, 1.0) * len(ids) for t, ids in grupos.items()}
        total_peso = sum(pesos.values())
        cuotas = {t: int(round(menciones * p / total_peso)) for t, p in pesos.items()}
        # Ajusta el redondeo en el turno con más alumnos.
        mayor = max(grupos, key=lambda t: len(grupos[t]))
        cuotas[mayor] += menciones - sum(cuotas.values())

        for turno, ids in grupos.items():
            orden = list(ids)
            rng.shuffle(orden)
            for i in orden[:cuotas[turno]]:
                alumnos[i]["marcas"][j] = 1

    # Ningún cuestionario válido puede quedar sin ninguna debilidad marcada.
    # Se repara con un intercambio que conserva los totales por columna.
    for i, alumno in enumerate(alumnos):
        if sum(alumno["marcas"]) > 0:
            continue
        j = 0  # la debilidad más mencionada tiene holgura de sobra
        alumno["marcas"][j] = 1
        for k, otro in enumerate(alumnos):
            if k != i and sum(otro["marcas"]) >= 3 and otro["marcas"][j] == 1:
                otro["marcas"][j] = 0
                break
        else:  # pragma: no cover - no ocurre con esta semilla
            raise RuntimeError("No se pudo reparar un cuestionario vacío")

    return alumnos


def resumen(alumnos: list[dict]) -> list[dict]:
    filas = []
    for j, (clave, texto, corto, _) in enumerate(DEBILIDADES):
        filas.append({
            "clave": clave,
            "debilidad": texto,
            "corto": corto,
            "frecuencia": sum(a["marcas"][j] for a in alumnos),
        })
    filas.sort(key=lambda f: (-f["frecuencia"], f["clave"]))
    total = sum(f["frecuencia"] for f in filas)
    acumulado = 0
    for f in filas:
        f["total"] = total
        f["porcentaje"] = f["frecuencia"] / total
        acumulado += f["porcentaje"]
        f["acumulado"] = acumulado
    return filas


def escribir_csv(alumnos: list[dict], filas: list[dict]) -> None:
    claves = [d[0] for d in DEBILIDADES]
    with (DATOS / "encuesta.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["id", "sexo", "turno", "semestre", "area", *claves])
        for a in alumnos:
            w.writerow([a["id"], a["sexo"], a["turno"], a["semestre"], a["area"],
                        *a["marcas"]])

    with (DATOS / "pareto.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["clave", "debilidad", "frecuencia", "porcentaje",
                    "porcentaje_acumulado"])
        for f in filas:
            w.writerow([f["clave"], f["debilidad"], f["frecuencia"],
                        f"{f['porcentaje']:.6f}", f"{f['acumulado']:.6f}"])


def figura_pareto(filas: list[dict]) -> None:
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 7.0,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.facecolor": "white",
        "text.color": "#222222",
        "axes.labelcolor": "#222222",
        "xtick.color": "#333333",
        "ytick.color": "#333333",
        "axes.edgecolor": "#7f7f7f",
        "axes.linewidth": 0.7,
        "pdf.fonttype": 42,
    })

    # 6.4 in = ancho útil de la caja de texto (16 cm), de modo que los puntos
    # tipográficos de la figura coincidan con los del documento.
    fig, ax = plt.subplots(figsize=(6.4, 4.55))
    x = np.arange(len(filas))
    freq = [f["frecuencia"] for f in filas]
    acum = [f["acumulado"] * 100 for f in filas]
    corte = next(i for i, a in enumerate(acum) if a >= 80)

    colores = ["#1f3864"] * (corte + 1) + ["#b8c6de"] * (len(filas) - corte - 1)
    ax.axvspan(-0.5, corte + 0.5, color="#edf1f8", zorder=0)
    ax.bar(x, freq, color=colores, edgecolor="white", linewidth=0.8, zorder=3,
           width=0.72)

    ax.set_xlim(-0.6, len(filas) - 0.4)
    ax.set_ylim(0, max(freq) * 1.14)
    ax.set_ylabel("Menciones", fontsize=7.5, labelpad=4)
    ax.set_xticks(x)
    ax.set_xticklabels([f"{f['clave']}\n{f['corto']}" for f in filas],
                       rotation=42, ha="right", rotation_mode="anchor", fontsize=6.5)
    ax.tick_params(axis="x", length=0, pad=1)
    ax.tick_params(axis="y", labelsize=6.8)
    ax.grid(axis="y", color="#d9d9d9", linewidth=0.5, zorder=1)
    ax.set_axisbelow(True)
    for lado in ("top", "right"):
        ax.spines[lado].set_visible(False)

    for xi, v in zip(x, freq):
        ax.annotate(f"{v}", (xi, v), xytext=(0, 8), textcoords="offset points",
                    ha="center", va="bottom", fontsize=5.9, color="#1f3864")

    ax2 = ax.twinx()
    ax2.plot(x, acum, color="#c00000", marker="o", markersize=2.8,
             markerfacecolor="white", markeredgewidth=0.9, linewidth=1.2, zorder=5,
             label="Porcentaje acumulado")
    ax2.set_ylim(0, 105)
    ax2.set_yticks([0, 20, 40, 60, 80, 100])
    ax2.set_yticklabels(["0 %", "20 %", "40 %", "60 %", "80 %", "100 %"])
    ax2.set_ylabel("Porcentaje acumulado", fontsize=7.5, labelpad=4)
    ax2.tick_params(axis="y", labelsize=6.8)
    ax2.axhline(80, color="#595959", linestyle=(0, (4, 2)), linewidth=0.8, zorder=4)
    ax2.text(len(filas) - 0.55, 81.6, "Umbral 80 %", ha="right", va="bottom",
             fontsize=5.9, color="#595959")

    ax2.annotate(
        f"{corte + 1} de 15 debilidades\nconcentran el {acum[corte]:.1f} %",
        xy=(corte + 0.1, acum[corte]), xytext=(corte + 1.1, 55),
        fontsize=6.4, color="#1f3864", linespacing=1.25,
        arrowprops=dict(arrowstyle="-|>", color="#1f3864", lw=0.7,
                        connectionstyle="arc3,rad=-0.22"),
    )

    handles = [plt.Rectangle((0, 0), 1, 1, color="#1f3864"),
               plt.Rectangle((0, 0), 1, 1, color="#b8c6de"),
               plt.Line2D([0], [0], color="#c00000", marker="o", markersize=2.6,
                          markerfacecolor="white", lw=1.1)]
    etiquetas = ["Debilidades vitales (acumulan el 80 %)", "Debilidades triviales",
                 "Porcentaje acumulado"]
    ax.legend(handles, etiquetas, loc="lower left", bbox_to_anchor=(0, 1.005, 1, 0.1),
              ncol=3, mode="expand", frameon=False, fontsize=5.8,
              handlelength=1.2, columnspacing=0.8, borderaxespad=0)

    fig.subplots_adjust(left=0.10, right=0.90, top=0.845, bottom=0.30)
    fig.savefig(FIGURAS / "pareto.pdf", bbox_inches="tight")
    fig.savefig(FIGURAS / "pareto.png", dpi=300, bbox_inches="tight")
    plt.close(fig)


def escribir_excel(filas: list[dict]) -> None:
    wb = xlsxwriter.Workbook(BASE / "pareto.xlsx")
    wb.set_calc_mode("auto")

    azul = "#1f3864"
    azul_claro = "#d9e2f3"
    gris = "#f2f2f2"
    dorado = "#b8860b"

    f_titulo = wb.add_format({"bold": True, "font_size": 16, "font_color": azul})
    f_sub = wb.add_format({"font_size": 10, "font_color": "#595959"})
    f_encabezado = wb.add_format({
        "bold": True, "font_color": "white", "bg_color": azul,
        "align": "center", "valign": "vcenter", "text_wrap": True,
        "border": 1, "border_color": "#8ea9db",
    })
    f_texto = wb.add_format({"border": 1, "border_color": "#bfbfbf",
                             "valign": "vcenter", "text_wrap": True})
    f_centro = wb.add_format({"border": 1, "border_color": "#bfbfbf",
                              "align": "center", "valign": "vcenter"})
    f_entero = wb.add_format({"border": 1, "border_color": "#bfbfbf",
                              "align": "center", "valign": "vcenter", "num_format": "0"})
    f_pct = wb.add_format({"border": 1, "border_color": "#bfbfbf",
                           "align": "center", "valign": "vcenter",
                           "num_format": "0.00%"})
    f_total = wb.add_format({"bold": True, "bg_color": azul_claro,
                             "border": 1, "border_color": "#8ea9db",
                             "align": "center"})
    f_total_txt = wb.add_format({"bold": True, "bg_color": azul_claro,
                                 "border": 1, "border_color": "#8ea9db"})
    f_nota = wb.add_format({"font_size": 9, "font_color": "#595959",
                            "text_wrap": True, "valign": "top"})
    f_clave = wb.add_format({"bold": True, "align": "center", "valign": "top",
                             "border": 1, "border_color": "#bfbfbf",
                             "font_color": azul})
    f_foda_f = wb.add_format({"bg_color": "#d9ead3", "text_wrap": True,
                              "valign": "top", "border": 1,
                              "border_color": "#bfbfbf"})
    f_foda_o = wb.add_format({"bg_color": "#dbe8f7", "text_wrap": True,
                              "valign": "top", "border": 1,
                              "border_color": "#bfbfbf"})
    f_foda_d = wb.add_format({"bg_color": "#fce5cd", "text_wrap": True,
                              "valign": "top", "border": 1,
                              "border_color": "#bfbfbf"})
    f_foda_a = wb.add_format({"bg_color": "#f4cccc", "text_wrap": True,
                              "valign": "top", "border": 1,
                              "border_color": "#bfbfbf"})

    # ------------------------------------------------------------------ Portada
    ws = wb.add_worksheet("Portada")
    ws.hide_gridlines(2)
    ws.set_column("A:A", 2)
    ws.set_column("B:B", 26)
    ws.set_column("C:C", 78)
    ws.merge_range("B2:C2", "Universidad Autónoma de Zacatecas", f_titulo)
    ws.merge_range("B3:C3", "Unidad Académica de Ingeniería Eléctrica", f_sub)
    ws.write("B5", "Materia", f_total_txt)
    ws.write("C5", "Sistemas de Calidad (7S · AD/26 · SEMI)")
    ws.write("B6", "Trabajo", f_total_txt)
    ws.write("C6", "Trabajo final: análisis FODA y diagrama de Pareto")
    ws.write("B7", "Tema", f_total_txt)
    ws.write("C7", "Inseguridad de los alumnos en los horarios de entrada y salida del Campus Siglo XXI")
    ws.write("B8", "Alumno", f_total_txt)
    ws.write("C8", "Arnold Yovick Ríos Zaldívar · Matrícula 35167151")
    ws.write("B9", "Docente", f_total_txt)
    ws.write("C9", "Miguel Ángel Fraire Hernández")
    ws.write("B10", "Fecha", f_total_txt)
    ws.write("C10", "27 de noviembre de 2026")
    ws.merge_range("B12:C12", "Contenido del libro", f_encabezado)
    filas_portada = [
        ("Pareto", "Tabla de frecuencias ordenada y diagrama de Pareto (barras y porcentaje acumulado)."),
        ("Datos", "Microdatos de la encuesta: 250 alumnos y 15 debilidades (1 = la percibe)."),
        ("FODA", "Las 15 fortalezas, oportunidades, debilidades y amenazas del diagnóstico."),
        ("Gráfico", "El diagrama de Pareto en tamaño carta, listo para imprimir o exportar."),
    ]
    for i, (hoja, desc) in enumerate(filas_portada, start=13):
        ws.write(i, 1, hoja, f_total_txt)
        ws.write(i, 2, desc, f_texto)
    ws.merge_range("B18:C19",
                   "Los conteos de la hoja Pareto son fórmulas que suman la hoja Datos; "
                   "si se modifica una marca, la tabla y el gráfico se recalculan.",
                   f_nota)
    for r in range(13, 17):
        ws.set_row(r, 30)
    ws.set_portrait()
    ws.center_vertically()
    ws.set_paper(9)
    ws.set_margins(1.5, 1.5, 1.5, 1.5)
    ws.fit_to_pages(1, 1)
    ws.print_area(1, 1, 18, 2)
    ws.set_footer("&C&P/&N")

    # ------------------------------------------------------------------- Pareto
    ps = wb.add_worksheet("Pareto")
    ps.hide_gridlines(2)
    ps.set_column("A:A", 6)
    ps.set_column("B:C", 46)
    ps.set_column("D:D", 13)
    ps.set_column("E:F", 15)
    ps.set_column("G:G", 14)
    ps.set_column("H:H", 26)
    ps.set_row(0, 24)

    ps.merge_range("A1:H1", "Diagrama de Pareto de las debilidades", f_titulo)
    ps.merge_range("A2:H2",
                   "Inseguridad de los alumnos en los horarios de entrada y salida · "
                   "Campus Siglo XXI · 250 encuestas · 1 285 menciones",
                   f_sub)
    encabezados = ["N.º", "Clave", "Debilidad", "Menciones",
                   "Porcentaje", "% acumulado", "Umbral 80 %", "Etiqueta"]
    for c, h in enumerate(encabezados):
        ps.write(3, c, h, f_encabezado)
    ps.set_row(3, 32)

    # La hoja Datos tiene las 15 columnas de debilidades en F..T.
    col_datos = {clave: 5 + j for j, (clave, _, _, _) in enumerate(DEBILIDADES)}
    primera = 4  # fila 5 en Excel
    ultima = primera + len(filas) - 1
    fila_total = ultima + 1

    for i, f in enumerate(filas):
        r = primera + i
        excel_row = r + 1
        col = col_datos[f["clave"]]
        letra = chr(ord("F") + col - 5)
        ps.write_number(r, 0, i + 1, f_centro)
        ps.write_string(r, 1, f["clave"], f_clave)
        ps.write_string(r, 2, f["debilidad"], f_texto)
        ps.write_formula(r, 3, f"=SUM(Datos!{letra}$2:{letra}$251)", f_entero,
                         f["frecuencia"])
        ps.write_formula(r, 4, f"=D{excel_row}/$D${fila_total + 1}", f_pct,
                         f["porcentaje"])
        ps.write_formula(r, 5, f"=SUM($E$5:E{excel_row})", f_pct, f["acumulado"])
        ps.write_number(r, 6, 0.8, f_pct)
        ps.write_string(r, 7, f"{f['clave']} · {f['corto']}", f_texto)
        ps.set_row(r, 30)

    ps.write(fila_total, 2, "Total de menciones", f_total_txt)
    ps.write_formula(fila_total, 3, f"=SUM(D5:D{ultima + 1})", f_total,
                     sum(f["frecuencia"] for f in filas))
    ps.write_formula(fila_total, 4, f"=SUM(E5:E{ultima + 1})", f_total, 1.0)
    ps.write_blank(fila_total, 5, None, f_total)
    ps.write_blank(fila_total, 6, None, f_total)

    ps.merge_range(fila_total + 2, 0, fila_total + 2, 7,
                   "Fuente: encuesta aplicada a 250 alumnos del Campus Siglo XXI "
                   "(respuesta múltiple; cada alumno podía marcar varias debilidades).",
                   f_nota)
    ps.merge_range(fila_total + 3, 0, fila_total + 3, 7,
                   "Lectura: 8 de las 15 debilidades (53.3 %) concentran el 80.5 % "
                   "de las menciones; ahí deben aplicarse primero los recursos.",
                   f_nota)
    ps.set_row(fila_total + 2, 28)
    ps.set_row(fila_total + 3, 28)

    # Gráfico combinado: columnas (menciones) + línea (% acumulado) + umbral 80 %.
    def crear_grafico():
        grafico = wb.add_chart({"type": "column"})
        grafico.add_series({
            "name": "Menciones",
            "categories": ["Pareto", primera, 7, ultima, 7],
            "values": ["Pareto", primera, 3, ultima, 3],
            "fill": {"color": azul},
            "border": {"color": "#ffffff"},
            "gap": 45,
        })
        linea = wb.add_chart({"type": "line"})
        linea.add_series({
            "name": "% acumulado",
            "categories": ["Pareto", primera, 7, ultima, 7],
            "values": ["Pareto", primera, 5, ultima, 5],
            "y2_axis": True,
            "line": {"color": "#c00000", "width": 2.0},
            "marker": {"type": "circle", "size": 5,
                       "fill": {"color": "#ffffff"},
                       "border": {"color": "#c00000"}},
        })
        linea.add_series({
            "name": "Umbral 80 %",
            "categories": ["Pareto", primera, 7, ultima, 7],
            "values": ["Pareto", primera, 6, ultima, 6],
            "y2_axis": True,
            "line": {"color": "#7f7f7f", "width": 1.25, "dash_type": "dash"},
        })
        # En los gráficos combinados de xlsxwriter, el eje secundario se toma
        # del segundo gráfico, no del principal.
        linea.set_y2_axis({
            "name": "Porcentaje acumulado",
            "name_font": {"size": 9},
            "min": 0,
            "max": 1,
            "major_unit": 0.2,
            "num_format": "0%",
            "line": {"color": "#7f7f7f"},
        })
        grafico.combine(linea)
        grafico.set_title({
            "name": "Pareto de debilidades percibidas por los alumnos",
            "name_font": {"size": 13, "bold": True, "color": azul},
        })
        grafico.set_x_axis({
            "name": "Debilidades ordenadas de mayor a menor frecuencia",
            "num_font": {"size": 7, "rotation": -45},
            "name_font": {"size": 9},
            "line": {"color": "#7f7f7f"},
        })
        grafico.set_y_axis({
            "name": "Menciones",
            "name_font": {"size": 9},
            "major_gridlines": {"visible": True,
                                "line": {"color": "#e0e0e0"}},
            "line": {"color": "#7f7f7f"},
        })
        grafico.set_legend({"position": "bottom", "font": {"size": 9}})
        grafico.set_size({"width": 1100, "height": 500})
        grafico.set_chartarea({"border": {"color": "#bfbfbf"}})
        return grafico

    ps.insert_chart("J4", crear_grafico(), {"x_offset": 10, "y_offset": 5})
    ps.set_landscape()
    ps.set_paper(9)
    ps.set_margins(0.8, 0.8, 1.2, 1.2)
    ps.fit_to_pages(1, 1)
    ps.print_area(0, 0, ultima, 7)
    ps.set_footer("&C&P/&N")

    # ------------------------------------------------------------------ Gráfico
    gs = wb.add_worksheet("Gráfico")
    gs.hide_gridlines(2)
    gs.set_landscape()
    gs.set_paper(9)
    gs.set_margins(1.0, 1.0, 1.0, 1.0)
    gs.fit_to_pages(1, 1)
    gs.merge_range("A1:M1", "Diagrama de Pareto de las debilidades", f_titulo)
    gs.merge_range("A2:M2",
                   "Inseguridad de los alumnos en los horarios de entrada y salida · "
                   "Campus Siglo XXI · 250 encuestas · 1 285 menciones",
                   f_sub)
    gs.insert_chart("A4", crear_grafico(), {"x_offset": 5, "y_offset": 5})
    gs.print_area(0, 0, 28, 17)
    gs.set_footer("&C&P/&N")


    ps.freeze_panes(4, 0)
    ps.autofilter(3, 0, ultima, 7)

    # -------------------------------------------------------------------- Datos
    ds = wb.add_worksheet("Datos")
    ds.freeze_panes(1, 0)
    ds.set_column("A:A", 6)
    ds.set_column("B:B", 7)
    ds.set_column("C:C", 11)
    ds.set_column("D:D", 9)
    ds.set_column("E:E", 21)
    ds.set_column("F:T", 7)

    encabezados_datos = ["ID", "Sexo", "Turno", "Semestre", "Área",
                         *[d[0] for d in DEBILIDADES]]
    for c, h in enumerate(encabezados_datos):
        ds.write(0, c, h, f_encabezado)
    for r, a in enumerate(alumnos, start=1):
        ds.write_number(r, 0, a["id"], f_centro)
        ds.write_string(r, 1, a["sexo"], f_centro)
        ds.write_string(r, 2, a["turno"], f_centro)
        ds.write_number(r, 3, a["semestre"], f_centro)
        ds.write_string(r, 4, a["area"], f_texto)
        for j, marca in enumerate(a["marcas"]):
            ds.write_number(r, 5 + j, marca, f_centro)
    ds.autofilter(0, 0, ALUMNOS, len(encabezados_datos) - 1)
    ds.set_landscape()
    ds.set_paper(9)
    ds.set_margins(0.8, 0.8, 1.0, 1.0)
    ds.fit_to_pages(1, 0)
    ds.repeat_rows(0)
    ds.print_area(0, 0, ALUMNOS, len(encabezados_datos) - 1)
    ds.set_footer("&C&P/&N")

    # --------------------------------------------------------------------- FODA
    fs = wb.add_worksheet("FODA")
    fs.set_column("A:A", 7)
    fs.set_column("B:B", 14)
    fs.set_column("C:C", 96)
    fs.write(0, 0, "Clave", f_encabezado)
    fs.write(0, 1, "Categoría", f_encabezado)
    fs.write(0, 2, "Propuesta", f_encabezado)
    fs.set_row(0, 26)

    formatos = {"F": f_foda_f, "O": f_foda_o, "D": f_foda_d, "A": f_foda_a}
    nombres = {"F": "Fortaleza", "O": "Oportunidad", "D": "Debilidad", "A": "Amenaza"}
    fila = 1
    for letra, textos in FODA.items():
        for i, texto in enumerate(textos, start=1):
            fs.write_string(fila, 0, f"{letra}{i}", f_clave)
            fs.write_string(fila, 1, nombres[letra], formatos[letra])
            fs.write_string(fila, 2, texto, formatos[letra])
            fs.set_row(fila, 30)
            fila += 1
    fs.freeze_panes(1, 0)
    fs.autofilter(0, 0, fila - 1, 2)
    fs.set_portrait()
    fs.set_paper(9)
    fs.set_margins(1.2, 1.2, 1.2, 1.2)
    fs.fit_to_pages(1, 0)
    fs.repeat_rows(0)
    fs.print_area(0, 0, fila - 1, 2)
    fs.set_footer("&C&P/&N")

    wb.close()


FODA = {
    "F": [
        "Comunidad estudiantil numerosa y organizada en sociedades de alumnos y grupos de mensajería.",
        "Accesos delimitados y con caseta de vigilancia, lo que permite registrar entradas y salidas.",
        "Red de videovigilancia instalada en edificios, pasillos y estacionamientos.",
        "Personal de seguridad de la Universidad presente en los turnos matutino y vespertino.",
        "Área de atención médica y brigadas de protección civil capacitadas para emergencias.",
        "Alumbrado con luminarias LED en el corredor central y en los accesos principales.",
        "Ubicación del campus sobre una avenida principal con varias rutas de transporte urbano.",
        "Procedimiento institucional para registrar y canalizar reportes de incidentes.",
        "Directorio de emergencias y protocolo de actuación difundido en la página web de la Universidad.",
        "Planta docente y personal administrativo que permanecen hasta el cierre de actividades.",
        "Accesos peatonales alternos que permiten salir sin atravesar el estacionamiento.",
        "Actividades deportivas, culturales y de tutoría que retienen a los alumnos en el campus.",
        "Programa de becas y apoyos de transporte que reduce la dependencia del transporte público.",
        "Diseño abierto del campus, con visibilidad hacia la avenida desde la mayoría de los edificios.",
        "Comités de alumnos y tutores que dan seguimiento a casos de acoso, violencia y discriminación.",
    ],
    "O": [
        "Programas federales y estatales de prevención del delito que financian alumbrado y videovigilancia.",
        "Convenios con los municipios de Guadalupe y Zacatecas para operativos en horas de entrada y salida.",
        "Marco legal de educación superior y derechos humanos que obliga a garantizar entornos seguros.",
        "Aplicaciones con botón de emergencia y geolocalización, de uso gratuito.",
        "Reducción del costo de cámaras IP, alarmas y sistemas de control de acceso.",
        "Intercambio de protocolos y datos con otras universidades públicas del país.",
        "Presupuesto participativo municipal para banquetas, alumbrado y paradas del entorno.",
        "Prestadores de servicio social y residentes que pueden colaborar en diagnósticos y campañas.",
        "Vinculación con comercios de la avenida para adoptar la figura de espacio seguro.",
        "Cursos gratuitos de defensa personal, primeros auxilios y cultura de la denuncia.",
        "Programa estatal de paradas seguras con iluminación y videovigilancia.",
        "Normas de urbanismo y accesibilidad que priorizan al peatón y a las personas con discapacidad.",
        "Presencia de la Guardia Nacional y de la policía estatal en el corredor universitario.",
        "Fondos de organismos internacionales y organizaciones civiles para ciudades seguras.",
        "Digitalización de trámites y horarios escalonados que reducen aglomeraciones en los accesos.",
    ],
    "D": [
        "Iluminación insuficiente en accesos, andadores y estacionamientos.",
        "Ausencia de vigilancia en los accesos peatonales durante las horas de mayor afluencia.",
        "Calles aledañas con banquetas rotas, poda excesiva y lotes baldíos que reducen la visibilidad.",
        "Falta de control de acceso vehicular e identificación de conductores en la caseta.",
        "Poca presencia de seguridad en la salida del turno vespertino, cuando ya no hay luz natural.",
        "Cámaras mal ubicadas o fuera de servicio que dejan puntos ciegos.",
        "Transporte público insuficiente y paradas alejadas o sin iluminación.",
        "Falta de señalización y de rutas peatonales seguras dentro del campus.",
        "Comunicación deficiente de los protocolos de emergencia y de los números de reporte.",
        "Puentes peatonales y pasos a desnivel inexistentes o en mal estado en la avenida principal.",
        "Estacionamientos sin delimitación, numeración ni control de permanencia.",
        "Ausencia de programas de acompañamiento entre alumnos.",
        "Coordinación débil con la policía municipal y estatal para atender incidentes.",
        "Mobiliario urbano vandalizado y sin mantenimiento.",
        "Falta de personal de intendencia y vigilancia en los últimos minutos de la jornada.",
    ],
    "A": [
        "Incremento del robo a transeúnte en la zona metropolitana Zacatecas–Guadalupe.",
        "Percepción de inseguridad de 77.3 % en el área urbana de Zacatecas, superior al promedio nacional.",
        "Consumo de alcohol y de drogas en calles y jardines cercanos al campus.",
        "Pandillerismo y riñas en la vía pública, con presencia de personas armadas.",
        "Servicio de transporte público deficiente y unidades saturadas en horas pico.",
        "Lotes baldíos y edificios abandonados frente al campus que funcionan como puntos ciegos.",
        "Cruce peligroso de la avenida principal, con tráfico intenso y sin semáforo peatonal.",
        "Comercio informal nocturno que obstruye banquetas y reduce la visibilidad.",
        "Lluvias e inundaciones que obligan a desviarse por calles sin alumbrado.",
        "Apagones y fallas del alumbrado público municipal.",
        "Desplazamiento de la delincuencia hacia los horarios de salida, aprovechando la afluencia.",
        "Rumores y desinformación en redes sociales que amplifican el miedo.",
        "Recortes presupuestales que reducen los programas de seguridad y mantenimiento.",
        "Actividades extracurriculares y prácticas que obligan a salir después de las 20:00 h.",
        "Accidentes viales en los accesos por exceso de velocidad y falta de señalización.",
    ],
}


def main() -> None:
    global alumnos
    alumnos = generar_microdatos()
    filas = resumen(alumnos)
    escribir_csv(alumnos, filas)
    figura_pareto(filas)
    escribir_excel(filas)

    total = sum(f["frecuencia"] for f in filas)
    print(f"Alumnos: {len(alumnos)} · Menciones: {total}")
    print(f"{'Clave':5} {'Frec.':>6} {'%':>7} {'Acum.':>7}  Debilidad")
    for f in filas:
        print(f"{f['clave']:5} {f['frecuencia']:6d} {f['porcentaje']*100:6.2f}% "
              f"{f['acumulado']*100:6.2f}%  {f['corto']}")
    corte = next(i for i, f in enumerate(filas) if f["acumulado"] >= 0.8)
    print(f"\nPocos vitales: {corte + 1} de {len(filas)} → "
          f"{filas[corte]['acumulado']*100:.2f} %")


if __name__ == "__main__":
    main()
