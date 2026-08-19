# Conversion de: matlab script para problema ilustrativo 3
import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk

N = 20000
x = np.arange(0, 5.1, 0.1)   # x = 0:0.1:5 en MATLAB
sigma = 1
u = np.random.rand(N)
r = sigma * np.sqrt(-2 * np.log(u))
r_ac = x / sigma**2 * np.exp(-(x / sigma)**2 / 2)

# (a) Histograma. En MATLAB, hist(r, x) usa x como CENTROS de bin
# (0, 0.1, ..., 5); en matplotlib bins=51 + range reproduce lo mismo.
plt.subplot(2, 1, 1)
plt.hist(r, bins=51, range=(-0.05, 5.05))
plt.xlabel('(a) Histograma para N=20000 muestras')
plt.xlim(0, 5)
plt.ylim(0, 1500)

# (b) PDF Rayleigh teorica
plt.subplot(2, 1, 1)
plt.hist(r, bins=51, range=(-0.05, 5.05))
plt.xlabel('(a) Histograma para N=20000 muestras')
plt.xlim(0, 5)
plt.ylim(0, 1500)

# (b) PDF Rayleigh teorica
plt.subplot(2, 1, 2)
plt.plot(x, r_ac)
plt.xlabel('(b) PDF Raleigh')

plt.tight_layout()
mplcyberpunk.add_glow_effects()
plt.show()
