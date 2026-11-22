import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import scipy.integrate as integrate
import mplcyberpunk

# Configuración del entorno visual
plt.style.use("cyberpunk")

# --- PROBLEMAS 13 y 14: Funciones Auxiliares ---
def graficar_correlador_temporal(K, A, varianzas, tipo_senal, titulo_ventana):
    fig, axes = plt.subplots(3, 2, figsize=(14, 10))
    fig.canvas.manager.set_window_title(titulo_ventana)
    fig.suptitle(f"{titulo_ventana} - Evolución Temporal", fontsize=16, color="cyan")
    
    k_steps = np.arange(1, K + 1)
    s_base = np.ones(K) * A
    
    for idx, var in enumerate(varianzas):
        sigma = np.sqrt(var)
        
        # Simular Tx = 0
        n_0 = np.random.normal(0, sigma, K)
        if tipo_senal == 'antipodal':
            r_0 = s_base + n_0 # Para antipodal, s0 es +A (lógico 0)
            tit_0 = f"$\sigma^2={var}$ & $s_0$ (Tx=0)"
        else: # On-Off
            r_0 = 0 + n_0 # Para On-Off, Tx=0 es sin señal
            tit_0 = f"$\sigma^2={var}$ & (Tx=0)"
            
        y_0 = np.cumsum(r_0 * s_base)
        
        ax0 = axes[idx, 0]
        ax0.plot(k_steps, y_0, color='cyan')
        ax0.set_title(tit_0)
        ax0.set_xticks([0, int(K/4), int(K/2), int(3*K/4), K])
        ax0.set_xticklabels(['0', f'{int(K/4)}Tb', f'{int(K/2)}Tb', f'{int(3*K/4)}Tb', f'{K}Tb'])
        mplcyberpunk.add_glow_effects(ax0)
        
        # Simular Tx = 1
        n_1 = np.random.normal(0, sigma, K)
        if tipo_senal == 'antipodal':
            r_1 = -s_base + n_1 # s1 es -A (lógico 1)
            tit_1 = f"$\sigma^2={var}$ & $s_1$ (Tx=1)"
        else: # On-Off
            r_1 = s_base + n_1 # s1 es +A (lógico 1)
            tit_1 = f"$\sigma^2={var}$ & (Tx=1)"
            
        y_1 = np.cumsum(r_1 * s_base)
        
        ax1 = axes[idx, 1]
        ax1.plot(k_steps, y_1, color='magenta')
        ax1.set_title(tit_1)
        ax1.set_xticks([0, int(K/4), int(K/2), int(3*K/4), K])
        ax1.set_xticklabels(['0', f'{int(K/4)}Tb', f'{int(K/2)}Tb', f'{int(3*K/4)}Tb', f'{K}Tb'])
        mplcyberpunk.add_glow_effects(ax1)

    plt.tight_layout()

# --- PROBLEMA 15: Simulación M=4 Ortogonal ---
def teo_M_ortogonal_BER(snr_lineal_array, M):
    pe_array = []
    factor_bits = (M / 2) / (M - 1) # Mapeo de Ps a Pb
    
    for snr in snr_lineal_array:
        mean = np.sqrt(2 * snr)
        # Integral para cálculo exacto de Probabilidad de Símbolo Correcto (Pc)
        # Integrando la PDF de la Gaussiana multiplicada por CDFs
        f = lambda y: stats.norm.pdf(y, loc=mean, scale=1.0) * (stats.norm.cdf(y))**(M-1)
        Pc, _ = integrate.quad(f, -10, 20) # Rango suficiente para integrar a infinito
        Ps = 1.0 - Pc
        pe_array.append(Ps * factor_bits)
    return np.array(pe_array)

def problema_15():
    N_simbolos = 10000
    M = 4
    # Diccionario para mapear símbolo (0,1,2,3) a bits para contar errores exactos
    bit_map = {0: np.array([0,0]), 1: np.array([0,1]), 2: np.array([1,0]), 3: np.array([1,1])}
    
    varianzas = [0.1, 0.5, 1.0]
    E_s = 1.0 # Energía por símbolo normalizada
    
    snr_db_teorico = np.linspace(-5, 15, 50)
    snr_lineal_teorico = 10**(snr_db_teorico / 10)
    # En M-Ortogonal, típicamente la SNR del eje x es Eb/N0. Es = k * Eb
    # Como log2(4) = 2, Es/N0 = 2 * Eb/N0. Calcularemos usando Es/N0
    pb_teorico = teo_M_ortogonal_BER(snr_lineal_teorico, M)
    
    pb_simulado = []
    snr_db_simulado = []
    
    for var in varianzas:
        sigma = np.sqrt(var)
        N0 = 2 * var
        snr_lineal_es = E_s / N0
        # Guardaremos SNR en dB respecto a Eb/N0 (Es/N0 / 2) para alinear con convenciones
        snr_db_simulado.append(10 * np.log10(snr_lineal_es / 2))
        
        simbolos_tx = np.random.randint(0, M, N_simbolos)
        errores_bit = 0
        
        # Simulación vectorizada por símbolo
        for m in range(M):
            # Máscara de los símbolos que son 'm'
            idx = (simbolos_tx == m)
            num_m = np.sum(idx)
            if num_m == 0: continue
            
            # Generar ruido para las 4 dimensiones de estos símbolos
            ruido = np.random.normal(0, sigma, (num_m, M))
            
            # Matriz de recepción: Ruido en todo, Señal solo en la columna 'm'
            r = ruido
            r[:, m] += np.sqrt(E_s)
            
            # Decisión: índice de la dimensión con mayor valor
            simbolos_rx = np.argmax(r, axis=1)
            
            # Contar errores a nivel de bit
            for rx_sym in simbolos_rx:
                if rx_sym != m:
                    # Comparar array de bits (ej: [0,1] vs [1,1]) y sumar cantidad de errores
                    errores_bit += np.sum(bit_map[m] != bit_map[rx_sym])
                    
        total_bits = N_simbolos * 2
        pb_simulado.append(errores_bit / total_bits)

    fig, ax = plt.subplots(figsize=(10, 7))
    fig.canvas.manager.set_window_title('Problema 15: M=4 Ortogonal')
    
    # Eb/N0 en dB para el eje X
    ax.semilogy(10 * np.log10(snr_lineal_teorico / 2), pb_teorico, label='BER Teórico', color='cyan')
    ax.semilogy(snr_db_simulado, pb_simulado, 's', label='BER Simulado', color='magenta', markersize=8)
    
    ax.set_title("BER vs SNR ($E_b/N_0$) para M=4 Ortogonal", fontsize=16)
    ax.set_xlabel("Relación Señal a Ruido por Bit ($E_b/N_0$ en dB)")
    ax.set_ylabel("Probabilidad de Bit Erróneo (BER)")
    ax.legend()
    mplcyberpunk.add_glow_effects(ax)
    
    plt.tight_layout()

if __name__ == "__main__":
    # --- Ejecutar Problema 13 ---
    # Antipodal, K=20 muestras, Varianzas: 1, 2, 4
    graficar_correlador_temporal(K=20, A=1, varianzas=[1, 2, 4], 
                                 tipo_senal='antipodal', titulo_ventana='Problema 13: Antipodal ($\sigma^2=1,2,4$)')
    
    # --- Ejecutar Problema 14 ---
    # On-Off, K=30 muestras, Varianzas: 1, 2, 4
    graficar_correlador_temporal(K=30, A=1, varianzas=[1, 2, 4], 
                                 tipo_senal='on-off', titulo_ventana='Problema 14: On-Off ($\sigma^2=1,2,4$)')
    
    # --- Ejecutar Problema 15 ---
    # Monte Carlo M=4 Ortogonal
    problema_15()
    
    plt.show()
