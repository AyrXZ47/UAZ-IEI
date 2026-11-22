function pe = sim_dsss(ebn0_db, L, N)
% SIM_DSSS Simulacion Monte Carlo de DS/SS BPSK sobre AWGN.
%   ebn0_db : Eb/N0 en dB (energia por bit de informacion)
%   L       : chips por bit (ganancia de procesamiento)
%   N       : numero de bits simulados
% El codigo PN es fijo y bipolar; la energia por chip es 1 y Eb = L.
ebn0 = 10^(ebn0_db / 10);
Eb = L;
N0 = Eb / ebn0;
sigma = sqrt(N0 / 2);

codigo = 2 * (rand(1, L) < 0.5) - 1;
datos = 2 * (rand(N, 1) < 0.5) - 1;      % N x 1

recibido = datos * codigo + sigma * randn(N, L);
decision = recibido * codigo';            % correlador
pe = mean((decision > 0) ~= (datos > 0));
end
