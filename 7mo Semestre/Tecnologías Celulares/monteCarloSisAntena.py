import numpy as np
import matplotlib.pyplot as plt

Nt, Nr = 2, 1
codebook = np.array([1+1j, 1-1j, -1+1j, -1-1j])

Es = 2
SNR_dB = np.arange(5, 21, 5)
BER = np.zeros(len(SNR_dB))

for i, snr_db in enumerate(SNR_dB):
    No = Es * 10 ** (-snr_db / 10)
    no_errors = 0
    no_symbols = 0

    while no_errors <= 100:
        # Simbolos QPSK
        s = (2 * np.random.randint(0, 2, 2) - 1) + 1j * (2 * np.random.randint(0, 2, 2) - 1)
        no_symbols += 2

        # Coeficientes del canal
        h = (np.random.randn(2) + 1j * np.random.randn(2)) / np.sqrt(2)

        # Generacion de ruido
        noise = np.sqrt(No / 2) * (np.random.randn(2) + 1j * np.random.randn(2))

        # Salidas del correlador (Alamouti 2x1)
        y1 = h[0] * s[0] + h[1] * s[1] + noise[0]
        y2 = -h[0] * np.conj(s[1]) + h[1] * np.conj(s[0]) + noise[1]

        # Estimacion de los simbolos s1 y s2 (combinacion)
        s_h = np.empty(2, dtype=complex)
        s_h[0] = y1 * np.conj(h[0]) + np.conj(y2) * h[1]
        s_h[1] = y1 * np.conj(h[1]) - np.conj(y2) * h[0]

        # Deteccion de maxima verosimilitud
        idx1 = np.argmin(np.abs(s_h[0] - codebook))
        idx2 = np.argmin(np.abs(s_h[1] - codebook))
        s_t = codebook[[idx1, idx2]]

        no_errors += np.count_nonzero(s_t != s)

    BER[i] = no_errors / no_symbols

plt.semilogy(SNR_dB, BER, marker='o')
plt.xlabel('SNR (dB)')
plt.ylabel('Tasa de error de simbolo (SER)')
plt.legend(['Alamouti: 4-PSK'])
plt.grid(True, which='both')
plt.show()
