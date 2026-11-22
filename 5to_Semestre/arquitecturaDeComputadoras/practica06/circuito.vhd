-- Tabla de verdad del profe: entra x[2:0], sale y[1:0].
--   x=000->01, 011->01, 110->01 : y=01
--   x=001->11, 111->11          : y=11
--   x=010->00                   : y=00
--   x=100->10, 101->10          : y=10
-- Mismas 8 filas, una salida por estructura: when, with, case, if.
library IEEE;
use IEEE.STD_LOGIC_1164.all;

entity tabla_wwci_23400357 is
  port (
    x  : in  STD_LOGIC_VECTOR(2 downto 0);
    y1 : out STD_LOGIC_VECTOR(1 downto 0);  -- via when/else
    y2 : out STD_LOGIC_VECTOR(1 downto 0);  -- via with/select
    y3 : out STD_LOGIC_VECTOR(1 downto 0);  -- via case
    y4 : out STD_LOGIC_VECTOR(1 downto 0)   -- via if
  );
end tabla_wwci_23400357;

architecture arqui_tabla of tabla_wwci_23400357 is
begin

  -- estructura condicional concurrente WHEN (y1)
  y1 <= "01" when (x = "000" or x = "011" or x = "110") else
        "11" when (x = "001" or x = "111") else
        "00" when (x = "010") else
        "10" when (x = "100" or x = "101") else
        "--";

  -- estructura de seleccion concurrente WITH (y2)
  with x select
    y2 <= "01" when "000",
          "11" when "001",
          "00" when "010",
          "01" when "011",
          "10" when "100",
          "10" when "101",
          "01" when "110",
          "11" when "111",
          "--" when others;

  -- estructura secuencial CASE dentro de process (y3)
  process (x)
  begin
    case x is
      when "000" => y3 <= "01";
      when "001" => y3 <= "11";
      when "010" => y3 <= "00";
      when "011" => y3 <= "01";
      when "100" => y3 <= "10";
      when "101" => y3 <= "10";
      when "110" => y3 <= "01";
      when "111" => y3 <= "11";
      when others => y3 <= "--";
    end case;
  end process;

  -- estructura secuencial IF dentro de process (y4)
  process (x)
  begin
    if (x = "000" or x = "011" or x = "110") then
      y4 <= "01";
    elsif (x = "001" or x = "111") then
      y4 <= "11";
    elsif (x = "010") then
      y4 <= "00";
    else
      y4 <= "10";
    end if;
  end process;
end arqui_tabla;
