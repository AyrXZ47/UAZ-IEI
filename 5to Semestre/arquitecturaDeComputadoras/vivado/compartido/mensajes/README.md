# mensajes — Nexys4 DDR

Muestra un mensaje de 8 caracteres en los displays de 7 segmentos, elegido con
un switch:

| SW[0] | displays (izq → der) |
|-------|----------------------|
| 0     | `HOLAIEIS`           |
| 1     | `35167151`           |

`HOLAIEIS` = "Hola Ingeniería Electrónica Industrial Semiescolarizado".

Es el mismo flujo que `bcd_diferentes`: un prescaler refresca los 8 displays en
multiplexado. Lo único que cambia es la fuente de datos.

## Arquitectura

```
CLK100MHZ ─ pres_500hz ─ clk_pres ─ contador (3 bits) ─┬─ dec_an ────── AN(7:0)
                                                       └─ rom_mensajes ─ seg(7:0)
SW[0] ─────────────────────────────────────────────────── rom_mensajes.sel
```

`mux_datos` + `Dec_bcd_seg` se reemplazan por `rom_mensajes`, que guarda
directamente el patrón de 7 segmentos de cada carácter (16 posiciones:
2 mensajes × 8 displays). No hace falta decodificador BCD porque los patrones
ya están en la ROM.

`dir = 0` es AN0 (el display de la derecha), igual que en `dec_an`.

## Mapa de caracteres

`seg = {a,b,c,d,e,f,g,dp}`, activo bajo. El XDC asigna `seg[7]=CA` … `seg[0]=DP`.

| dir    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|--------|---|---|---|---|---|---|---|---|
| sel=0  | S | I | E | I | A | L | O | H |
| sel=1  | 1 | 5 | 1 | 7 | 6 | 1 | 5 | 3 |

## Construir

```bash
vivado -mode batch -source build.tcl
```

o abrir `mensajes.xpr` y generar el bitstream desde la GUI.
Bitstream: `mensajes.runs/impl_1/design_1_wrapper.bit`.

Para programar: Hardware Manager → Open Target → Auto Connect →
Program Device → `design_1_wrapper.bit`. `rst` es BTNC.

## Verificar la ROM (GHDL)

```bash
cd sim && ./run.sh
```

El testbench recorre los 16 caracteres y falla si algún patrón no coincide.
