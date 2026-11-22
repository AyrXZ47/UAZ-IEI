----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 11/21/2026 09:41:15 PM
-- Design Name: 
-- Module Name: UC - Behavioral
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

entity UC is
    Port ( clk : in STD_LOGIC;
           rst : in STD_LOGIC;
           A_in : in STD_LOGIC_VECTOR (3 downto 0);
           B_in : in STD_LOGIC_VECTOR (3 downto 0);
           op_in : in STD_LOGIC_VECTOR (2 downto 0);
           dir_in : in STD_LOGIC_VECTOR (3 downto 0);
           ejecutar : in STD_LOGIC;
           A_out : out STD_LOGIC_VECTOR (3 downto 0);
           B_out : out STD_LOGIC_VECTOR (3 downto 0);
           op_out : out STD_LOGIC_VECTOR (2 downto 0);
           dir_out : out STD_LOGIC_VECTOR (3 downto 0);
           incrementar : out STD_LOGIC;
           L_E : out STD_LOGIC);
end UC;

architecture Behavioral of UC is

begin




A_out<=A_in;
B_out<=B_in;
op_out<=op_in;
dir_out<=dir_in;

    process(a_in,b_in,op_in,dir_in,ejecutar,clk,rst)
    begin
        if (rst='1') then
            incrementar<='0';
            L_E<='0';
        elsif (clk'event and clk='1') then
            if (ejecutar ='1') then
                incrementar<='1';
                L_E<='1';
            else 
                incrementar<='0';
                L_E<='0';
            end if;
        end if;
    end process;
    
    end Behavioral;