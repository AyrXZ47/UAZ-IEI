#!/usr/bin/env bash
# Compila los 12 reportes de las practicas de Tecnologias Celulares.
set -e

cd "$(dirname "$0")"
for i in $(seq 1 12); do
    printf 'practica%s: ' "$i"
    (cd "practica$i" && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex >/dev/null)
    printf 'ok\n'
done
