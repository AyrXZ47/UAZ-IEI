# Arquitectura de Computadoras — flujo de trabajo (Linux, sin Active-HDL)

Este directorio tiene TODO lo necesario para la materia sin Windows ni Active-HDL.
El profe usa Active-HDL (simulación) + Vivado (FPGA); aquí el equivalente es
**GHDL + GTKWave** (simulación) + **Vivado** (síntesis/programar placas).

---

## El ciclo de una práctica (SIEMPRE el mismo)

```bash
# 1. crear el esqueleto (genera <nombre>.vhd y tb_<nombre>.vhd)
vhdlnew mux2x1

# 2. editar: <nombre>.vhd es el DISEÑO (la lógica, pocas líneas),
#    tb_<nombre>.vhd es el TESTBENCH (estímulos + asserts)
nvim mux2x1.vhd tb_mux2x1.vhd

# 3. compilar + simular + abrir ondas (correr DENTRO de la carpeta de la práctica)
vhdlrun tb_mux2x1

# 4. editar → vhdlrun → mirar ondas → repetir. Ese es todo el ciclo.
```

- `vhdlrun` compila TODOS los `*.vhd` que no empiecen con `tb_`, elabora, corre
  el testbench y abre GTKWave con las señales ya cargadas (genera un `.gtkw`).
- Los errores de GHDL dan **archivo:línea** exacto, como un compilador de C.
- `ghdl --ls` lista las unidades compiladas si te pierdes.

## Cómo leer las ondas de GTKWave (esto es la mitad de la materia)

- Cada señal es una **fila**; el eje horizontal es el **tiempo**.
- Los "rectángulos" SON las señales: la línea **arriba = 1**, **abajo = 0**.
  Un bus vectorial (ej. `SAL[3:0]`) se dibuja como un bus hex/binario: es el
  valor del vector en cada instante.
- En el demux de la práctica 02 verás el `1` de `A` **saltando de vía en vía**
  en `SAL` cada vez que `SEL` cambia. Eso ES un demux, visto en el tiempo.
- `U` = sin inicializar (por eso los testbench inicializan con `:=`), `X` = conflicto.
- `Ctrl+Shift+F` = zoom fit. Rueda del ratón = pan. Doble click en una señal
  del árbol SST (izquierda) = agregarla a las ondas.

## Estructura del testbench (lo que Active-HDL genera solo, aquí se entiende)

```vhdl
stim : process
begin
  SEL <= "00"; wait for 100 ns;              -- estimulo: nano-segundos a mano
  assert SAL = "0001" report "fallo en 00" severity failure;  -- verificacion
  ...
  wait;                                       -- fin de la simulacion
end process;
```

El assert hace que la simulación **falle sola** si el circuito está mal.
NO pongas asserts en un proceso aparte sensible a (A,B,S): carrera de deltas
compararía contra `S` viejo y fallaría espuriamente al arrancar con `S='U'`.

---

## Workspaces (por qué las ventanas no te estorban)

- `vhdlrun` y `guirun` abren la GUI en un **workspace nuevo consecutivo** sin
  robar el foco (si tienes 3 en uso, abre el 4; si hay 10, el 11).
- Las mismas apps lanzadas por rofi/a pelo caen al workspace fijo **guis**
  (red de seguridad; un windowrule no puede computar "siguiente libre").
- Si una app no cae en `guis`, su `class` no está en la regex: verla con
  `hyprctl clients` y agregarla en `hyprland-home.nix` (repo nixos-config).

---

## Vivado (AMD) — estado

- Instalado en `~/opt/Xilinx/2026.1` (63 GB, fuera del store, NO se borra con
  rebuilds ni con `bootstrap.sh` — solo formateando el disco).
- Se abre con `vivado` (terminal) o "Vivado 2026.1" en rofi; es la única app
  que importa (Tcl Shell = lo mismo sin GUI, Information Center = updater).
- **2026.1 exige licencia AL ARRANCAR** (cambio de 2026.1). Licencia gratuita:
  1. Entrar con tu cuenta AMD en https://licensing.amd.com
  2. Create New License → **Vivado Basic Tier License, Node-Locked**
  3. NIC ID = MAC de esta laptop: **d8:80:83:06:30:bf** (WiFi)
  4. Descargar el `Xilinx.lic` y copiarlo a `~/.Xilinx/`
  5. Listo: `vivado` abre. (Básico limita XSIM a Windows — no importa: la
     simulación aquí es GHDL; síntesis para Artix-7 está completa.)
- La PC necesita su propia licencia (otra cuenta AMD) o re-apuntar la misma
  con `vlm` (Vivado License Manager) — ver Hackster "AMD FPGA Tools 2026.1".
- Copia a otra máquina: `rsync -a ~/opt/Xilinx/ destino:~/opt/Xilinx/` +
  `rsync -a ~/.Xilinx/ destino:.Xilinx/` + rebuild con el flake.
- Para borrarlo algún día: `rm -rf ~/opt/Xilinx ~/.Xilinx` y
  `modules.apps.vivado.enable = false` en el repo. Cero residuo.

## De qué depende el repo y qué no (super-reproducibilidad)

- Declarativo (vive en el repo, sobrevive a todo): ghdl/iverilog/verilator/
  gtkwave, `vhdlnew`, `vhdlrun`, `guirun`, dark mode de logisim, el rc de
  GTKWave, el wrapper FHS de Vivado.
- No declarativo (AMD no permite redistribuirlo): `~/opt/Xilinx` y el token
  `~/.Xilinx/wi_authentication_key`. Tras un formateo: rsync de vuelta desde
  la PC, o re-instalar con `~/vivado-install.sh` (watchdog) + `~/vivado-auth.sh`.

## Materias/herramientas ya cubiertas en este repo

| Profe usa | Aquí |
|---|---|
| Active-HDL (simulación VHDL) | `ghdl` + `gtkwave` + tu editor |
| Vivado (síntesis, Basys3/Nexys4) | `vivado` (Artix-7 instalado) |
| Logisim | `logisim-evolution` (dark mode forzado) |
| SimulIDE | `simulide` (sin dark: upstream no soporta temas en 1.1.0) |
