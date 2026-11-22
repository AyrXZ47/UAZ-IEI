import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# % Inicialización
# ---------------------------------------------------------
K = 20        # Número de muestras
A = 1         # Amplitud de la señal
l = np.arange(K + 1)  # Equivalente a l=0:K para el eje X de las gráficas

# % Definiendo las formas de onda de la señal
s_0 = A * np.ones(K)
# En Python concatenamos arreglos así:
s_1 = np.concatenate((A * np.ones(K // 2), -A * np.ones(K // 2)))

# ---------------------------------------------------------
# Función principal para evitar repetir código
# ---------------------------------------------------------
def simular_y_graficar(s_transmitida, desviacion_estandar, titulo, posicion_subplot):
    # Generación de ruido gaussiano ~N(0, std^2)
    ruido = np.random.normal(0, desviacion_estandar, K)
    r = s_transmitida + ruido  # Señal recibida
    
    # Inicializando señales de salida
    r_0 = np.zeros(K)
    r_1 = np.zeros(K)
    
    # El loop de correlación. 
    # Usamos range(1, K + 1) para que 'n' vaya de 1 a 20, igual que en MATLAB
    for n in range(1, K + 1):
        # En Python, el índice 'n-1' es donde guardamos el valor actual.
        # r[:n] toma exactamente 'n' elementos (del índice 0 al n-1)
        r_0[n-1] = np.sum(r[:n] * s_0[:n])
        r_1[n-1] = np.sum(r[:n] * s_1[:n])
        
    # Graficando los resultados
    plt.subplot(3, 2, posicion_subplot)
    
    # Prependemos un 0 para que coincida con la longitud de 'l' (21 elementos)
    # Equivalente en MATLAB a: plot(l, [0 r_0])
    r_0_plot = np.insert(r_0, 0, 0)
    r_1_plot = np.insert(r_1, 0, 0)
    
    plt.plot(l, r_0_plot, '-', label='r_0')
    plt.plot(l, r_1_plot, '--', label='r_1')
    
    # Configuración visual de la gráfica
    plt.xticks([0, 5, 10, 15, 20], ['0', '5Tb', '10Tb', '15Tb', '20Tb'])
    plt.axis([0, 20, -5, 30])
    plt.xlabel(titulo, fontsize=10)

# ---------------------------------------------------------
# Ejecución de los Casos
# ---------------------------------------------------------
plt.figure(figsize=(10, 12)) # Ajustamos el tamaño del canvas

# Caso 1: Ruido nulo (std = 0)
simular_y_graficar(s_0, 0, r'(a) $\sigma^2=0$ & $S_0$ is transmitted', 1)
simular_y_graficar(s_1, 0, r'(b) $\sigma^2=0$ & $S_1$ is transmitted', 2)

# Caso 2: Ruido bajo (std = 0.1)
simular_y_graficar(s_0, 0.1, r'(c) $\sigma^2=0.1$ & $S_0$ is transmitted', 3)
simular_y_graficar(s_1, 0.1, r'(d) $\sigma^2=0.1$ & $S_1$ is transmitted', 4)

# Caso 3: Ruido alto (std = 1)
simular_y_graficar(s_0, 1, r'(e) $\sigma^2=1$ & $S_0$ is transmitted', 5)
simular_y_graficar(s_1, 1, r'(f) $\sigma^2=1$ & $S_1$ is transmitted', 6)

plt.tight_layout() # Evita que los textos se empalmen
plt.show()

