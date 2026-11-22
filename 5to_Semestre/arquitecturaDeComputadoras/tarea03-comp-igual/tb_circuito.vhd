library IEEE;
use IEEE.STD_LOGIC_1164.all;
use IEEE.NUMERIC_STD.all;

entity tb_circuito is
end tb_circuito;

architecture t of tb_circuito is
  signal a  : STD_LOGIC_VECTOR(2 downto 0) := (others => '0');
  signal b  : STD_LOGIC_VECTOR(2 downto 0) := (others => '0');
  signal ig : STD_LOGIC;
begin

  uut : entity work.comp_igual_3bits(arqui_comp_igual_3bits)
        port map (a, b, ig);

  stim : process
  begin
    for i in 0 to 7 loop
      for j in 0 to 7 loop
        a <= STD_LOGIC_VECTOR(to_unsigned(i, 3));
        b <= STD_LOGIC_VECTOR(to_unsigned(j, 3));
        wait for 100 ns;
        assert (ig = '1') = (i = j)
          report "Falla con i=" & integer'image(i) & " j=" & integer'image(j)
          severity error;
      end loop;
    end loop;

    report "Listo: 64 combinaciones aplicadas. Abre el .vcd en gtkwave.";
    wait;
  end process;

end t;
