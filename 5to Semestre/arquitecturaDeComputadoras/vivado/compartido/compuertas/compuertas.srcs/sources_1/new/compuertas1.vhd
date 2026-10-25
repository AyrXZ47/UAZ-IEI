----------------------------------------------------------------------------------
-- Company: UAZ UAIE IEI
-- Engineer: Javier Antonio Aguinyaga Pichardo
-- 
-- Create Date: 26.09.2026 18:03:18
-- Design Name: compuertas1
-- Module Name: compuertas1 - Behavioral
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

entity compuertas1 is
    Port ( A : in STD_LOGIC;
           B : in STD_LOGIC;
           sel : in STD_LOGIC_VECTOR (2 downto 0);
           sal : out STD_LOGIC);
end compuertas1;

architecture Behavioral of compuertas1 is

begin
process(sel,A,B)
begin
    case sel is
        when "000"=>
            sal<=not a;
        when "001"=>
            sal<=not b;
        when "010"=>
            sal<=a and b;
        when "011"=>
            sal<=a or b;
        when "100"=>
            sal<= a nand b;
        when "101"=>
            sal<=a nor b;
        when "110"=>
        sal<= a xor b;
        when "111"=>
        sal<=a xnor b;
        when others=>
        sal<='0';
end case;
end process;
end Behavioral;
