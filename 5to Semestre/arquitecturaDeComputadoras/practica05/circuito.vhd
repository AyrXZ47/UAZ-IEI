-- Corrimientos de 4 bits controlados por ctrl (0..3), la logica copiada
-- del profe (con relleno '0' en el desplazamiento):
--   sal  via when/else, salW via with/select,
--   salC via case, salI via if/elsif. Las 4 deben dar la misma onda.
library IEEE;
use IEEE.STD_LOGIC_1164.all;

entity shift_wci_23400357 is
  port (
    ent  : in  STD_LOGIC_VECTOR(3 downto 0);
    ctrl : in  STD_LOGIC_VECTOR(1 downto 0);
    sal  : out STD_LOGIC_VECTOR(3 downto 0);  -- via when/else
    salC : out STD_LOGIC_VECTOR(3 downto 0);  -- via case
    salI : out STD_LOGIC_VECTOR(3 downto 0);  -- via if
    salW : out STD_LOGIC_VECTOR(3 downto 0)   -- via with/select
  );
end shift_wci_23400357;

architecture arqui_shift_wci of shift_wci_23400357 is
begin

  -- estructura condicional concurrente WHEN (sal)
  sal <= (ent)                          when (ctrl = "00") else
         ('0' & ent(3 downto 1))        when (ctrl = "01") else
         (ent(2 downto 0) & '0')        when (ctrl = "10") else
         (ent(0) & ent(1) & ent(2) & ent(3)) when (ctrl = "11") else
         "----";

  -- estructura condicional concurrente WITH (salW)
  with ctrl select
    salW <= (ent)                       when "00",
            ('0' & ent(3 downto 1))     when "01",
            (ent(2 downto 0) & '0')     when "10",
            (ent(0) & ent(1) & ent(2) & ent(3)) when "11",
            "----" when others;

  -- estructura secuencial CASE dentro de process (salC)
  process (ent, ctrl)
  begin
    case ctrl is
      when "00" =>
        salC <= ent;
      when "01" =>
        salC <= '0' & ent(3 downto 1);
      when "10" =>
        salC <= ent(2 downto 0) & '0';
      when "11" =>
        salC <= ent(0) & ent(1) & ent(2) & ent(3);
      when others =>
        salC <= "----";
    end case;
  end process;

  -- estructura secuencial IF dentro de process (salI)
  process (ent, ctrl)
  begin
    if (ctrl = "00") then
      salI <= ent;
    elsif (ctrl = "01") then
      salI <= '0' & ent(3 downto 1);
    elsif (ctrl = "10") then
      salI <= ent(2 downto 0) & '0';
    elsif (ctrl = "11") then
      salI <= ent(0) & ent(1) & ent(2) & ent(3);
    else
      salI <= "----";
    end if;
  end process;
end arqui_shift_wci;
