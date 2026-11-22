% Problema 8: los mismos cuatro usuarios, pero asincronos: el usuario 2 va
% retrasado un chip respecto al 1, el 3 uno respecto al 2 y el 4 uno
% respecto al 3. Se compara con el caso sincrono del problema 7.
clear; clc;
base = fileparts(mfilename('fullpath'));
addpath(fullfile(base, 'comun'));

G = gold31();
L = 31;
K = 4;
codigos = G(1:K, :);
N = 10000;
snr = 0:1:9;
rng(21);

pe_sync = zeros(numel(snr), K);
pe_asyn = zeros(numel(snr), K);
for k = 1:numel(snr)
    pe_sync(k, :) = simular_cdma(codigos, [0 0 0 0], snr(k), N);
    pe_asyn(k, :) = simular_cdma(codigos, [0 1 2 3], snr(k), N);
end

eje = 0:0.2:9;
teorica = qfunc(sqrt(2 * 10.^(eje / 10)));
c = colores();

f = figura_nueva(860, 560);
ht = semilogy(eje, teorica, '-', 'color', c(6,:), 'linewidth', 1.2);
ha = zeros(1, K);
for u = 1:K
    ha(u) = semilogy(snr, pe_asyn(:, u), 'o-', 'color', c(u,:), ...
                     'markerfacecolor', c(u,:), 'markersize', 4, 'linewidth', 1.3);
end
for u = 1:K
    semilogy(snr, pe_sync(:, u), '--', 'color', c(u,:), 'linewidth', 1.0);
end
hd = plot([NaN NaN], [NaN NaN], '--', 'color', c(6,:), 'linewidth', 1.2);
grid on;
xlabel('E_b/N_0 (dB)'); ylabel('BER');
titulo('CDMA asíncrono (líneas continuas) vs. síncrono (punteadas)');
hl = legend([ht ha hd], {'teoría de un usuario', 'usuario 1 asíncrono', ...
    'usuario 2 asíncrono', 'usuario 3 asíncrono', 'usuario 4 asíncrono', ...
    'síncrono (4 usuarios)'}, 'location', 'southwest');
set(hl, 'textcolor', [0.910 0.910 0.910], 'box', 'off');
ylim([1e-5 0.2]);
guardar(f, fullfile(base, 'figs', 'p08_cdma_asincrono.png'));

fid = fopen(fullfile(base, 'datos', 'problema08.txt'), 'w');
fprintf(fid, 'retardos = [0 1 2 3] chips, N = %d bits\n', N);
fprintf(fid, '%8s | %-27s | %-27s\n', 'Eb/N0', 'sincrono (u1..u4)', 'asincrono (u1..u4)');
for k = 1:numel(snr)
    fprintf(fid, '%8.0f | %7.4f %7.4f %7.4f %7.4f | %7.4f %7.4f %7.4f %7.4f\n', ...
            snr(k), pe_sync(k, :), pe_asyn(k, :));
end
fprintf(fid, 'media asincrona en 9 dB = %.5f\n', mean(pe_asyn(end, :)));
fprintf(fid, 'media sincrona en 9 dB   = %.5f\n', mean(pe_sync(end, :)));
fclose(fid);
printf('Problema 8 listo\n');
