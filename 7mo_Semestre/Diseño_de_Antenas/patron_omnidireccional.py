import numpy as np
import matplotlib.pyplot as plt

# Patrón de radiación de una antena omnidireccional simulada:
# dipolo de media onda — uniforme en azimut (φ), patrón F(θ) en elevación.
# F(θ) = cos(π/2·cosθ)/sinθ, máximo = 1 en θ = 90° (ecuador).


def patron(t):
    """Magnitud normalizada del dipolo λ/2 en cualquier corte vertical."""
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.abs(np.where(np.abs(np.sin(t)) > 1e-9,
                               np.cos(np.pi / 2 * np.cos(t)) / np.sin(t), 0.0))


theta = np.linspace(0, np.pi, 721)          # θ ∈ [0, π]: basta para energía y HPBW
theta_full = np.linspace(0, 2 * np.pi, 1441)  # corte completo para la gráfica polar
phi = np.linspace(0, 2 * np.pi, 361)

F = patron(theta) / patron(theta).max()     # patrón normalizado (campo)
F_full = patron(theta_full) / patron(theta).max()

D = 2 / np.trapezoid(F**2 * np.sin(theta), theta)  # directividad del sólido de revolución
mitad = theta[F >= 1 / np.sqrt(2)]                 # ancho de haz a −3 dB
hpbw = np.degrees(mitad.max() - mitad.min())
assert abs(D - 1.64) < 0.01, f"D = {D:.4f} ≠ 1.64 (dipolo λ/2)"
assert abs(hpbw - 78) < 1.0, f"HPBW = {hpbw:.1f}° ≠ 78° (dipolo λ/2)"

CYAN, PINK = "#08F7FE", "#FE53BB"
fig = plt.figure(figsize=(15, 5.2))

# Corte de elevación (contiene la información; φ no importa)
ax1 = fig.add_subplot(1, 3, 1, projection="polar")
ax1.plot(theta_full, F_full, color=CYAN, lw=2.4)
ax1.fill(theta_full, F_full, color=CYAN, alpha=0.15)
ax1.plot(theta_full, np.ones_like(theta_full), color="0.6", lw=1.0, ls="--", label="isotrópica")
ax1.plot(theta_full, np.full_like(theta_full, 1 / np.sqrt(2)), color="0.6", lw=0.7, ls=":")
ax1.text(np.pi / 2, 0.62, r"$-3$ dB", color="0.75", fontsize=9)
ax1.legend(loc="lower left", bbox_to_anchor=(-0.25, -0.08), fontsize=9)
ax1.set_theta_zero_location("N")
ax1.set_theta_direction(-1)
ax1.set_rticks([0.5, 1.0])
ax1.set_title("Plano de elevación (θ)\n$F(\\theta)=\\dfrac{\\cos(\\frac{\\pi}{2}\\cos\\theta)}{\\sin\\theta}$", pad=18)

# Corte azimutal: constante → omnidireccional
ax2 = fig.add_subplot(1, 3, 2, projection="polar")
ax2.plot(phi, np.ones_like(phi), color=PINK, lw=2.4)
ax2.fill(phi, np.ones_like(phi), color=PINK, alpha=0.15)
ax2.set_rticks([0.5, 1.0])
ax2.set_title("Plano azimutal (φ)\n$F(\\varphi)=1$ (omnidireccional)", pad=18)

# Diagrama 3D de la dona de radiación
ax3 = fig.add_subplot(1, 3, 3, projection="3d")
T, P = np.meshgrid(theta, phi)
R = patron(T) / patron(T).max()
X, Y, Z = R * np.sin(T) * np.cos(P), R * np.sin(T) * np.sin(P), R * np.cos(T)
ax3.plot_surface(X, Y, Z, cmap="cool", rstride=4, cstride=4, alpha=0.9, linewidth=0)
ax3.set_box_aspect((1, 1, 0.85))
ax3.view_init(elev=22, azim=-55)
ax3.set_axis_off()
ax3.set_title(f"Patrón 3D — $D = {D:.2f}$ ({10 * np.log10(D):.2f} dBi)\nHPBW = {hpbw:.1f}° en elevación", pad=0)

fig.suptitle("Antena omnidireccional simulada — dipolo de media onda", fontsize=14, y=0.99)
fig.tight_layout(rect=(0, 0, 1, 0.96))
print(f"D = {D:.3f} ({10 * np.log10(D):.2f} dBi), HPBW = {hpbw:.1f}°, F_max = {F.max():.3f}")

plt.show()
