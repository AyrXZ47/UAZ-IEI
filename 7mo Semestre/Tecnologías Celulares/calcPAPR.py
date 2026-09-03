import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()

T = 1
Fs = 200
t = np.arange(Fs) / (Fs * T)          # 0 : 1/(Fs*T) : T-1/(Fs*T)
K = 32
k = np.arange(1, K)                    # 1 .. K-1
rlz = 20

PAPR = np.zeros(rlz)
for j in range(rlz):
    # fases cuantizadas a {0, pi/2, pi, 3pi/2}
    theta = np.pi * np.floor(rng.random(k.size) / 0.25) / 2
    # x(i) = sum_l cos(2*pi*l*t(i)/T + theta(l)), vectorizado sobre t y l
    x = np.cos(2 * np.pi * np.outer(t, k) / T + theta).sum(axis=1)
    P_peak = np.max(x**2)
    P_av = np.sum(x**2) / Fs
    PAPR[j] = P_peak / P_av

plt.stem(PAPR)
plt.xlabel('Realización')
plt.ylabel('PAPR')
plt.show()
