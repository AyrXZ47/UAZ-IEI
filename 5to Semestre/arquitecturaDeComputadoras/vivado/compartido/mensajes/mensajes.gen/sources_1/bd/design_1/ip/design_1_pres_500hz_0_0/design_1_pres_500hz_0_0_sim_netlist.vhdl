-- Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
-- Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
-- --------------------------------------------------------------------------------
-- Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
-- Date        : Sat Oct 31 01:29:06 2026
-- Host        : nixos-pc running 64-bit unknown
-- Command     : write_vhdl -force -mode funcsim {/home/yovick/repos/UAZ-IEI/5to
--               Semestre/arquitecturaDeComputadoras/vivado/compartido/mensajes/mensajes.gen/sources_1/bd/design_1/ip/design_1_pres_500hz_0_0/design_1_pres_500hz_0_0_sim_netlist.vhdl}
-- Design      : design_1_pres_500hz_0_0
-- Purpose     : This VHDL netlist is a functional simulation representation of the design and should not be modified or
--               synthesized. This netlist cannot be used for SDF annotated simulation.
-- Device      : xc7a100tcsg324-1
-- --------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity design_1_pres_500hz_0_0_pres_500hz is
  port (
    clk_pres : out STD_LOGIC;
    clk : in STD_LOGIC;
    rst : in STD_LOGIC
  );
  attribute ORIG_REF_NAME : string;
  attribute ORIG_REF_NAME of design_1_pres_500hz_0_0_pres_500hz : entity is "pres_500hz";
end design_1_pres_500hz_0_0_pres_500hz;

architecture STRUCTURE of design_1_pres_500hz_0_0_pres_500hz is
  signal clk_pres_0 : STD_LOGIC;
  signal clk_pres_i_2_n_0 : STD_LOGIC;
  signal clk_pres_i_3_n_0 : STD_LOGIC;
  signal clk_pres_i_4_n_0 : STD_LOGIC;
  signal clk_pres_i_5_n_0 : STD_LOGIC;
  signal cont : STD_LOGIC_VECTOR ( 14 downto 0 );
  signal cont_1 : STD_LOGIC_VECTOR ( 14 downto 0 );
  signal \cont_reg[12]_i_2_n_0\ : STD_LOGIC;
  signal \cont_reg[12]_i_2_n_1\ : STD_LOGIC;
  signal \cont_reg[12]_i_2_n_2\ : STD_LOGIC;
  signal \cont_reg[12]_i_2_n_3\ : STD_LOGIC;
  signal \cont_reg[14]_i_2_n_3\ : STD_LOGIC;
  signal \cont_reg[4]_i_2_n_0\ : STD_LOGIC;
  signal \cont_reg[4]_i_2_n_1\ : STD_LOGIC;
  signal \cont_reg[4]_i_2_n_2\ : STD_LOGIC;
  signal \cont_reg[4]_i_2_n_3\ : STD_LOGIC;
  signal \cont_reg[8]_i_2_n_0\ : STD_LOGIC;
  signal \cont_reg[8]_i_2_n_1\ : STD_LOGIC;
  signal \cont_reg[8]_i_2_n_2\ : STD_LOGIC;
  signal \cont_reg[8]_i_2_n_3\ : STD_LOGIC;
  signal data0 : STD_LOGIC_VECTOR ( 14 downto 1 );
  signal \NLW_cont_reg[14]_i_2_CO_UNCONNECTED\ : STD_LOGIC_VECTOR ( 3 downto 1 );
  signal \NLW_cont_reg[14]_i_2_O_UNCONNECTED\ : STD_LOGIC_VECTOR ( 3 downto 2 );
  attribute SOFT_HLUTNM : string;
  attribute SOFT_HLUTNM of clk_pres_i_1 : label is "soft_lutpair0";
  attribute SOFT_HLUTNM of \cont[10]_i_1\ : label is "soft_lutpair5";
  attribute SOFT_HLUTNM of \cont[11]_i_1\ : label is "soft_lutpair5";
  attribute SOFT_HLUTNM of \cont[12]_i_1\ : label is "soft_lutpair6";
  attribute SOFT_HLUTNM of \cont[13]_i_1\ : label is "soft_lutpair6";
  attribute SOFT_HLUTNM of \cont[1]_i_1\ : label is "soft_lutpair0";
  attribute SOFT_HLUTNM of \cont[2]_i_1\ : label is "soft_lutpair1";
  attribute SOFT_HLUTNM of \cont[3]_i_1\ : label is "soft_lutpair1";
  attribute SOFT_HLUTNM of \cont[4]_i_1\ : label is "soft_lutpair2";
  attribute SOFT_HLUTNM of \cont[5]_i_1\ : label is "soft_lutpair2";
  attribute SOFT_HLUTNM of \cont[6]_i_1\ : label is "soft_lutpair3";
  attribute SOFT_HLUTNM of \cont[7]_i_1\ : label is "soft_lutpair3";
  attribute SOFT_HLUTNM of \cont[8]_i_1\ : label is "soft_lutpair4";
  attribute SOFT_HLUTNM of \cont[9]_i_1\ : label is "soft_lutpair4";
  attribute ADDER_THRESHOLD : integer;
  attribute ADDER_THRESHOLD of \cont_reg[12]_i_2\ : label is 35;
  attribute ADDER_THRESHOLD of \cont_reg[14]_i_2\ : label is 35;
  attribute ADDER_THRESHOLD of \cont_reg[4]_i_2\ : label is 35;
  attribute ADDER_THRESHOLD of \cont_reg[8]_i_2\ : label is 35;
begin
clk_pres_i_1: unisim.vcomponents.LUT1
    generic map(
      INIT => X"1"
    )
        port map (
      I0 => clk_pres_i_2_n_0,
      O => clk_pres_0
    );
clk_pres_i_2: unisim.vcomponents.LUT6
    generic map(
      INIT => X"FFFFFFFFEFFFFFFF"
    )
        port map (
      I0 => clk_pres_i_3_n_0,
      I1 => clk_pres_i_4_n_0,
      I2 => cont(14),
      I3 => cont(13),
      I4 => cont(0),
      I5 => clk_pres_i_5_n_0,
      O => clk_pres_i_2_n_0
    );
clk_pres_i_3: unisim.vcomponents.LUT4
    generic map(
      INIT => X"DFFF"
    )
        port map (
      I0 => cont(5),
      I1 => cont(6),
      I2 => cont(8),
      I3 => cont(7),
      O => clk_pres_i_3_n_0
    );
clk_pres_i_4: unisim.vcomponents.LUT4
    generic map(
      INIT => X"FFF7"
    )
        port map (
      I0 => cont(2),
      I1 => cont(1),
      I2 => cont(4),
      I3 => cont(3),
      O => clk_pres_i_4_n_0
    );
clk_pres_i_5: unisim.vcomponents.LUT4
    generic map(
      INIT => X"FFFE"
    )
        port map (
      I0 => cont(10),
      I1 => cont(9),
      I2 => cont(12),
      I3 => cont(11),
      O => clk_pres_i_5_n_0
    );
clk_pres_reg: unisim.vcomponents.FDCE
     port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => clk_pres_0,
      Q => clk_pres
    );
\cont[0]_i_1\: unisim.vcomponents.LUT1
    generic map(
      INIT => X"1"
    )
        port map (
      I0 => cont(0),
      O => cont_1(0)
    );
\cont[10]_i_1\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"8"
    )
        port map (
      I0 => clk_pres_i_2_n_0,
      I1 => data0(10),
      O => cont_1(10)
    );
\cont[11]_i_1\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"8"
    )
        port map (
      I0 => clk_pres_i_2_n_0,
      I1 => data0(11),
      O => cont_1(11)
    );
\cont[12]_i_1\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"8"
    )
        port map (
      I0 => clk_pres_i_2_n_0,
      I1 => data0(12),
      O => cont_1(12)
    );
\cont[13]_i_1\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"8"
    )
        port map (
      I0 => clk_pres_i_2_n_0,
      I1 => data0(13),
      O => cont_1(13)
    );
\cont[14]_i_1\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"8"
    )
        port map (
      I0 => clk_pres_i_2_n_0,
      I1 => data0(14),
      O => cont_1(14)
    );
\cont[1]_i_1\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"8"
    )
        port map (
      I0 => clk_pres_i_2_n_0,
      I1 => data0(1),
      O => cont_1(1)
    );
\cont[2]_i_1\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"8"
    )
        port map (
      I0 => clk_pres_i_2_n_0,
      I1 => data0(2),
      O => cont_1(2)
    );
\cont[3]_i_1\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"8"
    )
        port map (
      I0 => clk_pres_i_2_n_0,
      I1 => data0(3),
      O => cont_1(3)
    );
\cont[4]_i_1\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"8"
    )
        port map (
      I0 => clk_pres_i_2_n_0,
      I1 => data0(4),
      O => cont_1(4)
    );
\cont[5]_i_1\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"8"
    )
        port map (
      I0 => clk_pres_i_2_n_0,
      I1 => data0(5),
      O => cont_1(5)
    );
\cont[6]_i_1\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"8"
    )
        port map (
      I0 => clk_pres_i_2_n_0,
      I1 => data0(6),
      O => cont_1(6)
    );
\cont[7]_i_1\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"8"
    )
        port map (
      I0 => clk_pres_i_2_n_0,
      I1 => data0(7),
      O => cont_1(7)
    );
\cont[8]_i_1\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"8"
    )
        port map (
      I0 => clk_pres_i_2_n_0,
      I1 => data0(8),
      O => cont_1(8)
    );
\cont[9]_i_1\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"8"
    )
        port map (
      I0 => clk_pres_i_2_n_0,
      I1 => data0(9),
      O => cont_1(9)
    );
\cont_reg[0]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => cont_1(0),
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
      D => cont_1(10),
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
      D => cont_1(11),
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
      D => cont_1(12),
      Q => cont(12)
    );
\cont_reg[12]_i_2\: unisim.vcomponents.CARRY4
     port map (
      CI => \cont_reg[8]_i_2_n_0\,
      CO(3) => \cont_reg[12]_i_2_n_0\,
      CO(2) => \cont_reg[12]_i_2_n_1\,
      CO(1) => \cont_reg[12]_i_2_n_2\,
      CO(0) => \cont_reg[12]_i_2_n_3\,
      CYINIT => '0',
      DI(3 downto 0) => B"0000",
      O(3 downto 0) => data0(12 downto 9),
      S(3 downto 0) => cont(12 downto 9)
    );
\cont_reg[13]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => cont_1(13),
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
      D => cont_1(14),
      Q => cont(14)
    );
\cont_reg[14]_i_2\: unisim.vcomponents.CARRY4
     port map (
      CI => \cont_reg[12]_i_2_n_0\,
      CO(3 downto 1) => \NLW_cont_reg[14]_i_2_CO_UNCONNECTED\(3 downto 1),
      CO(0) => \cont_reg[14]_i_2_n_3\,
      CYINIT => '0',
      DI(3 downto 0) => B"0000",
      O(3 downto 2) => \NLW_cont_reg[14]_i_2_O_UNCONNECTED\(3 downto 2),
      O(1 downto 0) => data0(14 downto 13),
      S(3 downto 2) => B"00",
      S(1 downto 0) => cont(14 downto 13)
    );
\cont_reg[1]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => cont_1(1),
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
      D => cont_1(2),
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
      D => cont_1(3),
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
      D => cont_1(4),
      Q => cont(4)
    );
\cont_reg[4]_i_2\: unisim.vcomponents.CARRY4
     port map (
      CI => '0',
      CO(3) => \cont_reg[4]_i_2_n_0\,
      CO(2) => \cont_reg[4]_i_2_n_1\,
      CO(1) => \cont_reg[4]_i_2_n_2\,
      CO(0) => \cont_reg[4]_i_2_n_3\,
      CYINIT => cont(0),
      DI(3 downto 0) => B"0000",
      O(3 downto 0) => data0(4 downto 1),
      S(3 downto 0) => cont(4 downto 1)
    );
\cont_reg[5]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => cont_1(5),
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
      D => cont_1(6),
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
      D => cont_1(7),
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
      D => cont_1(8),
      Q => cont(8)
    );
\cont_reg[8]_i_2\: unisim.vcomponents.CARRY4
     port map (
      CI => \cont_reg[4]_i_2_n_0\,
      CO(3) => \cont_reg[8]_i_2_n_0\,
      CO(2) => \cont_reg[8]_i_2_n_1\,
      CO(1) => \cont_reg[8]_i_2_n_2\,
      CO(0) => \cont_reg[8]_i_2_n_3\,
      CYINIT => '0',
      DI(3 downto 0) => B"0000",
      O(3 downto 0) => data0(8 downto 5),
      S(3 downto 0) => cont(8 downto 5)
    );
\cont_reg[9]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => cont_1(9),
      Q => cont(9)
    );
end STRUCTURE;
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity design_1_pres_500hz_0_0 is
  port (
    clk : in STD_LOGIC;
    rst : in STD_LOGIC;
    clk_pres : out STD_LOGIC
  );
  attribute NotValidForBitStream : boolean;
  attribute NotValidForBitStream of design_1_pres_500hz_0_0 : entity is true;
  attribute CHECK_LICENSE_TYPE : string;
  attribute CHECK_LICENSE_TYPE of design_1_pres_500hz_0_0 : entity is "design_1_pres_500hz_0_0,pres_500hz,{}";
  attribute downgradeipidentifiedwarnings : string;
  attribute downgradeipidentifiedwarnings of design_1_pres_500hz_0_0 : entity is "yes";
  attribute ip_definition_source : string;
  attribute ip_definition_source of design_1_pres_500hz_0_0 : entity is "module_ref";
  attribute x_core_info : string;
  attribute x_core_info of design_1_pres_500hz_0_0 : entity is "pres_500hz,Vivado 2026.1";
end design_1_pres_500hz_0_0;

architecture STRUCTURE of design_1_pres_500hz_0_0 is
  attribute x_interface_info : string;
  attribute x_interface_info of clk : signal is "xilinx.com:signal:clock:1.0 clk CLK";
  attribute x_interface_mode : string;
  attribute x_interface_mode of clk : signal is "slave clk";
  attribute x_interface_parameter : string;
  attribute x_interface_parameter of clk : signal is "XIL_INTERFACENAME clk, ASSOCIATED_RESET rst, FREQ_HZ 100000000, FREQ_TOLERANCE_HZ 0, PHASE 0.0, CLK_DOMAIN design_1_CLK100MHZ, INSERT_VIP 0";
  attribute x_interface_info of rst : signal is "xilinx.com:signal:reset:1.0 rst RST";
  attribute x_interface_mode of rst : signal is "slave rst";
  attribute x_interface_parameter of rst : signal is "XIL_INTERFACENAME rst, POLARITY ACTIVE_LOW, INSERT_VIP 0";
begin
U0: entity work.design_1_pres_500hz_0_0_pres_500hz
     port map (
      clk => clk,
      clk_pres => clk_pres,
      rst => rst
    );
end STRUCTURE;
