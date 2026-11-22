-- Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
-- Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
-- --------------------------------------------------------------------------------
-- Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
-- Date        : Sat Nov 21 18:12:06 2026
-- Host        : nixos-laptop running 64-bit unknown
-- Command     : write_vhdl -force -mode funcsim
--               /tmp/opencode/harvard_fix/Harvard/Harvard.gen/sources_1/bd/harvard_design/ip/harvard_design_M_ROM_0_0/harvard_design_M_ROM_0_0_sim_netlist.vhdl
-- Design      : harvard_design_M_ROM_0_0
-- Purpose     : This VHDL netlist is a functional simulation representation of the design and should not be modified or
--               synthesized. This netlist cannot be used for SDF annotated simulation.
-- Device      : xc7a35tcpg236-1
-- --------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity harvard_design_M_ROM_0_0_M_ROM is
  port (
    dato : out STD_LOGIC_VECTOR ( 2 downto 0 );
    dir : in STD_LOGIC_VECTOR ( 3 downto 0 );
    clk : in STD_LOGIC
  );
  attribute ORIG_REF_NAME : string;
  attribute ORIG_REF_NAME of harvard_design_M_ROM_0_0_M_ROM : entity is "M_ROM";
end harvard_design_M_ROM_0_0_M_ROM;

architecture STRUCTURE of harvard_design_M_ROM_0_0_M_ROM is
  signal \dato[0]_i_1_n_0\ : STD_LOGIC;
  signal \dato[1]_i_1_n_0\ : STD_LOGIC;
  signal \dato[2]_i_1_n_0\ : STD_LOGIC;
  attribute SOFT_HLUTNM : string;
  attribute SOFT_HLUTNM of \dato[0]_i_1\ : label is "soft_lutpair0";
  attribute SOFT_HLUTNM of \dato[2]_i_1\ : label is "soft_lutpair0";
begin
\dato[0]_i_1\: unisim.vcomponents.LUT4
    generic map(
      INIT => X"5664"
    )
        port map (
      I0 => dir(0),
      I1 => dir(3),
      I2 => dir(2),
      I3 => dir(1),
      O => \dato[0]_i_1_n_0\
    );
\dato[1]_i_1\: unisim.vcomponents.LUT3
    generic map(
      INIT => X"28"
    )
        port map (
      I0 => dir(3),
      I1 => dir(1),
      I2 => dir(0),
      O => \dato[1]_i_1_n_0\
    );
\dato[2]_i_1\: unisim.vcomponents.LUT4
    generic map(
      INIT => X"2888"
    )
        port map (
      I0 => dir(3),
      I1 => dir(2),
      I2 => dir(0),
      I3 => dir(1),
      O => \dato[2]_i_1_n_0\
    );
\dato_reg[0]\: unisim.vcomponents.FDRE
     port map (
      C => clk,
      CE => '1',
      D => \dato[0]_i_1_n_0\,
      Q => dato(0),
      R => '0'
    );
\dato_reg[1]\: unisim.vcomponents.FDRE
     port map (
      C => clk,
      CE => '1',
      D => \dato[1]_i_1_n_0\,
      Q => dato(1),
      R => '0'
    );
\dato_reg[2]\: unisim.vcomponents.FDRE
     port map (
      C => clk,
      CE => '1',
      D => \dato[2]_i_1_n_0\,
      Q => dato(2),
      R => '0'
    );
end STRUCTURE;
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity harvard_design_M_ROM_0_0 is
  port (
    clk : in STD_LOGIC;
    dir : in STD_LOGIC_VECTOR ( 3 downto 0 );
    dato : out STD_LOGIC_VECTOR ( 2 downto 0 )
  );
  attribute NotValidForBitStream : boolean;
  attribute NotValidForBitStream of harvard_design_M_ROM_0_0 : entity is true;
  attribute CHECK_LICENSE_TYPE : string;
  attribute CHECK_LICENSE_TYPE of harvard_design_M_ROM_0_0 : entity is "harvard_design_M_ROM_0_0,M_ROM,{}";
  attribute DowngradeIPIdentifiedWarnings : string;
  attribute DowngradeIPIdentifiedWarnings of harvard_design_M_ROM_0_0 : entity is "yes";
  attribute IP_DEFINITION_SOURCE : string;
  attribute IP_DEFINITION_SOURCE of harvard_design_M_ROM_0_0 : entity is "module_ref";
  attribute X_CORE_INFO : string;
  attribute X_CORE_INFO of harvard_design_M_ROM_0_0 : entity is "M_ROM,Vivado 2026.1";
end harvard_design_M_ROM_0_0;

architecture STRUCTURE of harvard_design_M_ROM_0_0 is
  attribute X_INTERFACE_INFO : string;
  attribute X_INTERFACE_INFO of clk : signal is "xilinx.com:signal:clock:1.0 clk CLK";
  attribute X_INTERFACE_MODE : string;
  attribute X_INTERFACE_MODE of clk : signal is "slave";
  attribute X_INTERFACE_PARAMETER : string;
  attribute X_INTERFACE_PARAMETER of clk : signal is "XIL_INTERFACENAME clk, FREQ_HZ 100000000, FREQ_TOLERANCE_HZ 0, PHASE 0.0, CLK_DOMAIN harvard_design_clk, INSERT_VIP 0";
begin
inst: entity work.harvard_design_M_ROM_0_0_M_ROM
     port map (
      clk => clk,
      dato(2 downto 0) => dato(2 downto 0),
      dir(3 downto 0) => dir(3 downto 0)
    );
end STRUCTURE;
