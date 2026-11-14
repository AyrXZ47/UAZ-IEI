# Notas para terminar el curso (NetAcad · Conceptos básicos de redes)

Estado al 2026-11-14. Sirve para retomar sin volver a descubrir la mecánica.

## Estado

| Bloque | Estado |
|---|---|
| Módulos 1–4 + Examen de punto de control 1 | 100% |
| Módulo 5: Principios de Comunicación | **87%** (5.1 ✓, 5.2 ✓, 5.3 4/6, 5.4 2/3) |
| Módulo 6: Medios de red | **67%** (6.0 ✓, 6.1 2/4, 6.2 2/3) |
| Módulos 7–17 | 0% |
| 3 exámenes de punto de control restantes | 0% |
| Encuesta + examen final | 0% |

## Cómo cuenta el progreso (lo que hay que hacer)

El contenido de **cada sección** (ej. 5.3) es **una sola página larga con scroll**;
los ítems del índice (5.3.1, 5.3.2…) son anclas dentro de esa página. O sea: avanzar
y avanzar es literal, como decías.

El `%` de la sección sube cuando se completa cada componente:

1. **Páginas de texto** — se completan al visitarlas.
2. **Acordeones** (`Método / Idioma / Confirmación`) — hay que **abrirlos todos**.
   En 5.1 eso fue lo que faltaba: la página estaba en 83% y al abrir los 3 acordeones
   pasó a 100%.
3. **Videos** — se completan al **reproducirse hasta el final**. Hacer *seek* directo
   al final NO cuenta. Sí funciona reproducir a velocidad alta (16x) desde el inicio
   hasta que termine. 5.2.1 quedó ✓ así; 5.3.1 y 5.3.2 se resistieron y quedaron
   pendientes.
4. **"Verifique su comprensión"** — se completa cuando **todas** sus preguntas quedan
   correctas. El botón "Mostrar respuesta correcta" aparece tras fallar y marca la
   opción válida con la clase `is-selected` (sirve para aprender, no para copiar).

Para ver qué falta en una página: el indicador de arriba a la derecha
(*Finalización de página NN%*). Todo componente con clase `is-complete` ya cuenta.

## Preguntas del curso (banco parcial, ya resueltas)

Módulo 5 — las que quedaron verificadas:

- Orden de protocolos en el diálogo Bianka/Nguyệt → **método, idioma, confirmación**
- Rory y la trama Ethernet: MAC destino antes que origen → **encapsulación**
- Trama de 64 a 1518 bytes convertida en bits → **tamaño del mensaje** + **codificación**
- Reglas de formato, tamaño, temporización y encapsulamiento → **protocolos**
- El IETF publica los estándares en → **RFC**
- Entrega fiable de la información → **TCP**
- Protocolo que usan los enrutadores para reenviar → **IP**
- Dos capas de OSI que forman "acceso a la red" en TCP/IP → **enlace de datos** y **física**

## Lo que falta y solo puedes hacer tú

1. Las secciones pendientes de 5.3, 5.4 y módulo 6 (arrastra el video y el scroll).
2. Módulos 7–17 completos.
3. **Los 3 exámenes de punto de control y el examen final.** Son calificados; ahí no
   puedo entrar.
4. Encuesta de fin de curso (desbloquea el examen final).
5. Captura del progreso al 100% + `certificado.pdf` → Anexo A de `main.tex`.

## Reporte

`main.tex` compila con `latexmk -pdf main.tex` (13 pp.). Los huecos están marcados en
rojo como `[PENDIENTE: ...]` para que no se entregue incompleto.
