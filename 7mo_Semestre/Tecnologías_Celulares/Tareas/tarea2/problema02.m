% Problema 2: sistema DS/SS de baja probabilidad de interceptacion (LPI).
% Gp = 20 (13 dB); la senal llega 5 dB por debajo del ruido (Ps/Pn = -5 dB)
% antes del desensanchamiento. Se barre el SNR de entrada y se compara la
% BER medida con la teoria desplazada por la ganancia de procesamiento.
clear; clc;
base = fileparts(mfilename('fullpath'));
addpath(fullfile(base, 'comun'));

L = 20;                     % chips por bit -> 13 dB
Gp_dB = 10 * log10(L);
N = 200000;
snr_in = [-20:2:-6, -5, -4, -2, 0];   % Ec/N0 en la banda dispersa (dB)
rng(11);

pe = zeros(size(snr_in));
for k = 1:numel(snr_in)
    pe(k) = sim_dsss(snr_in(k) + Gp_dB, L, N);
end

eje = -20:0.25:0;
teorica = qfunc(sqrt(2 * 10.^((eje + Gp_dB) / 10)));
pe_plot = pe;
pe_plot(pe_plot == 0) = NaN;
c = colores();

f = figura_nueva(820, 520);
semilogy(eje, teorica, '-', 'color', c(2,:), 'linewidth', 1.8); hold on;
semilogy(snr_in, pe_plot, 'o', 'color', c(1,:), 'markerfacecolor', c(1,:), ...
         'markersize', 6, 'linewidth', 1.2);
ylim([1e-6 0.5]);
plot([-5 -5], [1e-6 0.5], '--', 'color', c(3,:), 'linewidth', 1.2);
plot(-5, qfunc(sqrt(2 * 10^((-5 + Gp_dB) / 10))), 's', 'color', c(3,:), ...
     'markerfacecolor', c(3,:), 'markersize', 8);
grid on;
xlabel('SNR de entrada P_S/P_N = E_c/N_0 (dB)'); ylabel('BER');
titulo('Detección LPI: la señal llega 5 dB bajo el ruido');
leyenda({'teoría Q(\surd(2E_b/N_0)), E_b/N_0 = SNR_{in} + 13 dB', ...
         'simulación Monte Carlo', 'punto de operación (-5 dB)'}, 'southwest');
ylim([1e-6 0.5]);
guardar(f, fullfile(base, 'figs', 'p02_lpi_ber.png'));

% Segunda figura: la senal oculta y la acumulacion coherente del correlador
M = 400;                                   % periodos del codigo
Eb = L;
N0 = Eb / 10^((-5 + Gp_dB) / 10);
sigma = sqrt(N0 / 2);
Ec = Eb / L;
codigo = 2 * (rand(1, L) < 0.5) - 1;
recibido = sqrt(Ec) * repmat(codigo, 1, M) + sigma * randn(1, L * M);

f = figura_nueva(880, 640);
subplot(2, 1, 1);
panel();
plot(1:L, recibido(1:L), '-o', 'color', c(6,:), 'markerfacecolor', c(6,:), ...
     'markersize', 4);
plot(1:L, sqrt(Ec) * codigo, '--', 'color', c(1,:), 'linewidth', 1.8);
xlabel('chip'); ylabel('r[n]');
titulo('Un periodo del código: la señal está 5 dB bajo el ruido');
leyenda({'muestra recibida', 'señal DS/SS'}, 'northeast');

subplot(2, 1, 2);
panel();
y = cumsum(recibido .* repmat(codigo, 1, M)) / sqrt(Ec);
w = cumsum(recibido .* repmat(circshift(codigo, [0 1]), 1, M)) / sqrt(Ec);
plot(1:L*M, y, '-', 'color', c(4,:), 'linewidth', 1.6);
plot(1:L*M, w, '-', 'color', c(2,:), 'linewidth', 1.2);
xlabel('chip acumulado'); ylabel('correlación acumulada / \surd E_c');
titulo('El correlador acumula la señal y cancela el ruido');
leyenda({'código correcto', 'código desplazado un chip'}, 'northwest');
guardar(f, fullfile(base, 'figs', 'p02_lpi_tiempo.png'));

fid = fopen(fullfile(base, 'datos', 'problema02.txt'), 'w');
fprintf(fid, 'L = %d (Gp = %.2f dB), N = %d bits\n', L, Gp_dB, N);
fprintf(fid, '%10s %14s %14s\n', 'SNR_in', 'Pe simulada', 'Pe teorica');
for k = 1:numel(snr_in)
    fprintf(fid, '%10.0f %14.6e %14.6e\n', snr_in(k), pe(k), ...
            qfunc(sqrt(2 * 10^((snr_in(k) + Gp_dB) / 10))));
end
fprintf(fid, 'Punto de operacion: SNR_in = -5 dB -> Pe teorica = %.6e\n', ...
        qfunc(sqrt(2 * 10^((-5 + Gp_dB) / 10))));
fclose(fid);

printf('Problema 2 listo\n');
