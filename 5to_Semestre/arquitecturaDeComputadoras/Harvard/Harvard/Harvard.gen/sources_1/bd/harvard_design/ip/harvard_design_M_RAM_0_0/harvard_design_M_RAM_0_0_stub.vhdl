-- Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
-- Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
-- --------------------------------------------------------------------------------
-- Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
-- Date        : Sat Nov 21 18:11:25 2026
-- Host        : nixos-laptop running 64-bit unknown
-- Command     : write_vhdl -force -mode synth_stub
--               /tmp/opencode/harvard_fix/Harvard/Harvard.gen/sources_1/bd/harvard_design/ip/harvard_design_M_RAM_0_0/harvard_design_M_RAM_0_0_stub.vhdl
-- Design      : harvard_design_M_RAM_0_0
-- Purpose     : Stub declaration of top-level module interface
-- Device      : xc7a35tcpg236-1
-- --------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity harvard_design_M_RAM_0_0 is
  Port ( 
    clk : in STD_LOGIC;
    dir_E : in STD_LOGIC_VECTOR ( 3 downto 0 );
    dir_L : in STD_LOGIC_VECTOR ( 3 downto 0 );
    dato_in : in STD_LOGIC_VECTOR ( 3 downto 0 );
    dato_out : out STD_LOGIC_VECTOR ( 3 downto 0 );
    L_E : in STD_LOGIC
  );

  attribute CHECK_LICENSE_TYPE : string;
  attribute CHECK_LICENSE_TYPE of harvard_design_M_RAM_0_0 : entity is "harvard_design_M_RAM_0_0,M_RAM,{}";
  attribute CORE_GENERATION_INFO : string;
  attribute CORE_GENERATION_INFO of harvard_design_M_RAM_0_0 : entity is "harvard_design_M_RAM_0_0,M_RAM,{x_ipProduct=Vivado 2026.1,x_ipVendor=xilinx.com,x_ipLibrary=module_ref,x_ipName=M_RAM,x_ipVersion=1.0,x_ipCoreRevision=1,x_ipLanguage=VERILOG,x_ipSimLanguage=MIXED}";
  attribute DowngradeIPIdentifiedWarnings : string;
  attribute DowngradeIPIdentifiedWarnings of harvard_design_M_RAM_0_0 : entity is "yes";
  attribute IP_DEFINITION_SOURCE : string;
  attribute IP_DEFINITION_SOURCE of harvard_design_M_RAM_0_0 : entity is "module_ref";
end harvard_design_M_RAM_0_0;

architecture stub of harvard_design_M_RAM_0_0 is
  attribute syn_black_box : boolean;
  attribute black_box_pad_pin : string;
  attribute syn_black_box of stub : architecture is true;
  attribute black_box_pad_pin of stub : architecture is "clk,dir_E[3:0],dir_L[3:0],dato_in[3:0],dato_out[3:0],L_E";
  attribute X_INTERFACE_INFO : string;
  attribute X_INTERFACE_INFO of clk : signal is "xilinx.com:signal:clock:1.0 clk CLK";
  attribute X_INTERFACE_MODE : string;
  attribute X_INTERFACE_MODE of clk : signal is "slave";
  attribute X_INTERFACE_PARAMETER : string;
  attribute X_INTERFACE_PARAMETER of clk : signal is "XIL_INTERFACENAME clk, FREQ_HZ 100000000, FREQ_TOLERANCE_HZ 0, PHASE 0.0, CLK_DOMAIN harvard_design_clk, INSERT_VIP 0";
  attribute X_CORE_INFO : string;
  attribute X_CORE_INFO of stub : architecture is "M_RAM,Vivado 2026.1";
begin
end;
