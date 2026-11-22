import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import scipy.integrate as integrate
import mplcyberpunk

# Configuración del entorno de neón
plt.style.use("cyberpunk")

# --- PROBLEMA 17: Simulación Monte Carlo M=4 Ortogonal ---
def problema_17():
    M = 4
    N_simbolos = 10000
    varianzas = [0.1, 1.0, 2.0]
    E_s = 1.0
    
    # 1. Cálculo Teórico
    snr_db_teorico = np.linspace(-5, 15, 50)
    snr_lineal_teorico = 10**(snr_db_teorico / 10)
    
    ps_teorico = []
    for snr in snr_lineal_teorico:
        mean = np.sqrt(2 * snr)
        # Integración para probabilidad exacta
        f = lambda y: stats.norm.pdf(y, loc=mean, scale=1.0) * (stats.norm.cdf(y))**(M-1)
        Pc, _ = integrate.quad(f, -10, 20)
        ps_teorico.append(1.0 - Pc)
        
    ps_simulado = []
    snr_db_simulado = []
    
    # Preparamos los scatter plots (1000 muestras)
    fig_scatter, axes_scatter = plt.subplots(1, 3, figsize=(18, 5))
    fig_scatter.canvas.manager.set_window_title('Problema 17: Scatters M=4 Ortogonal')
    fig_scatter.suptitle("Muestras recibidas proyectadas en 2D (r0 vs r1)", fontsize=16, color="cyan")
    
    for idx, var in enumerate(varianzas):
        sigma = np.sqrt(var)
        N0 = 2 * var
        snr_lineal_es = E_s / N0
        snr_db_simulado.append(10 * np.log10(snr_lineal_es))
        
        simbolos_tx = np.random.randint(0, M, N_simbolos)
        ruido = np.random.normal(0, sigma, (N_simbolos, M))
        
        r = ruido.copy()
        # El canal añade la energía a la dimensión correcta (ortogonalidad)
        r[np.arange(N_simbolos), simbolos_tx] += np.sqrt(E_s)
        
        simbolos_rx = np.argmax(r, axis=1)
        errores = np.sum(simbolos_tx != simbolos_rx)
        ps_simulado.append(errores / N_simbolos)
        
        # Extracción para Scatter Plot
        muestras = min(1000, N_simbolos)
        mask_tx0 = (simbolos_tx[:muestras*4] == 0)
        r_tx0 = r[:muestras*4][mask_tx0][:muestras]
        
        mask_tx1 = (simbolos_tx[:muestras*4] == 1) 
        r_tx1 = r[:muestras*4][mask_tx1][:muestras]
        
        ax = axes_scatter[idx]
        if len(r_tx0) > 0:
            ax.scatter(r_tx0[:, 0], r_tx0[:, 1], alpha=0.5, label='Tx=s0', s=15, color='cyan')
        if len(r_tx1) > 0:
            ax.scatter(r_tx1[:, 0], r_tx1[:, 1], alpha=0.5, label='Tx=s1', s=15, color='magenta')
            
        ax.set_title(f"$\sigma^2 = {var}$")
        ax.set_xlabel("Correlador 0 ($r_0$)")
        ax.set_ylabel("Correlador 1 ($r_1$)")
        ax.legend()
        mplcyberpunk.add_glow_effects(ax)
        
    # Gráfica Principal de SER vs SNR
    fig_ser = plt.figure(figsize=(10, 6))
    fig_ser.canvas.manager.set_window_title('Problema 17: Curva de Error M=4 Ortogonal')
    ax_ser = fig_ser.add_subplot(111)
    
    ax_ser.semilogy(snr_db_teorico, ps_teorico, label='SER Teórico', color='cyan')
    ax_ser.semilogy(snr_db_simulado, ps_simulado, 's', label='SER Simulado', color='magenta', markersize=8)
    
    ax_ser.set_title("SER vs $E_s/N_0$ (M=4 Ortogonal)")
    ax_ser.set_xlabel("Relación Señal a Ruido por Símbolo (dB)")
    ax_ser.set_ylabel("Probabilidad de Símbolo Erróneo (Ps)")
    ax_ser.legend()
    mplcyberpunk.add_glow_effects(ax_ser)


# --- PROBLEMA 18: Correlador bajo Ruido Extremo (1, 2, 4) ---
def problema_18():
    varianzas = [1, 2, 4]
    K = 40
    k_steps = np.arange(1, K + 1)
    A = 1
    
    # Representación discreta de señales ortogonales con transiciones
    s0 = np.ones(K) * A
    s1 = np.concatenate((np.ones(K//2), -np.ones(K//2))) * A
    
    fig, axes = plt.subplots(3, 1, figsize=(10, 12))
    fig.canvas.manager.set_window_title('Problema 18: Correlador Ortogonal (Ruido Extremo)')
    fig.suptitle("Salida del Correlador para Señales Ortogonales (Transmitiendo s0)", fontsize=16, color="cyan")
    
    for idx, var in enumerate(varianzas):
        sigma = np.sqrt(var)
        n = np.random.normal(0, sigma, K)
        
        # Asumimos que se transmite s0 en un canal súper ruidoso
        r = s0 + n
        
        # Correlación en tiempo discreto iterativa
        y0 = np.cumsum(r * s0)
        y1 = np.cumsum(r * s1)
        
        ax = axes[idx]
        ax.plot(k_steps, y0, label='Correlador 0 (Alineado con s0)', color='cyan')
        ax.plot(k_steps, y1, label='Correlador 1 (Alineado con s1)', color='magenta', linestyle='--')
        
        ax.set_title(f"Degradación del Canal: Varianza del Ruido $\sigma^2 = {var}$")
        ax.set_xlabel("Muestra Discreta (k)")
        ax.set_ylabel("Energía Acumulada")
        ax.legend()
        mplcyberpunk.add_glow_effects(ax)

    plt.tight_layout()

if __name__ == "__main__":
    problema_17()
    problema_18()
    
    # Despliegue simultáneo de todo el análisis
    plt.show()
