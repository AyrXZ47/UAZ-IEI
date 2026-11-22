--Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
--Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
----------------------------------------------------------------------------------
--Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
--Date        : Sat Oct 24 17:44:15 2026
--Host        : nixos-laptop running 64-bit unknown
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
    AN : out STD_LOGIC_VECTOR ( 7 downto 0 );
    CLK100MHZ : in STD_LOGIC;
    SW : in STD_LOGIC_VECTOR ( 15 downto 0 );
    rst : in STD_LOGIC;
    seg : out STD_LOGIC_VECTOR ( 7 downto 0 )
  );
end design_1_wrapper;

architecture STRUCTURE of design_1_wrapper is
  component design_1 is
  port (
    CLK100MHZ : in STD_LOGIC;
    rst : in STD_LOGIC;
    SW : in STD_LOGIC_VECTOR ( 15 downto 0 );
    seg : out STD_LOGIC_VECTOR ( 7 downto 0 );
    AN : out STD_LOGIC_VECTOR ( 7 downto 0 )
  );
  end component design_1;
begin
design_1_i: component design_1
     port map (
      AN(7 downto 0) => AN(7 downto 0),
      CLK100MHZ => CLK100MHZ,
      SW(15 downto 0) => SW(15 downto 0),
      rst => rst,
      seg(7 downto 0) => seg(7 downto 0)
    );
end STRUCTURE;
