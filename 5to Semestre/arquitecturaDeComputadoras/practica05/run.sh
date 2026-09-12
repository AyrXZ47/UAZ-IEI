#!/usr/bin/env bash
# Compila + simula + abre las ondas.
# Uso: ./run.sh [testbench] [duracion]   ej: ./run.sh tb_circuito 2us
set -euo pipefail
TB="${1:-tb_circuito}"
DUR="${2:-400ns}"
SRC="$(ls *.vhd | grep -v '^tb_')"
ghdl -a --std=08 $SRC "$TB.vhd"
ghdl -e --std=08 "$TB"
ghdl -r --std=08 "$TB" --stop-time="$DUR" --vcd="$TB.vcd"
gtkwave "$TB.vcd" >/dev/null 2>&1 &
