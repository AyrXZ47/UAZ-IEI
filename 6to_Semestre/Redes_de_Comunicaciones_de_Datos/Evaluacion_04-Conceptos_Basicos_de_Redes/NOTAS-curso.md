# Notas para terminar el curso (NetAcad · Conceptos básicos de redes)

Estado al 2026-11-14. Los conteos por sección se leyeron del árbol de
accesibilidad (`completed` / `in progress` / `start` por leaf), que es la
fuente confiable.

## Estado por módulo

**Aviso: el % del módulo no es estable.** Dos recargas seguidas dan números
distintos para el mismo módulo (observado: M8 62% ↔ 49%, M12 66% ↔ 53%,
M13 62% ↔ 49%, M17 60% ↔ 77%). El player calcula el progreso con estado
parcialmente cargado, así que el porcentaje sirve como referencia gruesa,
no como medición. Los **conteos por sección (N/M)** y el **estado por leaf**
del árbol de accesibilidad son la fuente confiable.

Rango observado tras las recargas de esta sesión:

| Módulo | % observado |
|---|---|
| 1–4 + Examen de punto de control 1 | 100% (estable) |
| 5. Principios de Comunicación | 93% |
| 6. Medios de red | 72% |
| 7. La capa de acceso | 91% |
| 8. El Protocolo de Internet | 61% |
| 9. IPv4 y segmentación de redes | 63% |
| 10. Formatos y reglas de IPv6 | 87% |
| 11. Direccionamiento Dinámico con DHCP | 83% |
| 12. Puertas de enlace a otras redes | 66% |
| 13. El proceso ARP | 62% |
| 14. Enrutamiento Entre Redes | 79% |
| 15. TCP y UDP | 86% |
| 16. Servicios de la Capa de Aplicación | 76% |
| 17. Utilidades de prueba de red | 77% |

Los módulos 7–17 arrancaron en **0%** en esta sesión.

### Secciones que quedaron cerradas al 100% (N/N)

`5.3`, `8.2`, `10.1`, `11.1`, `12.1`, `14.2`, `15.2`, `16.2`, `16.3` y todas las
`x.0 Introducción`.

### Hueco restante por sección

| Sección | Falta | Qué es |
|---|---|---|
| `5.4` | 1 | Cuestionario |
| `6.1` | 1 | Verifique su comprensión |
| `6.2` | 1 | Cuestionario |
| `7.3` | 1 | Cuestionario |
| `8.1` | 2 | `8.1.1` adobe-animate + `8.1.3` lab PT |
| `8.3` | 1 | Prueba |
| `9.1` | 4 | 4 × adobe-animate / adobe-animate-ia |
| `9.2` | 3 | adobe-animate-ia |
| `9.3` | 1 | Cuestionario |
| `9.4` | 1 | Cuestionario |
| `10.2` | **cerrada 6/6** | actividad `ipv6addressrepresentation` resuelta |
| `10.3` | 1 | Cuestionario |
| `11.2` | 1 | `11.2.3` **lab PT** (Configurar DHCP en un Enrutador Inalámbrico) — no es cuestionario |
| `11.3` | 1 | Cuestionario |
| `12.2` | 1 | `12.2.2` lab PT (NAT) |
| `12.3` | 1 | Prueba |
| `13.1` | 2 | `13.1.3` lab PT + `13.1.4` Verifique su conocimiento |
| `13.2` | 2 | `13.2.5` adobe-animate + `13.2.6` check |
| `13.3` | 1 | Evaluación |
| `14.1` | 1 | Cuestionario |
| `14.3` | 2 | labs PT (14.3.3 y 14.3.4) |
| `14.4` | 1 | Cuestionario |
| `15.1` | 1 | `15.1.2` → componente `media` (video); sus MCQ están completas |
| `15.3` | 1 | Cuestionario |
| `16.1` | 1 | `16.1.5` **lab PT** (video de `16.1.1` ya cerrado) |
| `16.4` | 2 | `16.4.3` lab PT |
| `16.5` | 1 | `16.5.3` lab PT |
| `16.6` | 1 | `16.6.4` lab PT |
| `16.7` | 1 | `16.7.5` tiene sus 3 MCQ en `is-complete`; lo que falta es un **`adobe-animate`** dentro de la misma página |
| `16.8` | 1 | Cuestionario |
| `17.1` | 2 | `17.1.3` y `17.1.6` labs PT |
| `17.2` | 1 | Cuestionario |

Los labs de Packet Tracer coinciden exactamente con los `.pka` publicados en la
pestaña **Resources** del curso (16.1.5, 16.4.3, 16.5.3, 16.6.4, 17.1.3, 17.1.6,
14.3.3, 14.3.4, 12.2.2, 8.1.3, 13.1.3, 11.2.3…).

### Confirmado leaf por leaf (árbol de accesibilidad)

| Sección | Leaf pendiente | Causa |
|---|---|---|
| `5.4` | `5.4.3 Cuestionario de Principios de Comunicación` | examen |
| `6.2` | `6.2.3 Cuestionario de medios de red` | examen |
| `7.3` | `7.3.3 Cuestionario de la Capa de Acceso` | examen |
| `11.2` | `11.2.3 Packet Tracer - Configurar DHCP en un Enrutador Inalámbrico` | lab PT |
| `11.3` | `11.3.3 Prueba de Direccionamiento Dinámico con DHCP` | examen |
| `15.3` | `15.3.3 Evaluación de TCP y UDP` | examen |
| `17.2` | `17.2.3 Cuestionario de Utilidades de Prueba de Red` | examen |
| `9.3` | `9.3.5 Verifique su comprensión - Segmentación de red` | check trabado |
| `9.4` | `9.4.3 Evaluación de segmentación de red y IPv4` | examen |
| `10.3` | `10.3.3 Evaluación de Formatos y reglas de direccionamiento IPv6` | examen |
| `14.1` | `14.1.3 Compruebe su comprensión - La necesidad de enrutamiento` | **`adobe-animate`** (sus MCQ están completas) |
| `14.4` | `14.4.3 Prueba de Enrutamiento Entre Redes` | examen |
| `16.4` | `16.4.2 HTTP y HTML` y `16.4.3 Packet Tracer` | **`adobe-animate`** + lab PT (página al 33%, todo lo demás `done`) |
| `16.5` | `16.5.3 Packet Tracer - Usar Servicios FTP` | lab PT |
| `16.8` | `16.8.3 Servicios de capa de aplicación Examen` | examen |
| `16.7` | `16.7.5` (3 MCQ en `is-complete`) | **`adobe-animate` en la misma página** |

Con esto **todos** los huecos de los módulos 5–17 quedan clasificados: examen,
lab PT, `adobe-animate` o check trabado. No queda ninguno sin causa identificada.

## Estado de las preguntas: ojo con esto

Algunas páginas de "Verifique su comprensión" quedaron en un estado inconsistente:

- las opciones tienen `is-disabled` (no se pueden marcar),
- **no hay** botón "Reiniciar",
- y hay un único "Enviar" global, también deshabilitado.

Verificado en `13.2.6` y `6.1.4`, y **persiste tras recargar**. También se
observó con el componente `mcq` en `is-complete=false`.

Es probable que lo haya provocado mi propia automatización: al pulsar
"Mostrar respuesta correcta" y no reenviar, el componente queda con la
respuesta revelada pero sin control para reintentar.

**Recomendación:** si una de estas páginas no te deja contestar, ábrela en una
ventana distinta o cierra y vuelve a entrar al curso; si sigue igual, avísale al
instructor, porque es un estado del componente en la plataforma, no del avance.

## Cerrado en la última pasada

- **`10.2` → 6/6.** El leaf `10.2.6 Actividad - Representaciones de Direcciones IPv6`
  es una tabla de rellenar (componente `ipv6addressrepresentation`). Para
  `2001:0000:0db8:1111:0000:0000:0000:0200` la respuesta que la plataforma
  acepta es:
  - Omitir ceros: `2001` `0` `db8` `1111` `0` `0` `0` `200`
  - Comprimido: `2001::db8:1111::200`
  Tiene botones **Revisar**, **Reinicio** y **Muéstrame**; "Muéstrame" revela
  los valores esperados.
- **`16.1` → 4/5.** El media pendiente era el video de `16.1.1`; se cerró
  reproduciéndolo **a velocidad 1x desde `duration-2s`** (el seek directo al
  final y el 16x no siempre registran).
- **`15.1` → 2/2.** El media de 515 s se cerró igual: 1x desde `duration-3s` y
  sondeo hasta `ended`. El intento anterior había fallado porque se comprobó el
  componente antes de que el video estuviera renderizado.

## Páginas de MCQ bloqueadas (estado del servidor)

Solo **tres** quedaron realmente trabadas: `6.1.4`, `13.2.6` y `9.3.5` — con
opciones en `is-disabled`, sin "Reiniciar" y sin "Enviar" habilitado.

Se descartaron las causas del lado del cliente, en este orden:

1. **Recarga de página** → mismo estado.
2. **Pestaña nueva, sesión de browse distinta** → mismo estado.
3. **`localStorage` + `sessionStorage` vaciados** → mismo estado.
4. **Logout y login reales en NetAcad** (sesión cerrada de verdad con
   `openid-connect/logout`, y vuelta a entrar con usuario y contraseña) →
   **mismo estado**. Esta es la prueba concluyente: el bloqueo está en el xAPI
   del LMS contra el par (actividad, usuario), no en el navegador.
5. **Clic en "Reset and retake"** → no aplica: existe solo en
   *Prueba de mi conocimiento*, no en los checks de sección.

**Corrección importante:** `15.1.2` y `14.1.3` **no** están trabadas. Sus MCQ
tienen todas `is-complete`; lo que les falta es otra componente:

- `15.1.2` → `media` (video)
- `14.1.3` → `adobe-animate`

**Qué hacer:** las tres trabadas necesitan que el instructor reinicie el intento;
no se pueden arreglar desde el navegador.

## `adobe-animate`: descartado también por teclado

En `16.7.5` el componente contiene únicamente un `<canvas>` y divs de texto
para lectores de pantalla (`ID_txt01`, `ID_speech01`…, todos `tabindex=-1`).
Se enfocó el contenedor (`tabindex=0`) y se pulsaron Espacio, → y Enter:
el estado siguió en `open`. No hay control accionable.

Aparece también en `16.4.2 "HTTP y HTML"`, que **parece** página de contenido
pero tiene un `adobe-animate` dentro (página al 33% con todo lo demás `done`).
Y en `16.6` la página queda al 75% con todas las componentes tipadas en `done`
y solo envoltorios `?` abiertos: el ítem que falta es el lab PT `16.6.4`.

## Hallazgo clave: las preguntas multi-selección

El player **deshabilita "Enviar"** hasta que marcas el número exacto de opciones
que pide la pregunta (3 en los casos vistos). Comprobar que el botón *exista*
no sirve: hay que comprobar que **no** tenga la clase `is-disabled`.

Si se marca una sola casilla y se pulsa "Enviar", no pasa nada y el componente
queda `is-complete=false` para siempre, aunque parezca contestado.

Algoritmo correcto por pregunta:

1. Marcar opciones **de una en una**, releyendo el botón después de cada clic.
2. Cuando "Enviar" pierda `is-disabled`, pulsarlo.
3. Si sale "Reiniciar" → falló: pulsar "Mostrar respuesta correcta" (marca las
   válidas con `is-selected`), "Reiniciar", marcarlas, "Enviar" otra vez.

Con esto se cerraron `12.1` (4/4) y `8.2` (3/3), y subieron M8, M9, M10, M11,
M12, M16 y M17.

## Qué leaf queda pendiente, uno por uno

Enumerado del árbol de accesibilidad. Entre corchetes, la causa.

**Módulo 17**
- `17.1` 4/6 → **17.1.3** *Packet Tracer - Usar el Comando ipconfig* [lab PT]
  y **17.1.6** *Packet Tracer - Usar el Comando ping* [lab PT]
- `17.2` 2/3 → **17.2.3** *Cuestionario de Utilidades* [examen]

**Módulo 12**
- `12.1` **4/4 ✓** — cerrado al marcar las 3 opciones que pedía cada pregunta
- `12.2` 1/2 → **12.2.2** *Packet Tracer - Examinar NAT* [lab PT]
- `12.3` 2/3 → **12.3.3** *Prueba de puertas de enlace* [examen]

**Módulo 13**
- `13.1` 2/4 → **13.1.3** *Packet Tracer - Identificación de direcciones IP y MAC*
  [lab PT] y **13.1.4** *Verifique su conocimiento — MAC* [evaluación interna]
- `13.2` 4/6 → **13.2.5** *ARP* [página con adobe-animate] y **13.2.6**
  *Verifique su Comprensión - Contención de la Difusión* [check]
- `13.3` 2/3 → **13.3.3** *Evaluación del Proceso ARP* [examen]

**Módulo 8**
- `8.1` 1/3 → **8.1.1** *La Dirección IPv4* [adobe-animate] y **8.1.3**
  *Packet Tracer - Conectarse a un Servidor Web* [lab PT]
- `8.2` **3/3 ✓** — cerrado con el arreglo de multi-selección
- `8.3` 2/3 → **8.3.3** *Prueba de El Protocolo de Internet* [examen]

## Las cuatro causas (todas requieren intervención humana)

1. **Exámenes** (`Cuestionario`, `Prueba`, `Evaluación de…`). Al abrir uno:
   > Instrucciones: El examen consta de 11 preguntas y se requiere el 70% para aprobar.

2. **Labs de Packet Tracer** (`Packet Tracer - Usar el Comando ping`, etc.).
   Hay que abrir el `.pka` y realizar la actividad.

3. **`adobe-animate` / `adobe-animate-ia`.** Verificado: no tienen ni un control
   HTML; la interacción vive dentro del canvas de la animación.

4. **"Verifique su comprensión" que se quedan abiertos.** Verificado en `12.1.4`:
   sus 12 inputs MCQ existen, **todas** sus componentes están `is-complete`, y
   aun así el leaf sigue `in progress`. Contestar las preguntas no lo cierra.

### Lo que NO bloquea (comprobado)

- **`dynamic-graphic`**: `10.1` está 3/3 con un `dynamic-graphic` incompleto.
- **Componentes `?`** (envoltorios): aparecen abiertos incluso en secciones 100%.

## Cómo cuenta el progreso

Cada **sección** es una sola página larga con scroll; los ítems del índice
(`5.3.1`, `5.3.2`…) son anclas dentro de esa página. El `%` sube al completar:
texto/tablas (al visitarlas), acordeones (todos abiertos), videos (reproducidos
hasta el final; el *seek* al final no cuenta, a 16x sí), MCQ (respuesta correcta)
y el examen de cierre de sección.

### Trampas del player

1. **El número en pantalla sobreestima.** Hay que recargar para leer lo guardado;
   cayó hasta 13 puntos al recargar.
2. **Si una sección ya está expandida, clicar su encabezado la colapsa** y no se
   visitan sus páginas. Revisar `aria-expanded` antes de clicar.
3. **Expandir un módulo muestra `0 / N`** hasta que refresca: artefacto de
   render, no pérdida de progreso.
4. El botón del acordeón **no** recibe `is-expanded`; el estado está en `aria-expanded`.
5. `snapshot()` sin `find` se trunca y devuelve vacío en árboles grandes.

## Preguntas de comprensión resueltas

- Orden de protocolos, diálogo Bianka/Nguyệt → **método, idioma, confirmación**
- Rory y la trama Ethernet (MAC destino antes que origen) → **encapsulación**
- Trama de 64 a 1518 bytes convertida en bits → **tamaño del mensaje** + **codificación**
- Reglas de formato, tamaño, temporización y encapsulamiento → **protocolos**
- El IETF publica estándares en → **RFC**
- Entrega fiable de la información → **TCP**
- Protocolo que usan los enrutadores para reenviar → **IP**
- Dos capas de OSI que forman "acceso a la red" en TCP/IP → **enlace de datos** y **física**

## Lo que queda para ti

1. Los **exámenes** de cierre de sección (Cuestionario / Prueba / Evaluación).
2. Los **labs de Packet Tracer** listados arriba.
3. Las actividades **adobe-animate** pendientes.
4. Los **4 exámenes de punto de control**.
5. **Encuesta de fin de curso** → desbloquea el **examen final**.
6. Captura al 100% + `certificado.pdf` → Anexo A de `main.tex`.

## Reporte

`main.tex` compila con `latexmk -pdf main.tex` (13 pp.). Huecos en rojo como
`[PENDIENTE: ...]`.
