-- Testbench: barre las 4 posiciones del selector y las 512 combinaciones de
-- las 9 entradas (2048 casos) y COMPRUEBA la salida contra un modelo calculado
-- con las MISMAS expresiones, y ademas que la version estructural y la
-- simplificada coincidan. Asi el circuito se autoverifica: si algo se rompe,
-- la simulacion falla sola.
library IEEE;
use IEEE.STD_LOGIC_1164.all;
use IEEE.NUMERIC_STD.all;

entity tb_circuito is
end tb_circuito;

architecture t of tb_circuito is
  signal ent : STD_LOGIC_VECTOR(8 downto 0) := (others => '0');
  signal s   : STD_LOGIC_VECTOR(1 downto 0) := "00";
  signal sal_est, sal_sim : STD_LOGIC;
begin

  -- Dos instancias: la del diagrama (estructural) y la de una linea (simplificada).
  uut_est : entity work.mux4x1_logica_23400357(estructural)
            port map (ent, s, sal_est);
  uut_sim : entity work.mux4x1_logica_23400357(simplificada)
            port map (ent, s, sal_sim);

  stim : process
    variable c0, c1, c2, c3, esperado : STD_LOGIC;
    variable e : STD_LOGIC_VECTOR(8 downto 0);
    variable fallos : integer := 0;
  begin
    -- Recorre las 4 opciones del selector y las 512 combinaciones de entradas.
    for k in 0 to 3 loop
      s <= STD_LOGIC_VECTOR(to_unsigned(k, 2));
      for i in 0 to 511 loop
        e := STD_LOGIC_VECTOR(to_unsigned(i, 9));
        ent <= e;
        wait for 1 ns;

        -- Modelo de referencia: las expresiones del diagrama.
        c0 := (not e(0)) or e(1);
        c1 := not ((not (e(2) or e(3) or e(4))) and e(5));
        c2 := (e(5) and e(6)) or (e(7) and e(8));
        c3 := (e(5) and e(6) and e(7)) xor e(8);

        case k is
          when 0    => esperado := c0;
          when 1    => esperado := c1;
          when 2    => esperado := c2;
          when others => esperado := c3;
        end case;

        -- Las dos arquitecturas deben dar lo mismo que el modelo.
        assert sal_est = esperado
          report "estructural: caso " & integer'image(i) & " s="
               & integer'image(k) & " dio " & STD_LOGIC'image(sal_est)
          severity error;
        assert sal_sim = esperado
          report "simplificada: caso " & integer'image(i) & " s="
               & integer'image(k) & " dio " & STD_LOGIC'image(sal_sim)
          severity error;

        if (sal_est /= esperado) or (sal_sim /= esperado) then
          fallos := fallos + 1;
        end if;
      end loop;
    end loop;

    assert fallos = 0 report "Fallaron " & integer'image(fallos) & " casos."
      severity failure;
    report "OK: 4 selectores x 512 combinaciones = 2048 casos correctos.";
    wait;
  end process;

end t;
