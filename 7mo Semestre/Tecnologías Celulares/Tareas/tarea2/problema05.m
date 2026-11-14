% Problema 5: suma modulo 2 de las salidas de dos LFSR de longitud maxima
% con m = 3 (L = 7) y m = 4 (L = 15). Se determina el periodo de la
% secuencia resultante y se calcula su autocorrelacion periodica.
clear; clc;
base = fileparts(mfilename('fullpath'));
addpath(fullfile(base, 'comun'));

c3 = 2 * lfsr_max([3 1]) - 1;    % x^3 + x + 1, L = 7
c4 = 2 * lfsr_max([4 1]) - 1;    % x^4 + x + 1, L = 15
comp = kron(ones(1, 15), c3) .* kron(ones(1, 7), c4);   % 105 chips

% periodo: primer desplazamiento que deja la secuencia igual
periodo = NaN;
for d = 1:numel(comp)
    if isequal(comp, circshift(comp, [0 d]))
        periodo = d;
        break;
    end
end

r = autocorr_per(comp);
vals = unique(round(r * 105)) / 105;

printf('periodo = %d (lcm(7,15) = %d)\n', periodo, lcm(7, 15));
printf('R(0) = %.4f, R(7) = %.4f, R(15) = %.4f, resto en [%.4f, %.4f]\n', ...
       r(1), r(8), r(16), min(r(2:end)), max(r(2:end)));

c = colores();
f = figura_nueva(880, 640);
subplot(2, 1, 1);
panel();
stairs(1:105, comp, 'color', c(1,:), 'linewidth', 1.0);
ylim([-1.4 1.4]); xlim([1 105]);
xlabel('chip'); ylabel('secuencia bipolar');
titulo('Suma módulo 2 de las secuencias m = 3 y m = 4 (105 chips)');

subplot(2, 1, 2);
panel();
plot(1:104, r(2:end), '-', 'color', c(2,:), 'linewidth', 1.2);
text(6, 0.022, 'R_c(0) = 1 (fuera de escala)', 'color', c(6,:), 'fontsize', 10);
plot([0 104], [-1/15 -1/15], '--', 'color', c(3,:), 'linewidth', 1.0);
plot([0 104], [-1/7 -1/7], '--', 'color', c(4,:), 'linewidth', 1.0);
plot([0 104], [1/105 1/105], ':', 'color', c(5,:), 'linewidth', 1.0);
xlim([1 104]); ylim([-0.2 0.05]);
xlabel('retardo \tau (chips)'); ylabel('R_c(\tau)');
titulo('Autocorrelación periódica del compuesto');
leyenda({'R_c(\tau)', '-1/15 (múltiplos de 7)', '-1/7 (múltiplos de 15)', '1/105'}, ...
        'southeast');
guardar(f, fullfile(base, 'figs', 'p05_compuesta.png'));

fid = fopen(fullfile(base, 'datos', 'problema05.txt'), 'w');
fprintf(fid, 'm = 3 (L = 7) y m = 4 (L = 15); compuesto de %d chips\n', numel(comp));
fprintf(fid, 'periodo medido = %d, lcm(7,15) = %d\n', periodo, lcm(7, 15));
fprintf(fid, 'R(0) = %.6f\n', r(1));
fprintf(fid, 'R(7) = %.6f (-1/15)\n', r(8));
fprintf(fid, 'R(15) = %.6f (-1/7)\n', r(16));
fprintf(fid, 'valores distintos (x105): %s\n', mat2str(round(vals * 105)));
fprintf(fid, 'cola: min = %.6f, max = %.6f\n', min(r(2:end)), max(r(2:end)));
fclose(fid);
printf('Problema 5 listo\n');
