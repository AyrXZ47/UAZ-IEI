----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 24.10.2026 16:37:10
-- Design Name: 
-- Module Name: dec_an - Behavioral
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

entity dec_an is
    Port ( ent : in STD_LOGIC_VECTOR (2 downto 0);
           sal : out STD_LOGIC_VECTOR (7 downto 0));
end dec_an;

architecture Behavioral of dec_an is

begin
sal<=("11111110") when (ent="000") else
("11111101") when (ent="001") else
("11111011") when (ent="010") else
("11110111") when (ent="011") else
("11101111") when (ent="100") else
("11011111") when (ent="101") else
("10111111") when (ent="110") else
("01111111") when (ent="111") else
("11111111");
end Behavioral;
