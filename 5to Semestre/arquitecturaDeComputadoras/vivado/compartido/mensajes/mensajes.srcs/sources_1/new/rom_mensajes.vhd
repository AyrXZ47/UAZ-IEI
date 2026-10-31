----------------------------------------------------------------------------------
-- Company:
-- Engineer:
--
-- Create Date: 30.10.2026
-- Design Name:
-- Module Name: rom_mensajes - Behavioral
-- Project Name: mensajes
-- Target Devices: Nexys4 DDR (xc7a100tcsg324-1)
-- Description: ROM de caracteres para los 8 displays de 7 segmentos.
--   sel = 0 -> "HOLA EIS"
--   sel = 1 -> "27803872"
--   dir = posicion del display (0 = AN0, el de la derecha).
--   seg = {a,b,c,d,e,f,g,dp}, activo bajo (mismo orden que Dec_bcd_seg).
----------------------------------------------------------------------------------

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity rom_mensajes is
    Port ( sel : in  STD_LOGIC;
           dir : in  STD_LOGIC_VECTOR (2 downto 0);
           seg : out STD_LOGIC_VECTOR (7 downto 0));
end rom_mensajes;

architecture Behavioral of rom_mensajes is

signal dir_sel : STD_LOGIC_VECTOR (3 downto 0);

begin

-- La direccion es {sel, dir}: 8 caracteres por mensaje.
dir_sel <= sel & dir;

process(dir_sel)
begin
    case dir_sel is
        -- sel = 0: "HOLA EIS"
        when "0000" => seg <= "01001001"; -- S
        when "0001" => seg <= "10011111"; -- I
        when "0010" => seg <= "01100001"; -- E
        when "0011" => seg <= "11111111"; -- (espacio)
        when "0100" => seg <= "00010001"; -- A
        when "0101" => seg <= "11100011"; -- L
        when "0110" => seg <= "00000011"; -- O
        when "0111" => seg <= "10001100"; -- H
        -- sel = 1: "27803872"
        when "1000" => seg <= "00100101"; -- 2
        when "1001" => seg <= "00011111"; -- 7
        when "1010" => seg <= "00000001"; -- 8
        when "1011" => seg <= "00001101"; -- 3
        when "1100" => seg <= "00000011"; -- 0
        when "1101" => seg <= "00000001"; -- 8
        when "1110" => seg <= "00011111"; -- 7
        when "1111" => seg <= "00100101"; -- 2
        when others => seg <= "11111111";
    end case;
end process;

end Behavioral;
