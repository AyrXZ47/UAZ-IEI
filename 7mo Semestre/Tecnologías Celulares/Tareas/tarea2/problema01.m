% Problema 1: DS/SS BPSK sobre AWGN con ganancia de procesamiento 10.
% La BER se mide contra Eb/N0 y se compara con BPSK sin dispersion: si las
% curvas coinciden, el ensanchamiento no aporta ganancia de desempeno.
clear; clc;
base = fileparts(mfilename('fullpath'));
addpath(fullfile(base, 'comun'));

L = 10;              % chips por bit = ganancia de procesamiento
N = 200000;          % bits por punto
ebn0 = 0:1:8;        % Eb/N0 en dB
rng(7);              % reproducibilidad

pe = zeros(size(ebn0));
for k = 1:numel(ebn0)
    pe(k) = sim_dsss(ebn0(k), L, N);
end

eje = 0:0.2:8;
teorica = qfunc(sqrt(2 * 10.^(eje / 10)));
c = colores();

f = figura_nueva(820, 520);
semilogy(ebn0, pe, 'o', 'color', c(1,:), 'markerfacecolor', c(1,:), ...
         'markersize', 6, 'linewidth', 1.2); hold on;
semilogy(eje, teorica, '-', 'color', c(2,:), 'linewidth', 1.8);
grid on;
xlabel('E_b/N_0 (dB)'); ylabel('BER');
titulo('DS/SS BPSK con G_p = 10 sobre AWGN');
leyenda({'simulación Monte Carlo', 'BPSK teórica Q(\surd(2E_b/N_0))'}, ...
        'southwest');
guardar(f, fullfile(base, 'figs', 'p01_ber.png'));

fid = fopen(fullfile(base, 'datos', 'problema01.txt'), 'w');
fprintf(fid, 'L = %d chips/bit, N = %d bits por punto\n', L, N);
fprintf(fid, '%8s %14s %14s\n', 'Eb/N0', 'Pe simulada', 'Pe teorica');
for k = 1:numel(ebn0)
    fprintf(fid, '%8.0f %14.6e %14.6e\n', ebn0(k), pe(k), ...
            qfunc(sqrt(2 * 10^(ebn0(k) / 10))));
end
fclose(fid);

printf('Problema 1 listo: %d puntos\n', numel(ebn0));
