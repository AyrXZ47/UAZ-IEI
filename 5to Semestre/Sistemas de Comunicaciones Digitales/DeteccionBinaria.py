import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

# ---------------------------------------------------------
# Problema Ilustrativo 6: Función Qfunct (con su Docstring)
# ---------------------------------------------------------
def qfunct(x):
    """
    [y] = qfunct(x)
    QFUNCT evalúa la función Q (Q-function).
      y = 1/sqrt(2*pi) * integral from x to inf of exp(-t^2/2) dt.
      y = (1/2) * erfc(x/sqrt(2)).
    """
    # Usamos scipy.special.erfc en lugar de la función nativa de MATLAB
    return 0.5 * erfc(x / np.sqrt(2))

# ---------------------------------------------------------
# Problema Ilustrativo 5: Detección Binaria
# ---------------------------------------------------------

# 1. Definiendo el rango de SNR
initial_snr = 0
final_snr = 15
snr_step = 0.25

# Equivalente a: snr_in_dB = initial_snr:snr_step:final_snr
# Le sumamos snr_step al final para que el 15 sea inclusivo
snr_in_dB = np.arange(initial_snr, final_snr + snr_step, snr_step)

# 2. Vectorización (Adiós al for i=1:length...)
# Convertimos todo el arreglo de dB a escala lineal de un solo golpe
snr = 10 ** (snr_in_dB / 10)

# Calculamos la Probabilidad de Error (Pe) para todos los valores al mismo tiempo
Pe = qfunct(np.sqrt(snr))

# 3. Gráfica (semilogy)
plt.semilogy(snr_in_dB, Pe, linewidth=2)

# Unos retoques extra para que se vea más pro que el default de MATLAB
plt.grid(True, which="both", linestyle="--", alpha=0.7) 
plt.xlabel('SNR (dB)')
plt.ylabel('Probabilidad de Error (Pe)')
plt.title('Detección Binaria: Probabilidad de Error vs SNR')

plt.show()
❯ python CorrelacionDeFormasDeOndaSeñal.py
Traceback (most recent call last):
  File "/home/rzlap/Documents/CorrelacionDeFormasDeOndaSeñal.py", line 2, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'
