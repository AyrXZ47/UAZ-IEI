----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 24.10.2026 17:07:54
-- Design Name: 
-- Module Name: pres_500hz - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: 
-- 
-- Dependencies: 
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
-- 
----------------------------------------------------------------------------------


library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity pres_500hz is
    generic(frec_in:integer:=100000000;
    frec_out:integer:=500;
    num_display:integer:=8
    );
    Port ( clk : in STD_LOGIC;
           rst : in STD_LOGIC;
           clk_pres : out STD_LOGIC);
end pres_500hz;

architecture Behavioral of pres_500hz is

signal cont: integer range 0 to (frec_in/frec_out/num_display):=0;
constant fin:integer :=(frec_in/frec_out/num_display)-1;
begin
process (clk,rst)
begin
    if (rst='1') then
        cont<=0;
        clk_pres<='0';
    elsif (clk'event and clk='1') then
            cont<=cont+1;
            if (cont=fin) then
            clk_pres<='1';
            cont<=0;
            else
            clk_pres<='0';
            end if;
            end if;
end process;
end Behavioral;
