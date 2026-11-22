import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import mplcyberpunk

# =====================================================================
# 1. Filtro Pasa-Bajas Butterworth Digital (Equivalente a la primera parte)
# =====================================================================
Fs = 48000
Fc = 2000
Fr = 3000
Rp = 2   # Ripple en banda de paso (k1)
Rs = 20  # Atenuación en banda de rechazo (k2)

# Frecuencias normalizadas de Nyquist (0 a 1, donde 1 es Fs/2)
nyq = 0.5 * Fs
Wp = Fc / nyq
Ws = Fr / nyq

# Encontrar el orden mínimo y la frecuencia natural
N, Wn = signal.buttord(Wp, Ws, Rp, Rs)
print(f"Orden del filtro pasa-bajas calculado: {N}")

# Diseñar el filtro digital Butterworth (Retorna coeficientes del numerador y denominador)
b_lp, a_lp = signal.butter(N, Wn, btype='low')

# Calcular la respuesta en frecuencia
w_lp, h_lp = signal.freqz(b_lp, a_lp, worN=8000)
frecuencias_lp = w_lp * Fs / (2 * np.pi)

# Gráfica del filtro Pasa-Bajas
plt.figure(figsize=(10, 5))
plt.semilogx(frecuencias_lp, 20 * np.log10(np.abs(h_lp) + 1e-12))
plt.title('Respuesta en Frecuencia: Filtro IIR Butterworth (Pasa-Bajas)')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Ganancia [dB]')
plt.grid(which='both', axis='both')
plt.axvline(Fc, color='green', linestyle='--', label=f'Fc = {Fc} Hz')
plt.axvline(Fr, color='red', linestyle='--', label=f'Fr = {Fr} Hz')
plt.ylim(-100, 5)
plt.legend()


# =====================================================================
# 2. Filtro Pasa-Banda Butterworth Digital (Equivalente a la segunda parte)
# =====================================================================
Wlo = 500 / nyq
Wup = 600 / nyq
W1 = 100 / nyq
W2 = 1000 / nyq
Rp_bp = 3
Rs_bp = 20

# Definir vectores de banda
Wc_bp = [Wlo, Wup]
Wr_bp = [W1, W2]

# Encontrar el orden mínimo
N_bp, Wn_bp = signal.buttord(Wc_bp, Wr_bp, Rp_bp, Rs_bp)
print(f"Orden del filtro pasa-banda calculado: {N_bp}")

# Diseñar el filtro pasa-banda
b_bp, a_bp = signal.butter(N_bp, Wn_bp, btype='bandpass')

# Calcular la respuesta en frecuencia
w_bp, h_bp = signal.freqz(b_bp, a_bp, worN=8000)
frecuencias_bp = w_bp * Fs / (2 * np.pi)

# Gráfica del filtro Pasa-Banda
plt.figure(figsize=(10, 5))
plt.semilogx(frecuencias_bp, 20 * np.log10(np.abs(h_bp) + 1e-12))
plt.title('Respuesta en Frecuencia: Filtro IIR Butterworth (Pasa-Banda)')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Ganancia [dB]')
plt.grid(which='both', axis='both')
plt.ylim(-60, 5)


mplcyberpunk.add_glow_effects()
plt.show()

