# Prácticas de Tecnologías Celulares

Implementación de las 12 prácticas del manual `PracticaTC.pdf` (Dr. Víktor Iván
Rodríguez Abdalá), cada una con su script, sus figuras, sus resultados y su reporte en
LaTeX.

## Estructura

```
practicas/
├── PracticaTC.pdf / .md      manual original y su conversión a Markdown
├── comun/
│   ├── preambulo.tex         portada, paquetes y macros de los reportes
│   └── estilo_graficas.py    tema oscuro y helpers de figuras/JSON
├── practicaN/
│   ├── practicaN.py          simulación y generación de resultados
│   ├── main.tex              reporte
│   ├── main.pdf              reporte compilado
│   ├── figs/                 figuras generadas por el script
│   └── datos/resultados.json números que cita el reporte
└── compilar.sh               compila los 12 reportes
```

## Cómo correr una práctica

```bash
cd practicaN
python3 practicaN.py          # genera figs/ y datos/resultados.json
latexmk -pdf main.tex         # compila el reporte
```

Los scripts no dependen del directorio de trabajo: usan `Path(__file__)` para localizar
sus carpetas. Solo requieren NumPy, SciPy y Matplotlib.

Para compilar todo:

```bash
./compilar.sh
```

## Notas

- **Python en lugar de MATLAB.** El manual pide MATLAB, pero en este repositorio el
  procesamiento se hace en Python (NumPy/SciPy), igual que en Comunicaciones
  Inalámbricas. Las funciones son equivalentes y los reportes lo indican.
- **Prácticas 1 y 12 sin hardware.** No había RTL-SDR conectado al momento de la corrida,
  así que esas dos usan capturas sintéticas etiquetadas como tales. La cadena de análisis
  (FFT, Welch, detección de portadoras, espectrograma) es la misma que se aplicaría a una
  captura real; el script está listo para sustituir la fuente por el receptor.
- **Estilo de figuras.** `comun/estilo_graficas.py` fija el tema oscuro que ya usa el
  resto del repositorio, para que las figuras no dependan del `matplotlibrc` local.
- **Números.** Los reportes citan los valores de `datos/resultados.json`; si se cambia una
  semilla o un parámetro, hay que volver a correr el script y actualizar el reporte.
