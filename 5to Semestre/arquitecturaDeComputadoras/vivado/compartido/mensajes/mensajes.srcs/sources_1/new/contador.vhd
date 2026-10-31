----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 24.10.2026 16:09:48
-- Design Name: 
-- Module Name: contador - Behavioral
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

entity contador is
    Port ( clk : in STD_LOGIC;
           rst : in STD_LOGIC;
           display : out std_logic_vector (2 downto 0));
end contador;

architecture Behavioral of contador is

signal auxN:std_logic_vector(2 downto 0):="000";

begin
    process(clk,rst)
    begin
        if (rst='1') then
        auxN<="000";
        elsif (clk'event and clk='1')then
            auxN<=auxN+1;
            end if;
            end process;
display<=auxN;
end Behavioral;
