"""Deteccion de senal LPI (Low Probability of Intercept).

Equivale al script MATLAB de Proakis (m-secuencia + autocorrelacion +
filtro acoplado). La senal utiliza una secuencia m (PRBS) de longitud L
escondida bajo ruido; el filtro acoplado acumula la energia de la senal
mientras el ruido se cancela, revelando la senal al final.

Uso:  python DeteccionSeñalLPI.py
"""

import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk

L = 1023          # longitud de la secuencia m (2^10 - 1)
s = 1             # amplitud de la senal
var = 10          # varianza del ruido (SNR bajo => senal por debajo del ruido)

rng = np.random.default_rng(0)  # semilla fija => reproducible

# --- 1. Generar la secuencia m con registro de desplazamiento de 10 etapas
#        (polinomio: output = etapa1 xor etapa8)
sh_r = [1] + [0] * 9            # estado inicial del registro
output = np.zeros(L, dtype=int)
for i in range(L):
    output[i] = sh_r[0]
    temp = (sh_r[0] + sh_r[7]) % 2   # mod(sh_r(1)+sh_r(8),2), 0-indexed => sh_r[0]+sh_r[7]
    for j in range(9):
        sh_r[j] = sh_r[j + 1]
    sh_r[9] = temp

c = 2 * output - 1              # convertir 0/1 a +/-1

# --- 2. Autocorrelacion periodica de la secuencia m
#        Rc(m) = sum_n c(n)*c((n+m) mod L).  Pico Rc(0)=L, resto ~ +/-1.
idx = np.arange(L)
Rc = np.array([
    np.sum(c * c[(idx + m) % L]) for m in range(L)
])

# --- 3. Senal recibida: senal escondida bajo ruido (var=10)
r = s * c + np.sqrt(var) * rng.standard_normal(L)

# --- 4. Salida del filtro acoplado (correlacion acumulada)
#        y(n) = sum_{k=1..n} r(k)*c(k) => acumula senal, cancela ruido
y = np.cumsum(r * c)

# --- 5. Graficas (3 subplots apilados, estilo cyberpunk + glow)
plt.style.use("cyberpunk")
fig, axs = plt.subplots(3, 1, figsize=(10, 10))

axs[0].plot(Rc)
axs[0].set_ylim(-max(abs(Rc)), max(abs(Rc)))
axs[0].set_title("Autocorrelación")
axs[0].set_xlabel("m")
axs[0].set_ylabel("Rc(m)")

axs[1].plot(r)
axs[1].set_ylim(-max(abs(r)), max(abs(r)))
axs[1].set_title("Señal recibida (señal LPI escondida bajo el ruido)")
axs[1].set_xlabel("k")
axs[1].set_ylabel("r_k")

axs[2].plot(y)
axs[2].set_ylim(min(y), max(y))
axs[2].set_title("Salida del filtro acoplado (detecta la señal)")
axs[2].set_xlabel("n")
axs[2].set_ylabel("y_n")

mplcyberpunk.make_lines_glow()
plt.tight_layout()
plt.show()