# Conversion de: montecarlo de senales ortogonales (MATLAB)
# Nota: el original tenia typos que se corrigen aqui:
#   EbNo_dB=':0:5:35' -> np.arange(0,36,5)
#   las dos ramas del if ponian r_d=1 -> r_d=0 en la rama r(1)>=r(2) (acierto)
#   No_over_2 no estaba definido -> se hereda del caso antipodal.
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
        noise = np.sqrt(No_over_2[i]) * rng.standard_normal((BATCH, 2))
        r = noise
        r[:, 0] += alpha * np.sqrt(Eb)                     # rama con senal
        r_d = (r[:, 0] < r[:, 1]).astype(int)              # error si pierde senal
        no_bits += BATCH
        no_errors += r_d.sum()
    BER[i] = no_errors / no_bits

rho_b = Eb / No_over_2
P2 = 1 / 2 * (1 - np.sqrt(rho_b / (2 + rho_b)))            # valor teorico

plt.figure(figsize=(8, 5))
plt.semilogy(EbNo_dB, BER, '-*', label='simulacion de monte carlo')
plt.semilogy(EbNo_dB, P2, '-o', label='valor teorico')
plt.xlabel('SNR/bit promedio (dB)')
plt.ylabel('probabilidad de error')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
mplcyberpunk.add_glow_effects()
plt.show()