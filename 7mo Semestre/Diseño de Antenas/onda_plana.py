import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mplcyberpunk
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

plt.style.use("cyberpunk")

# ------------------------- Parámetros físicos de la onda plana -------------------------
A = 1.0                        # amplitud del campo eléctrico [V/m]
f = 300e6                      # frecuencia [Hz]  <-- cambia aquí la escala (ej. 300 MHz)
c = 3e8                        # velocidad de la luz en el vacío [m/s]
w = 2 * np.pi * f              # ω = 2πf [rad/s]
lam = c / f                    # λ = c/f [m]   (a 300 MHz → 1 m)
k = 2 * np.pi / lam            # k = 2π/λ [rad/m]
T = 1 / f                      # T = 1/f [s]   (a 300 MHz → 3.33 ns)
eta = 377.0                    # impedancia intrínseca del vacío η [Ω]
Hm = A / eta                   # amplitud magnética H_m = A/η [A/m]

# Dominios de las dos variables (distancia y tiempo)
x = np.linspace(0, 2 * lam, 200)      # distancia 0..2λ  [m]
t = np.linspace(0, 2 * T, 160)        # tiempo 0..2T  [s] (segundos)
x0 = 0.6 * lam                        # punto fijo donde se "mira" E(t)
mm = x * 1e3                          # distancia en [mm] para mejor lectura

# E(x,t) = A·cos(kx − ωt)  (propagación en +x, E en y, H en z)
Xg, Tg = np.meshgrid(mm, t)
Esurf = A * np.cos(k * Xg - w * Tg)

fig = plt.figure(figsize=(13, 6))
fig.suptitle("Onda plana uniforme  —  $E(x,t)$", fontsize=13)

ax1 = fig.add_subplot(1, 2, 1, projection="3d")
ax2 = fig.add_subplot(1, 2, 2, projection="3d")


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


# ============================== Subplot 1: E(x,t)  ==============================
ax1.plot_surface(Xg, Tg, Esurf, cmap="viridis", alpha=0.22, linewidth=0, antialiased=True)

# Corte E(t) en un punto fijo x0 (onda "respecto del tiempo")
fix_glow = make_glow(ax1, "#00DDDD", 2, label=f"$E(t)$ en $x_0$ = {x0*1e3:.0f} mm")
fpz = A * np.cos(k * x0 - w * t)
set_glow(fix_glow, [x0 * 1e3] * len(t), t, fpz)

# Corte móvil E(x) al tiempo actual (onda "respecto de la distancia")
snap_glow = make_glow(ax1, "#FF5555", 3, label="$E(x)$ al tiempo $t$ actual")

# Cresta: x = ct  (viaja a la velocidad de la luz, +x)
tcrest = x / c
crest_glow = make_glow(ax1, "#FFFFFF", 1.6, n=4, label="cresta: $x = ct$")
set_glow(crest_glow, mm, tcrest, np.full_like(mm, A))

# Marcas teóricas: λ, T y valor negativo
ax1.plot([0, lam * 1e3], [0, 0], [A + 0.35] * 2, "w--", lw=1.2)
ax1.text(0.5 * lam * 1e3, 0, A + 0.6, r"$\lambda$", color="white", fontsize=13)
ax1.plot([0, 0], [0, T], [A + 0.35] * 2, "w--", lw=1.2)
ax1.text(0, 0.5 * T, A + 0.6, r"$T$", color="white", fontsize=13)
ax1.text(lam * 1e3, 0.5 * T, -A - 0.5, "valor negativo:  $-A$", color="#FF9090", fontsize=9)

ax1.set_xlabel("distancia x [mm]")
ax1.set_ylabel("tiempo t [s]")
ax1.set_zlabel("E [V/m]")
ax1.set_xlim(0, 2 * lam * 1e3)
ax1.set_ylim(0, 2 * T)
ax1.set_zlim(-1.8, 1.8)
ax1.view_init(28, -62)
ax1.legend(fontsize=8, loc="upper right")

# ============================== Subplot 2: E y H perpendiculares ==============================
# E_y en la dirección y, H_z en la dirección z, ambas se propagan en +x.
# H se dibuja amplificada ×η para que coincida con E (H·η = E en el vacío).
E_glow = make_glow(ax2, "#FF5555", 3, label=r"$\mathbf{E}_y = A\cos(\omega t-kx)$  [V/m]")
H_glow = make_glow(ax2, "#00BBFF", 3, label=r"$\mathbf{H}_z = H_m\cos(\omega t-kx)$  [A/m]")

# Relleno bajo la curva (estilo "principio de integrales"): da perspectiva
Efill = Poly3DCollection([], color="#FF5555", alpha=0.4)
ax2.add_collection3d(Efill)
Hfill = Poly3DCollection([], color="#00BBFF", alpha=0.4)
ax2.add_collection3d(Hfill)


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


ax2.quiver([0.3 * lam * 1e3], [0], [0], [0.6 * lam * 1e3], [0], [0],
           color="white", arrow_length_ratio=0.15, lw=1.5)
ax2.text(0.3 * lam * 1e3, 0, 1.25, "propagación  $+x$", color="white", fontsize=11)
ax2.text(0.6 * lam * 1e3, 0, -1.35, r"$\eta = E/H \approx 377\,\Omega \Rightarrow H_m = A/\eta$",
         color="#00DDDD", fontsize=9)

# Guías para mostrar la amplitud máxima y el valor negativo
ax2.plot([0, 2 * lam * 1e3], [1, 1], [0, 0], "w--", lw=0.8, alpha=0.6)
ax2.plot([0, 2 * lam * 1e3], [-1, -1], [0, 0], "w--", lw=0.8, alpha=0.6)
ax2.text(0, 1.08, 0, r"$+A$", color="white", fontsize=10)
ax2.text(0, -1.28, 0, r"$-A$", color="white", fontsize=10)

ax2.set_xlabel("x [mm] (propagación)")
ax2.set_ylabel("E$_y$ [V/m]")
ax2.set_zlabel("H$_z$ [A/m]  ($\\times\\eta$, misma escala que E)")
ax2.set_xlim(0, 2 * lam * 1e3)
ax2.set_ylim(-1.5, 1.5)
ax2.set_zlim(-1.5, 1.5)
ax2.view_init(28, -65)
ax2.legend(fontsize=8)

# ============================== Animación ==============================
nframes = 240                     # avanza 2T en cada ciclo (misma velocidad, más fluido)
dt = 2 * T / nframes


def update(i):
    t0 = i * dt                   # tiempo actual, en segundos

    # Corte móvil: la onda en el espacio al tiempo t0 (viaja en +x)
    zred = A * np.cos(k * x - w * t0)
    set_glow(snap_glow, mm, np.full_like(mm, t0), zred)

    # Campos E y H al tiempo t0 (H se dibuja ×η para igualar escala)
    ev = zred
    set_glow(E_glow, mm, ev, np.zeros_like(mm))
    set_glow(H_glow, mm, np.zeros_like(mm), ev)

    # Relleno bajo la curva para ambas ondas
    Efill.set_verts(ribbon(mm[::2], ev[::2], "y"))
    Hfill.set_verts(ribbon(mm[::2], ev[::2], "z"))

    return snap_glow + E_glow + H_glow + [Efill, Hfill]


ani = animation.FuncAnimation(fig, update, frames=nframes, interval=30, blit=False)

plt.tight_layout()
plt.show()