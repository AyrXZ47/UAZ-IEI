-- Copyright 1986-2017 Xilinx, Inc. All Rights Reserved.
-- --------------------------------------------------------------------------------
-- Tool Version: Vivado v.2017.4.1 (win64) Build 2117270 Tue Jan 30 15:32:00 MST 2018
-- Date        : Sat Oct 10 14:49:58 2026
-- Host        : txinerlaptop running 64-bit major release  (build 9200)
-- Command     : write_vhdl -force -mode funcsim {c:/Users/janag/Documents/IEI/Arquitectura de
--               Computadoras/Proy_23400357/bcd_iguales/bcd_iguales.srcs/sources_1/bd/design_1/ip/design_1_Dec_bcd_seg_0_0/design_1_Dec_bcd_seg_0_0_sim_netlist.vhdl}
-- Design      : design_1_Dec_bcd_seg_0_0
-- Purpose     : This VHDL netlist is a functional simulation representation of the design and should not be modified or
--               synthesized. This netlist cannot be used for SDF annotated simulation.
-- Device      : xc7a100tcsg324-1
-- --------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity design_1_Dec_bcd_seg_0_0 is
  port (
    num : in STD_LOGIC_VECTOR ( 3 downto 0 );
    display : in STD_LOGIC_VECTOR ( 7 downto 0 );
    an : out STD_LOGIC_VECTOR ( 7 downto 0 );
    seg : out STD_LOGIC_VECTOR ( 7 downto 0 )
  );
  attribute NotValidForBitStream : boolean;
  attribute NotValidForBitStream of design_1_Dec_bcd_seg_0_0 : entity is true;
  attribute CHECK_LICENSE_TYPE : string;
  attribute CHECK_LICENSE_TYPE of design_1_Dec_bcd_seg_0_0 : entity is "design_1_Dec_bcd_seg_0_0,Dec_bcd_seg,{}";
  attribute downgradeipidentifiedwarnings : string;
  attribute downgradeipidentifiedwarnings of design_1_Dec_bcd_seg_0_0 : entity is "yes";
  attribute x_core_info : string;
  attribute x_core_info of design_1_Dec_bcd_seg_0_0 : entity is "Dec_bcd_seg,Vivado 2017.4.1";
end design_1_Dec_bcd_seg_0_0;

architecture STRUCTURE of design_1_Dec_bcd_seg_0_0 is
  signal \<const1>\ : STD_LOGIC;
  signal \^display\ : STD_LOGIC_VECTOR ( 7 downto 0 );
  signal \^seg\ : STD_LOGIC_VECTOR ( 7 downto 1 );
begin
  \^display\(7 downto 0) <= display(7 downto 0);
  an(7 downto 0) <= \^display\(7 downto 0);
  seg(7 downto 1) <= \^seg\(7 downto 1);
  seg(0) <= \<const1>\;
VCC: unisim.vcomponents.VCC
     port map (
      P => \<const1>\
    );
\seg[1]_INST_0\: unisim.vcomponents.LUT4
    generic map(
      INIT => X"4025"
    )
        port map (
      I0 => num(3),
      I1 => num(0),
      I2 => num(2),
      I3 => num(1),
      O => \^seg\(1)
    );
\seg[2]_INST_0\: unisim.vcomponents.LUT4
    generic map(
      INIT => X"5190"
    )
        port map (
      I0 => num(3),
      I1 => num(2),
      I2 => num(0),
      I3 => num(1),
      O => \^seg\(2)
    );
\seg[3]_INST_0\: unisim.vcomponents.LUT4
    generic map(
      INIT => X"5710"
    )
        port map (
      I0 => num(3),
      I1 => num(1),
      I2 => num(2),
      I3 => num(0),
      O => \^seg\(3)
    );
\seg[4]_INST_0\: unisim.vcomponents.LUT4
    generic map(
      INIT => X"C214"
    )
        port map (
      I0 => num(3),
      I1 => num(2),
      I2 => num(0),
      I3 => num(1),
      O => \^seg\(4)
    );
\seg[5]_INST_0\: unisim.vcomponents.LUT4
    generic map(
      INIT => X"A210"
    )
        port map (
      I0 => num(3),
      I1 => num(0),
      I2 => num(1),
      I3 => num(2),
      O => \^seg\(5)
    );
\seg[6]_INST_0\: unisim.vcomponents.LUT4
    generic map(
      INIT => X"AC48"
    )
        port map (
      I0 => num(3),
      I1 => num(2),
      I2 => num(0),
      I3 => num(1),
      O => \^seg\(6)
    );
\seg[7]_INST_0\: unisim.vcomponents.LUT4
    generic map(
      INIT => X"2094"
    )
        port map (
      I0 => num(3),
      I1 => num(2),
      I2 => num(0),
      I3 => num(1),
      O => \^seg\(7)
    );
end STRUCTURE;
