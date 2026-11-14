#!/usr/bin/env bash
# Ejecuta los 11 problemas y compila el reporte de la tarea 2.
set -e

cd "$(dirname "$0")"
export QT_QPA_PLATFORM=offscreen

for f in problema*.m; do
    printf '%s: ' "$f"
    octave --no-gui --quiet "$f" >/dev/null 2>&1
    printf 'ok\n'
done

latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex >/dev/null
printf 'main.pdf: ok\n'
