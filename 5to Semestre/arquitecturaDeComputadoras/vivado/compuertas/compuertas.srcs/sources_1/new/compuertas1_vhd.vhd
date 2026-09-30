----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 09/26/2026 11:03:26 PM
-- Design Name: 
-- Module Name: compuertas1_vhd - Behavioral
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

entity compuertas1_vhd is
    Port ( A : in STD_LOGIC;
           B : in STD_LOGIC;
           sel : in STD_LOGIC_VECTOR (2 downto 0);
           sal : out STD_LOGIC);
end compuertas1_vhd;

architecture Behavioral of compuertas1_vhd is

begin
process (sel,A,B)
begin
    case sel is 
        when "000"=>
            sal<=not A;
        when "001"=>
            sal<=not B;
        when "010"=>
            sal<=A and B;
        when "011"=>
            sal<=A or B;
        when "100"=>
            sal<=A nand B;
        when "101"=>
            sal<=A nor B;
        when "110"=>
            sal<=A xor B;
        when "111"=>
            sal<=A xnor B;
        when others=>
            sal<='0';

    end case;
end process;

end Behavioral;
