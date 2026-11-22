-- Testbench del demux 1x4: reproduce EXACTAMENTE lo que hizo el profe en
-- clase con sus "selectores de 100ns": A se queda en '1' toda la simulacion
-- (recuerda: cualquier valor distinto de 0) y SEL va cambiando cada 100 ns.
--
-- En GTKWave se vera el '1' saltando de SAL(0) -> SAL(1) -> SAL(2) -> SAL(3)
-- siguiendo a SEL. Eso ES un demux, visto en el tiempo.
library IEEE;
use IEEE.STD_LOGIC_1164.all;

entity tb_demux1x4 is
end tb_demux1x4;

architecture t of tb_demux1x4 is
  -- Inicializar con := evita el 'U' del arranque (sin esto, a t=0 todo es U/X)
  signal A   : STD_LOGIC := '1';
  signal SEL : STD_LOGIC_VECTOR(1 downto 0) := "00";
  signal SAL : STD_LOGIC_VECTOR(3 downto 0);
begin

  uut : entity work.demux1x4 port map (A => A, SEL => SEL, SAL => SAL);

  stim : process
  begin
    SEL <= "00"; wait for 100 ns;
    assert SAL = "0001" report "SEL=00: SAL deberia ser 0001" severity failure;

    SEL <= "01"; wait for 100 ns;
    assert SAL = "0010" report "SEL=01: SAL deberia ser 0010" severity failure;

    SEL <= "10"; wait for 100 ns;
    assert SAL = "0100" report "SEL=10: SAL deberia ser 0100" severity failure;

    SEL <= "11"; wait for 100 ns;
    assert SAL = "1000" report "SEL=11: SAL deberia ser 1000" severity failure;

    report "OK: el '1' de A recorrio SAL(0)->SAL(3) siguiendo a SEL (400 ns)";
    wait;
  end process;

end t;
