"""Generacion de secuencias Gold a partir de dos m-secuencias primas.

Equivale al script MATLAB de Proakis (generacionSecuenciasGold.m).
Imprime las L secuencias Gold y el maximo de la correlacion cruzada.

Uso:  python generacionSecuenciasGold.py
"""

import numpy as np

from funcionGeneracionSecuenciasGold import ss_mlsrs

connections1 = [1, 0, 1, 0, 0]
connections2 = [1, 1, 1, 0, 1]
sequence1 = ss_mlsrs(connections1)
sequence2 = ss_mlsrs(connections2)

L = 2 ** len(connections1) - 1
gold_seq = np.zeros((L, L), dtype=int)
for shift_amount in range(L):
    temp = np.concatenate((sequence2[shift_amount:], sequence2[:shift_amount]))
    gold_seq[shift_amount] = (sequence1 + temp) % 2

max_cross_corr = 0
for i in range(L - 1):
    for j in range(i + 1, L):
        c1 = 2 * gold_seq[i] - 1
        c2 = 2 * gold_seq[j] - 1
        for m in range(L):
            shifted_c2 = np.concatenate((c2[m:], c2[:m]))
            corr = abs(np.sum(c1 * shifted_c2))
            if corr > max_cross_corr:
                max_cross_corr = corr

np.set_printoptions(linewidth=120)
print("gold_seq:")
print(gold_seq)
print("max_cross_corr:", max_cross_corr)