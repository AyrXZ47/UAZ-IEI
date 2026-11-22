% Problema 6: autocorrelacion periodica de las 31 secuencias Gold de L = 31
% generadas con el par preferido x^5+x^2+1 y x^5+x^4+x^2+x+1.
clear; clc;
base = fileparts(mfilename('fullpath'));
addpath(fullfile(base, 'comun'));

L = 31;
s1 = 2 * lfsr_max([5 2]) - 1;
s2 = 2 * lfsr_max([5 4 2 1]) - 1;

G = zeros(L, L);                       % 31 secuencias de 31 chips
for k = 0:L - 1
    G(k + 1, :) = s1 .* circshift(s2, [0 k]);
end

R = zeros(L, L - 1);                   % lags 1..30
for k = 1:L
    r = autocorr_per(G(k, :));
    R(k, :) = r(2:end);
end

% correlacion cruzada maxima de la familia
max_cross = 0;
for i = 1:L
    for j = i + 1:L
        for k = 0:L - 1
            max_cross = max(max_cross, abs(sum(G(i, :) .* circshift(G(j, :), [0 k]))));
        end
    end
end

niveles = unique(round(R(:) * L));
conteo = arrayfun(@(v) sum(round(R(:) * L) == v), niveles);

printf('niveles (x L): %s\n', mat2str(niveles));
printf('conteo: %s\n', mat2str(conteo));
printf('max correlacion cruzada: %d/31 = %.4f\n', max_cross, max_cross / L);

c = colores();
f = figura_nueva(880, 640);
subplot(2, 1, 1);
panel();
for k = 1:L
    plot(1:L - 1, R(k, :), '-', 'color', c(1 + mod(k, 5), :), 'linewidth', 0.6);
end
plot([1 L - 1], [-9 -9] / L, '--', 'color', c(6,:), 'linewidth', 1.0);
plot([1 L - 1], [-1 -1] / L, '--', 'color', c(3,:), 'linewidth', 1.0);
plot([1 L - 1], [7 7] / L, '--', 'color', c(4,:), 'linewidth', 1.0);
xlim([1 L - 1]); ylim([-0.32 0.24]);
xlabel('retardo \tau (chips)'); ylabel('R_c(\tau)');
titulo('Autocorrelación de las 31 secuencias Gold (L = 31)');

subplot(2, 1, 2);
panel();
bar(niveles / L, conteo, 0.5, 'facecolor', c(1,:), 'edgecolor', c(1,:));
xlabel('valor de R_c en lags \tau \neq 0'); ylabel('número de casos');
titulo('Distribución de los tres valores de correlación');
text(niveles / L, conteo + 40, arrayfun(@(v) sprintf('%d', v), conteo, ...
     'UniformOutput', false), 'color', c(6,:), 'fontsize', 10, ...
     'horizontalalignment', 'center');
guardar(f, fullfile(base, 'figs', 'p06_gold.png'));

fid = fopen(fullfile(base, 'datos', 'problema06.txt'), 'w');
fprintf(fid, 'Par: x^5+x^2+1 y x^5+x^4+x^2+x+1, L = 31\n');
fprintf(fid, 'niveles R*tau*L: %s\n', mat2str(niveles));
fprintf(fid, 'conteo: %s\n', mat2str(conteo));
fprintf(fid, 'valores normalizados: %s\n', mat2str(niveles / L, 4));
fprintf(fid, 'max correlacion cruzada = %d/31 = %.4f\n', max_cross, max_cross / L);
fclose(fid);
printf('Problema 6 listo\n');
