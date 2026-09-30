--Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
--Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
----------------------------------------------------------------------------------
--Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
--Date        : Sat Sep 26 17:44:46 2026
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
    A : in STD_LOGIC;
    B : in STD_LOGIC;
    sal : out STD_LOGIC;
    sel : in STD_LOGIC_VECTOR ( 2 downto 0 )
  );
end design_1_wrapper;

architecture STRUCTURE of design_1_wrapper is
  component design_1 is
  port (
    A : in STD_LOGIC;
    B : in STD_LOGIC;
    sel : in STD_LOGIC_VECTOR ( 2 downto 0 );
    sal : out STD_LOGIC
  );
  end component design_1;
begin
design_1_i: component design_1
     port map (
      A => A,
      B => B,
      sal => sal,
      sel(2 downto 0) => sel(2 downto 0)
    );
end STRUCTURE;
