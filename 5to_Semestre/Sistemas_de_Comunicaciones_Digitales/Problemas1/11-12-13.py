import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import mplcyberpunk

def fseries(func, a, b, N):
    """Equivalente en Python de fseries.m"""
    T0 = b - a
    coeffs = []
    for n in range(N + 1):
        real_integrand = lambda t: np.real(func(t) * np.exp(-1j * 2 * np.pi * n * t / T0))
        imag_integrand = lambda t: np.imag(func(t) * np.exp(-1j * 2 * np.pi * n * t / T0))
        
        re_val, _ = quad(real_integrand, a, b, limit=100)
        im_val, _ = quad(imag_integrand, a, b, limit=100)
        
        coeffs.append((re_val + 1j * im_val) / T0)
    
    # Generar espectro bilateral (n de -N a N)
    cn = np.array(coeffs)
    cn_neg = np.conj(cn[1:])[::-1] # x_{-n} = x_n^* para señales reales
    return np.concatenate((cn_neg, cn))

# --- Función para Sinc normalizado ---
def sinc(x):
    # Equivalente a la definición de telecomunicaciones: sin(pi*x)/(pi*x)
    return np.sinc(x) 



# --- Función auxiliar para la Función de Transferencia H(f) ---
def H_eval(func_h, a, b, f_val):
    """Calcula H(f) evaluando la integral de Fourier numéricamente en f_val"""
    real_int = lambda t: np.real(func_h(t) * np.exp(-1j * 2 * np.pi * f_val * t))
    imag_int = lambda t: np.imag(func_h(t) * np.exp(-1j * 2 * np.pi * f_val * t))
    
    re_val, _ = quad(real_int, a, b, limit=100)
    im_val, _ = quad(imag_int, a, b, limit=100)
    
    return re_val + 1j * im_val

# ==========================================
# PROBLEMA 11
# ==========================================
T0_11 = 6.0
N_11 = 15
n_vals_11 = np.arange(-N_11, N_11 + 1)

def p11_x(t):
    return 1.0 if abs(t) <= 1.5 else 0.0

def p11_h(t):
    return np.exp(-t / 2.0) if 0 <= t <= 4.0 else 0.0

xn_11 = fseries(p11_x, -3.0, 3.0, N_11)
Hn_11 = np.array([H_eval(p11_h, 0.0, 4.0, n / T0_11) for n in n_vals_11])
yn_11 = xn_11 * Hn_11 # Teorema de sistemas LTI

# ==========================================
# PROBLEMA 12
# ==========================================
T0_12 = 6.0
N_12 = 15
n_vals_12 = np.arange(-N_12, N_12 + 1)

def p12_x(t):
    return np.exp(-3.0 * t) if abs(t) <= 3.0 else 0.0

def p12_h(t):
    return 1.0 if 0 <= t <= 4.0 else 0.0

xn_12 = fseries(p12_x, -3.0, 3.0, N_12)
Hn_12 = np.array([H_eval(p12_h, 0.0, 4.0, n / T0_12) for n in n_vals_12])
yn_12 = xn_12 * Hn_12

# ==========================================
# PROBLEMA 13
# ==========================================
# Vectores de tiempo y frecuencia de alta resolución
dt = 0.01
t = np.arange(-10, 10, dt)
f_freqs = np.fft.fftshift(np.fft.fftfreq(len(t), dt))

# Señales x(t) = Pi(t) y y(t) = Lambda(t)
x_arr = np.where(np.abs(t) < 0.5, 1.0, 0.0)
y_arr = np.where(np.abs(t) <= 1.0, 1.0 - np.abs(t), 0.0)

# Convolución en el tiempo (y escalado por dt)
z_conv_time = np.convolve(x_arr, y_arr, mode='same') * dt

# FFT de las tres cosas (escalando por dt para simular transformada continua)
X_f = np.fft.fftshift(np.fft.fft(x_arr)) * dt
Y_f = np.fft.fftshift(np.fft.fft(y_arr)) * dt
Z_f_from_conv = np.fft.fftshift(np.fft.fft(z_conv_time)) * dt

# Multiplicación en frecuencia
Z_f_from_mult = X_f * Y_f

# ==========================================
# GRAFICADO
# ==========================================
# Graficas Problemas 11 y 12
fig5, axs5 = plt.subplots(2, 2, figsize=(12, 8))
fig5.suptitle("Problemas 11 y 12: Señales a través de Sistemas LTI", fontsize=14)

axs5[0, 0].stem(n_vals_11, np.abs(yn_11))
axs5[0, 0].set_title('Magnitud de Salida P11')
axs5[1, 0].stem(n_vals_11, np.angle(yn_11))
axs5[1, 0].set_title('Fase de Salida P11')

axs5[0, 1].stem(n_vals_12, np.abs(yn_12))
axs5[0, 1].set_title('Magnitud de Salida P12')
axs5[1, 1].stem(n_vals_12, np.angle(yn_12))
axs5[1, 1].set_title('Fase de Salida P12')

fig5.tight_layout()
for ax in axs5.flat:
    mplcyberpunk.add_glow_effects(ax=ax)

# Gráfica Problema 13
fig6, axs6 = plt.subplots(1, 2, figsize=(12, 5))
fig6.suptitle("Problema 13: Verificación del Teorema de Convolución", fontsize=14)

# Enfocamos la vista en el centro del espectro para mejor apreciación
zoom_mask = (f_freqs > -3) & (f_freqs < 3)

axs6[0].plot(f_freqs[zoom_mask], np.abs(Z_f_from_conv[zoom_mask]), color='cyan')
axs6[0].set_title('|Z(f)| desde Convolución F[x(t) * y(t)]')

axs6[1].plot(f_freqs[zoom_mask], np.abs(Z_f_from_mult[zoom_mask]), color='magenta', linestyle='--')
axs6[1].set_title('|Z(f)| desde Multiplicación X(f)Y(f)')

fig6.tight_layout()
mplcyberpunk.add_glow_effects(ax=axs6[0])
mplcyberpunk.add_glow_effects(ax=axs6[1])

plt.show()

