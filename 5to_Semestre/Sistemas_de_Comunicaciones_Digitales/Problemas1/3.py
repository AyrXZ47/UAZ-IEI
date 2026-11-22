import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk

from scipy.integrate import quad


# 1. El equivalente moderno a fseries.m
def fseries(func, a, b, n_array):
    T = b - a
    xx = np.zeros(len(n_array), dtype=complex)
    
    # Calculamos la integral para cada armónico 'n'
    for idx, n in enumerate(n_array):
        # Separamos parte real e imaginaria porque 'quad' en Python prefiere integrales reales
        real_integrand = lambda t: np.real(func(t) * np.exp(-1j * 2 * np.pi * n * t / T))
        imag_integrand = lambda t: np.imag(func(t) * np.exp(-1j * 2 * np.pi * n * t / T))
        
        real_part, _ = quad(real_integrand, a, b, limit=100)
        imag_part, _ = quad(imag_integrand, a, b, limit=100)
        
        xx[idx] = (real_part + 1j * imag_part) / T
        
    return xx

# 2. Definimos los parámetros de la Misión 3
# A=1, T0=4, t0=1/2
T0 = 4
a = -T0/2  # Periodo de -2 a 2
b = T0/2

# Definimos tu pulso rectangular: Vale 1 entre -0.5 y 0.5, y 0 en el resto
def mi_senal(t):
    return np.where((t >= -0.5) & (t <= 0.5), 1.0, 0.0)

# 3. Ejecución
n = np.arange(-20, 21)
coeficientes = fseries(mi_senal, a, b, n)

# 4. Graficamos
plt.figure(1)
plt.stem(n, np.abs(coeficientes))
plt.title("Magnitud del Espectro (Método Numérico)")
mplcyberpunk.add_glow_effects()
plt.show()

