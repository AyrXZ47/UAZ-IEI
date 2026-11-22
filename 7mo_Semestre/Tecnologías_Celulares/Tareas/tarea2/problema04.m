% Problema 4: secuencia de longitud maxima con m = 12 (L = 4095).
% Se generan cinco periodos, se comprueba la repeticion y se calcula la
% autocorrelacion periodica de la secuencia bipolar (ecuacion 20).
clear; clc;
base = fileparts(mfilename('fullpath'));
addpath(fullfile(base, 'comun'));

m = 12;
taps = [12 6 4 1];          % x^12 + x^6 + x^4 + 1
L = 2^m - 1;
P = 5;
s = lfsr_max(taps, P * L);

repite = true;
for k = 1:P - 1
    repite = repite && isequal(s(1:L), s(k*L + 1:(k + 1)*L));
end

c = 2 * s(1:L) - 1;
r = autocorr_per(c);
cola = r(2:end);

printf('L = %d, periodos generados = %d, repite = %d\n', L, P, repite);
printf('R(0) = %.6f, cola: min %.6e max %.6e\n', r(1), min(cola), max(cola));
printf('unos = %d, ceros = %d\n', sum(s(1:L)), L - sum(s(1:L)));

c = colores();
f = figura_nueva(880, 620);
subplot(2, 1, 1);
panel();
plot(0:L-1, r, '-', 'color', c(1,:), 'linewidth', 1.2);
xlabel('retardo \tau (chips)'); ylabel('R_c(\tau)');
xlim([0 L-1]); ylim([-0.05 1.05]);
titulo(sprintf('Autocorrelación periódica, m = 12 (L = %d)', L));

subplot(2, 1, 2);
panel();
plot(0:200, r(1:201), '-o', 'color', c(2,:), 'markerfacecolor', c(2,:), ...
     'markersize', 3, 'linewidth', 1.2);
plot([0 200], [-1/L -1/L], '--', 'color', c(3,:), 'linewidth', 1.2);
ylim([-1.5/L, 0.5/L]);
xlabel('retardo \tau (chips)'); ylabel('R_c(\tau)');
titulo('Detalle del lóbulo lateral: R_c(\tau) = -1/L');
guardar(f, fullfile(base, 'figs', 'p04_autocorrelacion.png'));

fid = fopen(fullfile(base, 'datos', 'problema04.txt'), 'w');
fprintf(fid, 'm = %d, polinomio x^12+x^6+x^4+1, L = %d\n', m, L);
fprintf(fid, 'periodos generados = %d, la secuencia se repite = %d\n', P, repite);
fprintf(fid, 'unos = %d, ceros = %d\n', sum(s(1:L)), L - sum(s(1:L)));
fprintf(fid, 'R(0) = %.10f\n', r(1));
fprintf(fid, 'cola: min = %.10e, max = %.10e, media = %.10e\n', ...
        min(cola), max(cola), mean(cola));
fprintf(fid, '-1/L = %.10e\n', -1/L);
fclose(fid);
printf('Problema 4 listo\n');
