function pe = simular_cdma(G, delays, ebn0_db, N)
% SIMULAR_CDMA Monte Carlo de K usuarios CDMA con codigos G (K x L) y
% retardos en chips. Ec = 1 por chip, Eb = L. Ruido AWGN por chip.
K = size(G, 1);
L = size(G, 2);
ebn0 = 10^(ebn0_db / 10);
Eb = L;
N0 = Eb / ebn0;
sigma = sqrt(N0 / 2);

T = L * N + max(delays);
r = zeros(1, T);
D = zeros(K, N);
for u = 1:K
    D(u, :) = 2 * (rand(1, N) < 0.5) - 1;
    r(delays(u) + 1:delays(u) + L * N) += kron(D(u, :), G(u, :));
end
r = r + sigma * randn(1, T);

pe = zeros(1, K);
for u = 1:K
    idx = delays(u) + (0:N - 1) * L;
    ventanas = r(idx + (1:L)');            % L x N
    y = sum(ventanas .* repmat(G(u, :)', 1, N), 1);
    pe(u) = mean((y > 0) ~= (D(u, :) > 0));
end
end
