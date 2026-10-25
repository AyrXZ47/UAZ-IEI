-- Copyright 1986-2017 Xilinx, Inc. All Rights Reserved.
-- --------------------------------------------------------------------------------
-- Tool Version: Vivado v.2017.4.1 (win64) Build 2117270 Tue Jan 30 15:32:00 MST 2018
-- Date        : Sat Sep 26 16:05:29 2026
-- Host        : txinerlaptop running 64-bit major release  (build 9200)
-- Command     : write_vhdl -force -mode funcsim {c:/Users/janag/Documents/IEI/Arquitectura de
--               Computadoras/Proy_23400357/project_23400357/project_23400357.srcs/sources_1/bd/PRUEBA_DESING/ip/PRUEBA_DESING_FUENTE_PRUEBA_0_0/PRUEBA_DESING_FUENTE_PRUEBA_0_0_sim_netlist.vhdl}
-- Design      : PRUEBA_DESING_FUENTE_PRUEBA_0_0
-- Purpose     : This VHDL netlist is a functional simulation representation of the design and should not be modified or
--               synthesized. This netlist cannot be used for SDF annotated simulation.
-- Device      : xc7a100tcsg324-1
-- --------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity PRUEBA_DESING_FUENTE_PRUEBA_0_0 is
  port (
    SW : in STD_LOGIC_VECTOR ( 15 downto 0 );
    LED : out STD_LOGIC_VECTOR ( 15 downto 0 )
  );
  attribute NotValidForBitStream : boolean;
  attribute NotValidForBitStream of PRUEBA_DESING_FUENTE_PRUEBA_0_0 : entity is true;
  attribute CHECK_LICENSE_TYPE : string;
  attribute CHECK_LICENSE_TYPE of PRUEBA_DESING_FUENTE_PRUEBA_0_0 : entity is "PRUEBA_DESING_FUENTE_PRUEBA_0_0,FUENTE_PRUEBA,{}";
  attribute downgradeipidentifiedwarnings : string;
  attribute downgradeipidentifiedwarnings of PRUEBA_DESING_FUENTE_PRUEBA_0_0 : entity is "yes";
  attribute x_core_info : string;
  attribute x_core_info of PRUEBA_DESING_FUENTE_PRUEBA_0_0 : entity is "FUENTE_PRUEBA,Vivado 2017.4.1";
end PRUEBA_DESING_FUENTE_PRUEBA_0_0;

architecture STRUCTURE of PRUEBA_DESING_FUENTE_PRUEBA_0_0 is
  signal \^sw\ : STD_LOGIC_VECTOR ( 15 downto 0 );
begin
  LED(15 downto 0) <= \^sw\(15 downto 0);
  \^sw\(15 downto 0) <= SW(15 downto 0);
end STRUCTURE;
