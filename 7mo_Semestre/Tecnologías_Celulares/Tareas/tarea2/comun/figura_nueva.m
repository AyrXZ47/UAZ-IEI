function f = figura_nueva(ancho, alto)
% FIGURA_NUEVA Crea una figura con el tema oscuro del curso.
f = figure('visible', 'off', 'position', [0 0 ancho alto], ...
           'color', [0.129 0.161 0.275]);
set(f, 'inverthardcopy', 'off');   % conserva el fondo oscuro al imprimir
panel();
end
