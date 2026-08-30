-- Compuerta OR (diapositiva 32, "2 VHDL.pdf")
library IEEE;
use IEEE.STD_LOGIC_1164.all;

entity comp_or is
  port (
    A, B : in  STD_LOGIC;
    S    : out STD_LOGIC
  );
end comp_or;

architecture arq_comp_or of comp_or is
begin
  S <= A OR B;
end arq_comp_or;
