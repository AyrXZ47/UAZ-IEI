# Conversion de: proceso AR(2) + autocorrelacion + densidad espectral
# Dos procesos AR(2) con p=0.9 y p=0.99; se estima Rx y se grafica Sx (fft).
import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk
from rx_est import Rx_est

N = 1000
M = 50
p = [0.9, 0.99]
w = 1 / np.sqrt(2) * (np.random.randn(N) + 1j * np.random.randn(N))
c = np.zeros((len(p), N), dtype=complex)
Rx = np.zeros((len(p), M + 1), dtype=complex)
Sx = np.zeros((len(p), M + 1))

# Nota: en el original MATLAB hay typos:
#   lenght -> length ; c(n-1)/c(n-2) -> c(i,n-1)/c(i,n-2)
for i, pi in enumerate(p):
    for n in range(2, N):            # n = 3:N en MATLAB (indices 0-based)
        c[i, n] = (2 * pi * c[i, n - 1]
                   - pi**2 * c[i, n - 2]
                   + (1 - pi)**2 * w[n])
    Rx[i, :] = Rx_est(c[i, :], M)
    Sx[i, :] = np.fft.fftshift(np.abs(np.fft.fft(Rx[i, :])))

f = np.linspace(-0.5, 0.5, M + 1)   # frecuencias normalizadas para fftshift

plt.figure(figsize=(9, 5))
for i, pi in enumerate(p):
    plt.plot(f, Sx[i, :], label=f'p = {pi}')
plt.xlabel('Frecuencia normalizada (ciclos/muestra)')
plt.ylabel('S_x[f]')
plt.title('Densidad espectral estimada (AR(2))')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
mplcyberpunk.add_glow_effects()
plt.show()
