from matplotlib import pyplot as plt
import numpy as np

n=np.arange(-20, 21)
plt.figure(1)
plt.stem(n, np.abs(np.sinc(n/6)/3))
plt.show()

plt.figure(2)
plt.stem(n, np.angle(np.sinc(n/6)/3))
plt.show()
