import numpy as np
import matplotlib.pyplot as plt

p_db = np.arange(-20, 21)  # [-20:1:20]
np_db = p_db

# c(i,j) = 0.5*log2(1 + p(i)/np(j)): filas = p, columnas = potencia de ruido
NPg, Pg = np.meshgrid(10 ** (np_db / 10), 10 ** (p_db / 10))
C = 0.5 * np.log2(1 + Pg / NPg)

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
surf = ax.plot_surface(NPg, Pg, C, cmap="viridis")
ax.set_xlabel("potencia de ruido db")
ax.set_ylabel("p db")
ax.set_zlabel("capacidad bits/ transmision")
fig.colorbar(surf, ax=ax, shrink=0.6)
plt.show()
