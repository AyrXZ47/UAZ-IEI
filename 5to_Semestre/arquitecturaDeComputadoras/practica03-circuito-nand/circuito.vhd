-- Practica 3: circuito del diagrama (3 entradas A,B,C -> 1 salida F).
--
-- El diagrama tiene:
--   2 inversores alimentando una NAND  -> g1 = (A'B')'
--   esa NAND con C' en otra NAND       -> g2 = ((A'B')' * C')'
--   una AND de 3 entradas              -> g3 = A*B*C
--   y un OR final: F = g2 + g3
--
-- Simplificacion (De Morgan + absorcion):
--   F = ((A'B')' * C')' + ABC
--     = (A'B') + C + ABC        (De Morgan en el primer termino)
--     = A'B' + C                (C absorbe a ABC: C + C*AB = C)
--
-- O sea todo el circuito se reduce a: F = A'B' + C = (A+B)' + C
-- F vale 1 cuando C=1, o cuando A y B son 0 a la vez.
library IEEE;
use IEEE.STD_LOGIC_1164.all;

entity circuito is
  port (
    A, B, C : in  STD_LOGIC;
    F       : out STD_LOGIC
  );
end circuito;

-- ESTILO 1: tal cual el diagrama, compuerta por compuerta.
architecture estructural of circuito is
  signal nA, nB, nC : STD_LOGIC;
  signal g1, g2, g3 : STD_LOGIC;
begin
  nA <= not A;
  nB <= not B;
  nC <= not C;

  g1 <= nA nand nB;       -- (A'B')'
  g2 <= g1 nand nC;       -- ((A'B')' * C')'
  g3 <= A and B and C;    -- ABC

  F <= g2 or g3;
end estructural;

-- ESTILO 2: la version simplificada (2 compuertas: NOR + OR).
architecture simplificada of circuito is
begin
  F <= (not A and not B) or C;
end simplificada;
