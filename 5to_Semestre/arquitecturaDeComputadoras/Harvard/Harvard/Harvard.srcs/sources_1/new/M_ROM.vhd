----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 11/21/2026 10:11:42 PM
-- Design Name: 
-- Module Name: M_ROM - Behavioral
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
use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity M_ROM is
    Port ( clk : in STD_LOGIC;
           dir : in STD_LOGIC_VECTOR (3 downto 0);
           dato : out STD_LOGIC_VECTOR (2 downto 0));
end M_ROM;

architecture Behavioral of M_ROM is


type ROM is array (0 to 15) of STD_LOGIC_VECTOR (2 downto 0);
constant memoria : ROM :=("000","000","000","001","000","001","001","000",
                          "001","010","011","100","101","110","111","000");

begin

process (clk)
begin
    if (clk'event and clk='1') then
        dato<=memoria(to_integer(unsigned(dir)));
    end if;
end process;    


end Behavioral;
