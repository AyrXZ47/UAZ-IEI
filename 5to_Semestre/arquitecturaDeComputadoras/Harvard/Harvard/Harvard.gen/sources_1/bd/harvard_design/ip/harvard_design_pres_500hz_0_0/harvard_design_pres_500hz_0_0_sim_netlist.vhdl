-- Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
-- Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
-- --------------------------------------------------------------------------------
-- Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
-- Date        : Sat Nov 21 18:11:25 2026
-- Host        : nixos-laptop running 64-bit unknown
-- Command     : write_vhdl -force -mode funcsim
--               /tmp/opencode/harvard_fix/Harvard/Harvard.gen/sources_1/bd/harvard_design/ip/harvard_design_pres_500hz_0_0/harvard_design_pres_500hz_0_0_sim_netlist.vhdl
-- Design      : harvard_design_pres_500hz_0_0
-- Purpose     : This VHDL netlist is a functional simulation representation of the design and should not be modified or
--               synthesized. This netlist cannot be used for SDF annotated simulation.
-- Device      : xc7a35tcpg236-1
-- --------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity harvard_design_pres_500hz_0_0_pres_500hz is
  port (
    clk_pres : out STD_LOGIC;
    clk : in STD_LOGIC;
    rst : in STD_LOGIC
  );
  attribute ORIG_REF_NAME : string;
  attribute ORIG_REF_NAME of harvard_design_pres_500hz_0_0_pres_500hz : entity is "pres_500hz";
end harvard_design_pres_500hz_0_0_pres_500hz;

architecture STRUCTURE of harvard_design_pres_500hz_0_0_pres_500hz is
  signal clk_pres_1 : STD_LOGIC;
  signal clk_pres_i_2_n_0 : STD_LOGIC;
  signal clk_pres_i_3_n_0 : STD_LOGIC;
  signal clk_pres_i_4_n_0 : STD_LOGIC;
  signal clk_pres_i_5_n_0 : STD_LOGIC;
  signal cont : STD_LOGIC_VECTOR ( 15 downto 0 );
  signal \cont0_carry__0_n_0\ : STD_LOGIC;
  signal \cont0_carry__0_n_1\ : STD_LOGIC;
  signal \cont0_carry__0_n_2\ : STD_LOGIC;
  signal \cont0_carry__0_n_3\ : STD_LOGIC;
  signal \cont0_carry__1_n_0\ : STD_LOGIC;
  signal \cont0_carry__1_n_1\ : STD_LOGIC;
  signal \cont0_carry__1_n_2\ : STD_LOGIC;
  signal \cont0_carry__1_n_3\ : STD_LOGIC;
  signal \cont0_carry__2_n_2\ : STD_LOGIC;
  signal \cont0_carry__2_n_3\ : STD_LOGIC;
  signal cont0_carry_n_0 : STD_LOGIC;
  signal cont0_carry_n_1 : STD_LOGIC;
  signal cont0_carry_n_2 : STD_LOGIC;
  signal cont0_carry_n_3 : STD_LOGIC;
  signal cont_0 : STD_LOGIC_VECTOR ( 15 downto 0 );
  signal data0 : STD_LOGIC_VECTOR ( 15 downto 1 );
  signal \NLW_cont0_carry__2_CO_UNCONNECTED\ : STD_LOGIC_VECTOR ( 3 downto 2 );
  signal \NLW_cont0_carry__2_O_UNCONNECTED\ : STD_LOGIC_VECTOR ( 3 to 3 );
  attribute SOFT_HLUTNM : string;
  attribute SOFT_HLUTNM of clk_pres_i_1 : label is "soft_lutpair0";
  attribute SOFT_HLUTNM of clk_pres_i_3 : label is "soft_lutpair1";
  attribute ADDER_THRESHOLD : integer;
  attribute ADDER_THRESHOLD of cont0_carry : label is 35;
  attribute ADDER_THRESHOLD of \cont0_carry__0\ : label is 35;
  attribute ADDER_THRESHOLD of \cont0_carry__1\ : label is 35;
  attribute ADDER_THRESHOLD of \cont0_carry__2\ : label is 35;
  attribute SOFT_HLUTNM of \cont[0]_i_1\ : label is "soft_lutpair1";
  attribute SOFT_HLUTNM of \cont[15]_i_1\ : label is "soft_lutpair0";
begin
clk_pres_i_1: unisim.vcomponents.LUT4
    generic map(
      INIT => X"0001"
    )
        port map (
      I0 => clk_pres_i_2_n_0,
      I1 => clk_pres_i_3_n_0,
      I2 => clk_pres_i_4_n_0,
      I3 => clk_pres_i_5_n_0,
      O => clk_pres_1
    );
clk_pres_i_2: unisim.vcomponents.LUT4
    generic map(
      INIT => X"FFEF"
    )
        port map (
      I0 => cont(5),
      I1 => cont(4),
      I2 => cont(6),
      I3 => cont(7),
      O => clk_pres_i_2_n_0
    );
clk_pres_i_3: unisim.vcomponents.LUT4
    generic map(
      INIT => X"7FFF"
    )
        port map (
      I0 => cont(1),
      I1 => cont(0),
      I2 => cont(3),
      I3 => cont(2),
      O => clk_pres_i_3_n_0
    );
clk_pres_i_4: unisim.vcomponents.LUT4
    generic map(
      INIT => X"EFFF"
    )
        port map (
      I0 => cont(13),
      I1 => cont(12),
      I2 => cont(15),
      I3 => cont(14),
      O => clk_pres_i_4_n_0
    );
clk_pres_i_5: unisim.vcomponents.LUT4
    generic map(
      INIT => X"FFF7"
    )
        port map (
      I0 => cont(9),
      I1 => cont(8),
      I2 => cont(11),
      I3 => cont(10),
      O => clk_pres_i_5_n_0
    );
clk_pres_reg: unisim.vcomponents.FDCE
     port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => clk_pres_1,
      Q => clk_pres
    );
cont0_carry: unisim.vcomponents.CARRY4
     port map (
      CI => '0',
      CO(3) => cont0_carry_n_0,
      CO(2) => cont0_carry_n_1,
      CO(1) => cont0_carry_n_2,
      CO(0) => cont0_carry_n_3,
      CYINIT => cont(0),
      DI(3 downto 0) => B"0000",
      O(3 downto 0) => data0(4 downto 1),
      S(3 downto 0) => cont(4 downto 1)
    );
\cont0_carry__0\: unisim.vcomponents.CARRY4
     port map (
      CI => cont0_carry_n_0,
      CO(3) => \cont0_carry__0_n_0\,
      CO(2) => \cont0_carry__0_n_1\,
      CO(1) => \cont0_carry__0_n_2\,
      CO(0) => \cont0_carry__0_n_3\,
      CYINIT => '0',
      DI(3 downto 0) => B"0000",
      O(3 downto 0) => data0(8 downto 5),
      S(3 downto 0) => cont(8 downto 5)
    );
\cont0_carry__1\: unisim.vcomponents.CARRY4
     port map (
      CI => \cont0_carry__0_n_0\,
      CO(3) => \cont0_carry__1_n_0\,
      CO(2) => \cont0_carry__1_n_1\,
      CO(1) => \cont0_carry__1_n_2\,
      CO(0) => \cont0_carry__1_n_3\,
      CYINIT => '0',
      DI(3 downto 0) => B"0000",
      O(3 downto 0) => data0(12 downto 9),
      S(3 downto 0) => cont(12 downto 9)
    );
\cont0_carry__2\: unisim.vcomponents.CARRY4
     port map (
      CI => \cont0_carry__1_n_0\,
      CO(3 downto 2) => \NLW_cont0_carry__2_CO_UNCONNECTED\(3 downto 2),
      CO(1) => \cont0_carry__2_n_2\,
      CO(0) => \cont0_carry__2_n_3\,
      CYINIT => '0',
      DI(3 downto 0) => B"0000",
      O(3) => \NLW_cont0_carry__2_O_UNCONNECTED\(3),
      O(2 downto 0) => data0(15 downto 13),
      S(3) => '0',
      S(2 downto 0) => cont(15 downto 13)
    );
\cont[0]_i_1\: unisim.vcomponents.LUT1
    generic map(
      INIT => X"1"
    )
        port map (
      I0 => cont(0),
      O => cont_0(0)
    );
\cont[10]_i_1\: unisim.vcomponents.LUT5
    generic map(
      INIT => X"FFFE0000"
    )
        port map (
      I0 => clk_pres_i_2_n_0,
      I1 => clk_pres_i_3_n_0,
      I2 => clk_pres_i_4_n_0,
      I3 => clk_pres_i_5_n_0,
      I4 => data0(10),
      O => cont_0(10)
    );
\cont[11]_i_1\: unisim.vcomponents.LUT5
    generic map(
      INIT => X"FFFE0000"
    )
        port map (
      I0 => clk_pres_i_2_n_0,
      I1 => clk_pres_i_3_n_0,
      I2 => clk_pres_i_4_n_0,
      I3 => clk_pres_i_5_n_0,
      I4 => data0(11),
      O => cont_0(11)
    );
\cont[12]_i_1\: unisim.vcomponents.LUT5
    generic map(
      INIT => X"FFFE0000"
    )
        port map (
      I0 => clk_pres_i_2_n_0,
      I1 => clk_pres_i_3_n_0,
      I2 => clk_pres_i_4_n_0,
      I3 => clk_pres_i_5_n_0,
      I4 => data0(12),
      O => cont_0(12)
    );
\cont[13]_i_1\: unisim.vcomponents.LUT5
    generic map(
      INIT => X"FFFE0000"
    )
        port map (
      I0 => clk_pres_i_2_n_0,
      I1 => clk_pres_i_3_n_0,
      I2 => clk_pres_i_4_n_0,
      I3 => clk_pres_i_5_n_0,
      I4 => data0(13),
      O => cont_0(13)
    );
\cont[14]_i_1\: unisim.vcomponents.LUT5
    generic map(
      INIT => X"FFFE0000"
    )
        port map (
      I0 => clk_pres_i_2_n_0,
      I1 => clk_pres_i_3_n_0,
      I2 => clk_pres_i_4_n_0,
      I3 => clk_pres_i_5_n_0,
      I4 => data0(14),
      O => cont_0(14)
    );
\cont[15]_i_1\: unisim.vcomponents.LUT5
    generic map(
      INIT => X"FFFE0000"
    )
        port map (
      I0 => clk_pres_i_2_n_0,
      I1 => clk_pres_i_3_n_0,
      I2 => clk_pres_i_4_n_0,
      I3 => clk_pres_i_5_n_0,
      I4 => data0(15),
      O => cont_0(15)
    );
\cont[1]_i_1\: unisim.vcomponents.LUT5
    generic map(
      INIT => X"FFFE0000"
    )
        port map (
      I0 => clk_pres_i_2_n_0,
      I1 => clk_pres_i_3_n_0,
      I2 => clk_pres_i_4_n_0,
      I3 => clk_pres_i_5_n_0,
      I4 => data0(1),
      O => cont_0(1)
    );
\cont[2]_i_1\: unisim.vcomponents.LUT5
    generic map(
      INIT => X"FFFE0000"
    )
        port map (
      I0 => clk_pres_i_2_n_0,
      I1 => clk_pres_i_3_n_0,
      I2 => clk_pres_i_4_n_0,
      I3 => clk_pres_i_5_n_0,
      I4 => data0(2),
      O => cont_0(2)
    );
\cont[3]_i_1\: unisim.vcomponents.LUT5
    generic map(
      INIT => X"FFFE0000"
    )
        port map (
      I0 => clk_pres_i_2_n_0,
      I1 => clk_pres_i_3_n_0,
      I2 => clk_pres_i_4_n_0,
      I3 => clk_pres_i_5_n_0,
      I4 => data0(3),
      O => cont_0(3)
    );
\cont[4]_i_1\: unisim.vcomponents.LUT5
    generic map(
      INIT => X"FFFE0000"
    )
        port map (
      I0 => clk_pres_i_2_n_0,
      I1 => clk_pres_i_3_n_0,
      I2 => clk_pres_i_4_n_0,
      I3 => clk_pres_i_5_n_0,
      I4 => data0(4),
      O => cont_0(4)
    );
\cont[5]_i_1\: unisim.vcomponents.LUT5
    generic map(
      INIT => X"FFFE0000"
    )
        port map (
      I0 => clk_pres_i_2_n_0,
      I1 => clk_pres_i_3_n_0,
      I2 => clk_pres_i_4_n_0,
      I3 => clk_pres_i_5_n_0,
      I4 => data0(5),
      O => cont_0(5)
    );
\cont[6]_i_1\: unisim.vcomponents.LUT5
    generic map(
      INIT => X"FFFE0000"
    )
        port map (
      I0 => clk_pres_i_2_n_0,
      I1 => clk_pres_i_3_n_0,
      I2 => clk_pres_i_4_n_0,
      I3 => clk_pres_i_5_n_0,
      I4 => data0(6),
      O => cont_0(6)
    );
\cont[7]_i_1\: unisim.vcomponents.LUT5
    generic map(
      INIT => X"FFFE0000"
    )
        port map (
      I0 => clk_pres_i_2_n_0,
      I1 => clk_pres_i_3_n_0,
      I2 => clk_pres_i_4_n_0,
      I3 => clk_pres_i_5_n_0,
      I4 => data0(7),
      O => cont_0(7)
    );
\cont[8]_i_1\: unisim.vcomponents.LUT5
    generic map(
      INIT => X"FFFE0000"
    )
        port map (
      I0 => clk_pres_i_2_n_0,
      I1 => clk_pres_i_3_n_0,
      I2 => clk_pres_i_4_n_0,
      I3 => clk_pres_i_5_n_0,
      I4 => data0(8),
      O => cont_0(8)
    );
\cont[9]_i_1\: unisim.vcomponents.LUT5
    generic map(
      INIT => X"FFFE0000"
    )
        port map (
      I0 => clk_pres_i_2_n_0,
      I1 => clk_pres_i_3_n_0,
      I2 => clk_pres_i_4_n_0,
      I3 => clk_pres_i_5_n_0,
      I4 => data0(9),
      O => cont_0(9)
    );
\cont_reg[0]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => cont_0(0),
      Q => cont(0)
    );
\cont_reg[10]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => cont_0(10),
      Q => cont(10)
    );
\cont_reg[11]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => cont_0(11),
      Q => cont(11)
    );
\cont_reg[12]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => cont_0(12),
      Q => cont(12)
    );
\cont_reg[13]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => cont_0(13),
      Q => cont(13)
    );
\cont_reg[14]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => cont_0(14),
      Q => cont(14)
    );
\cont_reg[15]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => cont_0(15),
      Q => cont(15)
    );
\cont_reg[1]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => cont_0(1),
      Q => cont(1)
    );
\cont_reg[2]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => cont_0(2),
      Q => cont(2)
    );
\cont_reg[3]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => cont_0(3),
      Q => cont(3)
    );
\cont_reg[4]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => cont_0(4),
      Q => cont(4)
    );
\cont_reg[5]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => cont_0(5),
      Q => cont(5)
    );
\cont_reg[6]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => cont_0(6),
      Q => cont(6)
    );
\cont_reg[7]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => cont_0(7),
      Q => cont(7)
    );
\cont_reg[8]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => cont_0(8),
      Q => cont(8)
    );
\cont_reg[9]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => cont_0(9),
      Q => cont(9)
    );
end STRUCTURE;
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity harvard_design_pres_500hz_0_0 is
  port (
    clk : in STD_LOGIC;
    rst : in STD_LOGIC;
    clk_pres : out STD_LOGIC
  );
  attribute NotValidForBitStream : boolean;
  attribute NotValidForBitStream of harvard_design_pres_500hz_0_0 : entity is true;
  attribute CHECK_LICENSE_TYPE : string;
  attribute CHECK_LICENSE_TYPE of harvard_design_pres_500hz_0_0 : entity is "harvard_design_pres_500hz_0_0,pres_500hz,{}";
  attribute DowngradeIPIdentifiedWarnings : string;
  attribute DowngradeIPIdentifiedWarnings of harvard_design_pres_500hz_0_0 : entity is "yes";
  attribute IP_DEFINITION_SOURCE : string;
  attribute IP_DEFINITION_SOURCE of harvard_design_pres_500hz_0_0 : entity is "module_ref";
  attribute X_CORE_INFO : string;
  attribute X_CORE_INFO of harvard_design_pres_500hz_0_0 : entity is "pres_500hz,Vivado 2026.1";
end harvard_design_pres_500hz_0_0;

architecture STRUCTURE of harvard_design_pres_500hz_0_0 is
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
inst: entity work.harvard_design_pres_500hz_0_0_pres_500hz
     port map (
      clk => clk,
      clk_pres => clk_pres,
      rst => rst
    );
end STRUCTURE;
