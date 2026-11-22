-- Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
-- Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
-- --------------------------------------------------------------------------------
-- Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
-- Date        : Sat Nov 21 18:12:42 2026
-- Host        : nixos-laptop running 64-bit unknown
-- Command     : write_vhdl -force -mode funcsim
--               /tmp/opencode/harvard_fix/Harvard/Harvard.gen/sources_1/bd/harvard_design/ip/harvard_design_mux_datos_0_0/harvard_design_mux_datos_0_0_sim_netlist.vhdl
-- Design      : harvard_design_mux_datos_0_0
-- Purpose     : This VHDL netlist is a functional simulation representation of the design and should not be modified or
--               synthesized. This netlist cannot be used for SDF annotated simulation.
-- Device      : xc7a35tcpg236-1
-- --------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity harvard_design_mux_datos_0_0_mux_datos is
  port (
    sal : out STD_LOGIC_VECTOR ( 3 downto 0 );
    B : in STD_LOGIC_VECTOR ( 3 downto 0 );
    A : in STD_LOGIC_VECTOR ( 3 downto 0 );
    datoRam : in STD_LOGIC_VECTOR ( 3 downto 0 );
    sel : in STD_LOGIC_VECTOR ( 1 downto 0 );
    dir : in STD_LOGIC_VECTOR ( 3 downto 0 )
  );
  attribute ORIG_REF_NAME : string;
  attribute ORIG_REF_NAME of harvard_design_mux_datos_0_0_mux_datos : entity is "mux_datos";
end harvard_design_mux_datos_0_0_mux_datos;

architecture STRUCTURE of harvard_design_mux_datos_0_0_mux_datos is
begin
\sal[0]_INST_0\: unisim.vcomponents.LUT6
    generic map(
      INIT => X"F0AAFFCCF0AA00CC"
    )
        port map (
      I0 => B(0),
      I1 => A(0),
      I2 => datoRam(0),
      I3 => sel(1),
      I4 => sel(0),
      I5 => dir(0),
      O => sal(0)
    );
\sal[1]_INST_0\: unisim.vcomponents.LUT6
    generic map(
      INIT => X"F0AAFFCCF0AA00CC"
    )
        port map (
      I0 => B(1),
      I1 => A(1),
      I2 => datoRam(1),
      I3 => sel(1),
      I4 => sel(0),
      I5 => dir(1),
      O => sal(1)
    );
\sal[2]_INST_0\: unisim.vcomponents.LUT6
    generic map(
      INIT => X"F0AAFFCCF0AA00CC"
    )
        port map (
      I0 => B(2),
      I1 => A(2),
      I2 => datoRam(2),
      I3 => sel(1),
      I4 => sel(0),
      I5 => dir(2),
      O => sal(2)
    );
\sal[3]_INST_0\: unisim.vcomponents.LUT6
    generic map(
      INIT => X"F0AAFFCCF0AA00CC"
    )
        port map (
      I0 => B(3),
      I1 => A(3),
      I2 => datoRam(3),
      I3 => sel(1),
      I4 => sel(0),
      I5 => dir(3),
      O => sal(3)
    );
end STRUCTURE;
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity harvard_design_mux_datos_0_0 is
  port (
    A : in STD_LOGIC_VECTOR ( 3 downto 0 );
    B : in STD_LOGIC_VECTOR ( 3 downto 0 );
    dir : in STD_LOGIC_VECTOR ( 3 downto 0 );
    datoRam : in STD_LOGIC_VECTOR ( 3 downto 0 );
    sel : in STD_LOGIC_VECTOR ( 1 downto 0 );
    sal : out STD_LOGIC_VECTOR ( 3 downto 0 )
  );
  attribute NotValidForBitStream : boolean;
  attribute NotValidForBitStream of harvard_design_mux_datos_0_0 : entity is true;
  attribute CHECK_LICENSE_TYPE : string;
  attribute CHECK_LICENSE_TYPE of harvard_design_mux_datos_0_0 : entity is "harvard_design_mux_datos_0_0,mux_datos,{}";
  attribute DowngradeIPIdentifiedWarnings : string;
  attribute DowngradeIPIdentifiedWarnings of harvard_design_mux_datos_0_0 : entity is "yes";
  attribute IP_DEFINITION_SOURCE : string;
  attribute IP_DEFINITION_SOURCE of harvard_design_mux_datos_0_0 : entity is "module_ref";
  attribute X_CORE_INFO : string;
  attribute X_CORE_INFO of harvard_design_mux_datos_0_0 : entity is "mux_datos,Vivado 2026.1";
end harvard_design_mux_datos_0_0;

architecture STRUCTURE of harvard_design_mux_datos_0_0 is
begin
inst: entity work.harvard_design_mux_datos_0_0_mux_datos
     port map (
      A(3 downto 0) => A(3 downto 0),
      B(3 downto 0) => B(3 downto 0),
      datoRam(3 downto 0) => datoRam(3 downto 0),
      dir(3 downto 0) => dir(3 downto 0),
      sal(3 downto 0) => sal(3 downto 0),
      sel(1 downto 0) => sel(1 downto 0)
    );
end STRUCTURE;
