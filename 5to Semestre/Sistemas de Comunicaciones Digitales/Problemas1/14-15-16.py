import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk

# ==========================================
# SETUP DE TIEMPO Y FRECUENCIA
# ==========================================
dt = 0.01
fs = 1.0 / dt
t = np.arange(-10, 10, dt)
# Generamos el eje de frecuencias y lo centramos
f_freqs = np.fft.fftshift(np.fft.fftfreq(len(t), dt))

# ==========================================
# PROBLEMA 14
# ==========================================
x14 = np.zeros_like(t)
x14[(t >= -2) & (t < -1)] = 1
x14[(t >= -1) & (t < 1)] = np.abs(t[(t >= -1) & (t < 1)])
x14[(t >= 1) & (t < 2)] = 1

# FFT para señales aperiódicas escalada por dt
X14_num = np.fft.fftshift(np.fft.fft(x14)) * dt

# ==========================================
# PROBLEMA 15 (Numérico y Analítico)
# ==========================================
x15 = np.zeros_like(t)
# Lado positivo
x15[(t >= 0) & (t <= 1)] = t[(t >= 0) & (t <= 1)] + 1
x15[(t > 1) & (t <= 2)] = 2
x15[(t > 2) & (t <= 4)] = -t[(t > 2) & (t <= 4)] + 4
# Lado negativo (Espejo por ser par)
x15[(t >= -1) & (t < 0)] = -t[(t >= -1) & (t < 0)] + 1
x15[(t >= -2) & (t < -1)] = 2
x15[(t >= -4) & (t < -2)] = t[(t >= -4) & (t < -2)] + 4

X15_num = np.fft.fftshift(np.fft.fft(x15)) * dt

# Solución Analítica P15
f_safe = np.where(f_freqs == 0, 1e-10, f_freqs) # Evitar división por cero
X15_ana = (2 - 2*np.cos(2*np.pi*f_safe) - 2*np.cos(4*np.pi*f_safe) + 2*np.cos(8*np.pi*f_safe)) / (-4 * np.pi**2 * f_safe**2)
X15_ana[f_freqs == 0] = 11.0 # Límite analítico en f=0 (Área bajo la curva)

# ==========================================
# PROBLEMA 16
# ==========================================
h16 = np.zeros_like(t)
h16[(t >= 0) & (t <= 2)] = 1
h16[(t > 2) & (t <= 3)] = -1

H16_num = np.fft.fftshift(np.fft.fft(h16)) * dt
Y16_num = X15_num * H16_num # Y(f) = X(f)H(f)

# ==========================================
# GRAFICADO
# ==========================================
# Recortamos los ejes X para ver los detalles centrales (-2 a 2 Hz)
zoom_mask = (f_freqs > -2.5) & (f_freqs < 2.5)
f_zoom = f_freqs[zoom_mask]

# Figura para Problema 14
fig7, axs7 = plt.subplots(1, 2, figsize=(12, 4))
fig7.suptitle("Problema 14: Señal Trapezoidal Modificada", fontsize=14)
axs7[0].plot(f_zoom, np.abs(X14_num)[zoom_mask])
axs7[0].set_title('Magnitud Espectral P14')
axs7[1].plot(f_zoom, np.angle(X14_num)[zoom_mask])
axs7[1].set_title('Fase Espectral P14')
fig7.tight_layout()

# Figura para Problema 15
fig8, axs8 = plt.subplots(1, 2, figsize=(12, 4))
fig8.suptitle("Problema 15: Numérico vs Analítico", fontsize=14)
axs8[0].plot(f_zoom, np.abs(X15_num)[zoom_mask], label="Numérica")
axs8[0].plot(f_zoom, np.abs(X15_ana)[zoom_mask], linestyle='--', label="Analítica")
axs8[0].set_title('Magnitud Espectral P15')
axs8[0].legend()
axs8[1].plot(f_zoom, np.angle(X15_num)[zoom_mask])
axs8[1].set_title('Fase Espectral P15')
fig8.tight_layout()

# Figura para Problema 16
fig9, axs9 = plt.subplots(1, 2, figsize=(12, 4))
fig9.suptitle("Problema 16: Salida del Sistema LTI", fontsize=14)
axs9[0].plot(f_zoom, np.abs(Y16_num)[zoom_mask])
axs9[0].set_title('Magnitud de Salida P16')
axs9[1].plot(f_zoom, np.angle(Y16_num)[zoom_mask])
axs9[1].set_title('Fase de Salida P16')
fig9.tight_layout()

for ax in list(axs7) + list(axs8) + list(axs9):
    mplcyberpunk.add_glow_effects(ax=ax)

plt.show()

