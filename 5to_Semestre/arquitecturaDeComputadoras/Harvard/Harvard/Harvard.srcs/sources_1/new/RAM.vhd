----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 11/21/2026 10:41:12 PM
-- Design Name: 
-- Module Name: M_RAM - Behavioral
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

entity M_RAM is
    Port ( clk : in STD_LOGIC;
           dir_E : in STD_LOGIC_VECTOR (3 downto 0);
           dir_L : in STD_LOGIC_VECTOR (3 downto 0);
           dato_in : in STD_LOGIC_VECTOR (3 downto 0);
           dato_out : out STD_LOGIC_VECTOR (3 downto 0);
           L_E : in STD_LOGIC);
end M_RAM;

architecture Behavioral of M_RAM is


type RAM is array (0 to 15) of STD_LOGIC_VECTOR (3 downto 0);
signal memoria : RAM :=(others=>"0000");

begin
process(clk,dir_E,dir_L,dato_in,L_E)
begin
    if (clk'event and clk='1') then
        if (l_e='1') then -- escribir
            memoria(to_integer(unsigned(dir_E)))<=dato_in;
        else -- leer
            dato_out <=memoria (to_integer(unsigned(dir_L)));
        
        end if;
    end if;
end process;
end Behavioral;
