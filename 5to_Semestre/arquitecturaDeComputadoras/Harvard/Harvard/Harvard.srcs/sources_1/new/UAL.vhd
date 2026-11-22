----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 11/21/2026 09:41:15 PM
-- Design Name: 
-- Module Name: UAL - Behavioral
-- Project Name: Harvard
-- Target Devices: 
-- Tool Versions: 
-- Description: Unidad Aritmética Lógica de 4 bits.
--   op = "000" Suma        op = "100" XOR
--   op = "001" Resta       op = "101" NOT A
--   op = "010" AND         op = "110" A + 1
--   op = "011" OR          op = "111" A - 1
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
use IEEE.STD_LOGIC_UNSIGNED.ALL; -- permite + y - sobre STD_LOGIC_VECTOR

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity UAL is
    Port ( A : in STD_LOGIC_VECTOR (3 downto 0);
           B : in STD_LOGIC_VECTOR (3 downto 0);
           op : in STD_LOGIC_VECTOR (2 downto 0);
           res : out STD_LOGIC_VECTOR (3 downto 0);
           acarreo : out STD_LOGIC;
           cero : out STD_LOGIC);
end UAL;

architecture Behavioral of UAL is
signal auxA : STD_LOGIC_VECTOR (4 downto 0);
signal auxB : STD_LOGIC_VECTOR (4 downto 0);
signal auxRes : STD_LOGIC_VECTOR (4 downto 0);
begin

auxA <='0'&A;
auxB <= '0'&B;

process (a, b, op)
begin
    case (op) is
        when ("000") =>  -- Suma
            auxRes<=auxA+auxB;
        when ("001") =>  -- resta
            auxRes<=auxA-auxB;
        when ("010") =>  -- and
            auxRes<=auxA and auxB;
        when ("011") =>  -- or
            auxRes<=auxA or auxB;
        when ("100") =>  -- xor
            auxRes<=auxA xor auxB;
        when ("101") =>  -- not A
            auxRes<=not auxA;
        when ("110") =>  -- A+1
            auxRes<=auxA+1;
        when ("111") =>  -- A-1
            auxRes<=auxA-1;

    end case;
end process;

res <= auxRes(3 downto 0);
acarreo<=auxRes(4);
cero<='1' when (auxRes(3 downto 0)="0000") else '0';

end Behavioral;
