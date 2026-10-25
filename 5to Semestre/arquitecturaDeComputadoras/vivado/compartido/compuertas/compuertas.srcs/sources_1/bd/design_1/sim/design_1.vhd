--Copyright 1986-2017 Xilinx, Inc. All Rights Reserved.
----------------------------------------------------------------------------------
--Tool Version: Vivado v.2017.4.1 (win64) Build 2117270 Tue Jan 30 15:32:00 MST 2018
--Date        : Sat Sep 26 17:51:18 2026
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
    A : in STD_LOGIC;
    B : in STD_LOGIC;
    sal : out STD_LOGIC;
    sel : in STD_LOGIC_VECTOR ( 2 downto 0 )
  );
  attribute CORE_GENERATION_INFO : string;
  attribute CORE_GENERATION_INFO of design_1 : entity is "design_1,IP_Integrator,{x_ipVendor=xilinx.com,x_ipLibrary=BlockDiagram,x_ipName=design_1,x_ipVersion=1.00.a,x_ipLanguage=VHDL,numBlks=1,numReposBlks=1,numNonXlnxBlks=0,numHierBlks=0,maxHierDepth=0,numSysgenBlks=0,numHlsBlks=0,numHdlrefBlks=1,numPkgbdBlks=0,bdsource=USER,synth_mode=OOC_per_IP}";
  attribute HW_HANDOFF : string;
  attribute HW_HANDOFF of design_1 : entity is "design_1.hwdef";
end design_1;

architecture STRUCTURE of design_1 is
  component design_1_compuertas1_0_0 is
  port (
    A : in STD_LOGIC;
    B : in STD_LOGIC;
    sel : in STD_LOGIC_VECTOR ( 2 downto 0 );
    sal : out STD_LOGIC
  );
  end component design_1_compuertas1_0_0;
  signal A_0_1 : STD_LOGIC;
  signal B_0_1 : STD_LOGIC;
  signal compuertas1_0_sal : STD_LOGIC;
  signal sel_0_1 : STD_LOGIC_VECTOR ( 2 downto 0 );
begin
  A_0_1 <= A;
  B_0_1 <= B;
  sal <= compuertas1_0_sal;
  sel_0_1(2 downto 0) <= sel(2 downto 0);
compuertas1_0: component design_1_compuertas1_0_0
     port map (
      A => A_0_1,
      B => B_0_1,
      sal => compuertas1_0_sal,
      sel(2 downto 0) => sel_0_1(2 downto 0)
    );
end STRUCTURE;
