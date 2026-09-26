-- Practica 7: multiplexor 4x1 con logica en cada canal (el diagrama del profe).
--
-- Idea: hay 9 entradas ent(0)..ent(8), un selector s(1 downto 0) y una salida
-- sal. Primero se calcula el valor de cada uno de los 4 canales con sus
-- compuertas, y luego el mux 4x1 elige UNO de esos 4 segun s.
--
-- Canal 00: ent(0) pasa por un inversor y luego un OR con ent(1)
--           c0 = ent(0)' + ent(1)
-- Canal 01: NOR de 3 entradas (ent(2),ent(3),ent(4)); su salida entra a una
--           NAND de 2 junto con ent(5)
--           c1 = ((ent(2) + ent(3) + ent(4))' * ent(5))'
-- Canal 10: dos AND alimentando un OR
--           c2 = (ent(5) * ent(6)) + (ent(7) * ent(8))
-- Canal 11: AND de 3 entradas (ent5,ent6,ent7); su salida a una XOR con ent(8)
--           c3 = (ent(5) * ent(6) * ent(7)) XOR ent(8)
--
-- sal = c0 si s="00", c1 si s="01", c2 si s="10", c3 si s="11".
library IEEE;
use IEEE.STD_LOGIC_1164.all;

entity mux4x1_logica_23400357 is
  port (
    ent : in  STD_LOGIC_VECTOR(8 downto 0);  -- ent(0)..ent(8)
    s   : in  STD_LOGIC_VECTOR(1 downto 0);  -- selector: 00,01,10,11
    sal : out STD_LOGIC                      -- salida del mux
  );
end mux4x1_logica_23400357;

-- ESTILO 1: tal cual el diagrama, compuerta por compuerta.
architecture estructural of mux4x1_logica_23400357 is
  signal c0, c1, c2, c3   : STD_LOGIC;
  signal n0, nor234       : STD_LOGIC;
  signal a56, a78, a567   : STD_LOGIC;
begin
  -- canal 00
  n0  <= not ent(0);
  c0  <= n0 or ent(1);

  -- canal 01: NOR de 3 y luego NAND con ent(5)
  nor234 <= not (ent(2) or ent(3) or ent(4));
  c1  <= nor234 nand ent(5);

  -- canal 10
  a56 <= ent(5) and ent(6);
  a78 <= ent(7) and ent(8);
  c2  <= a56 or a78;

  -- canal 11: AND de 3 y luego XOR con ent(8)
  a567 <= ent(5) and ent(6) and ent(7);
  c3  <= a567 xor ent(8);

  -- mux 4x1
  with s select
    sal <= c0 when "00",
           c1 when "01",
           c2 when "10",
           c3 when others;
end estructural;

-- ESTILO 2: todo en una expresion concurrente, sin senales intermedias.
-- Equivalente al estructural (las senales de arriba solo dan claridad).
architecture simplificada of mux4x1_logica_23400357 is
begin
  with s select
    sal <= ((not ent(0)) or ent(1))                                       when "00",
           (not ((not (ent(2) or ent(3) or ent(4))) and ent(5)))          when "01",
           ((ent(5) and ent(6)) or (ent(7) and ent(8)))                   when "10",
           ((ent(5) and ent(6) and ent(7)) xor ent(8))                    when others;
end simplificada;
