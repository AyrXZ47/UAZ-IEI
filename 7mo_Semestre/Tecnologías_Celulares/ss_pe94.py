"""ss_Pe94: probabilidad de error por simulacion para DS/SS BPSK con
interferencia de tono sinusoidal (adaptacion del ejemplo de Proakis,
originalmente en MATLAB, archivo ss_Pe94.m).

Version vectorizada con numpy: el bucle de N simbolos se procesa en arrays
(N, Lc) de una vez. Semilla fija => resultados reproducibles.
"""

import numpy as np

_rng = np.random.default_rng(0)  # una secuencia por sesion, como en MATLAB


def ss_Pe94(snr_in_dB, Lc, A, w0, N=10000):
    """Pe simulada para DS/SS con interferencia de tono de amplitud A y
    frecuencia w0 (rad/muestra), usando Lc chips por simbolo."""
    snr = 10 ** (snr_in_dB / 10)
    sgma = 1.0
    Eb = 2 * sgma**2 * snr
    E_chip = Eb / Lc

    # simbolos de datos equiprobables +/-1
    data = np.where(_rng.random(N) < 0.5, -1.0, 1.0)            # (N,)

    # secuencia PN por simbolo (codigo nuevo por cada simbolo)
    pn = np.where(_rng.random((N, Lc)) < 0.5, -1.0, 1.0)        # (N, Lc)

    # senal transmitida: dato repetido por chip * PN, con energia E_chip
    trans_sig = np.sqrt(E_chip) * data[:, None] * pn

    noise = sgma * _rng.standard_normal((N, Lc))

    # interferencia: tono A*sin(w0*n), n = indice global de muestra (1-based)
    n = np.arange(1, N * Lc + 1).reshape(N, Lc)
    interference = A * np.sin(w0 * n)

    rec_sig = trans_sig + noise + interference

    # correlador: descorrelaciona con el PN y decide por signo de la
    # variable de decision (senal util = +sqrt(E_chip)*Lc si data=1)
    decision_variable = np.sum(rec_sig * pn, axis=1)
    decision = np.where(decision_variable > 0, 1.0, -1.0)

    return float(np.mean(decision != data))