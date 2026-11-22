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

# --- Problema 8 y 9 ---
T0_8 = 8.0
N_8 = 15
n_vals_8 = np.arange(-N_8, N_8 + 1)

def p8_cos(t):
    return np.cos(np.pi * t / 8.0) if abs(t) <= 4.0 else 0.0

def p9_sin(t):
    return np.sin(np.pi * t / 8.0) if abs(t) <= 4.0 else 0.0

# Cálculo numérico P8 y P9
cn_num_8 = fseries(p8_cos, -4.0, 4.0, N_8)
cn_num_9 = fseries(p9_sin, -4.0, 4.0, N_8)

# Cálculo analítico P8 y P9
cn_ana_8 = (2 * (-1.0)**n_vals_8) / (np.pi * (1 - 4 * n_vals_8**2))
# Para n=0 en P9, el límite es 0
cn_ana_9 = np.zeros_like(n_vals_8, dtype=complex)
for i, n in enumerate(n_vals_8):
    if n == 0:
        cn_ana_9[i] = 0
    else:
        cn_ana_9[i] = -1j * (4 * n * (-1.0)**n) / (np.pi * (1 - 4 * n**2))

# --- Problema 10 ---
T0_10 = 1e-6
N_10 = 20
n_vals_10 = np.arange(-N_10, N_10 + 1)

def p10_triangle(t):
    # Corrección de la pendiente para que la señal tenga sentido con T0 = 1e-6
    return max(0.5 - 1e6 * abs(t), 0.0) if abs(t) <= 5e-7 else 0.0

# Cálculo numérico P10 (el límite de quad maneja bien escalas pequeñas, pero es mejor mapearlo si falla)
cn_num_10 = fseries(p10_triangle, -5e-7, 5e-7, N_10)

# --- Graficado ---
fig3, axs3 = plt.subplots(2, 2, figsize=(12, 8))
fig3.suptitle("Problemas 8 (Coseno) y 9 (Seno)", fontsize=14)

# P8: Coseno
axs3[0, 0].stem(n_vals_8, np.abs(cn_num_8))
axs3[0, 0].set_title('Magnitud P8: cos(πt/8)')
axs3[1, 0].stem(n_vals_8, np.angle(cn_num_8))
axs3[1, 0].set_title('Fase P8 (Real, saltos 0 o π)')

# P9: Seno
axs3[0, 1].stem(n_vals_8, np.abs(cn_num_9))
axs3[0, 1].set_title('Magnitud P9: sin(πt/8)')
axs3[1, 1].stem(n_vals_8, np.angle(cn_num_9))
axs3[1, 1].set_title('Fase P9 (Imaginaria, ±π/2)')

fig3.tight_layout()
mplcyberpunk.add_glow_effects(ax=axs3[0,0])
mplcyberpunk.add_glow_effects(ax=axs3[0,1])
mplcyberpunk.add_glow_effects(ax=axs3[1,0])
mplcyberpunk.add_glow_effects(ax=axs3[1,1])

# --- Gráfica Problema 10 ---
fig4, axs4 = plt.subplots(1, 2, figsize=(12, 4))
fig4.suptitle("Problema 10 (Pulso Triangular Microsegundo)", fontsize=14)

axs4[0].stem(n_vals_10, np.abs(cn_num_10))
axs4[0].set_title('Magnitud Espectral P10')

axs4[1].stem(n_vals_10, np.angle(cn_num_10))
axs4[1].set_title('Fase Espectral P10')

fig4.tight_layout()
mplcyberpunk.add_glow_effects(ax=axs4[0])
mplcyberpunk.add_glow_effects(ax=axs4[1])

plt.show()

