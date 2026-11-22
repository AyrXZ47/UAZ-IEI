----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 24.10.2026 16:53:04
-- Design Name: 
-- Module Name: mux_datos - Behavioral
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

entity mux_datos is
    Port ( sw : in STD_LOGIC_VECTOR (15 downto 0);
           sel : in STD_LOGIC_VECTOR (2 downto 0);
           sal : out STD_LOGIC_VECTOR (3 downto 0));
end mux_datos;

architecture Behavioral of mux_datos is

begin

with sel select
    sal<=(sw(3 downto 0))when("000"),
    (sw(7 downto 4))when("001"),
    (sw(11 downto 8))when("010"),
    (sw(15 downto 12))when("011"),
    (sw(3 downto 0))when("100"),
    (sw(7 downto 4))when("101"),
    (sw(11 downto 8))when("110"),
    (sw(15 downto 12))when("111"), 
    "0000" when others;
end Behavioral;
