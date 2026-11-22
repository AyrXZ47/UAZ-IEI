"""Ortogonalidad de subportadoras (Problema ilustrativo 1).

Equivale al script MATLAB: demuestra que dos portadoras muestreadas
que difieren en n ciclos por ventana de M muestras son ortogonales
(su producto sumado da ~0) para n = 1, 2, 3.

Uso:  python ortogonalidadSubportadoras.py
"""

import numpy as np

rng = np.random.default_rng()

M = 50
m = np.arange(M)
phi_k = 2 * np.pi * rng.random()
phi_j = 2 * np.pi * rng.random()

x_k = np.sin(4 * np.pi * m / 5 + phi_k)

for n in (1, 2, 3):
    x_j = np.sin(4 * np.pi * m / 5 + 2 * np.pi * m * n / M + phi_j)
    suma = np.sum(x_k * x_j)
    print(f"El resultado del calculo para n={n} es: {suma:.6f}")
