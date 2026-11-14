function guardar(f, ruta)
% GUARDAR Imprime la figura a PNG y la cierra.
print(f, ruta, '-dpng', '-r150');
close(f);
end
