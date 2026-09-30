-- Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
-- Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
-- --------------------------------------------------------------------------------
-- Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
-- Date        : Sat Sep 26 16:03:03 2026
-- Host        : nixos-laptop running 64-bit unknown
-- Command     : write_vhdl -force -mode funcsim {/home/yovick/repos/UAZ-IEI/5to
--               Semestre/arquitecturaDeComputadoras/vivado/project_1/project_1.gen/sources_1/bd/design_leds/ip/design_leds_leds_0_0/design_leds_leds_0_0_sim_netlist.vhdl}
-- Design      : design_leds_leds_0_0
-- Purpose     : This VHDL netlist is a functional simulation representation of the design and should not be modified or
--               synthesized. This netlist cannot be used for SDF annotated simulation.
-- Device      : xc7a35tcpg236-1
-- --------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity design_leds_leds_0_0 is
  port (
    sw : in STD_LOGIC_VECTOR ( 15 downto 0 );
    led : out STD_LOGIC_VECTOR ( 15 downto 0 )
  );
  attribute NotValidForBitStream : boolean;
  attribute NotValidForBitStream of design_leds_leds_0_0 : entity is true;
  attribute CHECK_LICENSE_TYPE : string;
  attribute CHECK_LICENSE_TYPE of design_leds_leds_0_0 : entity is "design_leds_leds_0_0,leds,{}";
  attribute downgradeipidentifiedwarnings : string;
  attribute downgradeipidentifiedwarnings of design_leds_leds_0_0 : entity is "yes";
  attribute ip_definition_source : string;
  attribute ip_definition_source of design_leds_leds_0_0 : entity is "module_ref";
  attribute x_core_info : string;
  attribute x_core_info of design_leds_leds_0_0 : entity is "leds,Vivado 2026.1";
end design_leds_leds_0_0;

architecture STRUCTURE of design_leds_leds_0_0 is
  signal \^sw\ : STD_LOGIC_VECTOR ( 15 downto 0 );
begin
  \^sw\(15 downto 0) <= sw(15 downto 0);
  led(15 downto 0) <= \^sw\(15 downto 0);
end STRUCTURE;
