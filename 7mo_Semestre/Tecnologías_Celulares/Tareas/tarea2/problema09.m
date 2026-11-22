% Problema 9: seleccion de frecuencia en un sistema FH/FSK ortogonal binario.
% Un LFSR de m = 7 estados (L = 127) elige una de N = 127 bandas; cada banda
% contiene dos tonos FSK separados y sin traslape. Se muestra el patron de
% los primeros 10 intervalos de bit.
clear; clc;
base = fileparts(mfilename('fullpath'));
addpath(fullfile(base, 'comun'));

m = 7;
taps = [7 3];               % x^7 + x^3 + 1
L = 2^m - 1;
Nbandas = L;
f0 = 900;                   % MHz
df = 0.025;                 % separacion entre bandas (MHz)
dt = df / 4;                % tonos a +-df/4 del centro

estado = [1 0 1 0 1 0 1];   % estado inicial no nulo
retro = [1, taps(taps < m) + 1];
for k = 1:40                % calentamiento
    estado = [estado(2:m), mod(sum(estado(retro)), 2)];
end

hops = 10;
banda = zeros(1, hops);
estados = zeros(hops, m);
for k = 1:hops
    estados(k, :) = estado;
    banda(k) = bin2dec(sprintf('%d', estado)) + 1;
    estado = [estado(2:m), mod(sum(estado(retro)), 2)];
end

fc = f0 + (banda - 1) * df;
f1 = fc - dt;
f2 = fc + dt;

printf('bandas: %s\n', mat2str(banda));
printf('centros (MHz): %s\n', mat2str(fc, 6));

c = colores();
f = figura_nueva(880, 820);
subplot(3, 1, 1);
panel();
stem(1:hops, banda, 'filled', 'color', c(1,:), 'markerfacecolor', c(1,:), ...
     'markersize', 6, 'linewidth', 1.4);
xlim([0.5 hops + 0.5]); ylim([0 Nbandas + 5]);
xlabel('intervalo de bit'); ylabel('banda seleccionada');
titulo('Patrón de selección de frecuencia (primeros 10 bits)');

subplot(3, 1, 2);
panel();
for k = 1:hops
    line([k - 1, k], [fc(k), fc(k)], 'color', c(1,:), 'linewidth', 5);
end
xlim([0 hops]); ylim([f0 - df, f0 + Nbandas * df]);
xlabel('intervalo de bit'); ylabel('frecuencia (MHz)');
titulo('Salto de frecuencia: una banda distinta por intervalo');

subplot(3, 1, 3);
panel();
k = 1;
stem(f1(k), 1, 'filled', 'color', c(1,:), 'markerfacecolor', c(1,:), ...
     'markersize', 6, 'linewidth', 1.8);
stem(f2(k), 1, 'filled', 'color', c(2,:), 'markerfacecolor', c(2,:), ...
     'markersize', 6, 'linewidth', 1.8);
plot([fc(k) - df/2, fc(k) - df/2], [0 1.2], ':', 'color', c(6,:));
plot([fc(k) + df/2, fc(k) + df/2], [0 1.2], ':', 'color', c(6,:));
xlim([fc(k) - df, fc(k) + df]); ylim([0 1.25]);
xlabel('frecuencia (MHz)'); ylabel('amplitud');
titulo(sprintf('Detalle de la banda %d: dos tonos separados %.1f kHz', ...
               banda(k), df / 2 * 1000));
guardar(f, fullfile(base, 'figs', 'p09_fh_patron.png'));

fid = fopen(fullfile(base, 'datos', 'problema09.txt'), 'w');
fprintf(fid, 'm = 7, x^7+x^3+1, L = %d bandas, df = %.4f MHz\n', Nbandas, df);
fprintf(fid, 'estado inicial tras calentamiento = %s (banda %d)\n', ...
        sprintf('%d', estados(1,:)), banda(1));
fprintf(fid, '%8s %10s %12s %12s %12s\n', 'bit', 'estado', 'banda', 'f1 (MHz)', 'f2 (MHz)');
for k = 1:hops
    fprintf(fid, '%8d %10s %12d %12.6f %12.6f\n', k, sprintf('%d', estados(k,:)), ...
            banda(k), f1(k), f2(k));
end
fclose(fid);
printf('Problema 9 listo\n');
