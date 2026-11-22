import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d.proj3d import proj_transform

# Onda plana uniforme: propagación +y, E en ẑ (600 V/m), H en x̂ (1.59 A/m), λ = 6π m
# Mapeo en matplotlib: x → dirección de H, y → propagación, z → dirección de E
E0 = 600.0                     # amplitud de E [V/m]
H0 = 1.59                      # amplitud de H [A/m]
lam = 6 * np.pi                # longitud de onda [m] ≈ 18.85 m
k = 2 * np.pi / lam            # k = 1/3 rad/m
eta = E0 / H0                  # η = E/H ≈ 377 Ω (vacío libre)

y = np.linspace(0, 2 * lam, 400)
E = E0 * np.cos(k * y)
H = H0 * np.cos(k * y)
z0 = np.zeros_like(y)

RED, BLUE = "#ff5d5d", "#4da3ff"


class Arrow3D(FancyArrowPatch):
    """Flecha 3D robusta: FancyArrowPatch proyectado (quiver de mpl 3.11
    deforma los segmentos en este entorno)."""

    def __init__(self, x, y, z, dx, dy, dz, *args, **kwargs):
        super().__init__((0, 0), (0, 0), *args, **kwargs)
        self._xyz = (x, y, z)
        self._dxdydz = (dx, dy, dz)

    def do_3d_projection(self, renderer=None):
        x, y, z = self._xyz
        dx, dy, dz = self._dxdydz
        x0, y0, _ = proj_transform([x], [y], [z], self.axes.M)
        x1, y1, z1 = proj_transform([x + dx], [y + dy], [z + dz], self.axes.M)
        self.set_positions((x0[0], y0[0]), (x1[0], y1[0]))
        return z1[0]


def field_arrows(ax, ys, values, axis, color, scale=11):
    """Flechas de campo E (axis='z') o H (axis='x') sobre el eje de propagación."""
    for yv, v in zip(ys, values):
        d = (v, 0, 0) if axis == "x" else (0, 0, v)
        ax.add_artist(Arrow3D(0, yv, 0, *d, mutation_scale=scale,
                              arrowstyle="-|>", color=color, lw=1.4))


fig = plt.figure(figsize=(12, 7))
ax = fig.add_subplot(projection="3d")

# Curvas de campo
ax.plot(z0, y, E, color=RED, lw=2.8,
        label=r"$\mathbf{E}(y)=600\cos(ky)\,\hat{z}$  [V/m]")
ax.plot(H, y, z0, color=BLUE, lw=2.8,
        label=r"$\mathbf{H}(y)=1.59\cos(ky)\,\hat{x}$  [A/m]")

# Vectores de campo cada λ/16
ys = np.arange(0, 2 * lam + lam / 32, lam / 16)
field_arrows(ax, ys, E0 * np.cos(k * ys), "z", RED)
field_arrows(ax, ys, H0 * np.cos(k * ys), "x", BLUE)

# Flecha de propagación +y
ax.add_artist(Arrow3D(0, 2.15 * lam, 0, 0, 0.32 * lam, 0,
                      mutation_scale=18, arrowstyle="-|>", color="white", lw=2.2))
ax.text(0, 1.98 * lam, 200, r"propagación $+\hat{y}$", color="white", fontsize=11)

# Marca de λ entre dos crestas
ax.plot([0, 0], [0, lam], [E0 + 40] * 2, "w--", lw=1.1)
ax.text(0, 0.5 * lam, E0 + 110, r"$\lambda = 6\pi \approx 18.85$ m",
        color="white", fontsize=11, ha="center")

# Guías de amplitud
ax.plot([0, 0], [0, 2 * lam], [E0] * 2, color=RED, ls=":", lw=0.9, alpha=0.5)
ax.plot([0, 0], [0, 2 * lam], [-E0] * 2, color=RED, ls=":", lw=0.9, alpha=0.5)
ax.text(-1.15, 2.08 * lam, E0 + 40, r"$+600$ V/m", color=RED, fontsize=10)
ax.text(-1.15, 2.08 * lam, -E0 - 70, r"$-600$ V/m", color=RED, fontsize=10)
ax.plot([H0, H0], [0, 2 * lam], [0, 0], color=BLUE, ls=":", lw=0.9, alpha=0.5)
ax.plot([-H0, -H0], [0, 2 * lam], [0, 0], color=BLUE, ls=":", lw=0.9, alpha=0.5)
ax.text(H0 + 0.08, 0.25 * lam, 55, r"$+1.59$ A/m", color=BLUE, fontsize=10)
ax.text(-H0 - 0.62, 0.25 * lam, 55, r"$-1.59$ A/m", color=BLUE, fontsize=10)

# Ejes
ax.set_xlabel(r"$x$  (dirección de $\mathbf{H}$)")
ax.set_ylabel(r"$y$  (propagación)")
ax.set_zlabel(r"$z$  (dirección de $\mathbf{E}$)")
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(0, 2.55 * lam)
ax.set_zlim(-780, 1020)
ax.set_xticks([-H0, 0, H0])
ax.set_xticklabels([r"$-1.59$", "0", r"$+1.59$"])
ax.set_yticks([0, lam / 2, lam, 3 * lam / 2, 2 * lam])
ax.set_yticklabels(["0", r"$3\pi$", r"$6\pi$", r"$9\pi$", r"$12\pi$"])
ax.set_zticks([-600, 0, 600])
ax.view_init(elev=18, azim=-58)
ax.set_box_aspect((1.1, 3.2, 1.4))

# Datos de la onda
ax.text2D(0.02, 0.97,
          r"$k = 2\pi/\lambda = 1/3$ rad/m"
          "\n"
          r"$\eta = E/H \approx 377\ \Omega$ (vacío libre)"
          "\n"
          r"$f = c/\lambda \approx 15.9$ MHz"
          "\n"
          r"$\mathbf{E}\times\mathbf{H} = \hat{z}\times\hat{x} = +\hat{y}$",
          transform=ax.transAxes, fontsize=10, va="top", color="white")

ax.set_title("Onda electromagnética plana uniforme — propagación en $+\\hat{y}$")
ax.legend(loc="upper right", fontsize=10)

fig.savefig("oem_onda_plana.png", dpi=200, bbox_inches="tight")
fig.savefig("oem_onda_plana.pdf", bbox_inches="tight")
print(f"η = {eta:.2f} Ω, k = {k:.4f} rad/m, f = {3e8/lam/1e6:.2f} MHz, λ = {lam:.2f} m")

plt.show()
