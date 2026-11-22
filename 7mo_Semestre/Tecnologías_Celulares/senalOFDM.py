"""Senal OFDM en banda base (Problema ilustrativo 2).

Equivale al script MATLAB: genera 9 puntos 16-QAM, forma el espectro
hermitico X (N=20 portadoras), sintetiza x(t) en T=100, obtiene sus
muestras via IDFT (xn) y verifica que coinciden (e~0) y que la DFT
recupera X (ee~0). Grafica |x(t)| completa.

Uso:  python senalOFDM.py
"""

import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk

rng = np.random.default_rng()

K = 10
N = 2 * K
T = 100

a = np.sign(rng.random(36) - 0.5)
b = a.reshape(4, 9).T

# Genera los puntos 16QAM
XXX = 2 * b[:, 0] + b[:, 1] + 1j * (2 * b[:, 2] + b[:, 3])
XX = XXX
X = np.concatenate(([0], XX, [0], np.conj(XX[::-1])))

# Senal continua x(t), muestreada en t = 0..T
t = np.arange(T + 1)
k = np.arange(N)
xt = np.exp(1j * 2 * np.pi * np.outer(t, k) / T) @ (X / np.sqrt(N))

# Muestras de la senal: IDFT de N puntos de X
n = np.arange(N)
xn = np.exp(1j * 2 * np.pi * np.outer(n, k) / N) @ (X / np.sqrt(N))

# Revisa las diferencias entre xn y las muestras de x(t)
e = np.linalg.norm(xt[0:T:T // N] - xn)
print(f"norm(d) = {e:.6f} (debe ser ~0)")

# DFT recupera las portadoras de informacion
Y = np.zeros(10, dtype=complex)
for kk in range(1, 10):
    Y[kk] = np.sum(xn * np.exp(-1j * 2 * np.pi * kk * n / N)) / np.sqrt(N)
ee = np.linalg.norm(Y - X[:10])
print(f"norm(dd) = {ee:.6f} (debe ser ~0)")

plt.style.use("cyberpunk")
fig, ax = plt.subplots(figsize=(9, 6))

ax.plot(t, np.abs(xt), label="|x(t)|")
ax.plot(n * T // N, np.abs(xn), "o", label="muestras IDFT")
ax.set_xlabel("t")
ax.set_ylabel("|x(t)|")
ax.set_title("Senal OFDM (Problema ilustrativo 2)")
ax.legend()

mplcyberpunk.make_lines_glow()
plt.tight_layout()
plt.show()
