--Copyright 1986-2017 Xilinx, Inc. All Rights Reserved.
----------------------------------------------------------------------------------
--Tool Version: Vivado v.2017.4.1 (win64) Build 2117270 Tue Jan 30 15:32:00 MST 2018
--Date        : Sat Oct 10 17:20:41 2026
--Host        : txinerlaptop running 64-bit major release  (build 9200)
--Command     : generate_target design_1_wrapper.bd
--Design      : design_1_wrapper
--Purpose     : IP block netlist
----------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity design_1_wrapper is
  port (
    BTNC : in STD_LOGIC;
    LED : out STD_LOGIC;
    clk : in STD_LOGIC
  );
end design_1_wrapper;

architecture STRUCTURE of design_1_wrapper is
  component design_1 is
  port (
    clk : in STD_LOGIC;
    BTNC : in STD_LOGIC;
    LED : out STD_LOGIC
  );
  end component design_1;
begin
design_1_i: component design_1
     port map (
      BTNC => BTNC,
      LED => LED,
      clk => clk
    );
end STRUCTURE;
