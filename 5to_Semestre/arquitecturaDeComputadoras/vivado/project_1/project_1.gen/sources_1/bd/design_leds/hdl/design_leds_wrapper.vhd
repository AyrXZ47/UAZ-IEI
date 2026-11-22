--Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
--Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
----------------------------------------------------------------------------------
--Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
--Date        : Sat Sep 26 16:02:31 2026
--Host        : nixos-laptop running 64-bit unknown
--Command     : generate_target design_leds_wrapper.bd
--Design      : design_leds_wrapper
--Purpose     : IP block netlist
----------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity design_leds_wrapper is
  port (
    led : out STD_LOGIC_VECTOR ( 15 downto 0 );
    sw : in STD_LOGIC_VECTOR ( 15 downto 0 )
  );
end design_leds_wrapper;

architecture STRUCTURE of design_leds_wrapper is
  component design_leds is
  port (
    sw : in STD_LOGIC_VECTOR ( 15 downto 0 );
    led : out STD_LOGIC_VECTOR ( 15 downto 0 )
  );
  end component design_leds;
begin
design_leds_i: component design_leds
     port map (
      led(15 downto 0) => led(15 downto 0),
      sw(15 downto 0) => sw(15 downto 0)
    );
end STRUCTURE;
