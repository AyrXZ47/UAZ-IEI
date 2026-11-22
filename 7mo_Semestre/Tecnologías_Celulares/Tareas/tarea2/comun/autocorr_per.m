function r = autocorr_per(c)
% AUTOCORR_PER Autocorrelacion periodica (ecuacion 20) de una secuencia
% bipolar, con lags 0..L-1 y normalizada a 1 en el origen.
L = numel(c);
r = ifft(abs(fft(c)).^2) / L;
r = [r(1), r(L:-1:2)];
end
