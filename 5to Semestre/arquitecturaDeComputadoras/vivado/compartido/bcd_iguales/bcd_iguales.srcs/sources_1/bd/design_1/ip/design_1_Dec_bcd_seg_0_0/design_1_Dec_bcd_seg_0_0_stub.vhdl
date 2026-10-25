-- Copyright 1986-2017 Xilinx, Inc. All Rights Reserved.
-- --------------------------------------------------------------------------------
-- Tool Version: Vivado v.2017.4.1 (win64) Build 2117270 Tue Jan 30 15:32:00 MST 2018
-- Date        : Sat Oct 10 14:49:58 2026
-- Host        : txinerlaptop running 64-bit major release  (build 9200)
-- Command     : write_vhdl -force -mode synth_stub {c:/Users/janag/Documents/IEI/Arquitectura de
--               Computadoras/Proy_23400357/bcd_iguales/bcd_iguales.srcs/sources_1/bd/design_1/ip/design_1_Dec_bcd_seg_0_0/design_1_Dec_bcd_seg_0_0_stub.vhdl}
-- Design      : design_1_Dec_bcd_seg_0_0
-- Purpose     : Stub declaration of top-level module interface
-- Device      : xc7a100tcsg324-1
-- --------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity design_1_Dec_bcd_seg_0_0 is
  Port ( 
    num : in STD_LOGIC_VECTOR ( 3 downto 0 );
    display : in STD_LOGIC_VECTOR ( 7 downto 0 );
    an : out STD_LOGIC_VECTOR ( 7 downto 0 );
    seg : out STD_LOGIC_VECTOR ( 7 downto 0 )
  );

end design_1_Dec_bcd_seg_0_0;

architecture stub of design_1_Dec_bcd_seg_0_0 is
attribute syn_black_box : boolean;
attribute black_box_pad_pin : string;
attribute syn_black_box of stub : architecture is true;
attribute black_box_pad_pin of stub : architecture is "num[3:0],display[7:0],an[7:0],seg[7:0]";
attribute x_core_info : string;
attribute x_core_info of stub : architecture is "Dec_bcd_seg,Vivado 2017.4.1";
begin
end;
