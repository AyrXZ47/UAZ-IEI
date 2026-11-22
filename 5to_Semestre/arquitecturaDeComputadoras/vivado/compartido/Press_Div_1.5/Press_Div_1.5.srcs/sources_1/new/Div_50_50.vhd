----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 10.10.2026 17:25:32
-- Design Name: 
-- Module Name: Div_50_50 - Behavioral
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
use IEEE.STD_LOGIC_unsigned.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity Div_50_50 is
    Port ( clk : in STD_LOGIC;
           rst : in STD_LOGIC;
           clk_div : out STD_LOGIC);
end Div_50_50;

architecture Behavioral of Div_50_50 is
signal cont:std_logic_vector(26 downto 0):=(others=>'0');
signal cambio: std_logic:='0';
begin
 process(clk,rst)
  begin
  if (rst='1') then
    cont<=(others=>'0');
    cambio<='0';
  elsif (clk'event and clk='1') then
    cont<=cont+1;
    if (cont= "1000111100001101000111111111") then
        cambio<= not(cambio);
        cont<=(others=>'0');
    end if;
  end if;
end process;  
clk_div<=cambio;
end Behavioral;
