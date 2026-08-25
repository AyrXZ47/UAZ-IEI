"""ss_mlsrs: genera la secuencia de maxima longitud (m-secuencia) de un
registro de desplazamiento cuyas conexiones se dan como entrada
(0 = no conectado, 1 = conectado).

Adaptacion del ss_mlsrs.m de Proakis a Python.
"""

import numpy as np


def ss_mlsrs(connections):
    m = len(connections)
    L = 2**m - 1
    registers = [0] * (m - 1) + [1]        # contenido inicial del registro
    seq = np.zeros(L, dtype=int)
    seq[0] = registers[m - 1]
    for i in range(2, L + 1):
        new_reg_cont = [(connections[0] * seq[i - 2]) % 2]
        for j in range(2, m + 1):
            new_reg_cont.append(
                (registers[j - 2] + connections[j - 1] * seq[i - 2]) % 2
            )
        registers = new_reg_cont
        seq[i - 1] = registers[m - 1]
    return seq