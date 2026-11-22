-- Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
-- Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
-- --------------------------------------------------------------------------------
-- Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
-- Date        : Sat Oct 24 17:45:26 2026
-- Host        : nixos-laptop running 64-bit unknown
-- Command     : write_vhdl -force -mode synth_stub {/home/yovick/repos/UAZ-IEI/5to
--               Semestre/arquitecturaDeComputadoras/vivado/compartido/bcd_diferentes/bcd_diferentes.gen/sources_1/bd/design_1/ip/design_1_mux_datos_0_0/design_1_mux_datos_0_0_stub.vhdl}
-- Design      : design_1_mux_datos_0_0
-- Purpose     : Stub declaration of top-level module interface
-- Device      : xc7a100tcsg324-1
-- --------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity design_1_mux_datos_0_0 is
  Port ( 
    sw : in STD_LOGIC_VECTOR ( 15 downto 0 );
    sel : in STD_LOGIC_VECTOR ( 2 downto 0 );
    sal : out STD_LOGIC_VECTOR ( 3 downto 0 )
  );

  attribute CHECK_LICENSE_TYPE : string;
  attribute CHECK_LICENSE_TYPE of design_1_mux_datos_0_0 : entity is "design_1_mux_datos_0_0,mux_datos,{}";
  attribute core_generation_info : string;
  attribute core_generation_info of design_1_mux_datos_0_0 : entity is "design_1_mux_datos_0_0,mux_datos,{x_ipProduct=Vivado 2026.1,x_ipVendor=xilinx.com,x_ipLibrary=module_ref,x_ipName=mux_datos,x_ipVersion=1.0,x_ipCoreRevision=1,x_ipLanguage=VHDL,x_ipSimLanguage=MIXED}";
  attribute downgradeipidentifiedwarnings : string;
  attribute downgradeipidentifiedwarnings of design_1_mux_datos_0_0 : entity is "yes";
  attribute ip_definition_source : string;
  attribute ip_definition_source of design_1_mux_datos_0_0 : entity is "module_ref";
end design_1_mux_datos_0_0;

architecture stub of design_1_mux_datos_0_0 is
  attribute syn_black_box : boolean;
  attribute black_box_pad_pin : string;
  attribute syn_black_box of stub : architecture is true;
  attribute black_box_pad_pin of stub : architecture is "sw[15:0],sel[2:0],sal[3:0]";
  attribute x_core_info : string;
  attribute x_core_info of stub : architecture is "mux_datos,Vivado 2026.1";
begin
end;
