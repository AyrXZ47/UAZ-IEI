-- PLANTILLA de testbench. Casi no la tocas: solo actualizas las senales
-- del port map y el numero de combinaciones (2^entradas).
-- Su trabajo: meterle todas las combinaciones a tu circuito y grabar la
-- onda en el .vcd para verla en GTKWave.
library IEEE;
use IEEE.STD_LOGIC_1164.all;
use IEEE.NUMERIC_STD.all;  -- para to_unsigned (convertir numero -> bits)

entity tb_circuito is
end tb_circuito;             -- el nombre que va en: ghdl -e tb_circuito

architecture t of tb_circuito is
  -- Mismas senales que el port de tu circuito, en el mismo orden.
  signal A, B, C : STD_LOGIC := '0';  -- := '0' evita el 'U' del arranque
  signal F       : STD_LOGIC;
begin

  -- Instancia tu circuito: uut = "unit under test".
  -- "work.circuito(logica)" = entity circuito, architecture logica.
  uut : entity work.circuito(logica) port map (A, B, C, F);

  stim : process
    variable v : STD_LOGIC_VECTOR(2 downto 0);  -- aqui caben A,B,C
  begin
    -- Recorre las 2^3 = 8 combinaciones: 000,001,...,111.
    -- Para 4 entradas: 0 to 15 y STD_LOGIC_VECTOR(3 downto 0).
    for i in 0 to 7 loop
      v  := STD_LOGIC_VECTOR(to_unsigned(i, 3));  -- i en binario
      A  <= v(2);  B <= v(1);  C <= v(0);         -- parte el bus en bits
      wait for 100 ns;  -- deja pasar tiempo para que se vea en la onda
    end loop;

    report "Listo: 8 combinaciones aplicadas. Abre el .vcd en gtkwave.";
    wait;  -- el process se queda quieto; sin esto reiniciaria para siempre
  end process;

end t;
