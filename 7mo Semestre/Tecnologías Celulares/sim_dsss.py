"""Simulacion DS/SS: Pe vs SNR para 4 amplitudes de interferencia de tono.

Equivale al script MATLAB del ejemplo de Proakis (script principal).
Estilo cyberpunk con efecto glow (mplcyberpunk).

Uso:  python sim_dsss.py
"""

import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk

from ss_pe94 import ss_Pe94

Lc = 20
w0 = 1

# rango de SNR igual que el original: 0:2:30 dB
SNRindB = np.arange(0, 31, 2)
# para A=0 (sin interferencia) el original barre 0:1:8 dB
SNRindB4 = np.arange(0, 9, 1)

smld_err_prb1 = [ss_Pe94(s, Lc, 3, w0) for s in SNRindB]
smld_err_prb2 = [ss_Pe94(s, Lc, 7, w0) for s in SNRindB]
smld_err_prb3 = [ss_Pe94(s, Lc, 12, w0) for s in SNRindB]
smld_err_prb4 = [ss_Pe94(s, Lc, 0, w0) for s in SNRindB4]

plt.style.use("cyberpunk")
fig, ax = plt.subplots(figsize=(9, 6))

ax.semilogy(SNRindB, smld_err_prb1, "-o", label="A=3")
ax.semilogy(SNRindB, smld_err_prb2, "-o", label="A=7")
ax.semilogy(SNRindB, smld_err_prb3, "-o", label="A=12")
ax.semilogy(SNRindB4, smld_err_prb4, "-o", label="A=0")

ax.set_xlabel("SNR en dB")
ax.set_ylabel("Probabilidad de error (Pe)")
ax.set_title("DS/SS BPSK con interferencia de tono (Proakis)")
ax.legend()

mplcyberpunk.make_lines_glow()
plt.tight_layout()
plt.show()