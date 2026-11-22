import numpy as np

k = 11
# u: todas las 2^k palabras mensaje como filas (bit más significativo primero)
u = np.array([[int(b) for b in f"{i - 1:0{k}b}"] for i in range(1, 2**k + 1)])

g = np.array([[int(d) for d in row] for row in [
    "100000000001100",
    "010000000000110",
    "001000000000011",
    "000100000001010",
    "000010000001001",
    "000001000000101",
    "000000100001110",
    "000000010000111",
    "000000001001011",
    "000000000101101",
    "000000000011111",
]])

c = (u @ g) % 2
w_min = c[1:].sum(axis=1).min()  # peso mínimo de las palabras código distintas de cero

print("c =")
print(c)
print("w_min =", w_min)
