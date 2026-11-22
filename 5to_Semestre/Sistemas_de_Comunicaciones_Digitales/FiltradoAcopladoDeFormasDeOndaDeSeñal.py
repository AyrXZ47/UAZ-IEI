import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# % Inicialización
# ---------------------------------------------------------
K = 20        # Número de muestras
A = 1         # Amplitud de la señal
l = np.arange(K + 1)  # Eje X para las gráficas (de 0 a 20)

# % Definiendo las formas de onda de la señal
s_0 = A * np.ones(K)
s_1 = np.concatenate((A * np.ones(K // 2), -A * np.ones(K // 2)))

# ---------------------------------------------------------
# Función principal: Filtro Acoplado con Convolución
# ---------------------------------------------------------
def simular_filtro_acoplado(s_transmitida, desviacion_estandar, titulo, posicion_subplot):
    # 1. El Canal AWGN: Generamos ruido y lo sumamos a la señal
    ruido = np.random.normal(0, desviacion_estandar, K)
    r = s_transmitida + ruido  
    
    # 2. El Filtro Acoplado (Matched Filter) usando Convolución
    # Invertimos la señal original con [::-1] (el equivalente a wrev)
    # y hacemos la convolución con la señal recibida 'r'
    salida_filtro_0 = np.convolve(r, s_0[::-1])
    salida_filtro_1 = np.convolve(r, s_1[::-1])
    
    # 3. Recorte (Slicing) de la señal
    # La convolución genera un arreglo de tamaño 2K-1.
    # Nos quedamos solo con los primeros K elementos para empatar los tiempos.
    r_0 = salida_filtro_0[:K]
    r_1 = salida_filtro_1[:K]
        
    # 4. Gráficas
    plt.subplot(3, 2, posicion_subplot)
    
    # Ajuste para que la línea empiece en el origen (0,0), igual que [0 r_0] en MATLAB
    r_0_plot = np.insert(r_0, 0, 0)
    r_1_plot = np.insert(r_1, 0, 0)
    
    plt.plot(l, r_0_plot, '-', label='r_0')
    plt.plot(l, r_1_plot, '--', label='r_1')
    
    # Estética calcada de las diapositivas
    plt.xticks([0, 5, 10, 15, 20], ['0', '5Tb', '10Tb', '15Tb', '20Tb'])
    plt.axis([0, 20, -20, 30])
    plt.xlabel(titulo, fontsize=10)

# ---------------------------------------------------------
# Ejecución de la Simulación (Los 6 sub-casos)
# ---------------------------------------------------------
plt.figure(figsize=(10, 12)) 

# Caso 1: Ruido nulo (sigma^2 = 0)
simular_filtro_acoplado(s_0, 0, r'(a) $\sigma^2=0$ & $S_0$ is transmitted', 1)
simular_filtro_acoplado(s_1, 0, r'(b) $\sigma^2=0$ & $S_1$ is transmitted', 2)

# Caso 2: Ruido bajo (sigma^2 = 0.1)
simular_filtro_acoplado(s_0, 0.1, r'(c) $\sigma^2=0.1$ & $S_0$ is transmitted', 3)
simular_filtro_acoplado(s_1, 0.1, r'(d) $\sigma^2=0.1$ & $S_1$ is transmitted', 4)

# Caso 3: Ruido alto (sigma^2 = 1)
simular_filtro_acoplado(s_0, 1, r'(e) $\sigma^2=1$ & $S_0$ is transmitted', 5)
simular_filtro_acoplado(s_1, 1, r'(f) $\sigma^2=1$ & $S_1$ is transmitted', 6)

plt.tight_layout() # Para que los títulos y ejes no choquen entre sí
plt.show()

