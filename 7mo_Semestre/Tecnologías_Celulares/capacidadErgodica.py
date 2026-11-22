import math
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

H_simo = np.array([1, 0.5]).T
H_miso = np.array([1, 0.5])
Nr_simo = 2
Nt_miso = 2
n_simo = Nr_simo
n_miso = Nt_miso

SNR_dB = np.arange(0, 20.0001, 0.01)
SNR = 10 ** (SNR_dB / 10)
L = len(SNR)
C_simo = np.zeros(L)
C_miso = np.zeros(L)

for i in range(L):
    C_simo[i] = quad(lambda x: np.log2(1 + SNR[i] * x) * x ** (n_simo - 1) * np.exp(-x) / math.factorial(n_simo - 1),
                     0, np.inf)[0]
    C_miso[i] = quad(lambda x: np.log2(1 + SNR[i] * x / Nt_miso) * x ** (n_miso - 1) * np.exp(-x) / math.factorial(n_miso - 1),
                     0, np.inf)[0]

plt.plot(SNR_dB, C_simo, "-.", SNR_dB, C_miso)
plt.axis([0, 20, 0, 25])
plt.xlabel("SNR Promedio (dB)", fontsize=10)
plt.ylabel("Capacidad (bps/Hz)", fontsize=10)
plt.legend(["simo", "miso"])
plt.show()
