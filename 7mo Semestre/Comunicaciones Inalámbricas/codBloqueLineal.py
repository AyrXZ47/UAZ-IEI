import numpy as np

k = 4
# u: todas las 2^k palabras mensaje como filas (bit más significativo primero)
u = np.array([[int(b) for b in f"{i - 1:0{k}b}"] for i in range(1, 2**k + 1)])

g = np.array([
    [1, 0, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 0, 1],
])

c = (u @ g) % 2
w_min = c[1:].sum(axis=1).min()  # peso mínimo de las palabras código distintas de cero

print("c =")
print(c)
print("w_min =", w_min)
