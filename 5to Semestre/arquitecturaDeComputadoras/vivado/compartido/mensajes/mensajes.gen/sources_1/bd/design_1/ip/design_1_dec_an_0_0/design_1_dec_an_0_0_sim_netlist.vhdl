-- Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
-- Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
-- --------------------------------------------------------------------------------
-- Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
-- Date        : Sat Oct 31 01:29:06 2026
-- Host        : nixos-pc running 64-bit unknown
-- Command     : write_vhdl -force -mode funcsim {/home/yovick/repos/UAZ-IEI/5to
--               Semestre/arquitecturaDeComputadoras/vivado/compartido/mensajes/mensajes.gen/sources_1/bd/design_1/ip/design_1_dec_an_0_0/design_1_dec_an_0_0_sim_netlist.vhdl}
-- Design      : design_1_dec_an_0_0
-- Purpose     : This VHDL netlist is a functional simulation representation of the design and should not be modified or
--               synthesized. This netlist cannot be used for SDF annotated simulation.
-- Device      : xc7a100tcsg324-1
-- --------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity design_1_dec_an_0_0_dec_an is
  port (
    sal : out STD_LOGIC_VECTOR ( 7 downto 0 );
    ent : in STD_LOGIC_VECTOR ( 2 downto 0 )
  );
  attribute ORIG_REF_NAME : string;
  attribute ORIG_REF_NAME of design_1_dec_an_0_0_dec_an : entity is "dec_an";
end design_1_dec_an_0_0_dec_an;

architecture STRUCTURE of design_1_dec_an_0_0_dec_an is
  attribute SOFT_HLUTNM : string;
  attribute SOFT_HLUTNM of \sal[0]_INST_0\ : label is "soft_lutpair0";
  attribute SOFT_HLUTNM of \sal[1]_INST_0\ : label is "soft_lutpair0";
  attribute SOFT_HLUTNM of \sal[2]_INST_0\ : label is "soft_lutpair1";
  attribute SOFT_HLUTNM of \sal[3]_INST_0\ : label is "soft_lutpair1";
  attribute SOFT_HLUTNM of \sal[4]_INST_0\ : label is "soft_lutpair2";
  attribute SOFT_HLUTNM of \sal[5]_INST_0\ : label is "soft_lutpair2";
  attribute SOFT_HLUTNM of \sal[6]_INST_0\ : label is "soft_lutpair3";
  attribute SOFT_HLUTNM of \sal[7]_INST_0\ : label is "soft_lutpair3";
begin
\sal[0]_INST_0\: unisim.vcomponents.LUT3
    generic map(
      INIT => X"FE"
    )
        port map (
      I0 => ent(1),
      I1 => ent(2),
      I2 => ent(0),
      O => sal(0)
    );
\sal[1]_INST_0\: unisim.vcomponents.LUT3
    generic map(
      INIT => X"EF"
    )
        port map (
      I0 => ent(1),
      I1 => ent(2),
      I2 => ent(0),
      O => sal(1)
    );
\sal[2]_INST_0\: unisim.vcomponents.LUT3
    generic map(
      INIT => X"EF"
    )
        port map (
      I0 => ent(2),
      I1 => ent(0),
      I2 => ent(1),
      O => sal(2)
    );
\sal[3]_INST_0\: unisim.vcomponents.LUT3
    generic map(
      INIT => X"F7"
    )
        port map (
      I0 => ent(1),
      I1 => ent(0),
      I2 => ent(2),
      O => sal(3)
    );
\sal[4]_INST_0\: unisim.vcomponents.LUT3
    generic map(
      INIT => X"EF"
    )
        port map (
      I0 => ent(1),
      I1 => ent(0),
      I2 => ent(2),
      O => sal(4)
    );
\sal[5]_INST_0\: unisim.vcomponents.LUT3
    generic map(
      INIT => X"F7"
    )
        port map (
      I0 => ent(2),
      I1 => ent(0),
      I2 => ent(1),
      O => sal(5)
    );
\sal[6]_INST_0\: unisim.vcomponents.LUT3
    generic map(
      INIT => X"F7"
    )
        port map (
      I0 => ent(1),
      I1 => ent(2),
      I2 => ent(0),
      O => sal(6)
    );
\sal[7]_INST_0\: unisim.vcomponents.LUT3
    generic map(
      INIT => X"7F"
    )
        port map (
      I0 => ent(2),
      I1 => ent(0),
      I2 => ent(1),
      O => sal(7)
    );
end STRUCTURE;
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity design_1_dec_an_0_0 is
  port (
    ent : in STD_LOGIC_VECTOR ( 2 downto 0 );
    sal : out STD_LOGIC_VECTOR ( 7 downto 0 )
  );
  attribute NotValidForBitStream : boolean;
  attribute NotValidForBitStream of design_1_dec_an_0_0 : entity is true;
  attribute CHECK_LICENSE_TYPE : string;
  attribute CHECK_LICENSE_TYPE of design_1_dec_an_0_0 : entity is "design_1_dec_an_0_0,dec_an,{}";
  attribute downgradeipidentifiedwarnings : string;
  attribute downgradeipidentifiedwarnings of design_1_dec_an_0_0 : entity is "yes";
  attribute ip_definition_source : string;
  attribute ip_definition_source of design_1_dec_an_0_0 : entity is "module_ref";
  attribute x_core_info : string;
  attribute x_core_info of design_1_dec_an_0_0 : entity is "dec_an,Vivado 2026.1";
end design_1_dec_an_0_0;

architecture STRUCTURE of design_1_dec_an_0_0 is
begin
U0: entity work.design_1_dec_an_0_0_dec_an
     port map (
      ent(2 downto 0) => ent(2 downto 0),
      sal(7 downto 0) => sal(7 downto 0)
    );
end STRUCTURE;
