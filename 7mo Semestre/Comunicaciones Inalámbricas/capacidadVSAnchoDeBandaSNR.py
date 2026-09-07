import numpy as np
import matplotlib.pyplot as plt

# w = [1:5:20, 25:20:100, 130:50:300, 400:100:1000, 1250:250:5000, 5500:500:10000]
w = np.r_[
    np.arange(1, 21, 5),
    np.arange(25, 101, 20),
    np.arange(130, 301, 50),
    np.arange(400, 1001, 100),
    np.arange(1250, 5001, 250),
    np.arange(5500, 10001, 500),
]
pn0_db = np.arange(-20, 31)  # [-20:1:30]

# C(i,j) = w(i) * log2(1 + (P/N0) / w(i)), filas = p/n0 (dB), columnas = w
W, PD = np.meshgrid(w, pn0_db)
C = W * np.log2(1 + 10 ** (PD / 10) / W)

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
surf = ax.plot_surface(W, PD, C, cmap="viridis")
ax.set_title("capacidad vs ancho de banda SNR")
ax.set_xlabel("w (Hz)")
ax.set_ylabel("p/n0 (dB)")
ax.set_zlabel("c (bits/s)")
fig.colorbar(surf, ax=ax, shrink=0.6)
plt.show()
