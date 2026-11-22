-- Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
-- Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
-- --------------------------------------------------------------------------------
-- Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
-- Date        : Sat Oct 24 17:45:26 2026
-- Host        : nixos-laptop running 64-bit unknown
-- Command     : write_vhdl -force -mode funcsim {/home/yovick/repos/UAZ-IEI/5to
--               Semestre/arquitecturaDeComputadoras/vivado/compartido/bcd_diferentes/bcd_diferentes.gen/sources_1/bd/design_1/ip/design_1_mux_datos_0_0/design_1_mux_datos_0_0_sim_netlist.vhdl}
-- Design      : design_1_mux_datos_0_0
-- Purpose     : This VHDL netlist is a functional simulation representation of the design and should not be modified or
--               synthesized. This netlist cannot be used for SDF annotated simulation.
-- Device      : xc7a100tcsg324-1
-- --------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity design_1_mux_datos_0_0_mux_datos is
  port (
    sal : out STD_LOGIC_VECTOR ( 3 downto 0 );
    sel : in STD_LOGIC_VECTOR ( 2 downto 0 );
    sw : in STD_LOGIC_VECTOR ( 15 downto 0 )
  );
  attribute ORIG_REF_NAME : string;
  attribute ORIG_REF_NAME of design_1_mux_datos_0_0_mux_datos : entity is "mux_datos";
end design_1_mux_datos_0_0_mux_datos;

architecture STRUCTURE of design_1_mux_datos_0_0_mux_datos is
  signal \sal[0]_INST_0_i_1_n_0\ : STD_LOGIC;
  signal \sal[0]_INST_0_i_2_n_0\ : STD_LOGIC;
  signal \sal[1]_INST_0_i_1_n_0\ : STD_LOGIC;
  signal \sal[1]_INST_0_i_2_n_0\ : STD_LOGIC;
  signal \sal[2]_INST_0_i_1_n_0\ : STD_LOGIC;
  signal \sal[2]_INST_0_i_2_n_0\ : STD_LOGIC;
  signal \sal[3]_INST_0_i_1_n_0\ : STD_LOGIC;
  signal \sal[3]_INST_0_i_2_n_0\ : STD_LOGIC;
begin
\sal[0]_INST_0\: unisim.vcomponents.MUXF7
     port map (
      I0 => \sal[0]_INST_0_i_1_n_0\,
      I1 => \sal[0]_INST_0_i_2_n_0\,
      O => sal(0),
      S => sel(2)
    );
\sal[0]_INST_0_i_1\: unisim.vcomponents.LUT6
    generic map(
      INIT => X"AFA0CFCFAFA0C0C0"
    )
        port map (
      I0 => sw(12),
      I1 => sw(8),
      I2 => sel(1),
      I3 => sw(4),
      I4 => sel(0),
      I5 => sw(0),
      O => \sal[0]_INST_0_i_1_n_0\
    );
\sal[0]_INST_0_i_2\: unisim.vcomponents.LUT5
    generic map(
      INIT => X"FCBB3088"
    )
        port map (
      I0 => sw(8),
      I1 => sel(1),
      I2 => sw(4),
      I3 => sel(0),
      I4 => sw(0),
      O => \sal[0]_INST_0_i_2_n_0\
    );
\sal[1]_INST_0\: unisim.vcomponents.MUXF7
     port map (
      I0 => \sal[1]_INST_0_i_1_n_0\,
      I1 => \sal[1]_INST_0_i_2_n_0\,
      O => sal(1),
      S => sel(2)
    );
\sal[1]_INST_0_i_1\: unisim.vcomponents.LUT6
    generic map(
      INIT => X"AFA0CFCFAFA0C0C0"
    )
        port map (
      I0 => sw(13),
      I1 => sw(9),
      I2 => sel(1),
      I3 => sw(5),
      I4 => sel(0),
      I5 => sw(1),
      O => \sal[1]_INST_0_i_1_n_0\
    );
\sal[1]_INST_0_i_2\: unisim.vcomponents.LUT5
    generic map(
      INIT => X"FCBB3088"
    )
        port map (
      I0 => sw(9),
      I1 => sel(1),
      I2 => sw(5),
      I3 => sel(0),
      I4 => sw(1),
      O => \sal[1]_INST_0_i_2_n_0\
    );
\sal[2]_INST_0\: unisim.vcomponents.MUXF7
     port map (
      I0 => \sal[2]_INST_0_i_1_n_0\,
      I1 => \sal[2]_INST_0_i_2_n_0\,
      O => sal(2),
      S => sel(2)
    );
\sal[2]_INST_0_i_1\: unisim.vcomponents.LUT6
    generic map(
      INIT => X"AFA0CFCFAFA0C0C0"
    )
        port map (
      I0 => sw(14),
      I1 => sw(10),
      I2 => sel(1),
      I3 => sw(6),
      I4 => sel(0),
      I5 => sw(2),
      O => \sal[2]_INST_0_i_1_n_0\
    );
\sal[2]_INST_0_i_2\: unisim.vcomponents.LUT5
    generic map(
      INIT => X"FCBB3088"
    )
        port map (
      I0 => sw(10),
      I1 => sel(1),
      I2 => sw(6),
      I3 => sel(0),
      I4 => sw(2),
      O => \sal[2]_INST_0_i_2_n_0\
    );
\sal[3]_INST_0\: unisim.vcomponents.MUXF7
     port map (
      I0 => \sal[3]_INST_0_i_1_n_0\,
      I1 => \sal[3]_INST_0_i_2_n_0\,
      O => sal(3),
      S => sel(2)
    );
\sal[3]_INST_0_i_1\: unisim.vcomponents.LUT6
    generic map(
      INIT => X"AFA0CFCFAFA0C0C0"
    )
        port map (
      I0 => sw(15),
      I1 => sw(11),
      I2 => sel(1),
      I3 => sw(7),
      I4 => sel(0),
      I5 => sw(3),
      O => \sal[3]_INST_0_i_1_n_0\
    );
\sal[3]_INST_0_i_2\: unisim.vcomponents.LUT5
    generic map(
      INIT => X"FCBB3088"
    )
        port map (
      I0 => sw(11),
      I1 => sel(1),
      I2 => sw(7),
      I3 => sel(0),
      I4 => sw(3),
      O => \sal[3]_INST_0_i_2_n_0\
    );
end STRUCTURE;
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity design_1_mux_datos_0_0 is
  port (
    sw : in STD_LOGIC_VECTOR ( 15 downto 0 );
    sel : in STD_LOGIC_VECTOR ( 2 downto 0 );
    sal : out STD_LOGIC_VECTOR ( 3 downto 0 )
  );
  attribute NotValidForBitStream : boolean;
  attribute NotValidForBitStream of design_1_mux_datos_0_0 : entity is true;
  attribute CHECK_LICENSE_TYPE : string;
  attribute CHECK_LICENSE_TYPE of design_1_mux_datos_0_0 : entity is "design_1_mux_datos_0_0,mux_datos,{}";
  attribute downgradeipidentifiedwarnings : string;
  attribute downgradeipidentifiedwarnings of design_1_mux_datos_0_0 : entity is "yes";
  attribute ip_definition_source : string;
  attribute ip_definition_source of design_1_mux_datos_0_0 : entity is "module_ref";
  attribute x_core_info : string;
  attribute x_core_info of design_1_mux_datos_0_0 : entity is "mux_datos,Vivado 2026.1";
end design_1_mux_datos_0_0;

architecture STRUCTURE of design_1_mux_datos_0_0 is
begin
U0: entity work.design_1_mux_datos_0_0_mux_datos
     port map (
      sal(3 downto 0) => sal(3 downto 0),
      sel(2 downto 0) => sel(2 downto 0),
      sw(15 downto 0) => sw(15 downto 0)
    );
end STRUCTURE;
