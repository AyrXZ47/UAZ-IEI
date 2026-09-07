import numpy as np
import matplotlib.pyplot as plt
from math import factorial

ep = 0.3

n = np.arange(1, 62, 2)  # i = 1:2:61
pe = []
for i in n:
    s = 0.0
    for j in range((i + 1) // 2, i + 1):  # j = (i+1)/2 : i
        s += factorial(i) / factorial(i - j) * ep**j * (1 - ep) ** (i - j)
    pe.append(s)

plt.stem(n, pe)
plt.xlabel("n")
plt.ylabel("pe")
plt.title("probabilidad de error como una funcion de n en un codigo de repeticion simple")
plt.show()
