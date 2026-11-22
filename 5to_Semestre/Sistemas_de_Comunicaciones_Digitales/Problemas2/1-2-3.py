import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk

def plot_histogram_and_cdf(data, bins, title, problem_num):
    """Función auxiliar para graficar Histograma y CDF."""
    fig, axs = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle(f'Problema {problem_num}: {title}', fontsize=14)

    # Gráfica del Histograma
    count, bins_edges, ignored = axs[0].hist(data, bins=bins, density=True, 
                                             edgecolor='cyan', facecolor='black', alpha=0.7)
    axs[0].set_title('Histograma (Densidad)')
    axs[0].set_xlabel('Valor')
    axs[0].set_ylabel('Frecuencia')
    axs[0].grid(True, linestyle='--', alpha=0.5)

    # Gráfica de la Función de Distribución de Probabilidad (CDF)
    # Ordenamos los datos y calculamos la probabilidad acumulada
    x = np.sort(data)
    y = np.arange(1, len(x) + 1) / len(x)
    
    axs[1].plot(x, y, color='magenta', lw=2)
    axs[1].set_title('Función de Distribución de Probabilidad (CDF)')
    axs[1].set_xlabel('Valor')
    axs[1].set_ylabel('F(x)')
    axs[1].grid(True, linestyle='--', alpha=0.5)

    plt.tight_layout()
    plt.show()

# Cantidad de números aleatorios
N = 1000

# ---------------------------------------------------------
# Problema 1: Intervalo [0, 1]
# ---------------------------------------------------------
# numpy.random.rand genera muestras de una distribución uniforme en [0, 1)
data_p1 = np.random.rand(N)
plot_histogram_and_cdf(data_p1, bins=10, title='Distribución Uniforme en [0, 1]', problem_num=1)

# ---------------------------------------------------------
# Problema 2: Intervalo [-0.5, 0.5] (Asumido por el error tipográfico)
# ---------------------------------------------------------
# Desplazamos la señal original restando 0.5
data_p2 = np.random.rand(N) - 0.5
plot_histogram_and_cdf(data_p2, bins=10, title='Distribución Uniforme en [-0.5, 0.5]', problem_num=2)

# ---------------------------------------------------------
# Problema 3: Intervalo [-1, 1]
# ---------------------------------------------------------
# Escalamos por 2 (amplitud) y desplazamos por -1
data_p3 = 2 * np.random.rand(N) - 1
mplcyberpunk.add_glow_effects()
plot_histogram_and_cdf(data_p3, bins=10, title='Distribución Uniforme en [-1, 1]', problem_num=3)

