import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk

# Aplicar el estilo cyberpunk
plt.style.use("cyberpunk")

def plot_histogram_and_cdf(data, bins, title, problem_num, bin_width=None):
    """Función para graficar Histograma y CDF."""
    fig, axs = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle(f'Problema {problem_num}: {title}', fontsize=14)

    # Si se especifica el ancho del bin (para el problema 5 y 6)
    if bin_width:
        bins = np.arange(min(data), max(data) + bin_width, bin_width)

    # Histograma
    axs[0].hist(data, bins=bins, density=True, alpha=0.7)
    axs[0].set_title('Histograma (Densidad)')
    axs[0].set_xlabel('Valor')
    axs[0].set_ylabel('Frecuencia')

    # CDF
    x = np.sort(data)
    y = np.arange(1, len(x) + 1) / len(x)
    axs[1].plot(x, y, lw=2)
    axs[1].set_title('Función de Distribución de Probabilidad (CDF)')
    axs[1].set_xlabel('Valor')
    axs[1].set_ylabel('F(x)')

    mplcyberpunk.add_glow_effects(axs[1])
    plt.tight_layout()
    plt.show()

N = 1000

# ---------------------------------------------------------
# Problema 4: PDF Lineal f(x) = x/8
# ---------------------------------------------------------
# C = 4 * sqrt(A)
A = np.random.rand(N)
data_p4 = 4 * np.sqrt(A)
plot_histogram_and_cdf(data_p4, bins=20, title='Distribución Lineal f(x) = x/8', problem_num=4)

# ---------------------------------------------------------
# Problema 5: Gaussianas vía Rayleigh
# ---------------------------------------------------------
sigma_sq = 1
A_ray = np.random.rand(N)
B_ray = np.random.rand(N)

# Ecuación de Rayleigh y ángulos
R = np.sqrt(2 * sigma_sq * np.log(1 / (1 - A_ray)))
Theta = 2 * np.pi * B_ray

# Tomamos C como nuestra secuencia Gaussiana (D también lo es)
data_p5 = R * np.cos(Theta)

# Ancho de bin sugerido: sigma^2 / 5 = 1 / 5 = 0.2
ancho_bin = sigma_sq / 5
plot_histogram_and_cdf(data_p5, bins=None, title='Gaussianas (Método Rayleigh)', problem_num=5, bin_width=ancho_bin)

# ---------------------------------------------------------
# Problema 6: Gaussianas con función nativa
# ---------------------------------------------------------
data_p6 = np.random.randn(N)
plot_histogram_and_cdf(data_p6, bins=None, title='Gaussianas (np.random.randn)', problem_num=6, bin_width=ancho_bin)

