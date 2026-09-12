-- Testbench: ent = "1011" constante, ctrl recorre 0..3.
library IEEE;
use IEEE.STD_LOGIC_1164.all;
use IEEE.NUMERIC_STD.all;

entity tb_circuito is
end tb_circuito;

architecture t of tb_circuito is
  signal ent  : STD_LOGIC_VECTOR(3 downto 0) := "1011";
  signal ctrl : STD_LOGIC_VECTOR(1 downto 0) := (others => '0');
  signal sal, salC, salI, salW : STD_LOGIC_VECTOR(3 downto 0);
begin

  uut : entity work.shift_wci_23400357(arqui_shift_wci)
        port map (ent, ctrl, sal, salC, salI, salW);

  stim : process
    variable i : natural := 0;
  begin
    -- Estimulo INFINITO: ctrl 0..3 reciclando cada 100 ns, para siempre.
    -- La duracion de la simulacion la decide quien corre ./run.sh.
    loop
      ctrl <= STD_LOGIC_VECTOR(to_unsigned(i mod 4, 2));
      wait for 100 ns;
      i := i + 1;
    end loop;
  end process;

end t;
