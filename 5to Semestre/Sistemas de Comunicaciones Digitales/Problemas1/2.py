# Espectro Discreto de la Señal


from matplotlib import pyplot as plt
import numpy as np

n=np.arange(-20, 21)

plt.figure(1)
plt.stem(n, np.abs(np.sinc(2*n/5) * (2/5))) # Para la magnitud

plt.figure(2)
plt.stem(n, np.angle(np.sinc(2*n/5) * (2/5))) # Para la fase

plt.show()
