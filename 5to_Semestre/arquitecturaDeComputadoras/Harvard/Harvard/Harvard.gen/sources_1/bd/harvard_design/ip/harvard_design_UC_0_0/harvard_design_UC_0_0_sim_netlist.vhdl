-- Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
-- Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
-- --------------------------------------------------------------------------------
-- Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
-- Date        : Sat Nov 21 18:11:25 2026
-- Host        : nixos-laptop running 64-bit unknown
-- Command     : write_vhdl -force -mode funcsim
--               /tmp/opencode/harvard_fix/Harvard/Harvard.gen/sources_1/bd/harvard_design/ip/harvard_design_UC_0_0/harvard_design_UC_0_0_sim_netlist.vhdl
-- Design      : harvard_design_UC_0_0
-- Purpose     : This VHDL netlist is a functional simulation representation of the design and should not be modified or
--               synthesized. This netlist cannot be used for SDF annotated simulation.
-- Device      : xc7a35tcpg236-1
-- --------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity harvard_design_UC_0_0_UC is
  port (
    L_E : out STD_LOGIC;
    ejecutar : in STD_LOGIC;
    clk : in STD_LOGIC;
    rst : in STD_LOGIC
  );
  attribute ORIG_REF_NAME : string;
  attribute ORIG_REF_NAME of harvard_design_UC_0_0_UC : entity is "UC";
end harvard_design_UC_0_0_UC;

architecture STRUCTURE of harvard_design_UC_0_0_UC is
begin
incrementar_reg: unisim.vcomponents.FDCE
     port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => ejecutar,
      Q => L_E
    );
end STRUCTURE;
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity harvard_design_UC_0_0 is
  port (
    clk : in STD_LOGIC;
    rst : in STD_LOGIC;
    A_in : in STD_LOGIC_VECTOR ( 3 downto 0 );
    B_in : in STD_LOGIC_VECTOR ( 3 downto 0 );
    op_in : in STD_LOGIC_VECTOR ( 2 downto 0 );
    dir_in : in STD_LOGIC_VECTOR ( 3 downto 0 );
    ejecutar : in STD_LOGIC;
    A_out : out STD_LOGIC_VECTOR ( 3 downto 0 );
    B_out : out STD_LOGIC_VECTOR ( 3 downto 0 );
    op_out : out STD_LOGIC_VECTOR ( 2 downto 0 );
    dir_out : out STD_LOGIC_VECTOR ( 3 downto 0 );
    incrementar : out STD_LOGIC;
    L_E : out STD_LOGIC
  );
  attribute NotValidForBitStream : boolean;
  attribute NotValidForBitStream of harvard_design_UC_0_0 : entity is true;
  attribute CHECK_LICENSE_TYPE : string;
  attribute CHECK_LICENSE_TYPE of harvard_design_UC_0_0 : entity is "harvard_design_UC_0_0,UC,{}";
  attribute DowngradeIPIdentifiedWarnings : string;
  attribute DowngradeIPIdentifiedWarnings of harvard_design_UC_0_0 : entity is "yes";
  attribute IP_DEFINITION_SOURCE : string;
  attribute IP_DEFINITION_SOURCE of harvard_design_UC_0_0 : entity is "module_ref";
  attribute X_CORE_INFO : string;
  attribute X_CORE_INFO of harvard_design_UC_0_0 : entity is "UC,Vivado 2026.1";
end harvard_design_UC_0_0;

architecture STRUCTURE of harvard_design_UC_0_0 is
  signal \^a_in\ : STD_LOGIC_VECTOR ( 3 downto 0 );
  signal \^b_in\ : STD_LOGIC_VECTOR ( 3 downto 0 );
  signal \^l_e\ : STD_LOGIC;
  signal \^dir_in\ : STD_LOGIC_VECTOR ( 3 downto 0 );
  signal \^op_in\ : STD_LOGIC_VECTOR ( 2 downto 0 );
  attribute X_INTERFACE_INFO : string;
  attribute X_INTERFACE_INFO of clk : signal is "xilinx.com:signal:clock:1.0 clk CLK";
  attribute X_INTERFACE_MODE : string;
  attribute X_INTERFACE_MODE of clk : signal is "slave";
  attribute X_INTERFACE_PARAMETER : string;
  attribute X_INTERFACE_PARAMETER of clk : signal is "XIL_INTERFACENAME clk, ASSOCIATED_RESET rst, FREQ_HZ 100000000, FREQ_TOLERANCE_HZ 0, PHASE 0.0, CLK_DOMAIN harvard_design_clk, INSERT_VIP 0";
  attribute X_INTERFACE_INFO of rst : signal is "xilinx.com:signal:reset:1.0 rst RST";
  attribute X_INTERFACE_MODE of rst : signal is "slave";
  attribute X_INTERFACE_PARAMETER of rst : signal is "XIL_INTERFACENAME rst, POLARITY ACTIVE_LOW, INSERT_VIP 0";
begin
  A_out(3 downto 0) <= \^a_in\(3 downto 0);
  B_out(3 downto 0) <= \^b_in\(3 downto 0);
  L_E <= \^l_e\;
  \^a_in\(3 downto 0) <= A_in(3 downto 0);
  \^b_in\(3 downto 0) <= B_in(3 downto 0);
  \^dir_in\(3 downto 0) <= dir_in(3 downto 0);
  \^op_in\(2 downto 0) <= op_in(2 downto 0);
  dir_out(3 downto 0) <= \^dir_in\(3 downto 0);
  incrementar <= \^l_e\;
  op_out(2 downto 0) <= \^op_in\(2 downto 0);
inst: entity work.harvard_design_UC_0_0_UC
     port map (
      L_E => \^l_e\,
      clk => clk,
      ejecutar => ejecutar,
      rst => rst
    );
end STRUCTURE;
