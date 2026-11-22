import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()

T = 1
Fs = 200
t = np.arange(Fs) / (Fs * T)          # 0 : 1/(Fs*T) : T-1/(Fs*T)
K = 32
k = np.arange(1, K)                    # 1 .. K-1
rlz = 20
M = 4                                  # candidatos de fase aleatoria (SLM)

PAPR = np.zeros(rlz)

for j in range(rlz):
    # fases cuantizadas a {0, pi/2, pi, 3pi/2}
    theta = np.pi * np.floor(rng.random(k.size) / 0.25) / 2
    phi = 2 * np.pi * rng.random((M, k.size))
    # x(m,i) = sum_l cos(2*pi*l*t(i)/T + theta(l) + phi(m,l)), vectorizado
    x = np.cos(2 * np.pi * np.outer(t, k) / T + theta + phi[:, None, :]).sum(axis=2)
    P_av = np.sum(x**2, axis=1) / Fs
    PAPR_phi = np.max(x**2, axis=1) / P_av
    PAPR[j] = PAPR_phi.min()           # se elige el candidato con menor PAPR

plt.stem(PAPR)
plt.xlabel('Realizacion')
plt.ylabel('PAPR')
plt.show()
