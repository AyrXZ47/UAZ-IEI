import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk

# Aplicar el estilo
plt.style.use("cyberpunk")

def estimar_autocorrelacion(x, M):
    """Calcula la autocorrelación de x hasta el lag M."""
    N = len(x)
    Rx = np.zeros(M + 1)
    for m in range(M + 1):
        Rx[m] = np.sum(x[:N-m] * x[m:]) / (N - m)
    return Rx

# =====================================================================
# Problema 16: Filtrado Lineal Discreto
# =====================================================================
print("Calculando Problema 16...")
N_16 = 1000
M_16 = 50

x_16 = np.random.rand(N_16) - 0.5  # Uniforme en [-1/2, 1/2]
y_16 = np.zeros(N_16)

# Filtrado recursivo
y_16[0] = x_16[0]
for n in range(1, N_16):
    y_16[n] = 0.95 * y_16[n-1] + x_16[n]

# Autocorrelaciones
Rx_16 = estimar_autocorrelacion(x_16, M_16)
Ry_16 = estimar_autocorrelacion(y_16, M_16)

# Espectros de Potencia
Sx_16 = np.fft.fftshift(np.abs(np.fft.fft(Rx_16, n=256)))
Sy_16 = np.fft.fftshift(np.abs(np.fft.fft(Ry_16, n=256)))
f_16 = np.linspace(-0.5, 0.5, 256)

fig16, ax16 = plt.subplots(1, 2, figsize=(14, 5))
fig16.suptitle('Problema 16: Autocorrelación y Espectro de Potencia')

ax16[0].plot(range(M_16 + 1), Ry_16, color='cyan')
ax16[0].set_title('Autocorrelación $R_y(m)$')
ax16[0].set_xlabel('Lag m')

ax16[1].plot(f_16, Sy_16, color='magenta')
ax16[1].set_title('Espectro de Potencia $S_y(f)$')
ax16[1].set_xlabel('Frecuencia f')

mplcyberpunk.add_glow_effects(ax16[0])
mplcyberpunk.add_glow_effects(ax16[1])
plt.show()

# =====================================================================
# Problema 17: Proceso Aleatorio Pasabanda
# =====================================================================
print("Calculando Problema 17...")
N_17 = 1000
M_17 = 10

# Ruido blanco para componentes en fase y cuadratura
w_c = np.random.rand(N_17) - 0.5
w_s = np.random.rand(N_17) - 0.5

x_c = np.zeros(N_17)
x_s = np.zeros(N_17)

# Filtrado pasabajas
x_c[0], x_s[0] = w_c[0], w_s[0]
for n in range(1, N_17):
    x_c[n] = 0.5 * x_c[n-1] + w_c[n]
    x_s[n] = 0.5 * x_s[n-1] + w_s[n]

# Formación de la señal pasabanda
n_arr = np.arange(N_17)
x_bp = x_c * np.cos(np.pi / 2 * n_arr) - x_s * np.sin(np.pi / 2 * n_arr)

# Autocorrelaciones
Rc = estimar_autocorrelacion(x_c, M_17)
Rs = estimar_autocorrelacion(x_s, M_17)
R_bp = estimar_autocorrelacion(x_bp, M_17)

fig17, ax17 = plt.subplots(1, 2, figsize=(14, 5))
fig17.suptitle('Problema 17: Proceso Pasabanda')

ax17[0].plot(range(M_17 + 1), Rc, label='$R_c(m)$', color='cyan')
ax17[0].plot(range(M_17 + 1), Rs, label='$R_s(m)$', color='yellow', linestyle='--')
ax17[0].set_title('Autocorrelaciones Pasabajas')
ax17[0].legend()

ax17[1].plot(range(M_17 + 1), R_bp, color='magenta')
ax17[1].set_title('Autocorrelación Señal Pasabanda $R_x(m)$')

mplcyberpunk.add_glow_effects(ax17[0])
mplcyberpunk.add_glow_effects(ax17[1])
plt.show()

# =====================================================================
# Problema 18: Simulación Monte Carlo
# =====================================================================
print("\n--- Ejecutando Problema 18: Monte Carlo ---")
m_val = 3
N_mc = 10000  # Número de muestras (mayor a 10/P(m) para asegurar convergencia)
num_experimentos = 5
prob_verdadera = 1.35e-3

estimaciones = []

print(f"Probabilidad Verdadera P({m_val}) = {prob_verdadera}")
for i in range(num_experimentos):
    # Generar Y = m + G (G es N(0,1))
    Y = m_val + np.random.randn(N_mc)
    
    # Contar eventos Y < 0
    errores = np.sum(Y < 0)
    P_est = errores / N_mc
    estimaciones.append(P_est)
    
    print(f"Experimento {i+1}: {errores} muestras < 0 -> Estimación P(3) = {P_est:.5f}")

print(f"-> Promedio de las 5 estimaciones: {np.mean(estimaciones):.5f}")
print("-> Comentario: Las estimaciones varían ligeramente en cada corrida debido a la naturaleza estocástica del proceso, pero el promedio converge cerca del valor teórico. Para reducir la varianza entre estimaciones, se requeriría aumentar la cantidad de muestras N.")

# Visualización para el Problema 18
fig18, ax18 = plt.subplots(figsize=(10, 5))
ax18.bar(range(1, num_experimentos + 1), estimaciones, color='cyan', label='Estimaciones MC')
ax18.axhline(y=prob_verdadera, color='magenta', linestyle='--', label='Valor Teórico (1.35e-3)')
ax18.set_title('Problema 18: Simulación Monte Carlo para $P(Y < 0)$')
ax18.set_xlabel('Número de Experimento')
ax18.set_ylabel('Probabilidad Estimada')
ax18.legend()

mplcyberpunk.add_glow_effects(ax18)
plt.show()

