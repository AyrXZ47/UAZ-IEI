--Copyright 1986-2017 Xilinx, Inc. All Rights Reserved.
----------------------------------------------------------------------------------
--Tool Version: Vivado v.2017.4.1 (win64) Build 2117270 Tue Jan 30 15:32:00 MST 2018
--Date        : Sat Sep 26 16:04:52 2026
--Host        : txinerlaptop running 64-bit major release  (build 9200)
--Command     : generate_target PRUEBA_DESING.bd
--Design      : PRUEBA_DESING
--Purpose     : IP block netlist
----------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity PRUEBA_DESING is
  port (
    LED : out STD_LOGIC_VECTOR ( 15 downto 0 );
    SW : in STD_LOGIC_VECTOR ( 15 downto 0 )
  );
  attribute CORE_GENERATION_INFO : string;
  attribute CORE_GENERATION_INFO of PRUEBA_DESING : entity is "PRUEBA_DESING,IP_Integrator,{x_ipVendor=xilinx.com,x_ipLibrary=BlockDiagram,x_ipName=PRUEBA_DESING,x_ipVersion=1.00.a,x_ipLanguage=VHDL,numBlks=1,numReposBlks=1,numNonXlnxBlks=0,numHierBlks=0,maxHierDepth=0,numSysgenBlks=0,numHlsBlks=0,numHdlrefBlks=1,numPkgbdBlks=0,bdsource=USER,synth_mode=OOC_per_IP}";
  attribute HW_HANDOFF : string;
  attribute HW_HANDOFF of PRUEBA_DESING : entity is "PRUEBA_DESING.hwdef";
end PRUEBA_DESING;

architecture STRUCTURE of PRUEBA_DESING is
  component PRUEBA_DESING_FUENTE_PRUEBA_0_0 is
  port (
    SW : in STD_LOGIC_VECTOR ( 15 downto 0 );
    LED : out STD_LOGIC_VECTOR ( 15 downto 0 )
  );
  end component PRUEBA_DESING_FUENTE_PRUEBA_0_0;
  signal FUENTE_PRUEBA_0_LED : STD_LOGIC_VECTOR ( 15 downto 0 );
  signal SW_0_1 : STD_LOGIC_VECTOR ( 15 downto 0 );
begin
  LED(15 downto 0) <= FUENTE_PRUEBA_0_LED(15 downto 0);
  SW_0_1(15 downto 0) <= SW(15 downto 0);
FUENTE_PRUEBA_0: component PRUEBA_DESING_FUENTE_PRUEBA_0_0
     port map (
      LED(15 downto 0) => FUENTE_PRUEBA_0_LED(15 downto 0),
      SW(15 downto 0) => SW_0_1(15 downto 0)
    );
end STRUCTURE;
