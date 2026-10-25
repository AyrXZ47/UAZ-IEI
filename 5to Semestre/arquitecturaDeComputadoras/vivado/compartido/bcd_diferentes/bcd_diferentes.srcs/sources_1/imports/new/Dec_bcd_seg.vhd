----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 26.09.2026 19:32:17
-- Design Name: 
-- Module Name: Dec_bcd_seg - Behavioral
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

entity Dec_bcd_seg is
    Port ( num : in STD_LOGIC_VECTOR (3 downto 0);
          -- display : in STD_LOGIC_VECTOR (7 downto 0);
           -- an : out STD_LOGIC_VECTOR (7 downto 0);
           seg : out STD_LOGIC_VECTOR (7 downto 0));
end Dec_bcd_seg;

architecture Behavioral of Dec_bcd_seg is

begin
--an<=display;
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
      ("00010001") when (num="1010") else -- numero A
      ("11000001") when (num="1011") else -- numero B
      ("01100011") when (num="1100") else -- numero C
      ("10000101") when (num="1101") else -- numero D
      ("01100001") when (num="1110") else -- numero E
      ("01110000") when (num="1111") else -- numero F
      ("11111111");
end Behavioral;
