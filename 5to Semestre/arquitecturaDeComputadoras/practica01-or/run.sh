#!/usr/bin/env bash
# Compila + simula + abre las ondas. Uso: ./run.sh [testbench]
set -euo pipefail
TB="${1:-tb_comp_or}"
SRC="$(ls *.vhd | grep -v '^tb_')"
ghdl -a $SRC "$TB.vhd"
ghdl -e "$TB"
ghdl -r "$TB" --vcd="$TB.vcd"
gtkwave "$TB.vcd" >/dev/null 2>&1 &
