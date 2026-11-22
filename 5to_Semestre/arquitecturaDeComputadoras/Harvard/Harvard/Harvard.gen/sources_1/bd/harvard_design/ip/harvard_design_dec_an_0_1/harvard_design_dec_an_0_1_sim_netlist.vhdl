-- Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
-- Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
-- --------------------------------------------------------------------------------
-- Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
-- Date        : Sat Nov 21 18:12:42 2026
-- Host        : nixos-laptop running 64-bit unknown
-- Command     : write_vhdl -force -mode funcsim
--               /tmp/opencode/harvard_fix/Harvard/Harvard.gen/sources_1/bd/harvard_design/ip/harvard_design_dec_an_0_1/harvard_design_dec_an_0_1_sim_netlist.vhdl
-- Design      : harvard_design_dec_an_0_1
-- Purpose     : This VHDL netlist is a functional simulation representation of the design and should not be modified or
--               synthesized. This netlist cannot be used for SDF annotated simulation.
-- Device      : xc7a35tcpg236-1
-- --------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity harvard_design_dec_an_0_1_dec_an is
  port (
    sal : out STD_LOGIC_VECTOR ( 1 downto 0 );
    ent : in STD_LOGIC_VECTOR ( 1 downto 0 )
  );
  attribute ORIG_REF_NAME : string;
  attribute ORIG_REF_NAME of harvard_design_dec_an_0_1_dec_an : entity is "dec_an";
end harvard_design_dec_an_0_1_dec_an;

architecture STRUCTURE of harvard_design_dec_an_0_1_dec_an is
  attribute SOFT_HLUTNM : string;
  attribute SOFT_HLUTNM of \sal[0]_INST_0\ : label is "soft_lutpair0";
  attribute SOFT_HLUTNM of \sal[3]_INST_0\ : label is "soft_lutpair0";
begin
\sal[0]_INST_0\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"E"
    )
        port map (
      I0 => ent(0),
      I1 => ent(1),
      O => sal(0)
    );
\sal[3]_INST_0\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"7"
    )
        port map (
      I0 => ent(0),
      I1 => ent(1),
      O => sal(1)
    );
end STRUCTURE;
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity harvard_design_dec_an_0_1 is
  port (
    ent : in STD_LOGIC_VECTOR ( 1 downto 0 );
    sal : out STD_LOGIC_VECTOR ( 3 downto 0 )
  );
  attribute NotValidForBitStream : boolean;
  attribute NotValidForBitStream of harvard_design_dec_an_0_1 : entity is true;
  attribute CHECK_LICENSE_TYPE : string;
  attribute CHECK_LICENSE_TYPE of harvard_design_dec_an_0_1 : entity is "harvard_design_dec_an_0_1,dec_an,{}";
  attribute DowngradeIPIdentifiedWarnings : string;
  attribute DowngradeIPIdentifiedWarnings of harvard_design_dec_an_0_1 : entity is "yes";
  attribute IP_DEFINITION_SOURCE : string;
  attribute IP_DEFINITION_SOURCE of harvard_design_dec_an_0_1 : entity is "module_ref";
  attribute X_CORE_INFO : string;
  attribute X_CORE_INFO of harvard_design_dec_an_0_1 : entity is "dec_an,Vivado 2026.1";
end harvard_design_dec_an_0_1;

architecture STRUCTURE of harvard_design_dec_an_0_1 is
begin
inst: entity work.harvard_design_dec_an_0_1_dec_an
     port map (
      ent(1 downto 0) => ent(1 downto 0),
      sal(1) => sal(3),
      sal(0) => sal(0)
    );
\sal[1]_INST_0\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"B"
    )
        port map (
      I0 => ent(1),
      I1 => ent(0),
      O => sal(1)
    );
\sal[2]_INST_0\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"B"
    )
        port map (
      I0 => ent(0),
      I1 => ent(1),
      O => sal(2)
    );
end STRUCTURE;
