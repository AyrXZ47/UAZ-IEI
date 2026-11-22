-- Testbench de comp_or: es tu "harness" de simulacion.
-- Aqui viven los nano-segundos que tus companeros ajustan con clicks:
-- cada `wait for X ns;` es un punto de estimulo en el tiempo.
--
-- NOTA: el assert va DENTRO del proceso de estimulos, despues de cada wait.
-- Si lo pusieras en un proceso aparte sensible a (A,B,S), compararia contra S
-- viejo en el mismo delta en que A/B cambian (carrera de deltas) y fallaria
-- espuriamente al arrancar con S='U'.
library IEEE;
use IEEE.STD_LOGIC_1164.all;

entity tb_comp_or is
end tb_comp_or;

architecture t of tb_comp_or is
  -- senales para conectar el DUT (Device Under Test)
  signal A, B, S : STD_LOGIC;
begin

  -- instancia el circuito que quieres probar
  uut : entity work.comp_or port map (A => A, B => B, S => S);

  -- proceso de estimulos: corre una vez, en orden, de arriba a abajo.
  -- tras cada estimulo se espera (S se asienta) y se verifica el resultado.
  stim : process
  begin
    A <= '0'; B <= '0';
    wait for 10 ns;
    assert S = '0' report "00: S deberia ser 0" severity failure;

    A <= '0'; B <= '1';
    wait for 10 ns;
    assert S = '1' report "01: S deberia ser 1" severity failure;

    A <= '1'; B <= '0';
    wait for 10 ns;
    assert S = '1' report "10: S deberia ser 1" severity failure;

    A <= '1'; B <= '1';
    wait for 10 ns;
    assert S = '1' report "11: S deberia ser 1" severity failure;

    report "OK: 4/4 casos correctos (40 ns simulados)";
    wait;  -- se queda quieto para siempre: fin de la simulacion
  end process;

end t;
