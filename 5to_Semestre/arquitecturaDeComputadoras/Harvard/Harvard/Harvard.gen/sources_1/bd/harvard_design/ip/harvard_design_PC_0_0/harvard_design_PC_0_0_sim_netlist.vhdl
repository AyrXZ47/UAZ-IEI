-- Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
-- Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
-- --------------------------------------------------------------------------------
-- Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
-- Date        : Sat Nov 21 18:12:06 2026
-- Host        : nixos-laptop running 64-bit unknown
-- Command     : write_vhdl -force -mode funcsim
--               /tmp/opencode/harvard_fix/Harvard/Harvard.gen/sources_1/bd/harvard_design/ip/harvard_design_PC_0_0/harvard_design_PC_0_0_sim_netlist.vhdl
-- Design      : harvard_design_PC_0_0
-- Purpose     : This VHDL netlist is a functional simulation representation of the design and should not be modified or
--               synthesized. This netlist cannot be used for SDF annotated simulation.
-- Device      : xc7a35tcpg236-1
-- --------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity harvard_design_PC_0_0_PC is
  port (
    Dir : out STD_LOGIC_VECTOR ( 3 downto 0 );
    incremento : in STD_LOGIC;
    clk : in STD_LOGIC;
    rst : in STD_LOGIC
  );
  attribute ORIG_REF_NAME : string;
  attribute ORIG_REF_NAME of harvard_design_PC_0_0_PC : entity is "PC";
end harvard_design_PC_0_0_PC;

architecture STRUCTURE of harvard_design_PC_0_0_PC is
  signal \^dir\ : STD_LOGIC_VECTOR ( 3 downto 0 );
  signal plusOp : STD_LOGIC_VECTOR ( 3 downto 0 );
  attribute SOFT_HLUTNM : string;
  attribute SOFT_HLUTNM of \cont[0]_i_1\ : label is "soft_lutpair1";
  attribute SOFT_HLUTNM of \cont[1]_i_1\ : label is "soft_lutpair1";
  attribute SOFT_HLUTNM of \cont[2]_i_1\ : label is "soft_lutpair0";
  attribute SOFT_HLUTNM of \cont[3]_i_1\ : label is "soft_lutpair0";
begin
  Dir(3 downto 0) <= \^dir\(3 downto 0);
\cont[0]_i_1\: unisim.vcomponents.LUT1
    generic map(
      INIT => X"1"
    )
        port map (
      I0 => \^dir\(0),
      O => plusOp(0)
    );
\cont[1]_i_1\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"6"
    )
        port map (
      I0 => \^dir\(0),
      I1 => \^dir\(1),
      O => plusOp(1)
    );
\cont[2]_i_1\: unisim.vcomponents.LUT3
    generic map(
      INIT => X"78"
    )
        port map (
      I0 => \^dir\(0),
      I1 => \^dir\(1),
      I2 => \^dir\(2),
      O => plusOp(2)
    );
\cont[3]_i_1\: unisim.vcomponents.LUT4
    generic map(
      INIT => X"7F80"
    )
        port map (
      I0 => \^dir\(1),
      I1 => \^dir\(0),
      I2 => \^dir\(2),
      I3 => \^dir\(3),
      O => plusOp(3)
    );
\cont_reg[0]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => incremento,
      CLR => rst,
      D => plusOp(0),
      Q => \^dir\(0)
    );
\cont_reg[1]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => incremento,
      CLR => rst,
      D => plusOp(1),
      Q => \^dir\(1)
    );
\cont_reg[2]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => incremento,
      CLR => rst,
      D => plusOp(2),
      Q => \^dir\(2)
    );
\cont_reg[3]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => incremento,
      CLR => rst,
      D => plusOp(3),
      Q => \^dir\(3)
    );
end STRUCTURE;
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity harvard_design_PC_0_0 is
  port (
    clk : in STD_LOGIC;
    rst : in STD_LOGIC;
    incremento : in STD_LOGIC;
    Dir : out STD_LOGIC_VECTOR ( 3 downto 0 )
  );
  attribute NotValidForBitStream : boolean;
  attribute NotValidForBitStream of harvard_design_PC_0_0 : entity is true;
  attribute CHECK_LICENSE_TYPE : string;
  attribute CHECK_LICENSE_TYPE of harvard_design_PC_0_0 : entity is "harvard_design_PC_0_0,PC,{}";
  attribute DowngradeIPIdentifiedWarnings : string;
  attribute DowngradeIPIdentifiedWarnings of harvard_design_PC_0_0 : entity is "yes";
  attribute IP_DEFINITION_SOURCE : string;
  attribute IP_DEFINITION_SOURCE of harvard_design_PC_0_0 : entity is "module_ref";
  attribute X_CORE_INFO : string;
  attribute X_CORE_INFO of harvard_design_PC_0_0 : entity is "PC,Vivado 2026.1";
end harvard_design_PC_0_0;

architecture STRUCTURE of harvard_design_PC_0_0 is
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
inst: entity work.harvard_design_PC_0_0_PC
     port map (
      Dir(3 downto 0) => Dir(3 downto 0),
      clk => clk,
      incremento => incremento,
      rst => rst
    );
end STRUCTURE;
