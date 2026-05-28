import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk

# Aplicar tu estilo de preferencia
plt.style.use("cyberpunk")

# Parámetros generales
N = 1000

# =====================================================================
# Problema 10: Proceso de Gauss-Markov
# =====================================================================
print("Calculando Problema 10...")
rho = 0.85
W = np.random.randn(N) # Ruido Gaussiano (media 0, varianza 1)
X_gm = np.zeros(N)

# Relación recursiva
for i in range(1, N):
    X_gm[i] = rho * X_gm[i-1] + W[i]


# =====================================================================
# Problema 11: Autocorrelación y Espectro (Ruido Gaussiano)
# =====================================================================
print("Calculando Problema 11...")
M = 50
m_lags = np.arange(0, M + 1)
Rx_av = np.zeros(M + 1)
Sx_av = np.zeros(M + 1)

# Promediamos 10 realizaciones para limpiar el ruido de las estimaciones
num_realizaciones = 10
for _ in range(num_realizaciones):
    X_n = np.random.randn(N) # Usando Gaussiana en vez de uniforme
    
    # Estimar autocorrelación
    Rx = np.zeros(M + 1)
    for m in range(M + 1):
        # Multiplicación vectorizada y suma
        Rx[m] = np.sum(X_n[:N-m] * X_n[m:]) / (N - m)
        
    # Espectro de potencia usando FFT
    # Para que coincida con la visualización simétrica
    Sx = np.fft.fftshift(np.abs(np.fft.fft(Rx)))
    
    Rx_av += Rx
    Sx_av += Sx

Rx_av /= num_realizaciones
Sx_av /= num_realizaciones


# =====================================================================
# Problema 12: Autocorrelación de Espectro Triangular
# =====================================================================
print("Calculando Problema 12...")
N_fft = 256
B = 10.0 # Ancho de banda arbitrario para visualización
f = np.linspace(-2*B, 2*B, N_fft)

# Definir el espectro triangular
Sx_tri = np.where(np.abs(f) <= B, 1 - np.abs(f)/B, 0)

# Aplicar IFFT (necesitamos hacer ifftshift para que el pico esté en 0 antes de la IFFT)
Rx_tri = np.fft.ifft(np.fft.ifftshift(Sx_tri))
# Y luego fftshift para centrar el resultado en el tiempo
Rx_tri = np.fft.fftshift(Rx_tri).real


# =====================================================================
# Renderizado de Gráficas (Todo en una sola ventana para evitar bugs)
# =====================================================================
fig = plt.figure(figsize=(16, 10))

# --- Plot Problema 10 ---
ax1 = fig.add_subplot(2, 2, 1)
ax1.plot(X_gm, lw=1)
ax1.set_title('Problema 10: Proceso de Gauss-Markov')
ax1.set_xlabel('Muestra (n)')
ax1.set_ylabel('Amplitud')
mplcyberpunk.add_glow_effects(ax1)

# --- Plot Problema 11 (Autocorrelación) ---
ax2 = fig.add_subplot(2, 2, 2)
ax2.plot(m_lags, Rx_av, color='C1')
ax2.set_title('Problema 11: Autocorrelación Promedio')
ax2.set_xlabel('Lag (m)')
ax2.set_ylabel('Rx(m)')
mplcyberpunk.add_glow_effects(ax2)

# --- Plot Problema 12 (Espectro) ---
ax3 = fig.add_subplot(2, 2, 3)
ax3.plot(f, Sx_tri, color='C2')
ax3.set_title('Problema 12: Espectro de Potencia Triangular $S_x(f)$')
ax3.set_xlabel('Frecuencia (f)')
ax3.set_ylabel('$S_x(f)$')
mplcyberpunk.add_glow_effects(ax3)

# --- Plot Problema 12 (Autocorrelación) ---
ax4 = fig.add_subplot(2, 2, 4)
# El eje de tiempo centrado
t = np.linspace(-N_fft/2, N_fft/2 - 1, N_fft)
ax4.plot(t, Rx_tri, color='C3')
ax4.set_title('Problema 12: Autocorrelación $R_x(\\tau)$ (IFFT)')
ax4.set_xlabel('$\\tau$')
ax4.set_ylabel('$R_x(\\tau)$')
mplcyberpunk.add_glow_effects(ax4)

plt.tight_layout()
plt.show()

