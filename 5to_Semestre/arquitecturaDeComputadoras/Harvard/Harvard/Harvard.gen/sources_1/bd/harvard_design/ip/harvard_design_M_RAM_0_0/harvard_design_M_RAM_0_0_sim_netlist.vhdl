-- Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
-- Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
-- --------------------------------------------------------------------------------
-- Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
-- Date        : Sat Nov 21 18:11:25 2026
-- Host        : nixos-laptop running 64-bit unknown
-- Command     : write_vhdl -force -mode funcsim
--               /tmp/opencode/harvard_fix/Harvard/Harvard.gen/sources_1/bd/harvard_design/ip/harvard_design_M_RAM_0_0/harvard_design_M_RAM_0_0_sim_netlist.vhdl
-- Design      : harvard_design_M_RAM_0_0
-- Purpose     : This VHDL netlist is a functional simulation representation of the design and should not be modified or
--               synthesized. This netlist cannot be used for SDF annotated simulation.
-- Device      : xc7a35tcpg236-1
-- --------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity harvard_design_M_RAM_0_0_M_RAM is
  port (
    dato_out : out STD_LOGIC_VECTOR ( 3 downto 0 );
    clk : in STD_LOGIC;
    L_E : in STD_LOGIC;
    dato_in : in STD_LOGIC_VECTOR ( 3 downto 0 );
    dir_L : in STD_LOGIC_VECTOR ( 3 downto 0 );
    dir_E : in STD_LOGIC_VECTOR ( 3 downto 0 )
  );
  attribute ORIG_REF_NAME : string;
  attribute ORIG_REF_NAME of harvard_design_M_RAM_0_0_M_RAM : entity is "M_RAM";
end harvard_design_M_RAM_0_0_M_RAM;

architecture STRUCTURE of harvard_design_M_RAM_0_0_M_RAM is
  signal p_0_in : STD_LOGIC;
  signal p_0_out : STD_LOGIC_VECTOR ( 3 downto 0 );
  signal NLW_memoria_reg_0_15_0_3_DOC_UNCONNECTED : STD_LOGIC_VECTOR ( 1 downto 0 );
  signal NLW_memoria_reg_0_15_0_3_DOD_UNCONNECTED : STD_LOGIC_VECTOR ( 1 downto 0 );
  attribute METHODOLOGY_DRC_VIOS : string;
  attribute METHODOLOGY_DRC_VIOS of memoria_reg_0_15_0_3 : label is "";
  attribute RTL_RAM_BITS : integer;
  attribute RTL_RAM_BITS of memoria_reg_0_15_0_3 : label is 64;
  attribute RTL_RAM_NAME : string;
  attribute RTL_RAM_NAME of memoria_reg_0_15_0_3 : label is "harvard_design_M_RAM_0_0/inst/memoria_reg";
  attribute RTL_RAM_STYLE : string;
  attribute RTL_RAM_STYLE of memoria_reg_0_15_0_3 : label is "auto";
  attribute RTL_RAM_TYPE : string;
  attribute RTL_RAM_TYPE of memoria_reg_0_15_0_3 : label is "RAM_SDP";
  attribute ram_addr_begin : integer;
  attribute ram_addr_begin of memoria_reg_0_15_0_3 : label is 0;
  attribute ram_addr_end : integer;
  attribute ram_addr_end of memoria_reg_0_15_0_3 : label is 15;
  attribute ram_offset : integer;
  attribute ram_offset of memoria_reg_0_15_0_3 : label is 0;
  attribute ram_slice_begin : integer;
  attribute ram_slice_begin of memoria_reg_0_15_0_3 : label is 0;
  attribute ram_slice_end : integer;
  attribute ram_slice_end of memoria_reg_0_15_0_3 : label is 3;
begin
\dato_out[3]_i_1\: unisim.vcomponents.LUT1
    generic map(
      INIT => X"1"
    )
        port map (
      I0 => L_E,
      O => p_0_in
    );
\dato_out_reg[0]\: unisim.vcomponents.FDRE
     port map (
      C => clk,
      CE => p_0_in,
      D => p_0_out(0),
      Q => dato_out(0),
      R => '0'
    );
\dato_out_reg[1]\: unisim.vcomponents.FDRE
     port map (
      C => clk,
      CE => p_0_in,
      D => p_0_out(1),
      Q => dato_out(1),
      R => '0'
    );
\dato_out_reg[2]\: unisim.vcomponents.FDRE
     port map (
      C => clk,
      CE => p_0_in,
      D => p_0_out(2),
      Q => dato_out(2),
      R => '0'
    );
\dato_out_reg[3]\: unisim.vcomponents.FDRE
     port map (
      C => clk,
      CE => p_0_in,
      D => p_0_out(3),
      Q => dato_out(3),
      R => '0'
    );
memoria_reg_0_15_0_3: unisim.vcomponents.RAM32M
    generic map(
      INIT_A => X"0000000000000000",
      INIT_B => X"0000000000000000",
      INIT_C => X"0000000000000000",
      INIT_D => X"0000000000000000"
    )
        port map (
      ADDRA(4) => '0',
      ADDRA(3 downto 0) => dir_L(3 downto 0),
      ADDRB(4) => '0',
      ADDRB(3 downto 0) => dir_L(3 downto 0),
      ADDRC(4) => '0',
      ADDRC(3 downto 0) => dir_L(3 downto 0),
      ADDRD(4) => '0',
      ADDRD(3 downto 0) => dir_E(3 downto 0),
      DIA(1 downto 0) => dato_in(1 downto 0),
      DIB(1 downto 0) => dato_in(3 downto 2),
      DIC(1 downto 0) => B"00",
      DID(1 downto 0) => B"00",
      DOA(1 downto 0) => p_0_out(1 downto 0),
      DOB(1 downto 0) => p_0_out(3 downto 2),
      DOC(1 downto 0) => NLW_memoria_reg_0_15_0_3_DOC_UNCONNECTED(1 downto 0),
      DOD(1 downto 0) => NLW_memoria_reg_0_15_0_3_DOD_UNCONNECTED(1 downto 0),
      WCLK => clk,
      WE => L_E
    );
end STRUCTURE;
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity harvard_design_M_RAM_0_0 is
  port (
    clk : in STD_LOGIC;
    dir_E : in STD_LOGIC_VECTOR ( 3 downto 0 );
    dir_L : in STD_LOGIC_VECTOR ( 3 downto 0 );
    dato_in : in STD_LOGIC_VECTOR ( 3 downto 0 );
    dato_out : out STD_LOGIC_VECTOR ( 3 downto 0 );
    L_E : in STD_LOGIC
  );
  attribute NotValidForBitStream : boolean;
  attribute NotValidForBitStream of harvard_design_M_RAM_0_0 : entity is true;
  attribute CHECK_LICENSE_TYPE : string;
  attribute CHECK_LICENSE_TYPE of harvard_design_M_RAM_0_0 : entity is "harvard_design_M_RAM_0_0,M_RAM,{}";
  attribute DowngradeIPIdentifiedWarnings : string;
  attribute DowngradeIPIdentifiedWarnings of harvard_design_M_RAM_0_0 : entity is "yes";
  attribute IP_DEFINITION_SOURCE : string;
  attribute IP_DEFINITION_SOURCE of harvard_design_M_RAM_0_0 : entity is "module_ref";
  attribute X_CORE_INFO : string;
  attribute X_CORE_INFO of harvard_design_M_RAM_0_0 : entity is "M_RAM,Vivado 2026.1";
end harvard_design_M_RAM_0_0;

architecture STRUCTURE of harvard_design_M_RAM_0_0 is
  attribute X_INTERFACE_INFO : string;
  attribute X_INTERFACE_INFO of clk : signal is "xilinx.com:signal:clock:1.0 clk CLK";
  attribute X_INTERFACE_MODE : string;
  attribute X_INTERFACE_MODE of clk : signal is "slave";
  attribute X_INTERFACE_PARAMETER : string;
  attribute X_INTERFACE_PARAMETER of clk : signal is "XIL_INTERFACENAME clk, FREQ_HZ 100000000, FREQ_TOLERANCE_HZ 0, PHASE 0.0, CLK_DOMAIN harvard_design_clk, INSERT_VIP 0";
begin
inst: entity work.harvard_design_M_RAM_0_0_M_RAM
     port map (
      L_E => L_E,
      clk => clk,
      dato_in(3 downto 0) => dato_in(3 downto 0),
      dato_out(3 downto 0) => dato_out(3 downto 0),
      dir_E(3 downto 0) => dir_E(3 downto 0),
      dir_L(3 downto 0) => dir_L(3 downto 0)
    );
end STRUCTURE;
