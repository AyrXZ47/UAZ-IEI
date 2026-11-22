import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import mplcyberpunk

# ==========================================
# SETUP DE LA SEÑAL BASE
# ==========================================
fs = 1000.0  # Frecuencia de muestreo (1000 muestras/segundo)
t = np.arange(0, 10, 1/fs) # t de 0 a 10 segundos
x = np.cos(2 * np.pi * 47 * t) + np.cos(2 * np.pi * 219 * t)

# Función auxiliar para plotear el espectro de potencia (Welch)
def plot_welch(ax, signal_data, title):
    # nperseg=1024 imita el comportamiento estándar para ventanas de buen tamaño
    f, Pxx = signal.welch(signal_data, fs, window='hann', nperseg=1024)
    # Convertimos a decibelios (dB) para comparar con la Figura 1 del PDF
    Pxx_dB = 10 * np.log10(Pxx)
    ax.plot(f, Pxx_dB)
    ax.set_title(title)
    ax.set_xlabel('Frecuencia (Hz)')
    ax.set_ylabel('Power/frequency (dB/Hz)')
    ax.set_xlim(0, 500)
    ax.set_ylim(-180, 0)

# ==========================================
# PROBLEMA 17: Filtro Pasabajas (Lowpass)
# ==========================================
fc = 100.0 # Frecuencia de corte

# Butterworth Orden 4
b_lp4, a_lp4 = signal.butter(4, fc, btype='low', fs=fs)
y_lp4 = signal.filtfilt(b_lp4, a_lp4, x)

# Butterworth Orden 8
b_lp8, a_lp8 = signal.butter(8, fc, btype='low', fs=fs)
y_lp8 = signal.filtfilt(b_lp8, a_lp8, x)

# ==========================================
# PROBLEMA 18: Filtro Pasaaltas (Highpass)
# ==========================================
# Butterworth Orden 4
b_hp4, a_hp4 = signal.butter(4, fc, btype='high', fs=fs)
y_hp4 = signal.filtfilt(b_hp4, a_hp4, x)

# Butterworth Orden 8
b_hp8, a_hp8 = signal.butter(8, fc, btype='high', fs=fs)
y_hp8 = signal.filtfilt(b_hp8, a_hp8, x)

# ==========================================
# PROBLEMA 19: Hilbert, Envolvente y Equivalente Pasabajas
# ==========================================
# 1 & 2. Señal analítica z(t) (SciPy hilbert calcula la analítica completa directamente)
z = signal.hilbert(x)

# 3. Envolvente
envolvente = np.abs(z)

# 4. Equivalente Pasabajas para f0 = 47 Hz y f0 = 219 Hz
def equivalente_pasabajas(z_sig, f0, time_vec):
    xl = z_sig * np.exp(-1j * 2 * np.pi * f0 * time_vec)
    x_c = np.real(xl) # Componente en fase
    x_s = np.imag(xl) # Componente en cuadratura
    return x_c, x_s

xc_47, xs_47 = equivalente_pasabajas(z, 47.0, t)
xc_219, xs_219 = equivalente_pasabajas(z, 219.0, t)


# ==========================================
# GRAFICADO CYBERPUNK
# ==========================================
# Figura Problemas 17 y 18 (Densidades Espectrales de Potencia)
fig_filtros, axs_filtros = plt.subplots(2, 2, figsize=(14, 10))
fig_filtros.suptitle("Problemas 17 y 18: Filtrado Butterworth y PSD de Welch", fontsize=16)

plot_welch(axs_filtros[0, 0], y_lp4, 'P17: Pasabajas Orden 4 (fc=100Hz)')
plot_welch(axs_filtros[0, 1], y_lp8, 'P17: Pasabajas Orden 8 (Más atenuación en 219Hz)')
plot_welch(axs_filtros[1, 0], y_hp4, 'P18: Pasaaltas Orden 4 (fc=100Hz)')
plot_welch(axs_filtros[1, 1], y_hp8, 'P18: Pasaaltas Orden 8 (Más atenuación en 47Hz)')

plt.tight_layout()
for ax in axs_filtros.flat:
    mplcyberpunk.add_glow_effects(ax=ax)

# Figura Problema 19 (Envolvente y Equivalentes Pasabajas)
# Haremos zoom en un segmento pequeño (ej. 0 a 0.2 seg) para poder apreciar las ondas
zoom_t = (t >= 0) & (t <= 0.1)

fig_p19, axs_p19 = plt.subplots(3, 1, figsize=(12, 12))
fig_p19.suptitle("Problema 19: Hilbert y Equivalente Pasabajas (Zoom t=0 a 0.1s)", fontsize=16)

# Envolvente
axs_p19[0].plot(t[zoom_t], x[zoom_t], label='x(t) original', alpha=0.7)
axs_p19[0].plot(t[zoom_t], envolvente[zoom_t], label='Envolvente |z(t)|', color='magenta', linewidth=2)
axs_p19[0].set_title('Señal Original y su Envolvente')
axs_p19[0].legend()

# Equivalente f0 = 47
axs_p19[1].plot(t[zoom_t], xc_47[zoom_t], label='En Fase (xc)', color='cyan')
axs_p19[1].plot(t[zoom_t], xs_47[zoom_t], label='Cuadratura (xs)', color='lime', linestyle='--')
axs_p19[1].set_title('Equivalente Pasabajas (f0 = 47 Hz)')
axs_p19[1].legend()

# Equivalente f0 = 219
axs_p19[2].plot(t[zoom_t], xc_219[zoom_t], label='En Fase (xc)', color='cyan')
axs_p19[2].plot(t[zoom_t], xs_219[zoom_t], label='Cuadratura (xs)', color='lime', linestyle='--')
axs_p19[2].set_title('Equivalente Pasabajas (f0 = 219 Hz)')
axs_p19[2].legend()

plt.tight_layout()
for ax in axs_p19.flat:
    mplcyberpunk.add_glow_effects(ax=ax)

plt.show()

