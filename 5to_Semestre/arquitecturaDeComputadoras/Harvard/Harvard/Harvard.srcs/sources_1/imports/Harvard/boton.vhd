----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 07.11.2026 15:34:33
-- Design Name: 
-- Module Name: boton - Behavioral
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

entity boton is
    Port ( clk : in STD_LOGIC;
           rst : in STD_LOGIC;
           ent : in STD_LOGIC;
           sal : out STD_LOGIC);
end boton;

architecture Behavioral of boton is
type ME_boton is (reposo, activa, uno, cero);-- estadaso 
signal EA: ME_boton;-- estado actual 
signal ES: ME_boton;-- estado siguiente
begin
-- sincronia 
process (clk , rst)
begin 
    if (rst ='1') then 
        ea<=reposo;
    elsif (clk'event and clk='1') then 
        ea<=es;
    end if;
end process;
-- salidad 
process (ea)
begin 
    if (ea=uno) then 
        sal<='1';
    else
        sal<='0';
    end if;
end process;
-- estado siguiente
process (ea, ent)
begin 
    case ea is 
        when reposo =>
            if (ent='1')then 
                es<=activa;
            else
                es<=reposo;
            end if;
        when activa =>
            if (ent='0')then 
                 es<=uno;
            else
                 es<=activa;
            end if;
        when uno=>
            es<=cero;
        when cero=>
            es<=reposo; 
        when others=>  
            es<=reposo;
    end case; 
end process;
end Behavioral;
