# Conversion de: demodulador Rake, canal de dos trayectorias (MATLAB)
# Monte Carlo de BER con combinacion por maxima relacion senal/ruido (MRC)
# de D=2 ramas en desvanecimiento Rayleigh, comparado con la formula teorica.
import numpy as np
import matplotlib.pyplot as plt
from math import comb
import mplcyberpunk

D = 2
sigma = 1 / np.sqrt(2)                       # parametro del desvanecimiento Rayleigh
Eb = 1
EbNo_dB = np.arange(5, 26, 5)                # 5:5:25 en MATLAB
EbNo = 10 ** (EbNo_dB / 10)
No = Eb * 2 * sigma ** 2 * 10 ** (-EbNo_dB / 10)
BER = np.zeros(len(EbNo))

rng = np.random.default_rng()
BATCH = 10000                                # muestras por lote (acelera el while)

for i in range(len(EbNo)):
    no_errors = 0
    no_bits = 0
    while no_errors <= 100:
        u = rng.random((BATCH, 2))
        alpha = sigma * np.sqrt(-2 * np.log(u))          # amplitud Rayleigh por rama
        phi = 2 * np.pi * rng.random((BATCH, 2))
        c = alpha * np.exp(1j * phi)                     # ganancia compleja por rama
        noise = np.sqrt(No[i] / 2) * (rng.standard_normal((BATCH, 2))
                                      + 1j * rng.standard_normal((BATCH, 2)))
        r = c * np.sqrt(Eb) + noise
        R = np.real(np.conj(c[:, 0]) * r[:, 0] + np.conj(c[:, 1]) * r[:, 1])
        no_bits += BATCH
        no_errors += (R <= 0).sum()
    BER[i] = no_errors / no_bits

rho = EbNo                                    # SNR por rama
rho_b = D * rho
rho_b_dB = 10 * np.log10(rho_b)
K_D = comb(2 * D - 1, D)                      # (2D-1)!/(D!(D-1)!)
P_2 = K_D / (4 * rho) ** D

plt.figure(figsize=(8, 5))
plt.semilogy(rho_b_dB, BER, '-*', label='simulacion de monte carlo')
plt.semilogy(rho_b_dB, P_2, '-o', label='valor teorico')
plt.xlabel('SNR/bit (dB)')
plt.ylabel('BER')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
mplcyberpunk.add_glow_effects()
plt.show()