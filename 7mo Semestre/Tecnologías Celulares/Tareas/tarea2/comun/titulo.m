function titulo(texto)
% TITULO Titulo con el color del tema (Octave no hereda el color del eje).
t = title(texto);
set(t, 'color', [0.910 0.910 0.910], 'fontsize', 11);
end
