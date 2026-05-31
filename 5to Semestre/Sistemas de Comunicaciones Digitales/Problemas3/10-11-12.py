import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp
import mplcyberpunk

# Configurar el grid luminoso
plt.style.use("cyberpunk")

def Q_funct(x):
    return 0.5 * sp.erfc(x / np.sqrt(2))

# --- PROBLEMA 10: Señales On-Off (OOK) ---
def problema_10():
    E = 1 # Energía cuando está "On"
    N_bits = 10000
    varianzas = [0.1, 0.5, 1.0] 
    
    # Curva teórica
    snr_db_teorico = np.linspace(-5, 12, 50)
    snr_lineal_teorico = 10**(snr_db_teorico / 10)
    # Pe para OOK: Q(sqrt(E/(4*sigma^2))). SNR la definimos respecto a E/N0
    pe_teorico = Q_funct(np.sqrt(snr_lineal_teorico / 2))
    
    pe_simulado = []
    snr_db_simulado = []
    
    for var in varianzas:
        sigma = np.sqrt(var)
        snr_lineal = E / (2 * var)
        snr_db_simulado.append(10 * np.log10(snr_lineal))
        
        bits_tx = np.random.randint(0, 2, N_bits)
        errores = 0
        
        # Simulación vectorizada para mayor velocidad
        ruido = np.random.normal(0, sigma, N_bits)
        señal_tx = bits_tx * np.sqrt(E)  # 0 o sqrt(E)
        r = señal_tx + ruido
        
        umbral = np.sqrt(E) / 2
        bits_rx = (r > umbral).astype(int)
        
        errores = np.sum(bits_tx != bits_rx)
        pe_simulado.append(errores / N_bits)
        
    fig = plt.figure(figsize=(14, 6))
    fig.canvas.manager.set_window_title('Problema 10: Monte Carlo On-Off (OOK)')
    
    ax1 = fig.add_subplot(121)
    ax1.semilogy(snr_db_teorico, pe_teorico, label='Pe Teórico', color='cyan')
    ax1.semilogy(snr_db_simulado, pe_simulado, 's', label='Pe Simulado', color='magenta')
    ax1.set_title("BER vs SNR (On-Off Keying)")
    ax1.set_xlabel("SNR (dB)")
    ax1.set_ylabel("Probabilidad de Error (Pe)")
    ax1.legend()
    mplcyberpunk.add_glow_effects(ax1)
    
    ax2 = fig.add_subplot(122)
    sigma_scatter = np.sqrt(0.5)
    muestras = 500
    r_0 = np.random.normal(0, sigma_scatter, muestras)
    r_1 = np.sqrt(E) + np.random.normal(0, sigma_scatter, muestras)
    
    ax2.scatter(r_0, np.random.uniform(-0.1, 0.1, muestras), alpha=0.6, label='Tx = 0 (Off)', s=15)
    ax2.scatter(r_1, np.random.uniform(-0.1, 0.1, muestras), alpha=0.6, label='Tx = 1 (On)', s=15)
    ax2.axvline(np.sqrt(E)/2, color='white', linestyle='--', label='Umbral')
    ax2.set_title("Scatter Muestras OOK ($\sigma^2 = 0.5$)")
    ax2.set_xlabel("$r$")
    ax2.set_yticks([])
    ax2.legend()
    
    plt.tight_layout()

# --- PROBLEMA 11 y 12: Simulación M-PAM ---
def simular_MPAM(M, d, varianzas, N_simbolos, titulo_ventana, titulo_grafica):
    # Generar niveles: -(M-1)d, ..., -3d, -d, d, 3d, ..., (M-1)d
    niveles = np.arange(-(M-1), M, 2) * d
    
    # Para el cálculo teórico de SNR_s (Energía promedio por símbolo / N0)
    E_s = np.mean(niveles**2)
    
    snr_db_teorico = np.linspace(-5, 20, 50)
    snr_lineal_teorico = 10**(snr_db_teorico / 10)
    # P_s = 2(M-1)/M * Q(sqrt( 6*SNR_s / (M^2-1) ))
    factor = 2 * (M - 1) / M
    argumento_Q = np.sqrt((6 * snr_lineal_teorico) / (M**2 - 1))
    ps_teorico = factor * Q_funct(argumento_Q)
    
    ps_simulado = []
    snr_db_simulado = []
    
    for var in varianzas:
        sigma = np.sqrt(var)
        
        # Para simulación log, saltamos var=0 pero imprimiremos que es 0
        if var == 0:
            print(f"[{titulo_grafica}] Para varianza 0, el error simulado será 0.")
            continue
            
        N0 = 2 * var
        snr_lineal = E_s / N0
        snr_db_simulado.append(10 * np.log10(snr_lineal))
        
        simbolos_tx_idx = np.random.randint(0, M, N_simbolos)
        simbolos_tx = niveles[simbolos_tx_idx]
        ruido = np.random.normal(0, sigma, N_simbolos)
        r = simbolos_tx + ruido
        
        # Detector por mínima distancia Euclidiana
        diffs = np.abs(r[:, None] - niveles[None, :])
        simbolos_rx = niveles[np.argmin(diffs, axis=1)]
        
        errores = np.sum(simbolos_tx != simbolos_rx)
        ps_simulado.append(errores / N_simbolos)
        
    fig = plt.figure(figsize=(14, 6))
    fig.canvas.manager.set_window_title(titulo_ventana)
    
    ax1 = fig.add_subplot(121)
    ax1.semilogy(snr_db_teorico, ps_teorico, label='Ps Teórico', color='cyan')
    ax1.semilogy(snr_db_simulado, ps_simulado, 'x', label='Ps Simulado', color='magenta', markersize=8)
    ax1.set_title(f"SER vs SNR ({titulo_grafica})")
    ax1.set_xlabel("SNR por Símbolo ($E_s/N_0$ en dB)")
    ax1.set_ylabel("Probabilidad de Error (Ps)")
    ax1.legend()
    mplcyberpunk.add_glow_effects(ax1)
    
    # Gráfica de densidad para sigma^2 = 0.5 (1000 muestras solicitadas)
    ax2 = fig.add_subplot(122)
    muestras = 1000
    sigma_scatter = np.sqrt(0.5)
    
    # Generar símbolos uniformes y añadir ruido
    idx_scatter = np.random.randint(0, M, muestras)
    tx_scatter = niveles[idx_scatter]
    rx_scatter = tx_scatter + np.random.normal(0, sigma_scatter, muestras)
    
    # Colorear por nivel transmitido
    for nivel in niveles:
        mask = tx_scatter == nivel
        ax2.scatter(rx_scatter[mask], np.random.uniform(-0.1, 0.1, np.sum(mask)), alpha=0.7, s=15, label=f'Tx={nivel}')
        
    ax2.set_title(f"Scatter Muestras {titulo_grafica} ($\sigma^2 = 0.5$)")
    ax2.set_xlabel("Amplitud Recibida ($r$)")
    ax2.set_yticks([])
    
    # Ocultamos la leyenda si M=8 para no saturar la vista, o la ponemos afuera
    if M == 4:
        ax2.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=8)
    
    plt.tight_layout()

if __name__ == "__main__":
    # Ejecutamos las simulaciones
    problema_10()
    
    # Problema 11: 4-PAM, d=1 (niveles -3, -1, 1, 3), 10000 símbolos
    # Nota: El doc pide varianzas 0, 0.1, 0.5, 1.0. Para 0, no hay ruido, error = 0.
    simular_MPAM(M=4, d=1.0, varianzas=[0, 0.1, 0.5, 1.0], N_simbolos=10000, 
                 titulo_ventana='Problema 11: 4-PAM', titulo_grafica='4-PAM')
                 
    # Problema 12: 8-PAM, d=1 (niveles -7, -5, ..., 5, 7), 10000 símbolos
    simular_MPAM(M=8, d=1.0, varianzas=[0, 0.1, 0.5, 1.0], N_simbolos=10000, 
                 titulo_ventana='Problema 12: 8-PAM', titulo_grafica='8-PAM')
    
    # Desplegar en pantallas independientes
    plt.show()
