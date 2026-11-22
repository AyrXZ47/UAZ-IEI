-- Rotador/barrel shifter de 4 bits con when/else.
-- ctrl = "00": sin cambio, "01": corrimiento derecha con 0,
-- "10": corrimiento izquierda con 0, "11": rotacion izquierda.
library IEEE;
use IEEE.STD_LOGIC_1164.all;

entity shift_when_23400357 is
  port (
    ent  : in  STD_LOGIC_VECTOR(3 downto 0);
    ctrl : in  STD_LOGIC_VECTOR(1 downto 0);
    sal  : out STD_LOGIC_VECTOR(3 downto 0)
  );
end shift_when_23400357;

architecture arqui_shift_when_23400357 of shift_when_23400357 is
begin
  sal <= (ent)                          when (ctrl = "00") else
         ('0' & ent(3 downto 1))        when (ctrl = "01") else
         (ent(2 downto 0) & '0')        when (ctrl = "10") else
         (ent(0) & ent(1) & ent(2) & ent(3)) when (ctrl = "11") else
         "----";
end arqui_shift_when_23400357;
