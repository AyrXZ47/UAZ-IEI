import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk

# Función general para la magnitud del espectro de un pulso coseno
def X_mag(f, T, f0):
    # Aplicamos el teorema de modulación y desplazamiento
    term1 = np.sinc(T * (f - f0)) * np.exp(-1j * np.pi * (f - f0) * T)
    term2 = np.sinc(T * (f + f0)) * np.exp(-1j * np.pi * (f + f0) * T)
    return np.abs((T / 2) * (term1 + term2))

f = np.linspace(-6, 6, 2000)

plt.figure(figsize=(14, 6))

# --- PARTE 3a: Cambiando la frecuencia (f0) ---
plt.subplot(1, 2, 1)
f0_values = [1, 2, 4]
T_const = 4
for f0 in f0_values:
    plt.plot(f, X_mag(f, T_const, f0), label=f'f0 = {f0} Hz')
plt.title("Efecto de cambiar f0 (T=4)")
plt.xlabel("Frecuencia (f)")
plt.ylabel("Magnitud |X1(f)|")
plt.legend()
plt.grid(True)

# --- PARTE 3b: Cambiando el ancho del pulso (T) ---
plt.subplot(1, 2, 2)
T_values = [8, 16]
f0_const = 0.5
for T in T_values:
    # Ajustamos el eje f localmente para ver mejor el efecto de compresión
    f_zoom = np.linspace(-1.5, 1.5, 2000) 
    plt.plot(f_zoom, X_mag(f_zoom, T, f0_const), label=f'T = {T} s')
plt.title("Efecto de cambiar T (f0=0.5)")
plt.xlabel("Frecuencia (f)")
plt.ylabel("Magnitud |X2(f)|")
plt.legend()
plt.grid(True)

plt.tight_layout()
mplcyberpunk.add_glow_effects()
plt.show()
