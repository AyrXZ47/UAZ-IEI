import numpy as np

no_bits = 10
input = np.random.randint(0, 4, no_bits)
if no_bits % 2 != 0:
    input = np.append(input, 0)

L = len(input)

st_0 = 0
st_c = st_0
ant_1 = []
ant_2 = []

for i in range(L):
    st_p = st_c
    st_c = int(input[i])  # estados 0..3
    ant_1.append(st_p)
    ant_2.append(st_c)

if st_c != 0:
    ant_1.append(st_c)
    ant_2.append(0)

print('La secuencia de entrada es:                    ', input)
print('La secuencia transmitida en la antena 1 es:    ', ant_1)
print('La secuencia transmitida en la antena 2 es:    ', ant_2)
