import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk

# Activar el estilo
plt.style.use("cyberpunk")

# =====================================================================
# Problema 13: Espectro de salida Sy(f)
# =====================================================================
print("Graficando Problema 13...")
delta_f = 0.01
f_min, f_max = -2, 2
f_13 = np.arange(f_min, f_max + delta_f, delta_f)

# Sy(f) = 1 / (4 + (2*pi*f)^2)
Sy_13 = 1 / (4 + (2 * np.pi * f_13)**2)

fig13, ax13 = plt.subplots(figsize=(8, 5))
ax13.plot(f_13, Sy_13, color='cyan')
ax13.set_title('Problema 13: Potencia Espectral $S_y(f)$')
ax13.set_xlabel('Frecuencia (f)')
ax13.set_ylabel('$S_y(f)$')
mplcyberpunk.add_glow_effects(ax13)
plt.show()

# =====================================================================
# Problema 14: Autocorrelación Ry(tau) vía IFFT
# =====================================================================
print("Graficando Problema 14...")
N_14 = 256
delta_f_14 = 0.1

# Generar un vector de frecuencias adecuado para IFFT
# np.fft.fftfreq devuelve las frecuencias en el orden correcto: [0, +, -, -]
f_14 = np.fft.fftfreq(N_14, d=1/N_14) * delta_f_14 

# Evaluar el espectro en estas frecuencias
Sy_14 = 1 / (4 + (2 * np.pi * f_14)**2)

# Calcular autocorrelación mediante IFFT
Ry_14 = np.fft.ifft(Sy_14)

# Graficar aplicando fftshift para centrar en cero
fig14, ax14 = plt.subplots(figsize=(8, 5))
ax14.plot(np.fft.fftshift(Ry_14.real), color='magenta')
ax14.set_title('Problema 14: Autocorrelación $R_y(\\tau)$')
ax14.set_xlabel('Lag $\\tau$ (Muestras centradas)')
ax14.set_ylabel('$R_y(\\tau)$')
mplcyberpunk.add_glow_effects(ax14)
plt.show()

# =====================================================================
# Problema 15: Espectro de salida discreto Sy(f)
# =====================================================================
print("Graficando Problema 15...")
delta_w = 2 * np.pi / 100
w_15 = np.arange(-np.pi, np.pi + delta_w, delta_w)

# Sy(f) = 1 / (1.64 - 1.6*cos(w))
Sy_15 = 1 / (1.64 - 1.6 * np.cos(w_15))

fig15, ax15 = plt.subplots(figsize=(8, 5))
ax15.plot(w_15, Sy_15, color='yellow')
ax15.set_title('Problema 15: Potencia Espectral Discreta $S_y(f)$')
ax15.set_xlabel('Frecuencia Angular $\\omega$')
ax15.set_ylabel('$S_y(f)$')
mplcyberpunk.add_glow_effects(ax15)
plt.show()

