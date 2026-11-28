# Trabajo final — Sistemas de Calidad

Tema: inseguridad de los alumnos en los horarios de entrada y salida del
Campus Siglo XXI (UAZ). Entrega: análisis FODA con 15 planteamientos por
cuadrante, diagrama de Pareto de las debilidades y reporte con justificación
documentada.

## Contenido

| Archivo | Descripción |
| --- | --- |
| `main.tex` / `main.pdf` | Reporte completo (portada, FODA, Pareto, plan, bibliografía y anexos). |
| `pareto.xlsx` | Libro de Excel: portada, tabla de Pareto con fórmulas, gráfico nativo, microdatos y FODA. |
| `datos/encuesta.csv` | Microdatos: 250 alumnos × 15 debilidades (1 = la percibe). |
| `datos/pareto.csv` | Tabla resumen ordenada con porcentajes acumulados. |
| `datos/generar_datos.py` | Genera el CSV, la figura y el libro de Excel. |
| `figuras/pareto.png` | Figura del reporte (PNG, 300 dpi). |

## Compilar

```sh
latexmk -pdf main.tex
```

## Regenerar datos y figura

Requiere Python 3 con `matplotlib`, `numpy` y `xlsxwriter`:

```sh
python3 datos/generar_datos.py
```

El generador usa una semilla fija, de modo que los conteos del reporte, del
CSV y del libro de Excel siempre coinciden (1 285 menciones; ocho debilidades
acumulan el 80.47 %).

## Nota sobre los datos

La base es un ejercicio académico simulado y calibrado con los indicadores de
la ENSU del tercer trimestre de 2026, como se declara en el apartado 4.5 del
reporte. El procedimiento de tabulación y de Pareto es el que se aplicaría a
una base real.
