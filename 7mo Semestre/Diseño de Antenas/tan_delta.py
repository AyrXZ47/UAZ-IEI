import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Ejercicio 4 — Clasificación de materiales según tangente de pérdidas
# tan δ = σ/(ωε) = fc/f  con  fc = σ/(2π ε0 εr)  → rectas de pendiente −1 en log-log
eps0 = 8.854e-12                # permitividad del vacío [F/m]
UMBRAL_COND = 100.0             # tan δ ≥ 100  → buen conductor
UMBRAL_AISL = 0.01              # tan δ ≤ 0.01 → buen aislante

MATERIALES = [                  # (nombre, σ [S/m], εr, fc esperada, color)
    ("Aluminio",  3.84e7,  8.8, 7.846e16, "#FE53BB"),
    ("Porcelana", 1e-12,   6.0, 2.996e-3, "#08F7FE"),
    ("Cuarzo",    1e-17,   3.8, 4.730e-8, "#F5D300"),
]

f = np.logspace(-12, 20, 500)   # Hz: cubre las 6 fronteras de los 3 materiales

fig, ax = plt.subplots(figsize=(11, 6.5))

for nombre, sigma, er, fc_esp, color in MATERIALES:
    fc = sigma / (2 * np.pi * eps0 * er)
    assert abs(fc - fc_esp) / fc_esp < 0.01, f"{nombre}: fc = {fc:.3e} ≠ {fc_esp:.3e}"
    ax.loglog(f, fc / f, color=color, lw=2.2,
              label=fr"{nombre}:  $f_c = {fc:.2e}$ Hz")

# Zonas de clasificación (franjas horizontales)
ax.set_ylim(1e-10, 1e13)
ax.axhspan(UMBRAL_COND, 1e13, color="red",   alpha=0.07)
ax.axhspan(UMBRAL_AISL, UMBRAL_COND, color="green", alpha=0.05)
ax.axhspan(1e-10, UMBRAL_AISL, color="deepskyblue", alpha=0.07)

# Líneas umbral
ax.axhline(UMBRAL_COND, color="white", ls="--", lw=1.2)
ax.axhline(UMBRAL_AISL, color="white", ls="--", lw=1.2)
ax.text(9e19, 2.2e2, r"$\tan\delta = 100$", color="white", fontsize=10, ha="right")
ax.text(9e19, 2.2e-3, r"$\tan\delta = 0.01$", color="white", fontsize=10, ha="right")

# Nombres de las zonas
ax.text(1.5e-12, 1e11, "BUEN CONDUCTOR", color="#ff9db8", fontsize=10,
        fontweight="bold", va="center")
ax.text(1.5e-12, 1e-1, "DIELÉCTRICO DISIPATIVO", color="#9be8a8", fontsize=10,
        fontweight="bold", va="center")
ax.text(1.5e-12, 1e-7, "BUEN AISLANTE", color="#8fd4ff", fontsize=10,
        fontweight="bold", va="center")

ax.set_xlim(1e-12, 1e20)
ax.set_xlabel(r"frecuencia  $f$  [Hz]")
ax.set_ylabel(r"$\tan\delta = \dfrac{\sigma}{\omega\epsilon}$")
ax.set_title("Clasificación de materiales por tangente de pérdidas — Ejercicio 4")

# Entrada extra: recordatorio de que todas las curvas son fc/f (pendiente −1)
handles, labels = ax.get_legend_handles_labels()
handles.append(Line2D([0], [0], color="0.75", lw=1.2, ls="-"))
labels.append(r"todas: $\tan\delta = f_c/f$  (pendiente $-1$)")
ax.legend(handles, labels, loc="upper right", fontsize=9)

fig.tight_layout()
fig.savefig("tan_delta_clasificacion.png", dpi=200, bbox_inches="tight")
fig.savefig("tan_delta_clasificacion.pdf", bbox_inches="tight")
print("fc verificadas: Al ≈ 7.85e16 Hz, Porcelana ≈ 3.0e-3 Hz, Cuarzo ≈ 4.7e-8 Hz")

plt.show()
