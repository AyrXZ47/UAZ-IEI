function h = leyenda(etiquetas, ubicacion)
% LEYENDA Leyenda con texto claro sobre el fondo oscuro.
h = legend(etiquetas, 'location', ubicacion);
set(h, 'textcolor', [0.910 0.910 0.910], 'box', 'off');
end
