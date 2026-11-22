"""Recepcion OFDM con ruido gaussiano aditivo (Problema ilustrativo).

Equivale al script MATLAB: senal OFDM de 9 puntos 16-QAM con espectro
hermitico (N=20 portadoras), se le suma ruido gaussiano real de varianza
2 en las muestras, se demodula por DFT y se detecta por vecino mas
cercano. Cuenta los simbolos en error y grafica la constelacion recibida.

Uso:  python ruidoAditivoOFDM.py
"""

import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk

rng = np.random.default_rng()

K = 10
N = 2 * K
T = 100
variance = 2

noise = np.sqrt(variance) * rng.standard_normal(N)

a = np.sign(rng.random(36) - 0.5)
b = a.reshape(4, 9).T

# Genera los puntos 16QAM
XXX = 2 * b[:, 0] + b[:, 1] + 1j * (2 * b[:, 2] + b[:, 3])
XX = XXX
X = np.concatenate(([0], XX, [0], np.conj(XX[::-1])))

# Muestras de la senal: IDFT de N puntos de X
n = np.arange(N)
k = np.arange(N)
x = np.exp(1j * 2 * np.pi * np.outer(n, k) / N) @ (X / np.sqrt(N))

r = x + noise

# Demodulacion por DFT
Y = np.zeros(10, dtype=complex)
for kk in range(1, 10):
    Y[kk] = np.sum(r * np.exp(-1j * 2 * np.pi * kk * n / N)) / np.sqrt(N)


# Detecta el vecino mas cercano en la constelacion
def detectar(v):
    return np.where(v > 2, 3, np.where(v > 0, 1, np.where(v > -2, -1, -3)))


Z = detectar(Y[1:].real) + 1j * detectar(Y[1:].imag)
errores = np.count_nonzero(Z - X[1:10])
print(f"Simbolos en error: {errores} de 9")

# Constelacion recibida vs constelacion 16QAM ideal
plt.style.use("cyberpunk")
fig, ax = plt.subplots(figsize=(8, 8))

re, im = np.meshgrid([-3, -1, 1, 3], [-3, -1, 1, 3])
ax.scatter(re, im, marker="s", label="constelacion 16QAM")
ax.scatter(Y[1:].real, Y[1:].imag, label="puntos recibidos")
ax.set_xlabel("Re")
ax.set_ylabel("Im")
ax.set_title("Recepcion OFDM con ruido aditivo")
ax.set_aspect("equal")
ax.legend()

mplcyberpunk.make_lines_glow()
plt.tight_layout()
plt.show()
