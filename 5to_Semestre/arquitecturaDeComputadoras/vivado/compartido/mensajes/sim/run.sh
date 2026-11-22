#!/usr/bin/env bash
# Simula la ROM de mensajes con GHDL y abre las ondas.
# Uso: ./run.sh
set -euo pipefail
cd "$(dirname "$0")"

SRC="../mensajes.srcs/sources_1/new/rom_mensajes.vhd"

ghdl -a --std=93 "$SRC" tb_rom_mensajes.vhd
ghdl -e --std=93 tb_rom_mensajes
ghdl -r --std=93 tb_rom_mensajes --vcd=tb_rom_mensajes.vcd
gtkwave tb_rom_mensajes.vcd >/dev/null 2>&1 &
