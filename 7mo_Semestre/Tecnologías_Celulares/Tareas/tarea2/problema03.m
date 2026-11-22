% Problema 3: repeticion del ejemplo ilustrativo con Gp = 10, pero midiendo
% la BER contra el SNR de entrada (banda dispersa). La curva DS/SS queda
% 10 dB a la izquierda de BPSK estrecha: esa es la ganancia de procesamiento.
clear; clc;
base = fileparts(mfilename('fullpath'));
addpath(fullfile(base, 'comun'));

L = 10;
N = 200000;
snr_in = -20:1:-3;          % Ec/N0 en la banda dispersa
rng(3);

pe = zeros(size(snr_in));
for k = 1:numel(snr_in)
    pe(k) = sim_dsss(snr_in(k) + 10 * log10(L), L, N);
end

eje = -22:0.2:2;
ds_teoria = qfunc(sqrt(2 * 10.^((eje + 10 * log10(L)) / 10)));
bpsk = qfunc(sqrt(2 * 10.^(eje / 10)));
pe_plot = pe; pe_plot(pe_plot == 0) = NaN;
c = colores();

f = figura_nueva(820, 520);
semilogy(eje, bpsk, '-', 'color', c(2,:), 'linewidth', 1.6);
semilogy(eje, ds_teoria, '--', 'color', c(1,:), 'linewidth', 1.6);
semilogy(snr_in, pe_plot, 'o', 'color', c(3,:), 'markerfacecolor', c(3,:), ...
         'markersize', 6, 'linewidth', 1.2);
plot([-8.7 1.3], [0.05 0.05], '-', 'color', c(4,:), 'linewidth', 1.2);
text(-3.7, 0.058, '10 dB', 'color', c(4,:), 'fontsize', 11);
grid on;
xlabel('SNR de entrada E_c/N_0 (dB)'); ylabel('BER');
titulo('Ganancia de procesamiento: G_p = 10 dB con L = 10 chips/bit');
leyenda({'BPSK estrecha (referida a E_b/N_0)', ...
         'DS/SS teórica (referida a E_c/N_0)', ...
         'DS/SS simulada'}, 'southwest');
ylim([1e-5 0.5]); xlim([-22 2]);
guardar(f, fullfile(base, 'figs', 'p03_ganancia.png'));

fid = fopen(fullfile(base, 'datos', 'problema03.txt'), 'w');
fprintf(fid, 'L = %d, Gp = 10 dB, N = %d bits\n', L, N);
fprintf(fid, '%12s %12s %14s\n', 'SNR_in', 'Eb/N0', 'Pe simulada');
for k = 1:numel(snr_in)
    fprintf(fid, '%12.0f %12.0f %14.6e\n', snr_in(k), snr_in(k) + 10 * log10(L), pe(k));
end
fprintf(fid, 'Desplazamiento medido: %.0f dB\n', 10 * log10(L));
fclose(fid);

printf('Problema 3 listo\n');
