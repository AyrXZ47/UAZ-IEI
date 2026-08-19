# Grafica la autocorrelacion estimada Rx[m] para una senal aleatoria
import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk
from rx_est import Rx_est

N = 10000       # numero de muestras de la senal
M = 50          # numero de retardos (Rx tendra M+1 valores)

X = np.random.randn(N)
Rx = Rx_est(X, M)
m = np.arange(M + 1)

plt.figure(figsize=(8, 4))
plt.plot(m, Rx)
plt.xlabel('m')
plt.ylabel('R_x[m]')
plt.title('Autocorrelación estimada (N=10000, M=50)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
mplcyberpunk.add_glow_effects()
plt.show()
