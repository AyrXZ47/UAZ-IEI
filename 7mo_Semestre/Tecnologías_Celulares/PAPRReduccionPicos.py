import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()

T = 1
Fs = 200
t = np.arange(Fs) / (Fs * T)          # 0 : 1/(Fs*T) : T-1/(Fs*T)
K = 32
k = np.arange(1, K)                    # 1 .. K-1
rlz = 20
umbral = 10**0.3                       # 1.9953  (~3 dB)

PAPR = np.zeros(rlz)
PAPR_dB = np.zeros(rlz)
D = np.zeros(rlz)

for j in range(rlz):
    # fases cuantizadas a {0, pi/2, pi, 3pi/2}
    theta = np.pi * np.floor(rng.random(k.size) / 0.25) / 2
    x = np.cos(2 * np.pi * np.outer(t, k) / T + theta).sum(axis=1)
    x_h = x.copy()

    P_peak, idx = np.max(x**2), np.argmax(x**2)
    P_av = np.sum(x**2) / Fs
    PAPR[j] = P_peak / P_av
    PAPR_dB[j] = 10 * np.log10(PAPR[j])

    # reduccion de picos: recortar la muestra maxima hasta PAPR <= umbral
    if P_peak / P_av > umbral:
        n = 0
        # el bucle converge geometricamente; tope por seguridad
        # ponytail: el MATLAB original solo termina por redondeo flotante
        while P_peak / P_av > umbral and n < 10000:
            x_h[idx] = np.sqrt(umbral * P_av)
            P_peak, idx = np.max(x_h**2), np.argmax(x_h**2)
            P_av = np.sum(x_h**2) / Fs
            PAPR_dB[j] = 10 * np.log10(P_peak / P_av)
            n += 1

    D[j] = np.sum((x - x_h)**2) / Fs

plt.stem(D)
plt.xlabel('Realizacion')
plt.ylabel('Distorsion (D)')
plt.show()
