import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

# 1. Funciones de Apoyo
def qfunct(x):
    """Evalúa la probabilidad teórica (Q-function)."""
    return 0.5 * erfc(x / np.sqrt(2))

def smldPe54(snr_db):
    """
    Simulación Monte Carlo (El equivalente a la función oculta de MATLAB).
    Transmite bits, añade ruido AWGN y cuenta cuántos errores hubo.
    """
    N_bits = 1000000  # Número de bits simulados
    snr_lineal = 10 ** (snr_db / 10)
    
    # Generamos bits aleatorios (BPSK: -1 y 1)
    bits_tx = np.random.choice([-1, 1], size=N_bits)
    
    # Generamos el ruido AWGN
    ruido = np.random.normal(0, np.sqrt(1 / snr_lineal), N_bits)
    
    # Señal recibida y decisión
    bits_rx = bits_tx + ruido
    errores = np.sum(np.sign(bits_rx) != np.sign(bits_tx))
    
    return errores / N_bits

# ---------------------------------------------------------
# Problema Ilustrativo 6: Simulación Monte Carlo
# ---------------------------------------------------------

# Vectores de SNR (Equivalentes a 0:1:12 y 0:0.1:12)
SNRindB1 = np.arange(0, 13, 1)    
SNRindB2 = np.arange(0, 12.1, 0.1) 

# Tasa de error simulada (Simulated error rate)
# Usamos una "list comprehension" de Python, que es una forma súper elegante 
# de hacer el ciclo for en una sola línea.
smld_err_prb = [smldPe54(snr) for snr in SNRindB1]

# Tasa de error teórica (Theoretical error rate)
# Adiós al ciclo for. Procesamos todo el arreglo de un golpe (Vectorización)
SNR_lineal = 10 ** (SNRindB2 / 10)
theo_err_prb = qfunct(np.sqrt(SNR_lineal))

# Plotting commands follow
plt.figure(figsize=(8, 6))

# Graficamos la simulación usando '*' tal como en MATLAB
plt.semilogy(SNRindB1, smld_err_prb, '*', markersize=8, label='Simulada (Monte Carlo)')

# Graficamos la teórica con una línea continua. El 'hold' es automático.
plt.semilogy(SNRindB2, theo_err_prb, '-', label='Teórica (Qfunct)')

# Estética visual
plt.grid(True, which="both", linestyle="--", alpha=0.7)
plt.xlabel('SNR (dB)')
plt.ylabel('Probabilidad de Error')
plt.legend()
plt.title('Probabilidad de Error: Simulada vs Teórica')

plt.show()


