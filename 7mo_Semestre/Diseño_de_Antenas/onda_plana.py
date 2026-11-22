import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mplcyberpunk
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from mpl_toolkits.mplot3d.proj3d import proj_transform

plt.style.use("cyberpunk")

# ------------------------- Parámetros físicos de la onda plana -------------------------
A = 1.0                        # amplitud del campo eléctrico [V/m]
f = 100e6                      # frecuencia [Hz]  <-- cambia aquí la escala (ej. 300 MHz)
c = 3e8                        # velocidad de la luz en el vacío [m/s]
w = 2 * np.pi * f              # ω = 2πf [rad/s]
lam = c / f                    # λ = c/f [m]   (a 300 MHz → 1 m)
k = 2 * np.pi / lam            # k = 2π/λ [rad/m]
T = 1 / f                      # T = 1/f [s]   (a 300 MHz → 3.33 ns)
eta = 377.0                    # impedancia intrínseca del vacío η [Ω]
Hm = A / eta                   # amplitud magnética H_m = A/η [A/m]

# Dominio espacial
x = np.linspace(0, 2 * lam, 200)      # distancia 0..2λ  [m]
mm = x * 1e3                          # distancia en [mm] para mejor lectura

fig = plt.figure(figsize=(9, 6.5))
fig.suptitle("Onda plana uniforme — E y H perpendiculares, propagación en $+x$", fontsize=13)
ax = fig.add_subplot(projection="3d")


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


def make_glow(ax, color, lw, n=6, label=None):
    """Línea 3D con halo tipo cyberpunk: varias capas gruesas y translúcidas."""
    lines = []
    for i in range(n):
        lines.append(ax.plot([], [], [],
                             lw=lw + 3.0 * i / n, color=color,
                             alpha=1.0 if i == 0 else max(0.08, 0.5 - 0.42 * i / n),
                             label=label if i == 0 else None)[0])
    return lines


def set_glow(lines, xs, ys, zs):
    for ln in lines:
        ln.set_data(xs, ys)
        ln.set_3d_properties(zs)


# ==================== E y H perpendiculares ====================
# E_y en la dirección y, H_z en la dirección z, ambas se propagan en +x.
# H se dibuja amplificada ×η para que coincida con E (H·η = E en el vacío).
E_glow = make_glow(ax, "#FF5555", 3, label=r"$\mathbf{E}_y = A\cos(\omega t-kx)$  [V/m]")
H_glow = make_glow(ax, "#00BBFF", 3, label=r"$\mathbf{H}_z = H_m\cos(\omega t-kx)$  [A/m]")

# Relleno bajo la curva (estilo "principio de integrales"): da perspectiva
Efill = Poly3DCollection([], color="#FF5555", alpha=0.4)
ax.add_collection3d(Efill)
Hfill = Poly3DCollection([], color="#00BBFF", alpha=0.4)
ax.add_collection3d(Hfill)


def ribbon(xv, v, axis):
    """Tiras que unen la curva con el plano del eje (área bajo la curva en 3D)."""
    quads = []
    for i in range(len(xv) - 1):
        p0 = [xv[i], 0, 0]
        p1 = [xv[i + 1], 0, 0]
        if axis == "y":
            a0, a1 = [xv[i], v[i], 0], [xv[i + 1], v[i + 1], 0]
        else:
            a0, a1 = [xv[i], 0, v[i]], [xv[i + 1], 0, v[i + 1]]
        quads.append([a0, p0, p1, a1])
    return quads


ax.add_artist(Arrow3D(0.3 * lam * 1e3, 0, 0, 0.6 * lam * 1e3, 0, 0,
                      mutation_scale=16, arrowstyle="-|>", color="white", lw=1.8))
ax.text(0.3 * lam * 1e3, 0, 1.25, "propagación  $+x$", color="white", fontsize=11)
ax.text(0.6 * lam * 1e3, 0, -1.35, r"$\eta = E/H \approx 377\,\Omega \Rightarrow H_m = A/\eta$",
         color="#00DDDD", fontsize=9)

# Guías para mostrar la amplitud máxima y el valor negativo
ax.plot([0, 2 * lam * 1e3], [1, 1], [0, 0], "w--", lw=0.8, alpha=0.6)
ax.plot([0, 2 * lam * 1e3], [-1, -1], [0, 0], "w--", lw=0.8, alpha=0.6)
ax.text(0, 1.08, 0, r"$+A$", color="white", fontsize=10)
ax.text(0, -1.28, 0, r"$-A$", color="white", fontsize=10)

ax.set_xlabel("x [mm] (propagación)")
ax.set_ylabel("E$_y$ [V/m]")
ax.set_zlabel("H$_z$ [A/m]  ($\\times\\eta$, misma escala que E)")
ax.set_xlim(0, 2 * lam * 1e3)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1.5, 1.5)
ax.view_init(28, -65)
ax.legend(fontsize=8)

# ============================== Animación ==============================
nframes = 240                     # avanza 2T en cada ciclo (misma velocidad, más fluido)
dt = 2 * T / nframes


def update(i):
    t0 = i * dt                   # tiempo actual, en segundos

    # Campos E y H al tiempo t0 (H se dibuja ×η para igualar escala)
    ev = A * np.cos(k * x - w * t0)
    set_glow(E_glow, mm, ev, np.zeros_like(mm))
    set_glow(H_glow, mm, np.zeros_like(mm), ev)

    # Relleno bajo la curva para ambas ondas
    Efill.set_verts(ribbon(mm[::2], ev[::2], "y"))
    Hfill.set_verts(ribbon(mm[::2], ev[::2], "z"))

    return E_glow + H_glow + [Efill, Hfill]


ani = animation.FuncAnimation(fig, update, frames=nframes, interval=30, blit=False)

plt.tight_layout()
plt.show()
