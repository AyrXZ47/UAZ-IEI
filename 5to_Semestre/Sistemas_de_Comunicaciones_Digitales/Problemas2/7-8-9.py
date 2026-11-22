import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk

# Aplicar el estilo
plt.style.use("cyberpunk")

# =====================================================================
# Problema 7: Teorema del Límite Central
# =====================================================================
print("--- Ejecutando Problema 7 ---")
# 1. Vector de 1,000,000 componentes U(0,1)
X_7 = np.random.rand(1_000_000)

# 2. Promedio de cada 100 elementos consecutivos (Y tendrá longitud 10,000)
# Reshape divide el array en 10,000 filas de 100 columnas. mean(axis=1) promedia cada fila.
Y_7 = X_7.reshape(-1, 100).mean(axis=1)

# 3. Gráfica
fig7, ax7 = plt.subplots(figsize=(8, 5))
ax7.hist(Y_7, bins=40, density=True, color='cyan', alpha=0.7)
ax7.set_title('Problema 7: Teorema del Límite Central (40 bins)')
ax7.set_xlabel('Valor Promedio (Y)')
ax7.set_ylabel('Densidad')
mplcyberpunk.add_glow_effects(ax7)
plt.show()


# =====================================================================
# Problema 8: Estimación de Parámetros de Gaussiana Bivariada
# =====================================================================
print("\n--- Ejecutando Problema 8 ---")
m_teo = np.array([1, 2])
C_teo = np.array([[1, 0.5], [0.5, 1]])

# Generar 1000 pares
X_8 = np.random.multivariate_normal(m_teo, C_teo, 1000)
x1 = X_8[:, 0]
x2 = X_8[:, 1]

# 1. Determinar estadísticos de la muestra
m_hat_1 = np.mean(x1)
m_hat_2 = np.mean(x2)

# Usamos np.var y np.cov con ddof=0 para usar la misma fórmula del cuadernillo (dividido por 1000)
var_1 = np.var(x1, ddof=0)
var_2 = np.var(x2, ddof=0)
cov_12 = np.mean((x1 - m_hat_1) * (x2 - m_hat_2))

# 2. Comparar resultados
print("Resultados Teóricos vs Obtenidos (1000 muestras):")
print(f"Media 1:      Teórica = {m_teo[0]:.4f} | Muestra = {m_hat_1:.4f}")
print(f"Media 2:      Teórica = {m_teo[1]:.4f} | Muestra = {m_hat_2:.4f}")
print(f"Varianza 1:   Teórica = {C_teo[0,0]:.4f} | Muestra = {var_1:.4f}")
print(f"Varianza 2:   Teórica = {C_teo[1,1]:.4f} | Muestra = {var_2:.4f}")
print(f"Covarianza:   Teórica = {C_teo[0,1]:.4f} | Muestra = {cov_12:.4f}")

# 3. Gráfica de dispersión
fig8, ax8 = plt.subplots(figsize=(8, 6))
ax8.scatter(x1, x2, alpha=0.5, color='cyan', edgecolors='magenta', s=15)
ax8.set_title('Problema 8: Dispersión de Gaussiana Bivariada')
ax8.set_xlabel('Variable x1')
ax8.set_ylabel('Variable x2')
ax8.grid(True, linestyle='--', alpha=0.4)
mplcyberpunk.add_glow_effects(ax8)
plt.show()


# =====================================================================
# Problema 9: Estimación de la Media (P.I. 2.2 adaptado)
# =====================================================================
print("\n--- Ejecutando Problema 9 ---")
# Parámetros verdaderos
m_9 = 3
var_9 = 5
sigma_9 = np.sqrt(var_9)

N_muestras = 10
N_experimentos = 10
m_hats = np.zeros(N_experimentos)

# Ejecutar 10 experimentos
for i in range(N_experimentos):
    muestras = m_9 + sigma_9 * np.random.randn(N_muestras)
    m_hats[i] = np.mean(muestras)

# Valor medio global de las estimaciones
m_hat_global = np.mean(m_hats)

print(f"Verdadero valor medio de X: {m_9}")
print(f"Valor medio de las estimaciones (promedio de promedios): {m_hat_global:.4f}")

# Gráfica estilo "stem" como en el PDF
fig9, ax9 = plt.subplots(figsize=(10, 5))
marcadores, tallos, base = ax9.stem(range(1, 11), m_hats, basefmt=" ", linefmt='cyan', markerfmt='oc')
plt.setp(marcadores, markersize=8, markeredgecolor='magenta', markeredgewidth=2)

# Líneas de referencia
ax9.axhline(m_9, color='magenta', linestyle='-', lw=2, label='Media Verdadera (3)')
ax9.axhline(m_hat_global, color='yellow', linestyle='--', lw=2, label=f'Media Estimada ({m_hat_global:.2f})')

ax9.set_title('Problema 9: Estimaciones del Valor Medio')
ax9.set_xlabel('Número de Experimento')
ax9.set_ylabel('Valor Estimado de la Media')
ax9.set_ylim(0, 6)
ax9.set_xticks(range(1, 11))
ax9.legend()
mplcyberpunk.add_glow_effects(ax9)
plt.show()

