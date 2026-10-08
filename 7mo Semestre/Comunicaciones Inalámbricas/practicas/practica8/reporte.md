# Práctica 8. Proyecto integrador: caracterización experimental de un canal inalámbrico

**Materia:** Comunicaciones Inalámbricas
**Equipo:** RTL-SDR (`RTL2832U` + `R820T`), antena, transmisor de referencia (LoRa 433 MHz / generador RF)
**Script:** [`practica8.py`](practica8.py) — orquesta las prácticas 2 a 7 y agrega el modelo integral.

> **Nota:** los resultados numéricos de este reporte provienen de la corrida de verificación
> `python3 practica8.py --sim` (datos sintéticos). La campaña real se ejecuta con
> `python3 practica8.py --real` y regenera automáticamente `datos/resumen.json`; al terminar,
> se actualizan las tablas de las secciones 6–11 con los valores medidos.

---

## 1. Resumen

Se caracterizó un canal inalámbrico en un entorno interior mediante una campaña que integra las seis actividades del curso: pérdidas por trayectoria, shadowing log-normal, desvanecimiento Rayleigh, efecto Doppler, selectividad en frecuencia y capacidad de canal. El modelo obtenido para el entorno de verificación es:

| Actividad | Resultado |
|---|---|
| Pérdidas por trayectoria | n = 3.06, R² = 0.989 |
| Shadowing | µ = −49.2 dB, σ = 5.52 dB |
| Rayleigh | σ_R = 0.707, 26.0 % de desvanecimientos profundos |
| Doppler | fD = 1.04 / 3.06 / 12.70 Hz (estático / lento / rápido); Tc = 0.41 / 0.14 / 0.03 s |
| Coherencia en frecuencia | Bc(0.5) ≈ 722 kHz (LOS) y 623 kHz (NLOS) |
| Capacidad | 1335 / 832 / 474 kbps (LOS / NLOS / lejano), B = 200 kHz |

## 2. Introducción

El desempeño de un sistema inalámbrico depende de las características del canal de propagación. Este proyecto construye un modelo experimental integral combinando los fenómenos estudiados durante el curso en un mismo escenario, siguiendo los procedimientos de las prácticas 2 a 7.

## 3. Marco teórico

- **Pérdidas por trayectoria:** $PL(d) = PL(d_0) + 10\,n\log_{10}(d/d_0) + X_\sigma$.
- **Shadowing:** $X_\sigma \sim \mathcal{N}(0,\sigma^2)$ en dB (variaciones lentas, de gran escala).
- **Rayleigh:** envolvente $r=|x|$ con pdf $f(r)=\frac{r}{\sigma^2}e^{-r^2/2\sigma^2}$ (sin trayectoria dominante).
- **Doppler:** $f_D = v/\lambda$; tiempo de coherencia $T_c \approx 0.423/f_D$.
- **Selectividad en frecuencia:** multitrayectoria $h(t)=\sum_i a_i e^{j\phi_i}\delta(t-\tau_i)$; RMS delay spread $\sigma_\tau$; ancho de banda de coherencia $B_c \approx 1/(5\sigma_\tau)$.
- **Capacidad:** $C = B\log_2(1+\gamma)$ (Shannon–Hartley).

## 4. Metodología

`practica8.py` ejecuta las prácticas 2 a 7 en orden (modo `--sim` o `--real`), cada una guarda sus mediciones y métricas en `practicaN/datos/`, y después agrega todo en `datos/resumen.json`. Cada actividad conserva su propio script y figuras; el proyecto no duplica el procesamiento.

Configuración común del receptor: RTL-SDR a la frecuencia del transmisor (433.9 MHz en la campaña prevista), `SampleRate = 2.4 MHz`, ganancia fija calibrada, captura asíncrona sin pérdida de muestras.

## 5. Escenario experimental

Entorno interior del edificio (pasillos, oficinas, laboratorios) con transmisor fijo y receptor desplazado a 1, 2, 5, 10, 15 y 20 m para la actividad 1; a 10 m fijos para shadowing y Rayleigh; con movilidad del receptor para Doppler. Se recomienda elaborar un plano simplificado del área con la ubicación del transmisor y los puntos de medición (producto del proyecto).

## 6. Resultados de pérdidas por trayectoria

![Path loss](../practica2/figs/pathloss.png)

| Distancia (m) | Potencia (dB) |
|---|---|
| 1 | −39.66 |
| 2 | −51.44 |
| 5 | −62.36 |
| 10 | −71.51 |
| 15 | −74.09 |
| 20 | −82.36 |

Ajuste: **n = 3.06**, R² = 0.989, residuos σ = 1.51 dB. Consistente con un entorno de interior/oficinas (3.0–5.0).

## 7. Resultados de shadowing

![Shadowing](../practica3/figs/histograma.png)

µ = −49.2 dB, σ = 5.52 dB (IC 95 %: 4.43–6.62 dB), N = 50, p-valor de normalidad 0.617 (no se rechaza la hipótesis normal). σ queda en el rango reportado para interiores (4–12 dB).

## 8. Resultados de fading Rayleigh

![Rayleigh](../practica4/figs/histograma_rayleigh.png)

σ del ajuste Rayleigh = 0.707, 26.0 % de muestras por debajo del umbral 0.5 (teórico 22.1 % con σ ideal). La diferencia se debe a la correlación temporal del registro simulado (pocos desvanecimientos independientes en la ventana); en la medición real se espera un valor cercano al teórico.

## 9. Resultados Doppler

![Doppler](../practica5/figs/doppler.png)

| Escenario | fD (Hz) | Tc (s) |
|---|---|---|
| Estático | 1.04 | 0.407 |
| Lento | 3.06 | 0.138 |
| Rápido | 12.70 | 0.033 |

El ensanchamiento crece con la velocidad y el tiempo de coherencia disminuye en la misma proporción (Tc = 0.423/fD). El escenario estático queda en el piso del estimador (~1 Hz) por la duración finita del registro.

## 10. Resultados de selectividad en frecuencia

![Selectividad](../practica6/figs/correlacion.png)

| Escenario | Potencia (dB) | Variación espectral (dB) | Bc 0.9 | Bc 0.5 |
|---|---|---|---|---|
| LOS | −2.48 | 1.28 | 1.2 kHz | 713.7 kHz |
| NLOS | 2.67 | 5.78 | 186.3 kHz | 621.1 kHz |

El escenario NLOS presenta mayor variación espectral (rizado de la PSD) que el LOS, evidencia de selectividad en frecuencia por multitrayectoria. El criterio estricto 0.9 es sensible al rizado del estimador de PSD; el criterio 0.5 es más estable.

## 11. Capacidad de canal

![Shannon](../practica7/figs/shannon.png)

| Escenario | Ps (dB) | Pn (dB) | SNR (dB) | C (kbps) |
|---|---|---|---|---|
| LOS | 0.04 | −20.00 | 20.05 | 1334.7 |
| NLOS | 0.26 | −12.02 | 12.28 | 832.4 |
| Lejano | 1.19 | −5.00 | 6.20 | 473.7 |

La capacidad cae al degradarse el enlace: la SNR pasa de 20 a 6 dB y la capacidad de 1.33 Mbps a 0.47 Mbps con B = 200 kHz.

## 12. Discusión

1. **Mecanismos observados:** la potencia decae con la distancia de forma consistente con un entorno interior (n ≈ 3), con fluctuaciones lentas (shadowing σ ≈ 5.5 dB) y rápidas (Rayleigh) debidas a obstáculos y multitrayectoria.
2. **Relación distancia–potencia:** cada duplicación de distancia cuesta 10·n·log10(2) ≈ 9.2 dB con n = 3.06.
3. **Impacto del entorno:** el NLOS reduce la SNR (~8 dB menos) y aumenta la variación espectral, reduciendo la capacidad.
4. **Movilidad:** el movimiento del receptor ensancha el espectro Doppler y reduce Tc, haciendo el canal más variable en el tiempo.
5. **Selectividad:** hay evidencia de rizado espectral en NLOS, aunque la señal de la fuente (no blanca) limita la precisión del método.
6. **Capacidad:** la capacidad experimental sigue la tendencia de Shannon y es coherente con las prácticas de fading: los escenarios con más pérdidas y obstáculos tienen menor SNR y menor capacidad.

## 13. Conclusiones

Se integró el modelo completo del canal: pérdidas por trayectoria con n = 3.06, shadowing log-normal con σ = 5.52 dB, desvanecimiento Rayleigh, ensanchamiento Doppler de 1.04 a 12.70 Hz con tiempos de coherencia de 0.41 a 0.03 s, ancho de banda de coherencia del orden de cientos de kHz y capacidad de 0.47 a 1.33 Mbps en 200 kHz. Los scripts de las prácticas 2–7 quedan listos para repetir la campaña con el transmisor real (`practica8.py --real`), momento en el cual este reporte se regenera con los valores medidos.

## 14. Referencias

- Rodríguez Abdalá, V. I. *Comunicaciones Inalámbricas: Manual de Prácticas*. UAZ, 2026.
- Rappaport, T. S. *Wireless Communications: Principles and Practice*. 2ª ed., Prentice Hall.
- Goldsmith, A. *Wireless Communications*. Cambridge University Press.
- Documentación de SciPy (`scipy.signal.welch`, `spectrogram`) y NumPy.
