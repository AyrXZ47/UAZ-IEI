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

# --- Problema 5 ---
def rect_pulse(t):
    return 1.0 if abs(t) < 0.5 else 0.0

T0_5 = 4.6
N = 20
n_vals = np.arange(-N, N + 1)
# Cálculo numérico
cn_num_5 = fseries(rect_pulse, -T0_5/2, T0_5/2, N)
# Cálculo analítico
cn_ana_5 = (1/T0_5) * sinc(n_vals / T0_5)

# --- Problemas 6 y 7 ---
def lambda_pulse(t):
    # Pulso triangular periódico mod(t, T0)
    t_mod = ((t + 2.3) % 4.6) - 2.3
    return 1.0 - abs(t_mod) if abs(t_mod) <= 1.0 else 0.0

N_6 = 24
n_vals_6 = np.arange(-N_6, N_6 + 1)

# P6: Ventana simétrica
cn_num_6 = fseries(lambda_pulse, -2.3, 2.3, N_6)
# P7: Ventana desplazada
cn_num_7 = fseries(lambda_pulse, -1.3, 3.3, N_6)

# --- Graficado rápido P6 vs P7 (Magnitud y Fase) ---
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Magnitud
axs[0, 0].stem(n_vals_6, np.abs(cn_num_6))
axs[0, 0].set_title('Magnitud P6 [-2.3, 2.3]')
axs[0, 1].stem(n_vals_6, np.abs(cn_num_7))
axs[0, 1].set_title('Magnitud P7 [-1.3, 3.3]')

# Fase
axs[1, 0].stem(n_vals_6, np.angle(cn_num_6))
axs[1, 0].set_title('Fase P6 (Nota el ruido por redondeo)')
axs[1, 1].stem(n_vals_6, np.angle(cn_num_7))
axs[1, 1].set_title('Fase P7 (Ruido modificado por asimetría)')

plt.tight_layout()

mplcyberpunk.add_glow_effects()

# --- Gráficas del Problema 5 ---
fig2, axs2 = plt.subplots(1, 2, figsize=(12, 4))

# Magnitud P5 Numérica
axs2[0].stem(n_vals, np.abs(cn_num_5))
axs2[0].set_title('Magnitud P5 (Numérica)')

# Magnitud P5 Analítica
axs2[1].stem(n_vals, np.abs(cn_ana_5))
axs2[1].set_title('Magnitud P5 (Analítica)')

fig2.tight_layout()

# Aplicamos el estilo cyberpunk también a esta nueva figura
mplcyberpunk.add_glow_effects(ax=axs2[0])
mplcyberpunk.add_glow_effects(ax=axs2[1])

plt.show()

