--Copyright 1986-2017 Xilinx, Inc. All Rights Reserved.
----------------------------------------------------------------------------------
--Tool Version: Vivado v.2017.4.1 (win64) Build 2117270 Tue Jan 30 15:32:00 MST 2018
--Date        : Sat Sep 26 16:04:52 2026
--Host        : txinerlaptop running 64-bit major release  (build 9200)
--Command     : generate_target PRUEBA_DESING_wrapper.bd
--Design      : PRUEBA_DESING_wrapper
--Purpose     : IP block netlist
----------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity PRUEBA_DESING_wrapper is
  port (
    LED : out STD_LOGIC_VECTOR ( 15 downto 0 );
    SW : in STD_LOGIC_VECTOR ( 15 downto 0 )
  );
end PRUEBA_DESING_wrapper;

architecture STRUCTURE of PRUEBA_DESING_wrapper is
  component PRUEBA_DESING is
  port (
    LED : out STD_LOGIC_VECTOR ( 15 downto 0 );
    SW : in STD_LOGIC_VECTOR ( 15 downto 0 )
  );
  end component PRUEBA_DESING;
begin
PRUEBA_DESING_i: component PRUEBA_DESING
     port map (
      LED(15 downto 0) => LED(15 downto 0),
      SW(15 downto 0) => SW(15 downto 0)
    );
end STRUCTURE;
