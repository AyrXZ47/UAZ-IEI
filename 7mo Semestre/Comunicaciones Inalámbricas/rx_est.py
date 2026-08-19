# Conversion de la funcion MATLAB: Rx_est(X, M)
# Estima la autocorrelacion Rx[m] = E{X[n] * X[n+m-1]} para m = 1..M+1
# (normalizada por el numero real de terminos N-m+1, estimador no sesgado).
import numpy as np


def Rx_est(X, M):
    N = len(X)
    Rx = np.zeros(M + 1, dtype=X.dtype)   # complejo si X es complejo
    for m in range(1, M + 2):            # m = 1..M+1 (indices 1..M+1 en MATLAB)
        for n in range(0, N - m + 1):    # n = 1..N-m+1 en MATLAB
            Rx[m - 1] += X[n] * X[n + m - 1]
        Rx[m - 1] /= (N - m + 1)
    return Rx


if __name__ == "__main__":
    # Self-check: X[n]=X[n+m-1] determinista trivial. Para X = todos unos,
    # Rx[m] = promedio de productos de unos = 1 para todo m.
    X = np.ones(10)
    Rx = Rx_est(X, 3)
    assert np.allclose(Rx, 1.0), Rx
    print("Ok: Rx_est normalizado sobre X=ones ->", Rx)
