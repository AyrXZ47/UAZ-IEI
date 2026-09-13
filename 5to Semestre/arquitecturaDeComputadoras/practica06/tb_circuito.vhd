-- Testbench: barre las 8 combinaciones de x y COMPRUEBA contra la tabla.
-- Si alguna fila no coincide, rompe con error (asi el circuito se
-- autoverifica, no depende de que leas bien la onda).
library IEEE;
use IEEE.STD_LOGIC_1164.all;
use IEEE.NUMERIC_STD.all;

entity tb_circuito is
end tb_circuito;

architecture t of tb_circuito is
  signal x : STD_LOGIC_VECTOR(2 downto 0) := (others => '0');
  signal y1, y2, y3, y4 : STD_LOGIC_VECTOR(1 downto 0);
begin

  uut : entity work.tabla_wwci_23400357(arqui_tabla)
        port map (x, y1, y2, y3, y4);

  stim : process
    type t_tab is array (0 to 7) of STD_LOGIC_VECTOR(1 downto 0);
    constant ESPERA : t_tab := ("01", "11", "00", "01",
                                "10", "10", "01", "11");
    variable ok : boolean := true;
  begin
    for i in 0 to 7 loop
      x <= STD_LOGIC_VECTOR(to_unsigned(i, 3));
      wait for 10 ns;
      -- Las 4 estructuras deben dar lo mismo; se checa la when (y1)
      -- y ademas que todas coincidan entre si.
      assert y1 = ESPERA(i)
        report "Fila " & integer'image(i)
             & ": salio " & to_string(y1)
             & ", esperaba " & to_string(ESPERA(i))
        severity error;
      if y1 /= ESPERA(i) then
        ok := false;
      end if;
      assert (y1 = y2) and (y1 = y3) and (y1 = y4)
        report "Fila " & integer'image(i) & ": las 4 salidas difieren"
        severity error;
    end loop;

    assert ok report "La tabla NO coincide." severity failure;
    report "Tabla verificada: 8 de 8 filas correctas.";
    wait;
  end process;

end t;
