library IEEE;
use IEEE.STD_LOGIC_1164.all;

entity comp_igual_3bits is
  port (
    a   : in  STD_LOGIC_VECTOR(2 downto 0);
    b   : in  STD_LOGIC_VECTOR(2 downto 0);
    ig  : out STD_LOGIC
  );
end comp_igual_3bits;

architecture arqui_comp_igual_3bits of comp_igual_3bits is
begin
  ig <= '1' when a = b else '0';
end arqui_comp_igual_3bits;
