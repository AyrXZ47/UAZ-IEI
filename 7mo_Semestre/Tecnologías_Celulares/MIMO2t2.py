import numpy as np
import matplotlib.pyplot as plt

Nt = 2
H = np.array([[1, 0.5], [0.4, 0.8]])
lamda = np.linalg.eigvalsh(H @ H.conj().T)

SNR_dB = np.arange(0, 20.0001, 0.01)
SNR = 10 ** (SNR_dB / 10)

C = np.log2(1 + SNR * lamda[0] / Nt) + np.log2(1 + SNR * lamda[1] / Nt)
print(f"Los eigen valores son: {lamda}")

plt.plot(SNR_dB, C)
plt.axis([0, 20, 0, 15])
plt.xlabel("SNR Promedio (dB)", fontsize=10)
plt.ylabel("Capacidad (bps/Hz)", fontsize=10)
plt.show()
