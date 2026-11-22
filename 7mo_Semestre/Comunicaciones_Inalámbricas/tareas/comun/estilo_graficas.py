"""Estilo comun de las figuras de las practicas de Tecnologias Celulares.

Reproduce el tema oscuro que ya usa el resto del repositorio (matplotlibrc del
equipo) para que las figuras no dependan de la configuracion local.

Uso en cada practicaN.py:

    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "comun"))
    from estilo_graficas import COLORES, guardar, guardar_json, preparar
"""

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

FONDO = "#212946"
COLORES = ["#08f7fe", "#fe53bb", "#f5d300", "#00ff9f", "#b967ff", "#8d99ae"]

plt.rcParams.update(
    {
        "figure.dpi": 140,
        "savefig.dpi": 160,
        "savefig.bbox": "tight",
        "savefig.facecolor": FONDO,
        "figure.facecolor": FONDO,
        "axes.facecolor": FONDO,
        "axes.edgecolor": "#8d99ae",
        "axes.labelcolor": "#e8e8e8",
        "text.color": "#e8e8e8",
        "xtick.color": "#cfcfcf",
        "ytick.color": "#cfcfcf",
        "grid.color": "#3b4a7a",
        "grid.alpha": 0.55,
        "grid.linewidth": 0.6,
        "font.size": 10,
        "axes.titlesize": 11,
        "axes.labelsize": 10,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.prop_cycle": matplotlib.cycler(color=COLORES),
        "legend.frameon": False,
        "legend.fontsize": 9,
        "legend.labelcolor": "#e8e8e8",
        "lines.linewidth": 1.6,
        "lines.markersize": 4,
    }
)


def preparar(base):
    """Crea figs/ y datos/ junto al script y devuelve sus rutas."""
    base = Path(base)
    figs, datos = base / "figs", base / "datos"
    figs.mkdir(exist_ok=True)
    datos.mkdir(exist_ok=True)
    return figs, datos


def guardar(fig, ruta, cerrar=True):
    """Guarda una figura con el estilo comun."""
    ruta = Path(ruta)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(ruta, facecolor=FONDO)
    if cerrar:
        plt.close(fig)
    return ruta


def guardar_json(datos, ruta):
    """Escribe resultados serializables (convierte numpy a tipos nativos)."""
    def limpio(obj):
        if isinstance(obj, dict):
            return {k: limpio(v) for k, v in obj.items()}
        if isinstance(obj, (list, tuple)):
            return [limpio(v) for v in obj]
        if hasattr(obj, "item"):
            return obj.item()
        return obj

    ruta = Path(ruta)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(
        json.dumps(limpio(datos), indent=2, ensure_ascii=False), encoding="utf-8"
    )
    return ruta
