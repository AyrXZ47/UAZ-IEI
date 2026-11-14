function G = gold31()
% GOLD31 Las 31 secuencias Gold de longitud 31 del par preferido
% x^5+x^2+1 y x^5+x^4+x^2+x+1 (mismo par del ejemplo del libro).
s1 = 2 * lfsr_max([5 2]) - 1;
s2 = 2 * lfsr_max([5 4 2 1]) - 1;
G = zeros(31, 31);
for k = 0:30
    G(k + 1, :) = s1 .* circshift(s2, [0 k]);
end
end
