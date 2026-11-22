function s = lfsr_max(taps, n)
% LFSR_MAX Secuencia de longitud maxima de un LFSR de Fibonacci.
%   taps = exponentes del polinomio primitivo, p.ej. [12 6 4 1] para
%   x^12 + x^6 + x^4 + 1. La realimentacion es s(n+m) = suma mod 2 de
%   s(n+i) para cada exponente i < m. El estado inicial es 100...0.
%   n = numero de chips (por omision, un periodo completo 2^m - 1).
m = max(taps);
if nargin < 2 || isempty(n)
    n = 2^m - 1;
end
retro = [1, taps(taps < m) + 1];   % termino constante + reg(i+1) = s(n+i)
reg = [1 zeros(1, m - 1)];     % estado inicial no nulo
s = zeros(1, n);
for k = 1:n
    s(k) = reg(1);
    reg = [reg(2:m), mod(sum(reg(retro)), 2)];
end
end
