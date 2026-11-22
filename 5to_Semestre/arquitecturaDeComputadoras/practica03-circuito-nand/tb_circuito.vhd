-- Testbench: recorre las 8 combinaciones de ABC y verifica que el circuito
-- original (estructural) y el simplificado den EXACTAMENTE lo mismo.
-- Si alguna fila no coincide, la simulacion se detiene con error.
library IEEE;
use IEEE.STD_LOGIC_1164.all;

entity tb_circuito is
end tb_circuito;

architecture t of tb_circuito is
  signal A, B, C : STD_LOGIC := '0';  -- := evita el 'U' del arranque
  signal F1, F2  : STD_LOGIC;
begin

  u_orig : entity work.circuito(estructural)   port map (A, B, C, F1);
  u_simp : entity work.circuito(simplificada) port map (A, B, C, F2);

  stim : process
    -- las 8 filas de la tabla de verdad, en orden 000..111
    type tabla_t is array (0 to 7) of STD_LOGIC_VECTOR(2 downto 0);
    constant casos : tabla_t := ("000","001","010","011","100","101","110","111");
    -- respuesta esperada de F = A'B' + C
    type resp_t   is array (0 to 7) of STD_LOGIC;
    constant esp  : resp_t := ('1','1','0','1','0','1','0','1');
  begin
    for i in casos'range loop
      A <= casos(i)(2); B <= casos(i)(1); C <= casos(i)(0);
      wait for 100 ns;
      assert (F1 = esp(i)) and (F2 = esp(i))
        report "FALLA en ABC=" & STD_LOGIC'image(casos(i)(2))
             & STD_LOGIC'image(casos(i)(1))
             & STD_LOGIC'image(casos(i)(0))
        severity failure;
    end loop;

    report "OK: las 8 filas coinciden. F = A'B' + C verificado.";
    wait;
  end process;

end t;
