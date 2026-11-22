--Copyright 1986-2017 Xilinx, Inc. All Rights Reserved.
----------------------------------------------------------------------------------
--Tool Version: Vivado v.2017.4.1 (win64) Build 2117270 Tue Jan 30 15:32:00 MST 2018
--Date        : Sat Oct 10 14:53:50 2026
--Host        : txinerlaptop running 64-bit major release  (build 9200)
--Command     : generate_target design_1.bd
--Design      : design_1
--Purpose     : IP block netlist
----------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity design_1 is
  port (
    AN : out STD_LOGIC_VECTOR ( 7 downto 0 );
    SW : in STD_LOGIC_VECTOR ( 3 downto 0 );
    SW1 : in STD_LOGIC_VECTOR ( 7 downto 0 );
    seg : out STD_LOGIC_VECTOR ( 7 downto 0 )
  );
  attribute CORE_GENERATION_INFO : string;
  attribute CORE_GENERATION_INFO of design_1 : entity is "design_1,IP_Integrator,{x_ipVendor=xilinx.com,x_ipLibrary=BlockDiagram,x_ipName=design_1,x_ipVersion=1.00.a,x_ipLanguage=VHDL,numBlks=1,numReposBlks=1,numNonXlnxBlks=0,numHierBlks=0,maxHierDepth=0,numSysgenBlks=0,numHlsBlks=0,numHdlrefBlks=1,numPkgbdBlks=0,bdsource=USER,synth_mode=OOC_per_IP}";
  attribute HW_HANDOFF : string;
  attribute HW_HANDOFF of design_1 : entity is "design_1.hwdef";
end design_1;

architecture STRUCTURE of design_1 is
  component design_1_Dec_bcd_seg_0_0 is
  port (
    num : in STD_LOGIC_VECTOR ( 3 downto 0 );
    display : in STD_LOGIC_VECTOR ( 7 downto 0 );
    an : out STD_LOGIC_VECTOR ( 7 downto 0 );
    seg : out STD_LOGIC_VECTOR ( 7 downto 0 )
  );
  end component design_1_Dec_bcd_seg_0_0;
  signal Dec_bcd_seg_0_an : STD_LOGIC_VECTOR ( 7 downto 0 );
  signal Dec_bcd_seg_0_seg : STD_LOGIC_VECTOR ( 7 downto 0 );
  signal display_0_1 : STD_LOGIC_VECTOR ( 7 downto 0 );
  signal num_0_1 : STD_LOGIC_VECTOR ( 3 downto 0 );
begin
  AN(7 downto 0) <= Dec_bcd_seg_0_an(7 downto 0);
  display_0_1(7 downto 0) <= SW1(7 downto 0);
  num_0_1(3 downto 0) <= SW(3 downto 0);
  seg(7 downto 0) <= Dec_bcd_seg_0_seg(7 downto 0);
Dec_bcd_seg_0: component design_1_Dec_bcd_seg_0_0
     port map (
      an(7 downto 0) => Dec_bcd_seg_0_an(7 downto 0),
      display(7 downto 0) => display_0_1(7 downto 0),
      num(3 downto 0) => num_0_1(3 downto 0),
      seg(7 downto 0) => Dec_bcd_seg_0_seg(7 downto 0)
    );
end STRUCTURE;
