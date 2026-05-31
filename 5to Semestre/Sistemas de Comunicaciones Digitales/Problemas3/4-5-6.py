import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk

plt.style.use("cyberpunk")

def simular_filtro_acoplado(s0, s1, varianzas, titulo_base, filename):
    K = len(s0)
    k_steps = np.arange(1, K + 1)
    
    fig, axes = plt.subplots(len(varianzas), 1, figsize=(8, 3 * len(varianzas)))
    fig.suptitle(titulo_base + " (Filtro Acoplado - Transmitiendo s0)", fontsize=16, color="cyan")
    
    if len(varianzas) == 1:
        axes = [axes]
        
    # El filtro acoplado requiere la señal invertida en el tiempo
    h0 = np.flip(s0)
    h1 = np.flip(s1)
        
    for i, var in enumerate(varianzas):
        sigma = np.sqrt(var)
        n = np.random.normal(0, sigma, K)
        r = s0 + n  # Asumimos que se transmite s0
        
        # Convolución discreta (Filtro Acoplado)
        # Nos quedamos con los primeros K elementos para ver la evolución hasta Tb
        y0 = np.convolve(r, h0)[:K]
        y1 = np.convolve(r, h1)[:K]
            
        ax = axes[i]
        ax.plot(k_steps, y0, marker='o', label='Filtro Acoplado 0 (s0)')
        ax.plot(k_steps, y1, marker='x', linestyle='--', label='Filtro Acoplado 1 (s1)')
        
        ax.set_title(rf"Varianza del Ruido: $\sigma^2 = {var}$")
        ax.set_xlabel("Muestra (k)")
        ax.set_ylabel("Salida del Filtro (y)")
        ax.set_xticks(k_steps)
        ax.legend()
        
        mplcyberpunk.add_glow_effects(ax)

    plt.tight_layout()
    plt.savefig(filename)
    print(f"Gráfica guardada: {filename}")
    plt.show()

def simular_filtro_id(filename):
    # Problema 5: Filtro Integrate-and-Dump para señales antipodales (sin ruido)
    K = 14 # Número representativo de muestras para el intervalo
    k_steps = np.arange(1, K + 1)
    
    A = 1
    s0 = np.ones(K) * A
    s1 = np.ones(K) * -A
    
    # El filtro I&D es simplemente la suma acumulativa
    y0_transmitting_s0 = np.cumsum(s0)
    y1_transmitting_s1 = np.cumsum(s1)
    
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(k_steps, y0_transmitting_s0, marker='o', label='Transmitiendo $s_0(t)$', color='cyan')
    ax.plot(k_steps, y1_transmitting_s1, marker='s', label='Transmitiendo $s_1(t)$', color='magenta')
    
    ax.set_title("Problema 5: Salida del Filtro Integrate-and-Dump (I&D)", fontsize=16)
    ax.set_xlabel("Muestra (k)")
    ax.set_ylabel("Salida del Integrador")
    ax.set_xticks(k_steps)
    ax.legend()
    
    mplcyberpunk.add_glow_effects(ax)
    plt.tight_layout()
    plt.savefig(filename)
    print(f"Gráfica guardada: {filename}")
    plt.show()

if __name__ == "__main__":
    # --- PROBLEMA 4 ---
    # Señales: K=20 (basado en el problema ilustrativo 4)
    s0_p4 = np.ones(20)
    s1_p4 = np.concatenate((np.ones(10), -np.ones(10)))
    varianzas_p4 = [0.1, 1.0, 3.0]
    simular_filtro_acoplado(s0_p4, s1_p4, varianzas_p4, "Problema 4", "problema_4_cyberpunk.png")
    
    # --- PROBLEMA 5 ---
    # Filtro Integrate-and-Dump (sólo gráficas sin ruido solicitadas)
    simular_filtro_id("problema_5_cyberpunk.png")
    
    # --- PROBLEMA 6 ---
    # Señales: K=10 (condiciones del problema 1)
    s0_p6 = np.ones(10)
    s1_p6 = np.concatenate((np.ones(5), -np.ones(5)))
    varianzas_p6 = [0, 0.1, 0.5, 1.0]
    simular_filtro_acoplado(s0_p6, s1_p6, varianzas_p6, "Problema 6", "problema_6_cyberpunk.png")
