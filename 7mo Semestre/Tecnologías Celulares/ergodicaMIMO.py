import numpy as np
from scipy.integrate import tplquad, dblquad, quad
import matplotlib.pyplot as plt

SNR_dB = np.arange(0, 20.0001, 5)
SNR = 10 ** (SNR_dB / 10)
L = len(SNR)
C1 = np.zeros(L)
C2 = np.zeros(L)
C3 = np.zeros(L)

for i in range(L):
    # Nt = Nr = N = 1:
    C1[i] = quad(lambda x: np.log2(1 + SNR[i] * x) * np.exp(-x), 0, np.inf)[0]
    # Nt = Nr = N = 2:
    C2[i] = dblquad(lambda y, x: (np.log2(1 + SNR[i] * x / 2) + np.log2(1 + SNR[i] * y / 2)) / 2
                    * np.exp(-x - y) * (x - y) ** 2,
                    0, 1000, 0, 1000, epsabs=1e-5, epsrel=1e-3)[0]
    # Nt = Nr = N = 3:
    C3[i] = tplquad(lambda z, y, x: (np.log2(1 + SNR[i] * x / 3) + np.log2(1 + SNR[i] * y / 3) + np.log2(1 + SNR[i] * z / 3)) / 24
                    * np.exp(-x - y - z) * ((x - y) * (x - z) * (y - z)) ** 2,
                    0, 10, 0, 10, 0, 10, epsabs=1e-5, epsrel=1e-3)[0]

plt.plot(SNR_dB, C1, "-*", SNR_dB, C2, "-o", SNR_dB, C3, "-s")
plt.axis([0, 20, 0, 25])
plt.legend(["N_T=1,N_R=1", "N_T=2,N_R=2", "N_T=3,N_R=3"])
plt.xlabel("SNR Promedio (dB)", fontsize=10)
plt.ylabel("Capacidad (bps/Hz)", fontsize=10)
plt.savefig("ergodicaMIMO.png", dpi=150, bbox_inches="tight")
plt.show()
