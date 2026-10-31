-- Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
-- Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
-- --------------------------------------------------------------------------------
-- Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
-- Date        : Fri Oct 30 21:50:18 2026
-- Host        : nixos-pc running 64-bit unknown
-- Command     : write_vhdl -force -mode funcsim {/home/yovick/repos/UAZ-IEI/5to
--               Semestre/arquitecturaDeComputadoras/vivado/compartido/mensajes/mensajes.gen/sources_1/bd/design_1/ip/design_1_rom_mensajes_0_0/design_1_rom_mensajes_0_0_sim_netlist.vhdl}
-- Design      : design_1_rom_mensajes_0_0
-- Purpose     : This VHDL netlist is a functional simulation representation of the design and should not be modified or
--               synthesized. This netlist cannot be used for SDF annotated simulation.
-- Device      : xc7a100tcsg324-1
-- --------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity design_1_rom_mensajes_0_0_rom_mensajes is
  port (
    seg : out STD_LOGIC_VECTOR ( 5 downto 0 );
    sel : in STD_LOGIC;
    dir : in STD_LOGIC_VECTOR ( 2 downto 0 )
  );
  attribute ORIG_REF_NAME : string;
  attribute ORIG_REF_NAME of design_1_rom_mensajes_0_0_rom_mensajes : entity is "rom_mensajes";
end design_1_rom_mensajes_0_0_rom_mensajes;

architecture STRUCTURE of design_1_rom_mensajes_0_0_rom_mensajes is
  attribute SOFT_HLUTNM : string;
  attribute SOFT_HLUTNM of \seg[0]_INST_0\ : label is "soft_lutpair2";
  attribute SOFT_HLUTNM of \seg[1]_INST_0\ : label is "soft_lutpair0";
  attribute SOFT_HLUTNM of \seg[2]_INST_0\ : label is "soft_lutpair0";
  attribute SOFT_HLUTNM of \seg[3]_INST_0\ : label is "soft_lutpair1";
  attribute SOFT_HLUTNM of \seg[4]_INST_0\ : label is "soft_lutpair1";
  attribute SOFT_HLUTNM of \seg[5]_INST_0\ : label is "soft_lutpair2";
begin
\seg[0]_INST_0\: unisim.vcomponents.LUT4
    generic map(
      INIT => X"BFFF"
    )
        port map (
      I0 => sel,
      I1 => dir(2),
      I2 => dir(0),
      I3 => dir(1),
      O => seg(0)
    );
\seg[1]_INST_0\: unisim.vcomponents.LUT4
    generic map(
      INIT => X"17E0"
    )
        port map (
      I0 => sel,
      I1 => dir(1),
      I2 => dir(2),
      I3 => dir(0),
      O => seg(1)
    );
\seg[2]_INST_0\: unisim.vcomponents.LUT4
    generic map(
      INIT => X"CF82"
    )
        port map (
      I0 => sel,
      I1 => dir(1),
      I2 => dir(2),
      I3 => dir(0),
      O => seg(2)
    );
\seg[3]_INST_0\: unisim.vcomponents.LUT4
    generic map(
      INIT => X"7831"
    )
        port map (
      I0 => sel,
      I1 => dir(2),
      I2 => dir(0),
      I3 => dir(1),
      O => seg(3)
    );
\seg[4]_INST_0\: unisim.vcomponents.LUT4
    generic map(
      INIT => X"0790"
    )
        port map (
      I0 => sel,
      I1 => dir(1),
      I2 => dir(2),
      I3 => dir(0),
      O => seg(4)
    );
\seg[5]_INST_0\: unisim.vcomponents.LUT4
    generic map(
      INIT => X"8542"
    )
        port map (
      I0 => sel,
      I1 => dir(0),
      I2 => dir(2),
      I3 => dir(1),
      O => seg(5)
    );
end STRUCTURE;
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity design_1_rom_mensajes_0_0 is
  port (
    sel : in STD_LOGIC;
    dir : in STD_LOGIC_VECTOR ( 2 downto 0 );
    seg : out STD_LOGIC_VECTOR ( 7 downto 0 )
  );
  attribute NotValidForBitStream : boolean;
  attribute NotValidForBitStream of design_1_rom_mensajes_0_0 : entity is true;
  attribute CHECK_LICENSE_TYPE : string;
  attribute CHECK_LICENSE_TYPE of design_1_rom_mensajes_0_0 : entity is "design_1_rom_mensajes_0_0,rom_mensajes,{}";
  attribute downgradeipidentifiedwarnings : string;
  attribute downgradeipidentifiedwarnings of design_1_rom_mensajes_0_0 : entity is "yes";
  attribute ip_definition_source : string;
  attribute ip_definition_source of design_1_rom_mensajes_0_0 : entity is "module_ref";
  attribute x_core_info : string;
  attribute x_core_info of design_1_rom_mensajes_0_0 : entity is "rom_mensajes,Vivado 2026.1";
end design_1_rom_mensajes_0_0;

architecture STRUCTURE of design_1_rom_mensajes_0_0 is
begin
U0: entity work.design_1_rom_mensajes_0_0_rom_mensajes
     port map (
      dir(2 downto 0) => dir(2 downto 0),
      seg(5 downto 0) => seg(5 downto 0),
      sel => sel
    );
\seg[6]_INST_0\: unisim.vcomponents.LUT4
    generic map(
      INIT => X"004B"
    )
        port map (
      I0 => dir(1),
      I1 => dir(0),
      I2 => dir(2),
      I3 => sel,
      O => seg(6)
    );
\seg[7]_INST_0\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"2"
    )
        port map (
      I0 => dir(0),
      I1 => sel,
      O => seg(7)
    );
end STRUCTURE;
