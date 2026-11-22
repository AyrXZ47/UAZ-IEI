# Comunicaciones Inalámbricas

Scripts de la materia: conversión de gráficas MATLAB → Python.

## REGLA OBLIGATORIA: estilo visual de todas las gráficas

Toda gráfica generada en este repo **debe** usar los efectos de **glow** y de **color**
de [mplcyberpunk](https://github.com/dhaitz/mplcyberpunk).

`mplcyberpunk` ya está instalado de forma global en el entorno Nix de este equipo,
así que **no hace falta importarlo de otro lado ni configurarlo**: en cada script
basta con:

1. Importar el paquete:
   ```python
   import mplcyberpunk
   ```

2. Antes de mostrar/guardar la gráfica, aplicar el efecto de glow sobre las figuras
   y ejes activos:
   ```python
   mplcyberpunk.add_glow_effects()
   ```

El efecto de **color** (paleta cyberpunk) se aplica automáticamente con solo importar
`mplcyberpunk`; el **glow** se activa explícitamente con `add_glow_effects()`.

**Checklist por gráfica:**

- [ ] `import mplcyberpunk` presente en el top del script.
- [ ] `mplcyberpunk.add_glow_effects()` llamado justo antes de `plt.show()` /
      `plt.savefig()`.

Si una gráfica no cumple estas dos líneas, **no está terminada**.
