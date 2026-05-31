import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp
import mplcyberpunk

# Activar el estilo de neon
plt.style.use("cyberpunk")

# Función Q
def Q_funct(x):
    return 0.5 * sp.erfc(x / np.sqrt(2))

# --- PROBLEMA 7: Filtro Acoplado para la Fig. 2 ---
def problema_7():
    s0 = np.array([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1])
    s1 = np.array([-1, -1, -1, -1, -1, 1, 1, 1, 1, 1])
    varianzas = [0, 0.1, 0.5, 1.0]
    
    h0 = np.flip(s0)
    h1 = np.flip(s1)
    K = len(s0)
    k_steps = np.arange(1, K + 1)
    
    fig, axes = plt.subplots(len(varianzas), 1, figsize=(8, 10))
    fig.canvas.manager.set_window_title('Problema 7: Filtro Acoplado (Fig. 2)')
    fig.suptitle("Filtro Acoplado (Fig 2) - Transmitiendo s0", fontsize=14, color="cyan")
    
    for i, var in enumerate(varianzas):
        sigma = np.sqrt(var)
        n = np.random.normal(0, sigma, K)
        r = s0 + n  
        
        y0 = np.convolve(r, h0)[:K]
        y1 = np.convolve(r, h1)[:K]
            
        axes[i].plot(k_steps, y0, marker='o', label='Filtro 0 (s0)')
        axes[i].plot(k_steps, y1, marker='x', linestyle='--', label='Filtro 1 (s1)')
        axes[i].set_title(f"$\sigma^2 = {var}$")
        axes[i].legend()
        mplcyberpunk.add_glow_effects(axes[i])

    plt.tight_layout()

# --- PROBLEMA 8: Simulación Monte Carlo (Ortogonal) ---
def problema_8():
    E = 1
    N_bits = 10000
    varianzas = [0.1, 0.5, 1.0] # Omitimos 0 para log scale, error = 0 no se grafica bien
    
    snr_db_teorico = np.linspace(-5, 10, 50)
    snr_lineal_teorico = 10**(snr_db_teorico / 10)
    pe_teorico = Q_funct(np.sqrt(snr_lineal_teorico))
    
    pe_simulado = []
    snr_db_simulado = []
    
    # 1. Simulación Monte Carlo
    for var in varianzas:
        sigma = np.sqrt(var)
        # SNR = 1 / (2 * sigma^2) dado que E = 1
        snr_lineal = 1 / (2 * var)
        snr_db_simulado.append(10 * np.log10(snr_lineal))
        
        bits_tx = np.random.randint(0, 2, N_bits)
        errores = 0
        
        for bit in bits_tx:
            n0 = np.random.normal(0, sigma)
            n1 = np.random.normal(0, sigma)
            if bit == 0:
                r0, r1 = E + n0, n1
            else:
                r0, r1 = n0, E + n1
                
            bit_rx = 0 if r0 > r1 else 1
            if bit_rx != bit:
                errores += 1
                
        pe_simulado.append(errores / N_bits)
        
    fig = plt.figure(figsize=(14, 6))
    fig.canvas.manager.set_window_title('Problema 8: Monte Carlo Ortogonal')
    
    ax1 = fig.add_subplot(121)
    ax1.semilogy(snr_db_teorico, pe_teorico, label='Pe Teórico', color='cyan')
    ax1.semilogy(snr_db_simulado, pe_simulado, 'o', label='Pe Simulado', color='magenta')
    ax1.set_title("BER vs SNR (Ortogonal)")
    ax1.set_xlabel("SNR (dB)")
    ax1.set_ylabel("Probabilidad de Error (Pe)")
    ax1.legend()
    mplcyberpunk.add_glow_effects(ax1)
    
    # 2. Scatter Plot de 1000 muestras para sigma^2 = 0.5 (como representativo)
    ax2 = fig.add_subplot(122)
    sigma_scatter = np.sqrt(0.5)
    r0_0, r1_0 = E + np.random.normal(0, sigma_scatter, 500), np.random.normal(0, sigma_scatter, 500)
    r0_1, r1_1 = np.random.normal(0, sigma_scatter, 500), E + np.random.normal(0, sigma_scatter, 500)
    
    ax2.scatter(r0_0, r1_0, alpha=0.6, label='Tx = 0')
    ax2.scatter(r0_1, r1_1, alpha=0.6, label='Tx = 1')
    ax2.set_title("Scatter Muestras Ortogonales ($\sigma^2 = 0.5$)")
    ax2.set_xlabel("$r_0$")
    ax2.set_ylabel("$r_1$")
    ax2.legend()
    
    plt.tight_layout()

# --- PROBLEMA 9: Simulación Monte Carlo (Antipodal) ---
def problema_9():
    E = 1
    N_bits = 10000
    varianzas = [0.1, 0.5, 1.0]
    
    snr_db_teorico = np.linspace(-5, 10, 50)
    snr_lineal_teorico = 10**(snr_db_teorico / 10)
    pe_teorico = Q_funct(np.sqrt(2 * snr_lineal_teorico)) # Notar el factor de 2
    
    pe_simulado = []
    snr_db_simulado = []
    
    for var in varianzas:
        sigma = np.sqrt(var)
        snr_lineal = 1 / (2 * var)
        snr_db_simulado.append(10 * np.log10(snr_lineal))
        
        bits_tx = np.random.randint(0, 2, N_bits)
        errores = 0
        
        for bit in bits_tx:
            n = np.random.normal(0, sigma)
            r = E + n if bit == 0 else -E + n
                
            bit_rx = 0 if r > 0 else 1
            if bit_rx != bit:
                errores += 1
                
        pe_simulado.append(errores / N_bits)
        
    fig = plt.figure(figsize=(14, 6))
    fig.canvas.manager.set_window_title('Problema 9: Monte Carlo Antipodal')
    
    ax1 = fig.add_subplot(121)
    ax1.semilogy(snr_db_teorico, pe_teorico, label='Pe Teórico', color='cyan')
    ax1.semilogy(snr_db_simulado, pe_simulado, 's', label='Pe Simulado', color='magenta')
    ax1.set_title("BER vs SNR (Antipodal)")
    ax1.set_xlabel("SNR (dB)")
    ax1.set_ylabel("Probabilidad de Error (Pe)")
    ax1.legend()
    mplcyberpunk.add_glow_effects(ax1)
    
    ax2 = fig.add_subplot(122)
    sigma_scatter = np.sqrt(0.5)
    r_0 = E + np.random.normal(0, sigma_scatter, 500)
    r_1 = -E + np.random.normal(0, sigma_scatter, 500)
    
    # Gráfica unidimensional, y la hacemos jitter en Y para visibilidad
    ax2.scatter(r_0, np.random.uniform(-0.1, 0.1, 500), alpha=0.6, label='Tx = 0')
    ax2.scatter(r_1, np.random.uniform(-0.1, 0.1, 500), alpha=0.6, label='Tx = 1')
    ax2.axvline(0, color='white', linestyle='--', label='Umbral')
    ax2.set_title("Scatter Muestras Antipodales ($\sigma^2 = 0.5$)")
    ax2.set_xlabel("$r$")
    ax2.set_yticks([])
    ax2.legend()
    
    plt.tight_layout()

if __name__ == "__main__":
    problema_7()
    problema_8()
    problema_9()
    
    # Esto despliega todas las figuras generadas de manera independiente y bloquea el script hasta que las cierres
    plt.show()
