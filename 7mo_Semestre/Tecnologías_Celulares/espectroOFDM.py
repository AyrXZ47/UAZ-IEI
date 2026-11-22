import numpy as np
import matplotlib.pyplot as plt

T = 1
k = np.arange(6)
f_k = k / T
f = np.arange(0, 4/T + 0.01*4/T, 0.01*4/T)

# |U_k(f)| = sqrt(T/2) * |sinc((f-f_k)T) + sinc((f+f_k)T)|  (np.sinc = sin(pi x)/(pi x), igual que MATLAB)
U = np.abs(np.sqrt(T/2) * (np.sinc((f - f_k[:, None])*T) + np.sinc((f + f_k[:, None])*T)))
U_norm = U / U.max(axis=1, keepdims=True)
U_dB = 10*np.log10(U_norm + 1e-12)  # piso para evitar log(0)

for i in k:
    plt.plot(f, U_dB[i], label=f'k = {i}')
plt.axis([f.min(), f.max(), -180, 20])
plt.xlabel('f')
plt.ylabel('|U_k(f)| (dB)')
plt.legend()
plt.grid(True)
plt.show()
