import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import scipy.integrate as integrate
import scipy.special as sp
from scipy.interpolate import interp1d
import mplcyberpunk

# Neon vibes activados
plt.style.use("cyberpunk")

# --- FUNCIONES TEÓRICAS DE SER (Probabilidad de Error de Símbolo) ---

def Q_funct(x):
    return 0.5 * sp.erfc(x / np.sqrt(2))

def ser_m_pam(ebno_linear, M):
    k = np.log2(M)
    esno = k * ebno_linear
    arg = np.sqrt(6 * esno / (M**2 - 1))
    return 2 * (M - 1) / M * Q_funct(arg)

def ser_m_ortogonal(ebno_linear, M):
    k = np.log2(M)
    esno = k * ebno_linear
    mean = np.sqrt(2 * esno)
    # Integral exacta sobre la PDF y CDF de la Gaussiana
    f = lambda y: stats.norm.pdf(y) * (stats.norm.cdf(y + mean))**(M-1)
    Pc, _ = integrate.quad(f, -20, 20)
    return 1.0 - Pc

def ser_m_biortogonal(ebno_linear, M):
    k = np.log2(M)
    esno = k * ebno_linear
    mean = np.sqrt(2 * esno)
    
    def f(y):
        val = y + mean
        # phi(v) - phi(-v) asegura que estamos dentro de los límites antipodales
        cdf_term = stats.norm.cdf(val) - stats.norm.cdf(-val)
        if cdf_term < 0: cdf_term = 0
        return stats.norm.pdf(y) * (cdf_term)**((M/2) - 1)
        
    Pc, _ = integrate.quad(f, -mean, 20)
    return 1.0 - Pc

# --- RESOLUCIÓN DEL PROBLEMA 20 ---
def problema_20():
    M = 8
    target_ser = 1e-6
    
    ebno_db_rango = np.linspace(5, 22, 100)
    ebno_lin_rango = 10**(ebno_db_rango / 10)
    
    ser_pam = np.array([ser_m_pam(eb, M) for eb in ebno_lin_rango])
    ser_ort = np.array([ser_m_ortogonal(eb, M) for eb in ebno_lin_rango])
    ser_bio = np.array([ser_m_biortogonal(eb, M) for eb in ebno_lin_rango])
    
    # Interpolar para encontrar el valor exacto de dB requerido para SER = 10^-6
    # Usamos np.log10 en SER para estabilizar la interpolación numérica
    interp_pam = interp1d(np.log10(ser_pam), ebno_db_rango)
    interp_ort = interp1d(np.log10(ser_ort), ebno_db_rango)
    interp_bio = interp1d(np.log10(ser_bio), ebno_db_rango)
    
    db_pam = interp_pam(np.log10(target_ser))
    db_ort = interp_ort(np.log10(target_ser))
    db_bio = interp_bio(np.log10(target_ser))
    
    # Mostrar resultados numéricos en consola para la libreta
    print("="*50)
    print("RESULTADOS NUMÉRICOS PARA EL PROBLEMA 20")
    print(f"Eb/N0 requerido para alcanzar SER = {target_ser} (M={M}):")
    print(f"-> 8-PAM:          {db_pam:.2f} dB")
    print(f"-> 8-Biortogonal:  {db_bio:.2f} dB")
    print(f"-> 8-Ortogonal:    {db_ort:.2f} dB")
    print("="*50)

    # Graficar la comparativa
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.canvas.manager.set_window_title('Problema 20: Comparativa M=8')
    
    ax.semilogy(ebno_db_rango, ser_pam, label='8-PAM', color='cyan', linewidth=2)
    ax.semilogy(ebno_db_rango, ser_ort, label='8-Ortogonal', color='magenta', linewidth=2)
    ax.semilogy(ebno_db_rango, ser_bio, label='8-Biortogonal', color='yellow', linestyle='--', linewidth=2)
    
    # Línea objetivo
    ax.axhline(target_ser, color='white', linestyle=':', label=f'Objetivo ($10^{{-6}}$)')
    
    # Marcar los puntos exactos de intersección
    ax.scatter([db_pam, db_ort, db_bio], [target_ser, target_ser, target_ser], color='white', zorder=5, s=60)
    
    ax.set_title("Problema 20: Comparativa de Eficiencia Energética ($M=8$)", fontsize=16)
    ax.set_xlabel("Relación Energía por Bit a Ruido ($E_b/N_0$ en dB)")
    ax.set_ylabel("Probabilidad de Error de Símbolo (SER)")
    ax.set_ylim(1e-8, 1e-1)
    ax.set_xlim(5, 22)
    ax.legend(loc='upper right')
    
    mplcyberpunk.add_glow_effects(ax)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    problema_20()
