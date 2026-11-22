-- Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
-- Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
-- --------------------------------------------------------------------------------
-- Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
-- Date        : Sat Nov 21 18:12:07 2026
-- Host        : nixos-laptop running 64-bit unknown
-- Command     : write_vhdl -force -mode funcsim
--               /tmp/opencode/harvard_fix/Harvard/Harvard.gen/sources_1/bd/harvard_design/ip/harvard_design_UAL_0_0/harvard_design_UAL_0_0_sim_netlist.vhdl
-- Design      : harvard_design_UAL_0_0
-- Purpose     : This VHDL netlist is a functional simulation representation of the design and should not be modified or
--               synthesized. This netlist cannot be used for SDF annotated simulation.
-- Device      : xc7a35tcpg236-1
-- --------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity harvard_design_UAL_0_0 is
  port (
    A : in STD_LOGIC_VECTOR ( 3 downto 0 );
    B : in STD_LOGIC_VECTOR ( 3 downto 0 );
    op : in STD_LOGIC_VECTOR ( 2 downto 0 );
    res : out STD_LOGIC_VECTOR ( 3 downto 0 );
    acarreo : out STD_LOGIC;
    cero : out STD_LOGIC
  );
  attribute NotValidForBitStream : boolean;
  attribute NotValidForBitStream of harvard_design_UAL_0_0 : entity is true;
  attribute CHECK_LICENSE_TYPE : string;
  attribute CHECK_LICENSE_TYPE of harvard_design_UAL_0_0 : entity is "harvard_design_UAL_0_0,UAL,{}";
  attribute DowngradeIPIdentifiedWarnings : string;
  attribute DowngradeIPIdentifiedWarnings of harvard_design_UAL_0_0 : entity is "yes";
  attribute IP_DEFINITION_SOURCE : string;
  attribute IP_DEFINITION_SOURCE of harvard_design_UAL_0_0 : entity is "module_ref";
  attribute X_CORE_INFO : string;
  attribute X_CORE_INFO of harvard_design_UAL_0_0 : entity is "UAL,Vivado 2026.1";
end harvard_design_UAL_0_0;

architecture STRUCTURE of harvard_design_UAL_0_0 is
  signal acarreo_INST_0_i_1_n_0 : STD_LOGIC;
  signal acarreo_INST_0_i_2_n_0 : STD_LOGIC;
  signal cero_INST_0_i_1_n_0 : STD_LOGIC;
  signal \^res\ : STD_LOGIC_VECTOR ( 3 downto 0 );
  signal \res[1]_INST_0_i_1_n_0\ : STD_LOGIC;
  signal \res[1]_INST_0_i_2_n_0\ : STD_LOGIC;
  signal \res[2]_INST_0_i_1_n_0\ : STD_LOGIC;
  signal \res[2]_INST_0_i_2_n_0\ : STD_LOGIC;
  signal \res[2]_INST_0_i_3_n_0\ : STD_LOGIC;
  signal \res[2]_INST_0_i_4_n_0\ : STD_LOGIC;
  signal \res[3]_INST_0_i_1_n_0\ : STD_LOGIC;
  signal \res[3]_INST_0_i_2_n_0\ : STD_LOGIC;
  signal \res[3]_INST_0_i_3_n_0\ : STD_LOGIC;
  signal \res[3]_INST_0_i_4_n_0\ : STD_LOGIC;
  signal \res[3]_INST_0_i_5_n_0\ : STD_LOGIC;
  attribute SOFT_HLUTNM : string;
  attribute SOFT_HLUTNM of \res[2]_INST_0_i_3\ : label is "soft_lutpair0";
  attribute SOFT_HLUTNM of \res[2]_INST_0_i_4\ : label is "soft_lutpair0";
begin
  res(3 downto 0) <= \^res\(3 downto 0);
acarreo_INST_0: unisim.vcomponents.MUXF7
     port map (
      I0 => acarreo_INST_0_i_1_n_0,
      I1 => acarreo_INST_0_i_2_n_0,
      O => acarreo,
      S => op(2)
    );
acarreo_INST_0_i_1: unisim.vcomponents.LUT6
    generic map(
      INIT => X"000000000CE8CFE8"
    )
        port map (
      I0 => \res[3]_INST_0_i_4_n_0\,
      I1 => B(3),
      I2 => A(3),
      I3 => op(0),
      I4 => \res[3]_INST_0_i_3_n_0\,
      I5 => op(1),
      O => acarreo_INST_0_i_1_n_0
    );
acarreo_INST_0_i_2: unisim.vcomponents.LUT6
    generic map(
      INIT => X"0001FFFF80000000"
    )
        port map (
      I0 => A(3),
      I1 => A(1),
      I2 => A(0),
      I3 => A(2),
      I4 => op(1),
      I5 => op(0),
      O => acarreo_INST_0_i_2_n_0
    );
cero_INST_0: unisim.vcomponents.LUT6
    generic map(
      INIT => X"0000000000440347"
    )
        port map (
      I0 => \res[2]_INST_0_i_2_n_0\,
      I1 => op(2),
      I2 => \res[2]_INST_0_i_1_n_0\,
      I3 => \res[3]_INST_0_i_2_n_0\,
      I4 => \res[3]_INST_0_i_1_n_0\,
      I5 => cero_INST_0_i_1_n_0,
      O => cero
    );
cero_INST_0_i_1: unisim.vcomponents.LUT4
    generic map(
      INIT => X"FEAE"
    )
        port map (
      I0 => \^res\(0),
      I1 => \res[1]_INST_0_i_1_n_0\,
      I2 => op(2),
      I3 => \res[1]_INST_0_i_2_n_0\,
      O => cero_INST_0_i_1_n_0
    );
\res[0]_INST_0\: unisim.vcomponents.LUT5
    generic map(
      INIT => X"50EF47A8"
    )
        port map (
      I0 => op(2),
      I1 => op(0),
      I2 => op(1),
      I3 => A(0),
      I4 => B(0),
      O => \^res\(0)
    );
\res[1]_INST_0\: unisim.vcomponents.MUXF7
     port map (
      I0 => \res[1]_INST_0_i_1_n_0\,
      I1 => \res[1]_INST_0_i_2_n_0\,
      O => \^res\(1),
      S => op(2)
    );
\res[1]_INST_0_i_1\: unisim.vcomponents.LUT6
    generic map(
      INIT => X"BEAAC9DDC9DD1400"
    )
        port map (
      I0 => op(1),
      I1 => op(0),
      I2 => A(0),
      I3 => B(0),
      I4 => B(1),
      I5 => A(1),
      O => \res[1]_INST_0_i_1_n_0\
    );
\res[1]_INST_0_i_2\: unisim.vcomponents.LUT5
    generic map(
      INIT => X"84877B78"
    )
        port map (
      I0 => A(0),
      I1 => op(1),
      I2 => op(0),
      I3 => B(1),
      I4 => A(1),
      O => \res[1]_INST_0_i_2_n_0\
    );
\res[2]_INST_0\: unisim.vcomponents.MUXF7
     port map (
      I0 => \res[2]_INST_0_i_1_n_0\,
      I1 => \res[2]_INST_0_i_2_n_0\,
      O => \^res\(2),
      S => op(2)
    );
\res[2]_INST_0_i_1\: unisim.vcomponents.LUT6
    generic map(
      INIT => X"BFBAE0E5E0E51510"
    )
        port map (
      I0 => op(1),
      I1 => \res[2]_INST_0_i_3_n_0\,
      I2 => op(0),
      I3 => \res[2]_INST_0_i_4_n_0\,
      I4 => B(2),
      I5 => A(2),
      O => \res[2]_INST_0_i_1_n_0\
    );
\res[2]_INST_0_i_2\: unisim.vcomponents.LUT6
    generic map(
      INIT => X"E070E07F1F8F1F80"
    )
        port map (
      I0 => A(0),
      I1 => A(1),
      I2 => op(1),
      I3 => op(0),
      I4 => B(2),
      I5 => A(2),
      O => \res[2]_INST_0_i_2_n_0\
    );
\res[2]_INST_0_i_3\: unisim.vcomponents.LUT4
    generic map(
      INIT => X"DD4D"
    )
        port map (
      I0 => B(1),
      I1 => A(1),
      I2 => B(0),
      I3 => A(0),
      O => \res[2]_INST_0_i_3_n_0\
    );
\res[2]_INST_0_i_4\: unisim.vcomponents.LUT4
    generic map(
      INIT => X"E888"
    )
        port map (
      I0 => B(1),
      I1 => A(1),
      I2 => A(0),
      I3 => B(0),
      O => \res[2]_INST_0_i_4_n_0\
    );
\res[3]_INST_0\: unisim.vcomponents.MUXF7
     port map (
      I0 => \res[3]_INST_0_i_1_n_0\,
      I1 => \res[3]_INST_0_i_2_n_0\,
      O => \^res\(3),
      S => op(2)
    );
\res[3]_INST_0_i_1\: unisim.vcomponents.LUT6
    generic map(
      INIT => X"BFBAE0E5E0E51510"
    )
        port map (
      I0 => op(1),
      I1 => \res[3]_INST_0_i_3_n_0\,
      I2 => op(0),
      I3 => \res[3]_INST_0_i_4_n_0\,
      I4 => B(3),
      I5 => A(3),
      O => \res[3]_INST_0_i_1_n_0\
    );
\res[3]_INST_0_i_2\: unisim.vcomponents.LUT5
    generic map(
      INIT => X"888BBBB8"
    )
        port map (
      I0 => \res[3]_INST_0_i_5_n_0\,
      I1 => op(1),
      I2 => op(0),
      I3 => B(3),
      I4 => A(3),
      O => \res[3]_INST_0_i_2_n_0\
    );
\res[3]_INST_0_i_3\: unisim.vcomponents.LUT6
    generic map(
      INIT => X"D4DD4444DDDDD4DD"
    )
        port map (
      I0 => B(2),
      I1 => A(2),
      I2 => A(0),
      I3 => B(0),
      I4 => A(1),
      I5 => B(1),
      O => \res[3]_INST_0_i_3_n_0\
    );
\res[3]_INST_0_i_4\: unisim.vcomponents.LUT6
    generic map(
      INIT => X"EEEEE888E8888888"
    )
        port map (
      I0 => B(2),
      I1 => A(2),
      I2 => B(0),
      I3 => A(0),
      I4 => A(1),
      I5 => B(1),
      O => \res[3]_INST_0_i_4_n_0\
    );
\res[3]_INST_0_i_5\: unisim.vcomponents.LUT5
    generic map(
      INIT => X"BFFD4002"
    )
        port map (
      I0 => op(0),
      I1 => A(1),
      I2 => A(0),
      I3 => A(2),
      I4 => A(3),
      O => \res[3]_INST_0_i_5_n_0\
    );
end STRUCTURE;
