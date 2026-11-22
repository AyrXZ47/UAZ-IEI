% Problema 11: diversidad dual en FH/FSK con interferencia de banda parcial.
% Se compara el combinador de ley cuadratica con pesos iguales (ejemplo
% ilustrativo) contra el ponderado del problema: w = 50 sin interferencia y
% w = 1/sigma^2 = 2/E con interferencia, para E >= 4.
clear; clc;
base = fileparts(mfilename('fullpath'));
addpath(fullfile(base, 'comun'));

alpha = 0.1;
J0 = 1;
N0 = 0;
N = 500000;
snr = 7:2:17;              % E en dB (E = 5 ... 50, cumple E >= 4)
rng(41);

pe_base = zeros(size(snr));
pe_adapt = zeros(size(snr));
for k = 1:numel(snr)
    E = 10^(snr(k) / 10);
    bit = rand(1, N) < 0.5;
    jam = rand(2, N) < alpha;                 % 2 saltos por bit
    V = (J0 / alpha) * jam;

    z1 = zeros(2, N);
    z2 = zeros(2, N);
    for h = 1:2
        n1 = sqrt(V(h, :) / 2) .* (randn(1, N) + 1i * randn(1, N));
        n2 = sqrt(V(h, :) / 2) .* (randn(1, N) + 1i * randn(1, N));
        r1 = sqrt(E) * (bit == 0) + n1;
        r2 = sqrt(E) * (bit == 1) + n2;
        z1(h, :) = abs(r1).^2;
        z2(h, :) = abs(r2).^2;
    end

    % combinador con pesos iguales (ejemplo ilustrativo)
    Lb = (z1(1, :) - z2(1, :)) + (z1(2, :) - z2(2, :));
    pe_base(k) = mean((Lb < 0) ~= bit);

    % pesos del problema: 50 sin interferencia, 2/E con interferencia
    w = 50 * (~jam) + (2 / E) * jam;
    La = w(1, :) .* (z1(1, :) - z2(1, :)) + w(2, :) .* (z1(2, :) - z2(2, :));
    pe_adapt(k) = mean((La < 0) ~= bit);
end

c = colores();
f = figura_nueva(840, 540);
semilogy(snr, pe_base, 'o-', 'color', c(2,:), 'markerfacecolor', c(2,:), ...
         'markersize', 5, 'linewidth', 1.4);
semilogy(snr, pe_adapt, 's-', 'color', c(1,:), 'markerfacecolor', c(1,:), ...
         'markersize', 5, 'linewidth', 1.4);
grid on;
xlabel('E (energía por salto) en dB'); ylabel('BER');
titulo('Diversidad dual: pesos iguales vs. pesos 50 y 2/E (\alpha = 0.1)');
leyenda({'pesos iguales (ejemplo ilustrativo)', 'pesos w = 50 y w = 2/E'}, ...
        'southwest');
ylim([1e-5 0.1]);
guardar(f, fullfile(base, 'figs', 'p11_diversidad.png'));

fid = fopen(fullfile(base, 'datos', 'problema11.txt'), 'w');
fprintf(fid, 'alpha = %.1f, N = %d bits, J0 = %d, N0 = %d, 2 saltos por bit\n', ...
        alpha, N, J0, N0);
fprintf(fid, '%8s %10s %14s %14s %10s\n', 'E(dB)', 'E', 'Pe iguales', 'Pe 50/2E', 'mejora');
for k = 1:numel(snr)
    fprintf(fid, '%8.0f %10.2f %14.6e %14.6e %10.1f\n', snr(k), 10^(snr(k)/10), ...
            pe_base(k), pe_adapt(k), pe_base(k) / max(pe_adapt(k), 1e-12));
end
fclose(fid);
printf('Problema 11 listo\n');
