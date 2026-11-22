library IEEE;
use IEEE.STD_LOGIC_1164.all;
use IEEE.NUMERIC_STD.all;

entity tb_circuito is
end tb_circuito;

architecture t of tb_circuito is
  signal ent  : STD_LOGIC_VECTOR(3 downto 0) := (others => '0');
  signal ctrl : STD_LOGIC_VECTOR(1 downto 0) := (others => '0');
  signal sal  : STD_LOGIC_VECTOR(3 downto 0);
begin

  uut : entity work.shift_when_23400357(arqui_shift_when_23400357)
        port map (ent, ctrl, sal);

  stim : process
  begin
    -- Solo ctrl="00" con todas las entradas, para ver el bus entero.
    for i in 0 to 15 loop
      ent <= STD_LOGIC_VECTOR(to_unsigned(i, 4));
      ctrl <= "00";
      wait for 100 ns;
    end loop;

    -- Un patron fijo (1010) con los 4 controles, para ver los shift/rot.
    for i in 0 to 3 loop
      ent  <= "1010";
      ctrl <= STD_LOGIC_VECTOR(to_unsigned(i, 2));
      wait for 100 ns;
    end loop;

    report "Listo: 16 + 4 combinaciones aplicadas. Abre el .vcd en gtkwave.";
    wait;
  end process;

end t;
