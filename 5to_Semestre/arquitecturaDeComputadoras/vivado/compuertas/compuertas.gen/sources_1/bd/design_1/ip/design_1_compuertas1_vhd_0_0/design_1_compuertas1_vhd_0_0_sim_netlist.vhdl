-- Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
-- Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
-- --------------------------------------------------------------------------------
-- Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
-- Date        : Sat Sep 26 17:45:40 2026
-- Host        : nixos-laptop running 64-bit unknown
-- Command     : write_vhdl -force -mode funcsim {/home/yovick/repos/UAZ-IEI/5to
--               Semestre/arquitecturaDeComputadoras/vivado/compuertas/compuertas.gen/sources_1/bd/design_1/ip/design_1_compuertas1_vhd_0_0/design_1_compuertas1_vhd_0_0_sim_netlist.vhdl}
-- Design      : design_1_compuertas1_vhd_0_0
-- Purpose     : This VHDL netlist is a functional simulation representation of the design and should not be modified or
--               synthesized. This netlist cannot be used for SDF annotated simulation.
-- Device      : xc7a35tcpg236-1
-- --------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity design_1_compuertas1_vhd_0_0_compuertas1_vhd is
  port (
    sal : out STD_LOGIC;
    sel : in STD_LOGIC_VECTOR ( 2 downto 0 );
    B : in STD_LOGIC;
    A : in STD_LOGIC
  );
  attribute ORIG_REF_NAME : string;
  attribute ORIG_REF_NAME of design_1_compuertas1_vhd_0_0_compuertas1_vhd : entity is "compuertas1_vhd";
end design_1_compuertas1_vhd_0_0_compuertas1_vhd;

architecture STRUCTURE of design_1_compuertas1_vhd_0_0_compuertas1_vhd is
begin
\sal__0\: unisim.vcomponents.LUT5
    generic map(
      INIT => X"C54A4BB3"
    )
        port map (
      I0 => sel(2),
      I1 => sel(1),
      I2 => B,
      I3 => sel(0),
      I4 => A,
      O => sal
    );
end STRUCTURE;
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity design_1_compuertas1_vhd_0_0 is
  port (
    A : in STD_LOGIC;
    B : in STD_LOGIC;
    sel : in STD_LOGIC_VECTOR ( 2 downto 0 );
    sal : out STD_LOGIC
  );
  attribute NotValidForBitStream : boolean;
  attribute NotValidForBitStream of design_1_compuertas1_vhd_0_0 : entity is true;
  attribute CHECK_LICENSE_TYPE : string;
  attribute CHECK_LICENSE_TYPE of design_1_compuertas1_vhd_0_0 : entity is "design_1_compuertas1_vhd_0_0,compuertas1_vhd,{}";
  attribute downgradeipidentifiedwarnings : string;
  attribute downgradeipidentifiedwarnings of design_1_compuertas1_vhd_0_0 : entity is "yes";
  attribute ip_definition_source : string;
  attribute ip_definition_source of design_1_compuertas1_vhd_0_0 : entity is "module_ref";
  attribute x_core_info : string;
  attribute x_core_info of design_1_compuertas1_vhd_0_0 : entity is "compuertas1_vhd,Vivado 2026.1";
end design_1_compuertas1_vhd_0_0;

architecture STRUCTURE of design_1_compuertas1_vhd_0_0 is
begin
U0: entity work.design_1_compuertas1_vhd_0_0_compuertas1_vhd
     port map (
      A => A,
      B => B,
      sal => sal,
      sel(2 downto 0) => sel(2 downto 0)
    );
end STRUCTURE;
