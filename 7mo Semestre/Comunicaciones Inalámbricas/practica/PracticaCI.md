Universidad Autónoma de Zacatecas

“Francisco García Salinas”

Unidad Académica de Ingeniería Eléctrica

# Comunicaciones Inalámbricas Manual de Prácticas

Dr. Víktor Iván Rodríguez Abdalá

28 de septiembre de 2026


## Índice


## 1. Introducción

El presente manual tiene como propósito complementar los contenidos de la asignatura de Comunicaciones Inalámbricas mediante el desarrollo de actividades experimentales utilizando receptores de radio denido por software RTL-SDR y MATLAB.

Las prácticas permitirán observar fenómenos reales asociados con:

- Propagación inalámbrica.

- Atenuación por trayectoria.

- Shadowing.

- Desvanecimiento Rayleigh.

- Efecto Doppler.

- Canales selectivos en frecuencia.

- Capacidad de canal.

## 2. Objetivos Generales

- 1. Utilizar MATLAB para adquirir señales mediante receptores RTL-SDR.

- 2. Analizar señales inalámbricas reales.

- 3. Relacionar resultados experimentales con los modelos teóricos.

- 4. Aplicar técnicas de procesamiento digital de señales.

- 5. Caracterizar canales inalámbricos reales.

## 3. Equipo requerido

- Computadora personal.

- MATLAB.

- Communications Toolbox.

- Signal Processing Toolbox.

- Communications Toolbox Support Package for RTL-SDR Radio.

- Receptor RTL-SDR V4.

- Antena telescópica.


## 4. Configuración del RTL-SDR en MATLAB

Instalar el soporte RTL-SDR ejecutando:

supportPackageInstaller

Seleccionar:

Communications Toolbox Support Package for RTL-SDR Radio

Vericar el funcionamiento mediante:

Si la instalación es correcta, MATLAB mostrará la información del dispositivo conectado.

1

1


## 5. Práctica 1. Introducción al RTL-SDR y análisis espec- tral de señales inalámbricas

## 5.1. Objetivo General

Familiarizar al estudiante con el uso del receptor RTL-SDR desde MATLAB para la adquisición y análisis de señales inalámbricas reales.

## 5.2. Objetivos Específicos

- Congurar un receptor RTL-SDR.

- Adquirir muestras IQ.

- Visualizar las componentes I y Q.

- Obtener espectros mediante FFT.

- Estimar frecuencia central y ancho de banda.

## 5.3. Fundamento Teórico

Las muestras capturadas por el receptor SDR se representan como

donde:

- I[n] es la componente en fase.

- Q[n] es la componente en cuadratura.

El análisis espectral puede realizarse mediante la Transformada Discreta de Fourier

permitiendo determinar la distribución espectral de potencia.

## 5.4. Material y Equipo

- MATLAB.

- RTL-SDR.

- Antena.

- Computadora personal.


## 5.5. Procedimiento

## 5.5.1. Verificación del dispositivo

Ejecute:

```
info = sdrinfo(’RTL -SDR’)
```

1

Registre la información obtenida.

## 5.5.2. Configuración del receptor

Congure una estación FM comercial.

```
rx = comm.SDRRTLReceiver;
```

1

2

```
rx.CenterFrequency = 100.5 e6;
```

3

```
rx.SampleRate = 2.4e6;
```

4

```
rx.SamplesPerFrame = 4096;
```

5

```
rx.EnableTunerAGC = true;
```

6

## 5.5.3. Captura de muestras

```
[data ,len] = rx();
```

1

2

```
release(rx);
```

3

## Verique:

- Que len sea diferente de cero.

- Que data sea un vector complejo.

## 5.5.4. Visualización temporal

```
1 figure
2
3 subplot (2,1,1)
4 plot(real(data))
5 grid on
6 title(’Componente␣I’)
7
8 subplot (2,1,2)
9 plot(imag(data))
10 grid on
11 title(’Componente␣Q’)
```


## 5.5.5. Potencia recibida

```
P = mean(abs(data).^2);
```

1

2

```
Pdb = 10* log10(P);
```

3

Registre el valor obtenido.

## 5.5.6. Análisis espectral

```
1 Fs = rx.SampleRate;
2
3 N = length(data);
4
5 X = fftshift(fft(data));
6
7 f = linspace(-Fs/2,Fs/2,N);
8
9 PSD = 20* log10(abs(X));
10
11 figure
12 plot(f/1e6 ,PSD)
13
14 grid on
15
16 xlabel(’Frecuencia␣(MHz)’)
17 ylabel(’Magnitud␣(dB)’)
18
19 title(’Espectro␣de␣la␣senal ’)
```

## 5.5.7. Espectrograma

```
1 figure
2
3 spectrogram(data ,...
4 1024 ,...
5 512 ,...
6 1024 ,...
7 Fs ,...
8 ’centered ’)
9
10 title(’Espectrograma ’)
11 colorbar
```


## 5.6. Actividades

- 1. Identique una estación FM comercial.

- 2. Determine la frecuencia central observada.

- 3. Estime el ancho de banda.

- 4. Calcule la potencia promedio recibida.

- 5. Obtenga la FFT.

- 6. Obtenga el espectrograma.

## 5.7. Cuestionario

- 1. ¿Qué representan las componentes I y Q?

- 2. ¿Por qué se utilizan muestras complejas?

- 3. ¿Qué información proporciona la FFT?

- 4. ¿Qué diferencias observa entre el dominio temporal y frecuencial?

- 5. ¿Por qué es útil el espectrograma?

## 5.8. Entregables

- 1. Objetivo.

- 2. Desarrollo experimental.

- 3. Código MATLAB.

- 4. Grácas de I y Q.

- 5. FFT.

- 6. Espectrograma.

- 7. Respuestas al cuestionario.

- 8. Conclusiones.


## 6. Práctica 2. Medición experimental de pérdidas por tra- yectoria

## 6.1. Objetivo General

Caracterizar experimentalmente la atenuación de una señal inalámbrica en función de la distancia utilizando un receptor RTL-SDR y MATLAB, obteniendo el exponente de pérdidas por trayectoria del entorno analizado.

## 6.2. Objetivos Específicos

- Medir la potencia recibida a diferentes distancias.

- Construir la curva de pérdidas por trayectoria.

- Estimar el exponente de pérdidas del medio de propagación.

- Comparar resultados experimentales con el modelo teórico de propagación.

- Introducir al estudiante en la caracterización experimental de canales inalámbricos.

## 6.3. Introducción

La potencia de una señal inalámbrica disminuye conforme aumenta la distancia entre el transmisor y el receptor. Este fenómeno se conoce como pérdida por trayectoria (Path Loss) y constituye uno de los parámetros fundamentales para el diseño y análisis de sistemas de

comunicaciones inalámbricas.

En un entorno real la potencia recibida puede aproximarse mediante el modelo logarítmico

de propagación:

donde:

- PL(d) es la pérdida por trayectoria en dB.

- d es la distancia entre transmisor y receptor.

- d0 es la distancia de referencia.

- n es el exponente de pérdidas.

Los valores típicos de n son:


*Tabla 1: Valores típicos del exponente de pérdidas.*

| Entorno | n |
| --- | --- |
| Espacio libre | 2.0 |
| Exterior urbano | 2.7 - 3.5 |
| Interior ocinas | 3.0 - 5.0 |
| Interior con obstáculos 4.0 - 6.0 |   |

## 6.4. Fundamento Teórico

La potencia recibida puede estimarse a partir de las muestras IQ capturadas por el RTL-

SDR utilizando:

donde x[k] representa las muestras complejas recibidas.

En escala logarítmica:

La diferencia entre la potencia medida a distintas distancias permite estimar las pérdidas

por trayectoria.

## 6.5. Material y Equipo

- Computadora personal.

- MATLAB.

- RTL-SDR.

- Antena.

- Fuente transmisora estable.

## Opciones de transmisor

- Nodo LoRa.

- Generador RF.

- Beacon inalámbrico.

- Transmisor ISM de 433 MHz.

- Transmisor ISM de 915 MHz.


## 6.6. Escenario de Medición

Seleccione un entorno de medición:

- Pasillo del edicio E17-A.

- Segundo piso del edicio E17-A.

- Exteriores de la Unidad Académica.

Ubique el transmisor en una posición ja.

Realice mediciones para las siguientes distancias:

```
1 m, 2 m, 5 m, 10 m, 15 m y 20 m.
```

## 6.7. Procedimiento Experimental

## 6.7.1. Configuración del receptor

Congure el RTL-SDR a la frecuencia del transmisor.

```
rx = comm.SDRRTLReceiver;
```

1

2

```
rx.CenterFrequency = 915e6;
```

3

```
rx.SampleRate = 2.4e6;
```

4

```
rx.SamplesPerFrame = 4096;
```

5

```
rx.EnableTunerAGC = true;
```

6

## 6.7.2. Captura de muestras

Para cada distancia capture diez bloques de datos.

```
1 Nmed = 10;
2
3 Potencia = zeros(Nmed ,1);
4
5 for k = 1: Nmed
6
7 [data ,len] = rx();
8
9 Potencia(k) = mean(abs(data).^2);
10
11 end
12
13 release(rx);
```


## 6.7.3. Promedio de potencia

Obtenga la potencia promedio.

```
Pmean = mean(Potencia);
```

1

2

```
Pdb = 10* log10(Pmean);
```

3

Registre el valor obtenido para cada distancia.

## 6.8. Registro Experimental

Complete la siguiente tabla.

*Tabla 2: Datos experimentales.*

| Distancia (m) Potencia (dB) Observaciones |
| --- |
| 1 |
| 2 |
| 5 |
| 10 |
| 15 |
| 20 |

## 6.9. Procesamiento en MATLAB

Introduzca las mediciones obtenidas.

```
1 d = [1 2 5 10 15 20];
2
3 Pr = [ ];
4
5 figure
6
7 plot(d,Pr ,’o-’,’LineWidth ’ ,2)
8
9 grid on
10
11 xlabel(’Distancia␣(m)’)
12 ylabel(’Potencia␣recibida␣(dB)’)
13
14 title(’Potencia␣recibida␣versus␣distancia ’)
```

## 6.10. Estimación del Exponente de Pérdidas

Ajuste una recta utilizando mínimos cuadrados.


```
1 x = log10(d);
2
3 p = polyfit(x,Pr ,1);
4
5 n = -p(1) /10
```

El valor calculado corresponde a una estimación experimental del exponente de pérdidas.

## 6.11. Resultados Esperados

El estudiante deberá obtener:

- Curva de potencia recibida contra distancia.

- Estimación experimental del exponente de pérdidas.

- Comparación con valores teóricos.

- Análisis del entorno de propagación.

## 6.12. Análisis de Resultados

Discuta los siguientes aspectos:

- 1. ¿La potencia disminuye conforme aumenta la distancia?

- 2. ¿Cómo se compara el valor estimado de n con los valores reportados en la literatura?

- 3. ¿Qué efectos del entorno afectan las mediciones?

- 4. ¿Existen reexiones o bloqueos evidentes?

## 6.13. Cuestionario

- 1. ¿Qué representa físicamente el exponente de pérdidas?

- 2. ¿Por qué el valor de n cambia según el entorno?

- 3. ¿Qué diferencias existen entre espacio libre y un entorno interior?

- 4. ¿Por qué es necesario realizar múltiples mediciones en cada punto?

- 5. ¿Qué factores limitan la precisión del experimento?


## 6.14. Entregables

El reporte deberá incluir:

- 1. Objetivo.

- 2. Fundamento teórico.

- 3. Desarrollo experimental.

- 4. Código MATLAB utilizado.

- 5. Tabla de mediciones.

- 6. Gráca de potencia contra distancia.

- 7. Valor estimado del exponente de pérdidas.

- 8. Respuestas al cuestionario.

- 9. Conclusiones.


## 7. Práctica 3. Caracterización experimental del shado- wing log-normal

## 7.1. Objetivo General

Caracterizar las variaciones lentas de potencia presentes en un canal inalámbrico real mediante mediciones experimentales utilizando un receptor RTL-SDR y MATLAB.

## 7.2. Objetivos Específicos

- Medir la variabilidad espacial de la potencia recibida.

- Identicar el efecto de obstáculos sobre la propagación.

- Obtener la desviación estándar del shadowing.

- Vericar el comportamiento log-normal del canal.

- Complementar el modelo de pérdidas por trayectoria obtenido en la práctica anterior.

## 7.3. Introducción

Además de la pérdida media por trayectoria estudiada en la práctica anterior, las se- ñales inalámbricas experimentan uctuaciones de potencia causadas por edicios, paredes, mobiliario, vegetación y otros obstáculos presentes en el entorno.

Estas variaciones lentas reciben el nombre de shadowing o desvanecimiento de gran escala y suelen modelarse mediante una variable aleatoria gaussiana en dB:

donde:

- PL(d) representa la pérdida total.

- n es el exponente de pérdidas.

- Xσ representa una variable aleatoria gaussiana con media cero y desviación estándar σ.

La desviación estándar σ caracteriza la intensidad del shadowing presente en el escenario

analizado.


## 7.4. Fundamento Teórico

Si la pérdida media por trayectoria es removida de las mediciones experimentales, las uctuaciones residuales pueden aproximarse mediante una distribución normal:

Xσ ∼ N(0, σ2)

La desviación estándar de las mediciones se calcula mediante:

donde:

- xi son las mediciones en dB.

- µ es la media.

Valores típicos de σ son:

*Tabla 3: Valores típicos de shadowing.*

| Entorno | σ (dB) |
| --- | --- |
| Espacio libre | 2 – 4 |
| Exterior urbano | 6 – 10 |
| Interior ocinas | 4 – 12 |
| Entornos industriales 8 – 15 |   |

## 7.5. Material y Equipo

- Computadora personal.

- MATLAB.

- RTL-SDR.

- Antena.

- Fuente transmisora ja.

## 7.6. Escenario Experimental

Seleccione una distancia ja entre transmisor y receptor.

Se recomienda:

- 10 metros.


Mantenga constante la distancia durante toda la práctica.

Realice mediciones en diferentes posiciones cercanas al punto de recepción:

- Pasillo.

- Interior de ocina.

- Cerca de paredes.

- Cerca de puertas.

- Presencia y ausencia de personas.

El objetivo es modicar el entorno manteniendo aproximadamente la misma distancia al

transmisor.

## 7.7. Procedimiento Experimental

## 7.7.1. Configuración del receptor

Congure el RTL-SDR.

```
rx = comm.SDRRTLReceiver;
```

1

2

```
rx.CenterFrequency = 915e6;
```

3

```
rx.SampleRate = 2.4e6;
```

4

```
rx.SamplesPerFrame = 4096;
```

5

6

```
rx.EnableTunerAGC = true;
```

7

## 7.7.2. Adquisición de datos

Realice 50 mediciones independientes.

```
1 Nmed = 50;
2
3 Pr = zeros(Nmed ,1);
4
5 for k = 1: Nmed
6
7 [data ,len] = rx();
8
9 P = mean(abs(data).^2);
10
11 Pr(k) = 10* log10(P);
12
13 end
14
15 release(rx);
```


## 7.7.3. Análisis estadístico

Obtenga la media y desviación estándar.

```
1 mu = mean(Pr);
2
3 sigma = std(Pr);
```

Registre ambos valores.

## 7.8. Visualización de Resultados

Graque las mediciones obtenidas.

```
1 figure
2
3 plot(Pr ,’o-’)
4
5 grid on
6
7 xlabel(’Medicion ’)
8 ylabel(’Potencia␣(dB)’)
9
10 title(’Variacion␣de␣potencia␣recibida ’)
```

## 7.9. Histograma Experimental

Construya el histograma de las mediciones.

```
1 figure
2
3 histogram(Pr)
4
5 grid on
6
7 xlabel(’Potencia␣(dB)’)
8 ylabel(’Frecuencia ’)
9
10 title(’Histograma␣de␣potencia␣recibida ’)
```

## 7.10. Ajuste Gaussiano

Obtenga el ajuste estadístico.

```
1 pd = fitdist(Pr ,’Normal ’);
2
3 mu = pd.mu
4
5 sigma = pd.sigma
```


Graque la distribución ajustada.

```
1 figure
2
3 histogram(Pr ,...
4 ’Normalization ’,’pdf’)
5
6 hold on
7
8 x = linspace(min(Pr) ,...
9 max(Pr) ,100);
10
11 plot(x,...
12 pdf(pd ,x) ,...
13 ’LineWidth ’ ,2)
14
15 grid on
16
17 xlabel(’Potencia␣(dB)’)
18 ylabel(’Densidad ’)
19
20 title(’Modelo␣gaussiano␣del␣shadowing ’)
```

## 7.11. Registro Experimental

Complete la siguiente tabla.

|   | Tabla 4: Resultados obtenidos. |
| --- | --- |
| Parámetro | Valor |
| Media µ (dB) |   |
| Desviación estándar σ (dB) |   |
| Número de mediciones |   |
| Entorno evaluado |   |

## 7.12. Resultados Esperados

El estudiante deberá obtener:

- Variaciones de potencia debidas al entorno.

- Histograma de potencia recibida.

- Ajuste gaussiano de las mediciones.

- Valor experimental de σ.

- Modelo log-normal del shadowing.


## 7.13. Análisis de Resultados

## Discuta:

- 1. ¿Las mediciones presentan una distribución aproximadamente normal?

- 2. ¿Qué elementos del entorno afectan más la propagación?

- 3. ¿Cómo se compara el valor de σ con los valores reportados en la literatura?

- 4. ¿Qué diferencias existen entre pérdida por trayectoria y shadowing?

## 7.14. Cuestionario

- 1. ¿Qué es el shadowing?

- 2. ¿Qué diferencia existe entre fading de gran escala y fading de pequeña escala?

- 3. ¿Por qué el shadowing suele modelarse mediante una distribución log-normal?

- 4. ¿Qué representa físicamente la desviación estándar σ?

- 5. ¿Cómo afecta el entorno interior al valor de σ?

## 7.15. Entregables

- El reporte deberá incluir:

- 1. Objetivo.

- 2. Fundamento teórico.

- 3. Desarrollo experimental.

- 4. Código MATLAB utilizado.

- 5. Gráca de potencia versus medición.

- 6. Histograma experimental.

- 7. Ajuste gaussiano.

- 8. Valor obtenido de σ.

- 9. Respuestas al cuestionario.

- 10. Conclusiones.


## 8. Práctica 4. Caracterización experimental del desvane- cimiento Rayleigh

## 8.1. Objetivo General

Caracterizar experimentalmente el desvanecimiento de pequeña escala presente en un canal inalámbrico mediante el análisis estadístico de las amplitudes recibidas utilizando un receptor RTL-SDR y MATLAB.

## 8.2. Objetivos Específicos

- Observar uctuaciones rápidas de amplitud causadas por multitrayectoria.

- Analizar la envolvente de una señal recibida.

- Obtener el histograma de amplitudes.

- Vericar el ajuste de una distribución Rayleigh.

- Relacionar las mediciones experimentales con el modelo teórico de fading Rayleigh.

## 8.3. Introducción

En entornos inalámbricos urbanos e interiores, la señal transmitida llega al receptor por múltiples trayectorias debido a reexiones, difracciones y dispersión.

Cuando no existe una trayectoria dominante entre transmisor y receptor, la amplitud de la señal recibida puede modelarse mediante una distribución Rayleigh.

Este fenómeno es conocido como desvanecimiento Rayleigh y constituye uno de los mo- delos más utilizados para describir canales inalámbricos móviles.

## 8.4. Fundamento Teórico

La envolvente de una señal compleja puede obtenerse mediante

r[n] = x[n]

donde:

- x[n] representa las muestras IQ recibidas.

- r[n] representa la amplitud instantánea.

La función de densidad de probabilidad Rayleigh está dada por:

donde σ representa el parámetro de dispersión de la distribución.


## 8.5. Material y Equipo

- Computadora personal.

- MATLAB.

- RTL-SDR.

- Antena.

- Transmisor continuo de referencia.

## 8.6. Escenario Experimental

Ubique el transmisor en una posición ja. Durante la adquisición:

- Mantenga jo el transmisor.

- Desplace lentamente el receptor varios metros.

- Realice mediciones en un entorno interior.

- Procure la existencia de paredes, puertas y mobiliario.

El objetivo es provocar cambios en las trayectorias de propagación y observar las varia- ciones rápidas de amplitud.

## 8.7. Procedimiento Experimental

## 8.7.1. Configuración del receptor

Congure el RTL-SDR.

```
rx = comm.SDRRTLReceiver;
```

1

2

```
rx.CenterFrequency = 915e6;
```

3

```
rx.SampleRate = 2.4e6;
```

4

```
rx.SamplesPerFrame = 262144;
```

5

6

```
rx.EnableTunerAGC = true;
```

7

## 8.7.2. Captura de datos

Adquiera muestras IQ.

```
1 [data ,len] = rx();
2
3 release(rx);
```


## 8.7.3. Obtención de la envolvente

Calcule la amplitud instantánea.

```
r = abs(data);
```

1

## 8.7.4. Normalización

Normalice las amplitudes.

```
r = r./sqrt(mean(r.^2));
```

1

## 8.8. Visualización Temporal

Graque la envolvente obtenida.

```
1 figure
2
3 plot(r)
4
5 grid on
6
7 xlabel(’Muestra ’)
8 ylabel(’Amplitud ’)
9
10 title(’Envolvente␣de␣la␣senal␣recibida ’)
```

Identique regiones donde ocurran desvanecimientos profundos.

## 8.9. Histograma Experimental

Construya el histograma de amplitudes.

```
1 figure
2
3 histogram(r,...
4 ’Normalization ’,’pdf’)
5
6 grid on
7
8 xlabel(’Amplitud ’)
9 ylabel(’Densidad ’)
10
11 title(’Histograma␣experimental ’)
```


## 8.10. Ajuste de una Distribución Rayleigh

Obtenga el modelo estadístico utilizando MATLAB.

```
pd = fitdist(r,’Rayleigh ’);
```

1

Genere la comparación entre modelo y medición.

```
1 figure
2
3 histogram(r,...
4 ’Normalization ’,’pdf’)
5
6 hold on
7
8 x = linspace (0,max(r) ,200);
9
10 plot(x,...
11 pdf(pd ,x) ,...
12 ’LineWidth ’ ,2)
13
14 grid on
15
16 xlabel(’Amplitud ’)
17 ylabel(’Densidad ’)
18
19 title(’Ajuste␣Rayleigh ’)
20 legend(’Experimental ’ ,...
21 ’Modelo␣Rayleigh ’)
```

## 8.11. Nivel de Desvanecimiento

Determine la cantidad de muestras por debajo de un umbral.

```
1 umbral = 0.5;
2
3 Ndeep = sum(r < umbral);
4
5 Porcentaje = ...
6 100* Ndeep/length(r);
```

Registre el porcentaje de desvanecimientos profundos observados.

## 8.12. Registro Experimental

Complete la siguiente tabla.


## Tabla 5: Resultados obtenidos.

Parámetro

Frecuencia de operación Cantidad de muestras Media de amplitud Desviación estándar Porcentaje de fading profundo

Valor

## 8.13. Resultados Esperados

El estudiante deberá obtener:

- Variaciones rápidas de amplitud.

- Histograma experimental.

- Ajuste estadístico Rayleigh.

- Identicación de desvanecimientos profundos.

- Relación entre multitrayectoria y fading.

## 8.14. Análisis de Resultados

Discuta los siguientes aspectos:

- 1. ¿La envolvente presenta variaciones importantes de amplitud?

- 2. ¿El histograma obtenido se aproxima a una distribución Rayleigh?

- 3. ¿Qué fenómenos físicos originan los desvanecimientos?

- 4. ¿Cómo afecta el movimiento del receptor al comportamiento observado?

## 8.15. Cuestionario

- 1. ¿Qué es el desvanecimiento Rayleigh?

- 2. ¿Cuál es la diferencia entre shadowing y fading Rayleigh?

- 3. ¿Qué condiciones favorecen un canal Rayleigh?

- 4. ¿Qué es un desvanecimiento profundo?

- 5. ¿Cómo se relaciona la multitrayectoria con la distribución Rayleigh?

- 6. ¿Qué impacto tiene el fading Rayleigh en el desempeño de un sistema de comunicacio- nes?


## 8.16. Entregables

El reporte deberá incluir:

- 1. Objetivo.

- 2. Fundamento teórico.

- 3. Desarrollo experimental.

- 4. Código MATLAB utilizado.

- 5. Gráca de la envolvente temporal.

- 6. Histograma experimental.

- 7. Ajuste Rayleigh.

- 8. Análisis de los desvanecimientos observados.

- 9. Respuestas al cuestionario.

- 10. Conclusiones.


## 9. Práctica 5. Caracterización experimental del efecto Dop- pler y tiempo de coherencia

## 9.1. Objetivo General

Analizar experimentalmente el efecto Doppler en un canal inalámbrico móvil mediante la adquisición de señales utilizando un receptor RTL-SDR y MATLAB.

## 9.2. Objetivos Específicos

- Observar la variación temporal de un canal inalámbrico móvil.

- Estimar la frecuencia Doppler máxima.

- Analizar el espectro Doppler.

- Determinar el tiempo de coherencia del canal.

- Relacionar la movilidad con la variación temporal del canal.

## 9.3. Introducción

Cuando existe movimiento relativo entre transmisor y receptor, la frecuencia observada diere ligeramente de la frecuencia transmitida.

Este fenómeno se conoce como efecto Doppler y provoca variaciones temporales de am- plitud y fase en la señal recibida.

El efecto Doppler es uno de los principales mecanismos que originan canales variantes en

el tiempo.

## 9.4. Fundamento Teórico

La frecuencia Doppler máxima está dada por

donde

- v es la velocidad relativa.

- λ es la longitud de onda.

Considerando

se obtiene


El tiempo de coherencia puede aproximarse mediante

## 9.5. Material y Equipo

- Computadora personal.

- MATLAB.

- RTL-SDR.

- Antena.

- Transmisor continuo.

## 9.6. Escenario Experimental

Ubique el transmisor en una posición ja.

Realice mediciones en tres escenarios:

- 1. Receptor estacionario.

- 2. Receptor caminando lentamente.

- 3. Receptor caminando rápidamente.

Durante las mediciones mantenga la recepción continua.

## 9.7. Configuración del Receptor

```
1 rx = comm.SDRRTLReceiver;
2
3 rx.CenterFrequency = 915e6;
4
5 rx.SampleRate = 240e3;
6
7 rx.SamplesPerFrame = 262144;
8
9 rx.EnableTunerAGC = true;
```


## 9.8. Captura de Datos

```
[data ,len] = rx();
```

1

2

```
release(rx);
```

3

Obtenga la envolvente:

```
r = abs(data);
```

1

## 9.9. Variación Temporal

```
1 figure
2
3 plot(r)
4
5 grid on
6
7 xlabel(’Muestra ’)
8 ylabel(’Amplitud ’)
9
10 title(’Variacion␣temporal␣del␣canal ’)
```

Observe la rapidez con que cambia la amplitud conforme aumenta la velocidad.

## 9.10. Espectro Doppler

Obtenga la densidad espectral de potencia.

```
1 Fs = rx.SampleRate;
2
3 [PSD ,f] = pwelch( ...
4 data ,...
5 4096 ,...
6 2048 ,...
7 4096 ,...
8 Fs ,...
9 ’centered ’);
10
11 figure
12
13 plot(f,10* log10(PSD))
14
15 grid on
16
17 xlabel(’Frecuencia␣(Hz)’)
18 ylabel(’PSD␣(dB/Hz)’)
19
```


title(’Espectro␣Doppler ’)

20

## 9.11. Estimación de la Frecuencia Doppler

Mida aproximadamente el ancho del espectro Doppler y determine

fD

Registre el valor obtenido.

## 9.12. Estimación del Tiempo de Coherencia

Calcule:

donde fd corresponde a la frecuencia Doppler máxima estimada.

1

## 9.13. Registro Experimental

*Tabla 6: Resultados experimentales.*

Estático

Movimiento lento

Movimiento rápido

## 9.14. Resultados Esperados

- Variación temporal observable de la envolvente.

- Ensanchamiento Doppler.

- Estimación experimental de la frecuencia Doppler.

- Cálculo del tiempo de coherencia.

## 9.15. Análisis de Resultados

## Discuta:

- 1. ¿Cómo cambia el espectro Doppler con la velocidad?

- 2. ¿Qué relación existe entre velocidad y tiempo de coherencia?

- 3. ¿Qué implicaciones tiene un tiempo de coherencia pequeño?


## 9.16. Cuestionario

- 1. ¿Qué es el efecto Doppler?

- 2. ¿Qué parámetros determinan la frecuencia Doppler máxima?

- 3. ¿Qué representa el tiempo de coherencia?

- 4. ¿Por qué el tiempo de coherencia disminuye cuando aumenta la velocidad?

- 5. ¿Cómo afecta el Doppler a un sistema de comunicaciones inalámbricas?

## 9.17. Entregables

- 1. Objetivo.

- 2. Desarrollo experimental.

- 3. Código MATLAB.

- 4. Gráca temporal.

- 5. Espectro Doppler.

- 6. Estimación de fD.

- 7. Cálculo de Tc.

- 8. Respuestas al cuestionario.

- 9. Conclusiones.


## 10. Práctica 6. Caracterización experimental de canales selectivos en frecuencia

## 10.1. Objetivo General

Caracterizar experimentalmente un canal selectivo en frecuencia mediante el análisis de la respuesta espectral de una señal recibida utilizando un receptor RTL-SDR y MATLAB.

## 10.2. Objetivos Específicos

- Identicar los efectos de la multitrayectoria sobre una señal inalámbrica.

- Analizar la respuesta en frecuencia del canal.

- Estimar el ancho de banda de coherencia.

- Relacionar la dispersión temporal con la selectividad en frecuencia.

- Comparar canales no selectivos y selectivos en frecuencia.

## 10.3. Introducción

Cuando una señal se propaga a través de múltiples trayectorias, cada componente llega al receptor con diferente amplitud y retardo.

Si la dispersión temporal del canal es sucientemente grande, diferentes componentes espectrales de la señal experimentan ganancias distintas.

En estas condiciones el canal se denomina selectivo en frecuencia.

Este fenómeno constituye una de las principales causas de degradación en sistemas de banda ancha y es el motivo por el que técnicas como OFDM incorporan mecanismos de mitigación.

## 10.4. Fundamento Teórico

La respuesta impulsional de un canal multitrayectoria puede modelarse mediante

donde:

- ai es la amplitud de la trayectoria i.

- ϕi es la fase.

- τi es el retardo.


La respuesta en frecuencia se obtiene mediante

H(f) = Fh(t)

El ancho de banda de coherencia puede aproximarse mediante

donde στ corresponde al RMS Delay Spread.

## 10.5. Material y Equipo

- Computadora personal.

- MATLAB.

- RTL-SDR.

- Antena.

- Transmisor continuo en banda ISM.

## 10.6. Escenario Experimental

Seleccione un entorno interior con abundantes reectores:

- Pasillos.

- Ocinas.

- Laboratorios.

Realice mediciones en:

- 1. Línea de vista directa (LOS).

- 2. Sin línea de vista (NLOS).

## 10.7. Configuración del RTL-SDR

```
1 rx = comm.SDRRTLReceiver;
2
3 rx.CenterFrequency = 915e6;
4
5 rx.SampleRate = 2.4e6;
6
7 rx.SamplesPerFrame = 262144;
8
9 rx.EnableTunerAGC = true;
```


## 10.8. Captura de Datos

```
[data ,len] = rx();
```

1

2

```
release(rx);
```

3

## 10.9. Espectro de la Señal

```
1 Fs = rx.SampleRate;
2
3 N = length(data);
4
5 X = fftshift(fft(data));
6
7 f = linspace(-Fs/2,Fs/2,N);
8
9 figure
10
11 plot(f/1e6 ,...
12 20* log10(abs(X)))
13
14 grid on
15
16 xlabel(’Frecuencia␣(MHz)’)
17 ylabel(’Magnitud␣(dB)’)
18
19 title(’Respuesta␣espectral ’)
```

## 10.10. Variaciones Espectrales

Calcule una versión suavizada del espectro.

```
1 PSD = abs(X).^2;
2
3 PSD = PSD./max(PSD);
4
5 figure
6
7 plot(f/1e6 ,...
8 10* log10(PSD))
9
10 grid on
```

Observe regiones donde distintas componentes espectrales experimentan atenuaciones di-

ferentes.


## 10.11. Función de Correlación en Frecuencia

Obtenga una estimación simplicada.

```
1 R = xcorr(PSD ,’coeff ’);
2
3 figure
4
5 plot(R)
6
7 grid on
8
9 title(’Correlacion␣en␣frecuencia ’)
```

## 10.12. Estimación del Ancho de Banda de Coherencia

Determine experimentalmente el ancho de frecuencia para el cual la correlación permanece

por encima de:

0.9

o

0.5

según el criterio seleccionado.

Registre dicho valor como ancho de banda de coherencia.

## 10.13. Registro Experimental

*Tabla 7: Resultados experimentales.*

| Escenario | LOS NLOS |
| --- | --- |
| Potencia promedio (dB) |   |
| Variación espectral (dB) |   |
| Ancho de banda de coherencia |   |

## 10.14. Resultados Esperados

- Respuesta espectral del canal.

- Evidencia de selectividad en frecuencia.

- Comparación LOS y NLOS.

- Estimación del ancho de banda de coherencia.


## 10.15. Análisis de Resultados

## Discuta:

- 1. ¿El canal afecta todas las frecuencias por igual?

- 2. ¿Qué diferencias encuentra entre LOS y NLOS?

- 3. ¿Qué relación existe entre multitrayectoria y selectividad en frecuencia?

- 4. ¿Qué implicaciones tiene un ancho de banda de coherencia pequeño?

## 10.16. Cuestionario

- 1. ¿Qué es un canal selectivo en frecuencia?

- 2. ¿Qué es el RMS Delay Spread?

- 3. ¿Qué es el ancho de banda de coherencia?

- 4. ¿Cómo afecta la multitrayectoria a señales de banda ancha?

- 5. ¿Por qué OFDM es adecuado para estos canales?

## 10.17. Entregables

- 1. Objetivo.

- 2. Desarrollo experimental.

- 3. Código MATLAB.

- 4. Respuesta espectral.

- 5. Estimación de ancho de banda de coherencia.

- 6. Respuestas al cuestionario.

- 7. Conclusiones.


## 11. Práctica 7. Estimación experimental de la capacidad de canal

## 11.1. Objetivo General

Estimar experimentalmente la capacidad de un canal inalámbrico utilizando mediciones reales obtenidas mediante un receptor RTL-SDR y MATLAB.

## 11.2. Objetivos Específicos

- Medir la potencia de señal y ruido.

- Estimar la relación señal a ruido (SNR).

- Calcular la capacidad de Shannon.

- Analizar la inuencia de la SNR sobre la capacidad.

- Comparar diferentes escenarios de propagación.

## 11.3. Introducción

La capacidad de canal representa la máxima tasa de transmisión libre de errores que puede alcanzarse en un sistema de comunicaciones.

Para un canal AWGN, la capacidad está dada por el teorema de Shannon:

donde:

- C es la capacidad del canal (bps).

- B es el ancho de banda (Hz).

- γ es la SNR lineal.

En los sistemas inalámbricos la capacidad varía continuamente debido a los efectos de propagación estudiados en las prácticas anteriores.

## 11.4. Fundamento Teórico

La potencia promedio recibida puede estimarse mediante

La potencia de ruido puede obtenerse en una banda libre de señales:


La relación señal a ruido se calcula como

o en dB como

## 11.5. Material y Equipo

- Computadora personal.

- MATLAB.

- RTL-SDR.

- Antena.

- Fuente transmisora continua.

## 11.6. Escenario Experimental

Realice mediciones en tres escenarios:

- 1. Línea de vista directa (LOS).

- 2. Interior con obstáculos.

- 3. Distancia máxima posible dentro del área de medición.

## 11.7. Configuración del RTL-SDR

```
1 rx = comm.SDRRTLReceiver;
2
3 rx.CenterFrequency = 915e6;
4
5 rx.SampleRate = 2.4e6;
6
7 rx.SamplesPerFrame = 262144;
8
9 rx.EnableTunerAGC = true;
```


## 11.8. Captura de Señal

```
[data ,len] = rx();
```

1

2

```
release(rx);
```

3

## 11.9. Estimación de Potencia de Señal

```
Ps = mean(abs(data).^2);
```

1

2

```
Ps_dB = 10* log10(Ps);
```

3

Registre el valor obtenido.

## 11.10. Estimación de Potencia de Ruido

Seleccione una frecuencia cercana donde no exista transmisión.

Repita la captura:

```
1 [dataNoise ,len] = rx();
```

## Calcule:

```
Pn = mean(abs(dataNoise).^2);
```

1

2

```
Pn_dB = 10* log10(Pn);
```

3

## 11.11. Cálculo de la SNR

```
SNR = Ps/Pn;
```

1

2

```
SNR_dB = 10* log10(SNR);
```

3

## 11.12. Capacidad de Shannon

Considere inicialmente:

Calcule:

```
B = 200e3;
```

1

2

```
C = B*log2 (1+ SNR);
```

3


Obtenga el resultado en:

```
kbps
y
Mbps
```

## 11.13. Capacidad para Diferentes Valores de SNR

Genere la curva teórica:

```
1 snr_db = -10:30;
2
3 snr = 10.^( snr_db /10);
4
5 C = log2 (1+ snr);
6
7 figure
8
9 plot(snr_db ,C,...
10 ’LineWidth ’ ,2)
11
12 grid on
13
14 xlabel(’SNR␣(dB)’)
15 ylabel(’Capacidad␣(bps/Hz)’)
16
17 title(’Capacidad␣de␣Shannon ’)
```

Marque sobre la curva el punto correspondiente a la medición experimental.

## 11.14. Registro Experimental

*Tabla 8: Resultados experimentales.*

| Escenario | LOS NLOS Lejano |
| --- | --- |
| Potencia señal (dB) |   |
| Potencia ruido (dB) |   |
| SNR (dB) |   |
| Capacidad (kbps) |   |

## 11.15. Resultados Esperados

- Estimación de la SNR del canal.

- Capacidad experimental.


- Comparación entre distintos escenarios.

- Relación entre propagación y capacidad.

## 11.16. Análisis de Resultados

## Discuta:

- 1. ¿Cómo afecta la distancia a la capacidad?

- 2. ¿Qué impacto tienen los obstáculos?

- 3. ¿Existe relación entre los resultados de las prácticas de fading y la capacidad obtenida?

- 4. ¿Qué ocurriría si se duplicara el ancho de banda?

## 11.17. Cuestionario

- 1. ¿Qué representa la capacidad de Shannon?

- 2. ¿Por qué la capacidad aumenta con la SNR?

- 3. ¿Qué ocurre cuando la SNR es muy baja?

- 4. ¿Qué factores del canal afectan la capacidad?

- 5. ¿Por qué la capacidad real de un sistema suele ser menor que la capacidad teórica?

## 11.18. Entregables

- 1. Objetivo.

- 2. Fundamento teórico.

- 3. Desarrollo experimental.

- 4. Código MATLAB.

- 5. Cálculo de SNR.

- 6. Cálculo de capacidad.

- 7. Curva de Shannon.

- 8. Tabla de resultados.

- 9. Respuestas al cuestionario.

- 10. Conclusiones.


## 12. Práctica 8. Proyecto integrador: caracterización ex- perimental de un canal inalámbrico

## 12.1. Objetivo General

Caracterizar experimentalmente un canal inalámbrico real mediante mediciones realizadas con un receptor RTL-SDR y MATLAB, obteniendo un modelo completo de propagación para

el entorno analizado.

## 12.2. Objetivos Específicos

- Determinar las pérdidas por trayectoria del canal.

- Caracterizar el shadowing.

- Identicar la presencia de fading Rayleigh.

- Analizar el efecto Doppler bajo condiciones de movilidad.

- Estimar el ancho de banda de coherencia.

- Calcular la capacidad promedio del canal.

- Integrar todos los resultados obtenidos durante el curso.

## 12.3. Introducción

El desempeño de un sistema inalámbrico depende directamente de las características del canal de propagación.

En esta práctica se realizará una campaña de medición completa para obtener un modelo experimental del canal inalámbrico en un entorno real.

Los estudiantes deberán utilizar los procedimientos desarrollados en las prácticas anterio- res para construir una descripción integral del canal.

## 12.4. Escenario de Medición

El proyecto deberá desarrollarse en un área real. Ejemplos:

- Edicio E17-A.

- Pasillos de la Unidad Académica.

- Área exterior cercana a los edicios.

- Laboratorios.

Cada equipo deberá elaborar un plano simplicado del área evaluada.


## 12.5. Material y Equipo

- Computadora personal.

- MATLAB.

- RTL-SDR.

- Antena.

- Transmisor de referencia.

- Cinta métrica o distanciómetro.

## 12.6. Actividades

## 12.6.1. Actividad 1. Pérdidas por trayectoria

Realice mediciones de potencia para múltiples distancias.

Se recomienda considerar al menos:

Obtenga el modelo:

Determine experimentalmente:

n

## 12.6.2. Actividad 2. Shadowing

Para una distancia ja:

- Realice al menos 50 mediciones.

- Construya un histograma.

- Obtenga la desviación estándar.

Determine:

σ


## 12.6.3. Actividad 3. Fading Rayleigh

Adquiera muestras IQ con movimiento del receptor. Obtenga:

- Envolvente temporal.

- Histograma de amplitud.

- Ajuste Rayleigh.

Analice los desvanecimientos profundos.

## 12.6.4. Actividad 4. Efecto Doppler

Repita las mediciones anteriores bajo movilidad. Determine:

- Frecuencia Doppler máxima.

- Tiempo de coherencia.

## 12.7. Actividad 5. Selectividad en frecuencia

Obtenga la respuesta espectral del canal.

Determine:

- Variaciones espectrales.

- Ancho de banda de coherencia.

Compare un escenario LOS y un escenario NLOS.

## 12.8. Actividad 6. Capacidad de canal

Mida:

- Potencia de señal.

- Potencia de ruido.

Calcule:

y

para distintos escenarios.


## 12.9. Resultados Esperados

El proyecto deberá generar:

- 1. Curva de pérdidas por trayectoria.

- 2. Valor experimental del exponente de pérdidas.

- 3. Distribución log-normal del shadowing.

- 4. Distribución Rayleigh del fading.

- 5. Espectro Doppler.

- 6. Tiempo de coherencia.

- 7. Ancho de banda de coherencia.

- 8. Capacidad de canal.

## 12.10. Análisis de Resultados

## Discuta:

- 1. Principales mecanismos de propagación observados.

- 2. Relación entre distancia y potencia recibida.

- 3. Impacto del entorno sobre el shadowing.

- 4. Efecto de la movilidad sobre el canal.

- 5. Evidencia de selectividad en frecuencia.

- 6. Variación de la capacidad según el escenario.

## 12.11. Producto Final

Cada equipo deberá entregar:

- 1. Reporte técnico.

- 2. Base de datos de mediciones.

- 3. Scripts MATLAB desarrollados.

- 4. Plano del área caracterizada.

- 5. Presentación de resultados.


## 12.12. Estructura del Reporte

- 1. Resumen.

- 2. Introducción.

- 3. Marco teórico.

- 4. Metodología.

- 5. Escenario experimental.

- 6. Resultados de pérdidas por trayectoria.

- 7. Resultados de shadowing.

- 8. Resultados de fading Rayleigh.

- 9. Resultados Doppler.

- 10. Resultados de selectividad en frecuencia.

- 11. Capacidad de canal.

- 12. Discusión.

- 13. Conclusiones.

- 14. Referencias.

## 12.13. Criterios de Evaluación

*Tabla 9: Rúbrica de evaluación.*

| Concepto | Ponderación |
| --- | --- |
| Calidad de las mediciones | 20% |
| Procesamiento en MATLAB 20% |   |
| Análisis de resultados | 25% |
| Reporte técnico | 20% |
| Presentación nal | 15% |
