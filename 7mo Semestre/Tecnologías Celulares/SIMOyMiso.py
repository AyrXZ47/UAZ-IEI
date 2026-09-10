import numpy as np
import matplotlib.pyplot as plt

H_simo = np.array([1, 0.5]).T
H_miso = np.array([1, 0.5])
Nt_miso = 2
Nr_simo = 2

SNR_dB = np.arange(0, 20.0001, 0.01)
SNR = 10 ** (SNR_dB / 10)

C_simo = np.log2(1 + SNR * np.sum(H_simo ** 2))
C_miso = np.log2(1 + SNR * np.sum(H_miso ** 2) / Nt_miso)

plt.plot(SNR_dB, C_simo, "-.", SNR_dB, C_miso)
plt.axis([0, 20, 0, 15])
plt.xlabel("SNR Promedio (dB)", fontsize=10)
plt.ylabel("Capacidad (bps/Hz)", fontsize=10)
plt.legend(["simo", "miso"])
plt.show()
