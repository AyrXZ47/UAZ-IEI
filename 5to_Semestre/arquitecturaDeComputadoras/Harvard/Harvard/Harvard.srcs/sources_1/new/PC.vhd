----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 11/21/2026 10:02:14 PM
-- Design Name: 
-- Module Name: PC - Behavioral
-- Project Name: Harvard
-- Target Devices: 
-- Tool Versions: 
-- Description: Contador de programa (Program Counter) de 4 bits.
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
use IEEE.STD_LOGIC_UNSIGNED.ALL; -- permite cont+1 sobre STD_LOGIC_VECTOR

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity PC is
    Port ( clk : in STD_LOGIC;
           rst : in STD_LOGIC;
           incremento : in STD_LOGIC;
           Dir : out STD_LOGIC_VECTOR (3 downto 0));
end PC;

architecture Behavioral of PC is
signal cont:STD_LOGIC_VECTOR (3 downto 0):="0000";
begin

process(clk,rst,incremento)
begin
    if (rst='1') then
        cont<="0000";
    elsif(clk'event and clk='1') then
        if (incremento ='1') then
            cont<=cont+1;
        end if;
    end if;
end process;

Dir<=cont;

end Behavioral;
