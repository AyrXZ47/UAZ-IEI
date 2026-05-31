import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk

# Configurar el estilo Cyberpunk
plt.style.use("cyberpunk")

def simular_correlador(s0, s1, varianzas, titulo_base, filename):
    k_steps = np.arange(1, 11)
    
    # Se simula el caso donde s0 es la señal transmitida
    fig, axes = plt.subplots(len(varianzas), 1, figsize=(8, 3 * len(varianzas)))
    fig.suptitle(titulo_base + " (Transmitiendo s0)", fontsize=16, color="cyan")
    
    # Asegurar que axes sea iterable si solo hay 1 varianza (no pasa aquí, pero es buena práctica)
    if len(varianzas) == 1:
        axes = [axes]
        
    for i, var in enumerate(varianzas):
        sigma = np.sqrt(var)
        # Generar AWGN
        n = np.random.normal(0, sigma, 10)
        
        # Señal recibida
        r = s0 + n
        
        # Inicializar salidas de los correladores
        c0 = np.zeros(10)
        c1 = np.zeros(10)
        
        # Correlación discreta iterativa
        for k in range(10):
            c0[k] = np.sum(r[:k+1] * s0[:k+1])
            c1[k] = np.sum(r[:k+1] * s1[:k+1])
            
        # Graficar
        ax = axes[i]
        ax.plot(k_steps, c0, marker='o', label='Correlador 0 (s0)')
        ax.plot(k_steps, c1, marker='x', linestyle='--', label='Correlador 1 (s1)')
        
        ax.set_title(rf"Varianza del Ruido: $\sigma^2 = {var}$")
        ax.set_xlabel("Muestra (k)")
        ax.set_ylabel("Salida del Correlador")
        ax.set_xticks(k_steps)
        ax.legend()
        
        # Aplicar el efecto de brillo cyberpunk a las líneas
        mplcyberpunk.add_glow_effects(ax)

    plt.tight_layout()
    plt.savefig(filename)
    print(f"Gráfica guardada: {filename}")
    plt.show()

if __name__ == "__main__":
    # --- PROBLEMA 1 ---
    # Señales: s0 constante, s1 mitad positiva mitad negativa
    s0_p1 = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    s1_p1 = np.array([1, 1, 1, 1, 1, -1, -1, -1, -1, -1])
    varianzas_p1 = [0, 0.1, 0.5, 1.0]
    simular_correlador(s0_p1, s1_p1, varianzas_p1, "Problema 1", "problema_1_cyberpunk.png")
    
    # --- PROBLEMA 2 ---
    # Señales: s0 toda negativa, s1 mitad negativa mitad positiva
    s0_p2 = np.array([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1])
    s1_p2 = np.array([-1, -1, -1, -1, -1, 1, 1, 1, 1, 1])
    varianzas_p2 = [0, 0.1, 0.5, 1.0]
    simular_correlador(s0_p2, s1_p2, varianzas_p2, "Problema 2", "problema_2_cyberpunk.png")
    
    # --- PROBLEMA 3 ---
    # Señales: Mismas que el Problema 1, pero ruido severo
    varianzas_p3 = [0.1, 1.0, 3.0]
    simular_correlador(s0_p1, s1_p1, varianzas_p3, "Problema 3", "problema_3_cyberpunk.png")
