# Conversion de: SimulacionMonteCarlo de senales antipodales (MATLAB)
# Simula BER sobre canal Rayleigh hasta acumular 100 errores por punto SNR.
import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk

Eb = 1
EbNo_dB = np.arange(0, 36, 5)      # 0:5:35 en MATLAB
No_over_2 = Eb * 10 ** (-EbNo_dB / 10)
sigma = 1                          # parametro del desvanecimiento Rayleigh
BER = np.zeros(len(EbNo_dB))

rng = np.random.default_rng()
BATCH = 10000                      # muestras por lote (acelera el while)

for i in range(len(EbNo_dB)):
    no_errors = 0
    no_bits = 0
    while no_errors <= 100:
        u = rng.random(BATCH)
        alpha = sigma * np.sqrt(-2 * np.log(u))            # amplitud Rayleigh
        noise = np.sqrt(No_over_2[i]) * rng.standard_normal(BATCH)
        y = alpha * np.sqrt(Eb) + noise
        y_d = (y <= 0).astype(int)                         # error si y<=0
        no_bits += BATCH
        no_errors += y_d.sum()
    BER[i] = no_errors / no_bits

rho_b = Eb / No_over_2
P2 = 1 / 2 * (1 - np.sqrt(rho_b / (1 + rho_b)))            # valor teorico

plt.figure(figsize=(8, 5))
plt.semilogy(EbNo_dB, BER, '-*', label='simulacion monte carlo')
plt.semilogy(EbNo_dB, P2, '-o', label='valor teorico')
plt.xlabel('SNR/bit (dB) promedio')
plt.ylabel('probabilidad de error')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
mplcyberpunk.add_glow_effects()
plt.show()