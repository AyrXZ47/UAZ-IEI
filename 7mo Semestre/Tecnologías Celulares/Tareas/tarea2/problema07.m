% Problema 7: cuatro usuarios CDMA sincronizados en el tiempo, cada uno con
% una secuencia Gold distinta de L = 31. N = 10000 bits por usuario.
clear; clc;
base = fileparts(mfilename('fullpath'));
addpath(fullfile(base, 'comun'));

G = gold31();
L = 31;
K = 4;
codigos = G(1:K, :);          % cuatro secuencias de la tabla
N = 10000;
snr = 0:1:9;
rng(21);

pe = zeros(numel(snr), K);
for k = 1:numel(snr)
    pe(k, :) = simular_cdma(codigos, zeros(1, K), snr(k), N);
end

eje = 0:0.2:9;
teorica = qfunc(sqrt(2 * 10.^(eje / 10)));
c = colores();

f = figura_nueva(840, 540);
semilogy(eje, teorica, '-', 'color', c(6,:), 'linewidth', 1.4);
for u = 1:K
    semilogy(snr, pe(:, u), 'o-', 'color', c(u,:), 'markerfacecolor', c(u,:), ...
             'markersize', 4, 'linewidth', 1.2);
end
grid on;
xlabel('E_b/N_0 (dB)'); ylabel('BER');
titulo('CDMA síncrono: 4 usuarios con secuencias Gold (L = 31)');
leyenda({'usuario único (teoría)', 'usuario 1', 'usuario 2', 'usuario 3', ...
         'usuario 4'}, 'southwest');
ylim([1e-5 0.2]);
guardar(f, fullfile(base, 'figs', 'p07_cdma_sincrono.png'));

fid = fopen(fullfile(base, 'datos', 'problema07.txt'), 'w');
fprintf(fid, '4 usuarios sincronos, L = 31, N = %d bits\n', N);
fprintf(fid, 'R(0) entre pares de codigos = -1/31 = %.4f\n', -1/L);
fprintf(fid, '%10s %12s %12s %12s %12s\n', 'Eb/N0', 'user1', 'user2', 'user3', 'user4');
for k = 1:numel(snr)
    fprintf(fid, '%10.0f %12.5f %12.5f %12.5f %12.5f\n', snr(k), pe(k, :));
end
fprintf(fid, 'MAI maxima (3 interferentes): %.4f = %.1f dB bajo la senal\n', ...
        3 / L^2, 10 * log10(L^2 / 3));
fclose(fid);
printf('Problema 7 listo\n');
