"""Simulacion FH/SS con interferencia de banda parcial (Proakis, ejemplo ilustrativo 7).

Equivale al script MATLAB ss_Pe96: Monte Carlo (N=10000 bits) contra el valor
teorico. Estilo cyberpunk con efecto glow (mplcyberpunk).

Uso:  python simulacionSistemaFH.py
"""

import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk

rng = np.random.default_rng()


def ss_pe96(rho_in_dB, N=10000):
    """Tasa de error medida (Monte Carlo) para FH/SS con banda parcial."""
    rho = 10 ** (rho_in_dB / 10)      # energia por bit en unidades lineales
    alpha = 2 / rho if rho > 2 else 1  # factor de banda parcial optimo
    sgma = np.sqrt(1 / (2 * alpha))

    data = (rng.random(N) < 0.5).astype(int)

    r1c = np.zeros(N)
    r1s = np.zeros(N)
    r2c = np.zeros(N)
    r2s = np.zeros(N)
    r1c[data == 0] = np.sqrt(rho)
    r2c[data == 1] = np.sqrt(rho)

    hit = rng.random(N) < alpha
    m = hit.sum()
    r1c[hit] += rng.normal(0, sgma, m)
    r1s[hit] += rng.normal(0, sgma, m)
    r2c[hit] += rng.normal(0, sgma, m)
    r2s[hit] += rng.normal(0, sgma, m)

    r1 = r1c ** 2 + r1s ** 2
    r2 = r2c ** 2 + r2s ** 2
    decis = (r1 <= r2).astype(int)  # r1 > r2 -> bit 0

    return np.mean(decis != data)


rho_b1 = np.arange(0, 36, 5)        # rho en dB para tasa simulada
rho_b2 = np.arange(0, 35.1, 0.1)    # rho en dB para tasa teorica

smld_err_prb = [ss_pe96(r) for r in rho_b1]

temp = 10 ** (rho_b2 / 10)
theo_err_rate = np.where(temp > 2, 1 / (np.exp(1) * temp), 0.5 * np.exp(-temp / 2))

plt.style.use("cyberpunk")
fig, ax = plt.subplots(figsize=(9, 6))

ax.semilogy(rho_b1, smld_err_prb, "-*", label="simulacion monte carlo")
ax.semilogy(rho_b2, theo_err_rate, "--", label="valor teorico")
ax.set_xlabel("SNR promedio (dB)")
ax.set_ylabel("BER")
ax.set_title("FH/SS con interferencia de banda parcial (Proakis)")
ax.legend()

mplcyberpunk.make_lines_glow()
plt.tight_layout()
plt.show()