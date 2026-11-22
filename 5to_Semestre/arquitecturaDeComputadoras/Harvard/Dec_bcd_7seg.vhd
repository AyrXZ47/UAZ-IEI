----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 26.09.2026 19:31:38
-- Design Name: 
-- Module Name: Dec_bcd_7seg - Behavioral
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

entity Dec_bcd_7seg is
    Port ( num : in STD_LOGIC_VECTOR (3 downto 0);
           seg : out STD_LOGIC_VECTOR (7 downto 0));
end Dec_bcd_7seg;

architecture Behavioral of Dec_bcd_7seg is
begin -- A B C D E F G DP
seg<= ("00000011") when (num="0000") else -- numero 0
    ("10011111") when (num="0001") else -- numero 1
    ("00100101") when (num="0010") else -- numero 2
    ("00001101") when (num="0011") else -- numero 3
    ("10011001") when (num="0100") else -- numero 4
    ("01001001") when (num="0101") else -- numero 5
    ("01000001") when (num="0110") else -- numero 6
    ("00011111") when (num="0111") else -- numero 7
    ("00000001") when (num="1000") else -- numero 8
    ("00001001") when (num="1001") else -- numero 9
    ("00010000") when (num="1010") else -- numero A
    ("11000000") when (num="1011") else -- numero b
    ("01100010") when (num="1100") else -- numero C
    ("10000100") when (num="1101") else -- numero d
    ("01100000") when (num="1110") else -- numero E
    ("01110000") when (num="1111") else -- numero F
    ("11111111");
end Behavioral;
