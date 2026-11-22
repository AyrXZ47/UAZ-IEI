% Problema 10: FH/FSK binario con deteccion no coherente (ley cuadratica)
% e interferencia de banda parcial con densidad espectral J0/alpha, alpha=0.1.
% Se mide la BER contra Eb/J0 y se compara con la teoria.
clear; clc;
base = fileparts(mfilename('fullpath'));
addpath(fullfile(base, 'comun'));

alpha = 0.1;
N = 500000;
J0 = 1;
N0 = 0;                    % caso limitado por el interferidor
snr = 0:2:20;              % Eb/J0 en dB
rng(31);

pe = zeros(size(snr));
for k = 1:numel(snr)
    Eb = J0 * 10^(snr(k) / 10);
    bit = rand(1, N) < 0.5;
    jam = rand(1, N) < alpha;
    V = N0 + (J0 / alpha) * jam;            % varianza compleja por muestra

    n1 = sqrt(V / 2) .* (randn(1, N) + 1i * randn(1, N));
    n2 = sqrt(V / 2) .* (randn(1, N) + 1i * randn(1, N));
    r1 = sqrt(Eb) * (bit == 0) + n1;
    r2 = sqrt(Eb) * (bit == 1) + n2;

    decision = abs(r2).^2 > abs(r1).^2;     % decide bit 1 si gana el tono 2
    pe(k) = mean(decision ~= bit);
end

eje = 0:0.2:20;
Eb_eje = 10.^(eje / 10);
teorica = alpha * 0.5 * exp(-Eb_eje / (2 * J0 / alpha));
completa = 0.5 * exp(-Eb_eje / (2 * J0));          % referencia alpha = 1
c = colores();

f = figura_nueva(840, 540);
semilogy(eje, completa, ':', 'color', c(6,:), 'linewidth', 1.4);
semilogy(eje, teorica, '-', 'color', c(2,:), 'linewidth', 1.8);
semilogy(snr, pe, 'o', 'color', c(1,:), 'markerfacecolor', c(1,:), ...
         'markersize', 6, 'linewidth', 1.2);
grid on;
xlabel('E_b/J_0 (dB)'); ylabel('BER');
titulo('FH/FSK con interferencia de banda parcial (\alpha = 0.1)');
leyenda({'banda completa (\alpha = 1)', 'teoría \alpha = 0.1', ...
         'simulación Monte Carlo'}, 'southwest');
ylim([1e-6 0.5]);
guardar(f, fullfile(base, 'figs', 'p10_fh_banda_parcial.png'));

fid = fopen(fullfile(base, 'datos', 'problema10.txt'), 'w');
fprintf(fid, 'alpha = %.1f, N = %d bits, N0 = %d, J0 = %d\n', alpha, N, N0, J0);
fprintf(fid, '%10s %14s %14s\n', 'Eb/J0', 'Pe simulada', 'Pe teorica');
for k = 1:numel(snr)
    Eb = 10^(snr(k) / 10);
    fprintf(fid, '%10.0f %14.6e %14.6e\n', snr(k), pe(k), ...
            alpha * 0.5 * exp(-Eb / (2 * J0 / alpha)));
end
fprintf(fid, 'cada 20 unidades (13 dB) de Eb/J0 reducen la BER en un factor e\n');
fclose(fid);
printf('Problema 10 listo\n');
