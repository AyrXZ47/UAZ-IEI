-- Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
-- Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
-- --------------------------------------------------------------------------------
-- Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
-- Date        : Sat Nov 21 18:12:07 2026
-- Host        : nixos-laptop running 64-bit unknown
-- Command     : write_vhdl -force -mode synth_stub
--               /tmp/opencode/harvard_fix/Harvard/Harvard.gen/sources_1/bd/harvard_design/ip/harvard_design_UAL_0_0/harvard_design_UAL_0_0_stub.vhdl
-- Design      : harvard_design_UAL_0_0
-- Purpose     : Stub declaration of top-level module interface
-- Device      : xc7a35tcpg236-1
-- --------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity harvard_design_UAL_0_0 is
  Port ( 
    A : in STD_LOGIC_VECTOR ( 3 downto 0 );
    B : in STD_LOGIC_VECTOR ( 3 downto 0 );
    op : in STD_LOGIC_VECTOR ( 2 downto 0 );
    res : out STD_LOGIC_VECTOR ( 3 downto 0 );
    acarreo : out STD_LOGIC;
    cero : out STD_LOGIC
  );

  attribute CHECK_LICENSE_TYPE : string;
  attribute CHECK_LICENSE_TYPE of harvard_design_UAL_0_0 : entity is "harvard_design_UAL_0_0,UAL,{}";
  attribute CORE_GENERATION_INFO : string;
  attribute CORE_GENERATION_INFO of harvard_design_UAL_0_0 : entity is "harvard_design_UAL_0_0,UAL,{x_ipProduct=Vivado 2026.1,x_ipVendor=xilinx.com,x_ipLibrary=module_ref,x_ipName=UAL,x_ipVersion=1.0,x_ipCoreRevision=1,x_ipLanguage=VERILOG,x_ipSimLanguage=MIXED}";
  attribute DowngradeIPIdentifiedWarnings : string;
  attribute DowngradeIPIdentifiedWarnings of harvard_design_UAL_0_0 : entity is "yes";
  attribute IP_DEFINITION_SOURCE : string;
  attribute IP_DEFINITION_SOURCE of harvard_design_UAL_0_0 : entity is "module_ref";
end harvard_design_UAL_0_0;

architecture stub of harvard_design_UAL_0_0 is
  attribute syn_black_box : boolean;
  attribute black_box_pad_pin : string;
  attribute syn_black_box of stub : architecture is true;
  attribute black_box_pad_pin of stub : architecture is "A[3:0],B[3:0],op[2:0],res[3:0],acarreo,cero";
  attribute X_CORE_INFO : string;
  attribute X_CORE_INFO of stub : architecture is "UAL,Vivado 2026.1";
begin
end;
