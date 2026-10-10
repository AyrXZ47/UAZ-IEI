-- Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
-- Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
-- --------------------------------------------------------------------------------
-- Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
-- Date        : Sat Oct 10 17:23:21 2026
-- Host        : nixos-laptop running 64-bit unknown
-- Command     : write_vhdl -force -mode funcsim {/home/yovick/repos/UAZ-IEI/5to
--               Semestre/arquitecturaDeComputadoras/vivado/Press_Div/Press_Div.gen/sources_1/bd/design_1/ip/design_1_div_50_50_0_0/design_1_div_50_50_0_0_sim_netlist.vhdl}
-- Design      : design_1_div_50_50_0_0
-- Purpose     : This VHDL netlist is a functional simulation representation of the design and should not be modified or
--               synthesized. This netlist cannot be used for SDF annotated simulation.
-- Device      : xc7a35tcpg236-1
-- --------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity design_1_div_50_50_0_0_div_50_50 is
  port (
    clk_div : out STD_LOGIC;
    clk : in STD_LOGIC;
    rst : in STD_LOGIC
  );
  attribute ORIG_REF_NAME : string;
  attribute ORIG_REF_NAME of design_1_div_50_50_0_0_div_50_50 : entity is "div_50_50";
end design_1_div_50_50_0_0_div_50_50;

architecture STRUCTURE of design_1_div_50_50_0_0_div_50_50 is
  signal cambio_i_1_n_0 : STD_LOGIC;
  signal cambio_i_3_n_0 : STD_LOGIC;
  signal cambio_i_4_n_0 : STD_LOGIC;
  signal cambio_i_5_n_0 : STD_LOGIC;
  signal cambio_i_6_n_0 : STD_LOGIC;
  signal cambio_i_7_n_0 : STD_LOGIC;
  signal cambio_i_8_n_0 : STD_LOGIC;
  signal \^clk_div\ : STD_LOGIC;
  signal \cont[0]_i_2_n_0\ : STD_LOGIC;
  signal \cont[0]_i_3_n_0\ : STD_LOGIC;
  signal \cont[0]_i_4_n_0\ : STD_LOGIC;
  signal \cont[0]_i_5_n_0\ : STD_LOGIC;
  signal \cont[0]_i_6_n_0\ : STD_LOGIC;
  signal \cont[12]_i_2_n_0\ : STD_LOGIC;
  signal \cont[12]_i_3_n_0\ : STD_LOGIC;
  signal \cont[12]_i_4_n_0\ : STD_LOGIC;
  signal \cont[12]_i_5_n_0\ : STD_LOGIC;
  signal \cont[16]_i_2_n_0\ : STD_LOGIC;
  signal \cont[16]_i_3_n_0\ : STD_LOGIC;
  signal \cont[16]_i_4_n_0\ : STD_LOGIC;
  signal \cont[16]_i_5_n_0\ : STD_LOGIC;
  signal \cont[20]_i_2_n_0\ : STD_LOGIC;
  signal \cont[20]_i_3_n_0\ : STD_LOGIC;
  signal \cont[20]_i_4_n_0\ : STD_LOGIC;
  signal \cont[20]_i_5_n_0\ : STD_LOGIC;
  signal \cont[24]_i_2_n_0\ : STD_LOGIC;
  signal \cont[24]_i_3_n_0\ : STD_LOGIC;
  signal \cont[24]_i_4_n_0\ : STD_LOGIC;
  signal \cont[4]_i_2_n_0\ : STD_LOGIC;
  signal \cont[4]_i_3_n_0\ : STD_LOGIC;
  signal \cont[4]_i_4_n_0\ : STD_LOGIC;
  signal \cont[4]_i_5_n_0\ : STD_LOGIC;
  signal \cont[8]_i_2_n_0\ : STD_LOGIC;
  signal \cont[8]_i_3_n_0\ : STD_LOGIC;
  signal \cont[8]_i_4_n_0\ : STD_LOGIC;
  signal \cont[8]_i_5_n_0\ : STD_LOGIC;
  signal cont_reg : STD_LOGIC_VECTOR ( 26 downto 0 );
  signal \cont_reg[0]_i_1_n_0\ : STD_LOGIC;
  signal \cont_reg[0]_i_1_n_1\ : STD_LOGIC;
  signal \cont_reg[0]_i_1_n_2\ : STD_LOGIC;
  signal \cont_reg[0]_i_1_n_3\ : STD_LOGIC;
  signal \cont_reg[0]_i_1_n_4\ : STD_LOGIC;
  signal \cont_reg[0]_i_1_n_5\ : STD_LOGIC;
  signal \cont_reg[0]_i_1_n_6\ : STD_LOGIC;
  signal \cont_reg[0]_i_1_n_7\ : STD_LOGIC;
  signal \cont_reg[12]_i_1_n_0\ : STD_LOGIC;
  signal \cont_reg[12]_i_1_n_1\ : STD_LOGIC;
  signal \cont_reg[12]_i_1_n_2\ : STD_LOGIC;
  signal \cont_reg[12]_i_1_n_3\ : STD_LOGIC;
  signal \cont_reg[12]_i_1_n_4\ : STD_LOGIC;
  signal \cont_reg[12]_i_1_n_5\ : STD_LOGIC;
  signal \cont_reg[12]_i_1_n_6\ : STD_LOGIC;
  signal \cont_reg[12]_i_1_n_7\ : STD_LOGIC;
  signal \cont_reg[16]_i_1_n_0\ : STD_LOGIC;
  signal \cont_reg[16]_i_1_n_1\ : STD_LOGIC;
  signal \cont_reg[16]_i_1_n_2\ : STD_LOGIC;
  signal \cont_reg[16]_i_1_n_3\ : STD_LOGIC;
  signal \cont_reg[16]_i_1_n_4\ : STD_LOGIC;
  signal \cont_reg[16]_i_1_n_5\ : STD_LOGIC;
  signal \cont_reg[16]_i_1_n_6\ : STD_LOGIC;
  signal \cont_reg[16]_i_1_n_7\ : STD_LOGIC;
  signal \cont_reg[20]_i_1_n_0\ : STD_LOGIC;
  signal \cont_reg[20]_i_1_n_1\ : STD_LOGIC;
  signal \cont_reg[20]_i_1_n_2\ : STD_LOGIC;
  signal \cont_reg[20]_i_1_n_3\ : STD_LOGIC;
  signal \cont_reg[20]_i_1_n_4\ : STD_LOGIC;
  signal \cont_reg[20]_i_1_n_5\ : STD_LOGIC;
  signal \cont_reg[20]_i_1_n_6\ : STD_LOGIC;
  signal \cont_reg[20]_i_1_n_7\ : STD_LOGIC;
  signal \cont_reg[24]_i_1_n_2\ : STD_LOGIC;
  signal \cont_reg[24]_i_1_n_3\ : STD_LOGIC;
  signal \cont_reg[24]_i_1_n_5\ : STD_LOGIC;
  signal \cont_reg[24]_i_1_n_6\ : STD_LOGIC;
  signal \cont_reg[24]_i_1_n_7\ : STD_LOGIC;
  signal \cont_reg[4]_i_1_n_0\ : STD_LOGIC;
  signal \cont_reg[4]_i_1_n_1\ : STD_LOGIC;
  signal \cont_reg[4]_i_1_n_2\ : STD_LOGIC;
  signal \cont_reg[4]_i_1_n_3\ : STD_LOGIC;
  signal \cont_reg[4]_i_1_n_4\ : STD_LOGIC;
  signal \cont_reg[4]_i_1_n_5\ : STD_LOGIC;
  signal \cont_reg[4]_i_1_n_6\ : STD_LOGIC;
  signal \cont_reg[4]_i_1_n_7\ : STD_LOGIC;
  signal \cont_reg[8]_i_1_n_0\ : STD_LOGIC;
  signal \cont_reg[8]_i_1_n_1\ : STD_LOGIC;
  signal \cont_reg[8]_i_1_n_2\ : STD_LOGIC;
  signal \cont_reg[8]_i_1_n_3\ : STD_LOGIC;
  signal \cont_reg[8]_i_1_n_4\ : STD_LOGIC;
  signal \cont_reg[8]_i_1_n_5\ : STD_LOGIC;
  signal \cont_reg[8]_i_1_n_6\ : STD_LOGIC;
  signal \cont_reg[8]_i_1_n_7\ : STD_LOGIC;
  signal load : STD_LOGIC;
  signal \NLW_cont_reg[24]_i_1_CO_UNCONNECTED\ : STD_LOGIC_VECTOR ( 3 downto 2 );
  signal \NLW_cont_reg[24]_i_1_O_UNCONNECTED\ : STD_LOGIC_VECTOR ( 3 to 3 );
  attribute ADDER_THRESHOLD : integer;
  attribute ADDER_THRESHOLD of \cont_reg[0]_i_1\ : label is 35;
  attribute ADDER_THRESHOLD of \cont_reg[12]_i_1\ : label is 35;
  attribute ADDER_THRESHOLD of \cont_reg[16]_i_1\ : label is 35;
  attribute ADDER_THRESHOLD of \cont_reg[20]_i_1\ : label is 35;
  attribute ADDER_THRESHOLD of \cont_reg[24]_i_1\ : label is 35;
  attribute ADDER_THRESHOLD of \cont_reg[4]_i_1\ : label is 35;
  attribute ADDER_THRESHOLD of \cont_reg[8]_i_1\ : label is 35;
begin
  clk_div <= \^clk_div\;
cambio_i_1: unisim.vcomponents.LUT2
    generic map(
      INIT => X"6"
    )
        port map (
      I0 => load,
      I1 => \^clk_div\,
      O => cambio_i_1_n_0
    );
cambio_i_2: unisim.vcomponents.LUT6
    generic map(
      INIT => X"8000000000000000"
    )
        port map (
      I0 => cambio_i_3_n_0,
      I1 => cambio_i_4_n_0,
      I2 => cambio_i_5_n_0,
      I3 => cambio_i_6_n_0,
      I4 => cambio_i_7_n_0,
      I5 => cambio_i_8_n_0,
      O => load
    );
cambio_i_3: unisim.vcomponents.LUT6
    generic map(
      INIT => X"8000000000000000"
    )
        port map (
      I0 => cont_reg(20),
      I1 => cont_reg(21),
      I2 => cont_reg(22),
      I3 => cont_reg(23),
      I4 => cont_reg(26),
      I5 => cont_reg(24),
      O => cambio_i_3_n_0
    );
cambio_i_4: unisim.vcomponents.LUT4
    generic map(
      INIT => X"1000"
    )
        port map (
      I0 => cont_reg(1),
      I1 => cont_reg(0),
      I2 => cont_reg(13),
      I3 => cont_reg(8),
      O => cambio_i_4_n_0
    );
cambio_i_5: unisim.vcomponents.LUT4
    generic map(
      INIT => X"8000"
    )
        port map (
      I0 => cont_reg(18),
      I1 => cont_reg(16),
      I2 => cont_reg(15),
      I3 => cont_reg(14),
      O => cambio_i_5_n_0
    );
cambio_i_6: unisim.vcomponents.LUT6
    generic map(
      INIT => X"0000000000000001"
    )
        port map (
      I0 => cont_reg(10),
      I1 => cont_reg(11),
      I2 => cont_reg(12),
      I3 => cont_reg(17),
      I4 => cont_reg(25),
      I5 => cont_reg(19),
      O => cambio_i_6_n_0
    );
cambio_i_7: unisim.vcomponents.LUT3
    generic map(
      INIT => X"01"
    )
        port map (
      I0 => cont_reg(4),
      I1 => cont_reg(3),
      I2 => cont_reg(2),
      O => cambio_i_7_n_0
    );
cambio_i_8: unisim.vcomponents.LUT4
    generic map(
      INIT => X"0001"
    )
        port map (
      I0 => cont_reg(9),
      I1 => cont_reg(7),
      I2 => cont_reg(6),
      I3 => cont_reg(5),
      O => cambio_i_8_n_0
    );
cambio_reg: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => cambio_i_1_n_0,
      Q => \^clk_div\
    );
\cont[0]_i_2\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"2"
    )
        port map (
      I0 => cont_reg(0),
      I1 => load,
      O => \cont[0]_i_2_n_0\
    );
\cont[0]_i_3\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"2"
    )
        port map (
      I0 => cont_reg(3),
      I1 => load,
      O => \cont[0]_i_3_n_0\
    );
\cont[0]_i_4\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"2"
    )
        port map (
      I0 => cont_reg(2),
      I1 => load,
      O => \cont[0]_i_4_n_0\
    );
\cont[0]_i_5\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"2"
    )
        port map (
      I0 => cont_reg(1),
      I1 => load,
      O => \cont[0]_i_5_n_0\
    );
\cont[0]_i_6\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"1"
    )
        port map (
      I0 => cont_reg(0),
      I1 => load,
      O => \cont[0]_i_6_n_0\
    );
\cont[12]_i_2\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"2"
    )
        port map (
      I0 => cont_reg(15),
      I1 => load,
      O => \cont[12]_i_2_n_0\
    );
\cont[12]_i_3\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"2"
    )
        port map (
      I0 => cont_reg(14),
      I1 => load,
      O => \cont[12]_i_3_n_0\
    );
\cont[12]_i_4\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"2"
    )
        port map (
      I0 => cont_reg(13),
      I1 => load,
      O => \cont[12]_i_4_n_0\
    );
\cont[12]_i_5\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"2"
    )
        port map (
      I0 => cont_reg(12),
      I1 => load,
      O => \cont[12]_i_5_n_0\
    );
\cont[16]_i_2\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"2"
    )
        port map (
      I0 => cont_reg(19),
      I1 => load,
      O => \cont[16]_i_2_n_0\
    );
\cont[16]_i_3\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"2"
    )
        port map (
      I0 => cont_reg(18),
      I1 => load,
      O => \cont[16]_i_3_n_0\
    );
\cont[16]_i_4\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"2"
    )
        port map (
      I0 => cont_reg(17),
      I1 => load,
      O => \cont[16]_i_4_n_0\
    );
\cont[16]_i_5\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"2"
    )
        port map (
      I0 => cont_reg(16),
      I1 => load,
      O => \cont[16]_i_5_n_0\
    );
\cont[20]_i_2\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"2"
    )
        port map (
      I0 => cont_reg(23),
      I1 => load,
      O => \cont[20]_i_2_n_0\
    );
\cont[20]_i_3\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"2"
    )
        port map (
      I0 => cont_reg(22),
      I1 => load,
      O => \cont[20]_i_3_n_0\
    );
\cont[20]_i_4\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"2"
    )
        port map (
      I0 => cont_reg(21),
      I1 => load,
      O => \cont[20]_i_4_n_0\
    );
\cont[20]_i_5\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"2"
    )
        port map (
      I0 => cont_reg(20),
      I1 => load,
      O => \cont[20]_i_5_n_0\
    );
\cont[24]_i_2\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"2"
    )
        port map (
      I0 => cont_reg(26),
      I1 => load,
      O => \cont[24]_i_2_n_0\
    );
\cont[24]_i_3\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"2"
    )
        port map (
      I0 => cont_reg(25),
      I1 => load,
      O => \cont[24]_i_3_n_0\
    );
\cont[24]_i_4\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"2"
    )
        port map (
      I0 => cont_reg(24),
      I1 => load,
      O => \cont[24]_i_4_n_0\
    );
\cont[4]_i_2\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"2"
    )
        port map (
      I0 => cont_reg(7),
      I1 => load,
      O => \cont[4]_i_2_n_0\
    );
\cont[4]_i_3\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"2"
    )
        port map (
      I0 => cont_reg(6),
      I1 => load,
      O => \cont[4]_i_3_n_0\
    );
\cont[4]_i_4\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"2"
    )
        port map (
      I0 => cont_reg(5),
      I1 => load,
      O => \cont[4]_i_4_n_0\
    );
\cont[4]_i_5\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"2"
    )
        port map (
      I0 => cont_reg(4),
      I1 => load,
      O => \cont[4]_i_5_n_0\
    );
\cont[8]_i_2\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"2"
    )
        port map (
      I0 => cont_reg(11),
      I1 => load,
      O => \cont[8]_i_2_n_0\
    );
\cont[8]_i_3\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"2"
    )
        port map (
      I0 => cont_reg(10),
      I1 => load,
      O => \cont[8]_i_3_n_0\
    );
\cont[8]_i_4\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"2"
    )
        port map (
      I0 => cont_reg(9),
      I1 => load,
      O => \cont[8]_i_4_n_0\
    );
\cont[8]_i_5\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"2"
    )
        port map (
      I0 => cont_reg(8),
      I1 => load,
      O => \cont[8]_i_5_n_0\
    );
\cont_reg[0]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => \cont_reg[0]_i_1_n_7\,
      Q => cont_reg(0)
    );
\cont_reg[0]_i_1\: unisim.vcomponents.CARRY4
     port map (
      CI => '0',
      CO(3) => \cont_reg[0]_i_1_n_0\,
      CO(2) => \cont_reg[0]_i_1_n_1\,
      CO(1) => \cont_reg[0]_i_1_n_2\,
      CO(0) => \cont_reg[0]_i_1_n_3\,
      CYINIT => '0',
      DI(3 downto 1) => B"000",
      DI(0) => \cont[0]_i_2_n_0\,
      O(3) => \cont_reg[0]_i_1_n_4\,
      O(2) => \cont_reg[0]_i_1_n_5\,
      O(1) => \cont_reg[0]_i_1_n_6\,
      O(0) => \cont_reg[0]_i_1_n_7\,
      S(3) => \cont[0]_i_3_n_0\,
      S(2) => \cont[0]_i_4_n_0\,
      S(1) => \cont[0]_i_5_n_0\,
      S(0) => \cont[0]_i_6_n_0\
    );
\cont_reg[10]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => \cont_reg[8]_i_1_n_5\,
      Q => cont_reg(10)
    );
\cont_reg[11]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => \cont_reg[8]_i_1_n_4\,
      Q => cont_reg(11)
    );
\cont_reg[12]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => \cont_reg[12]_i_1_n_7\,
      Q => cont_reg(12)
    );
\cont_reg[12]_i_1\: unisim.vcomponents.CARRY4
     port map (
      CI => \cont_reg[8]_i_1_n_0\,
      CO(3) => \cont_reg[12]_i_1_n_0\,
      CO(2) => \cont_reg[12]_i_1_n_1\,
      CO(1) => \cont_reg[12]_i_1_n_2\,
      CO(0) => \cont_reg[12]_i_1_n_3\,
      CYINIT => '0',
      DI(3 downto 0) => B"0000",
      O(3) => \cont_reg[12]_i_1_n_4\,
      O(2) => \cont_reg[12]_i_1_n_5\,
      O(1) => \cont_reg[12]_i_1_n_6\,
      O(0) => \cont_reg[12]_i_1_n_7\,
      S(3) => \cont[12]_i_2_n_0\,
      S(2) => \cont[12]_i_3_n_0\,
      S(1) => \cont[12]_i_4_n_0\,
      S(0) => \cont[12]_i_5_n_0\
    );
\cont_reg[13]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => \cont_reg[12]_i_1_n_6\,
      Q => cont_reg(13)
    );
\cont_reg[14]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => \cont_reg[12]_i_1_n_5\,
      Q => cont_reg(14)
    );
\cont_reg[15]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => \cont_reg[12]_i_1_n_4\,
      Q => cont_reg(15)
    );
\cont_reg[16]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => \cont_reg[16]_i_1_n_7\,
      Q => cont_reg(16)
    );
\cont_reg[16]_i_1\: unisim.vcomponents.CARRY4
     port map (
      CI => \cont_reg[12]_i_1_n_0\,
      CO(3) => \cont_reg[16]_i_1_n_0\,
      CO(2) => \cont_reg[16]_i_1_n_1\,
      CO(1) => \cont_reg[16]_i_1_n_2\,
      CO(0) => \cont_reg[16]_i_1_n_3\,
      CYINIT => '0',
      DI(3 downto 0) => B"0000",
      O(3) => \cont_reg[16]_i_1_n_4\,
      O(2) => \cont_reg[16]_i_1_n_5\,
      O(1) => \cont_reg[16]_i_1_n_6\,
      O(0) => \cont_reg[16]_i_1_n_7\,
      S(3) => \cont[16]_i_2_n_0\,
      S(2) => \cont[16]_i_3_n_0\,
      S(1) => \cont[16]_i_4_n_0\,
      S(0) => \cont[16]_i_5_n_0\
    );
\cont_reg[17]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => \cont_reg[16]_i_1_n_6\,
      Q => cont_reg(17)
    );
\cont_reg[18]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => \cont_reg[16]_i_1_n_5\,
      Q => cont_reg(18)
    );
\cont_reg[19]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => \cont_reg[16]_i_1_n_4\,
      Q => cont_reg(19)
    );
\cont_reg[1]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => \cont_reg[0]_i_1_n_6\,
      Q => cont_reg(1)
    );
\cont_reg[20]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => \cont_reg[20]_i_1_n_7\,
      Q => cont_reg(20)
    );
\cont_reg[20]_i_1\: unisim.vcomponents.CARRY4
     port map (
      CI => \cont_reg[16]_i_1_n_0\,
      CO(3) => \cont_reg[20]_i_1_n_0\,
      CO(2) => \cont_reg[20]_i_1_n_1\,
      CO(1) => \cont_reg[20]_i_1_n_2\,
      CO(0) => \cont_reg[20]_i_1_n_3\,
      CYINIT => '0',
      DI(3 downto 0) => B"0000",
      O(3) => \cont_reg[20]_i_1_n_4\,
      O(2) => \cont_reg[20]_i_1_n_5\,
      O(1) => \cont_reg[20]_i_1_n_6\,
      O(0) => \cont_reg[20]_i_1_n_7\,
      S(3) => \cont[20]_i_2_n_0\,
      S(2) => \cont[20]_i_3_n_0\,
      S(1) => \cont[20]_i_4_n_0\,
      S(0) => \cont[20]_i_5_n_0\
    );
\cont_reg[21]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => \cont_reg[20]_i_1_n_6\,
      Q => cont_reg(21)
    );
\cont_reg[22]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => \cont_reg[20]_i_1_n_5\,
      Q => cont_reg(22)
    );
\cont_reg[23]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => \cont_reg[20]_i_1_n_4\,
      Q => cont_reg(23)
    );
\cont_reg[24]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => \cont_reg[24]_i_1_n_7\,
      Q => cont_reg(24)
    );
\cont_reg[24]_i_1\: unisim.vcomponents.CARRY4
     port map (
      CI => \cont_reg[20]_i_1_n_0\,
      CO(3 downto 2) => \NLW_cont_reg[24]_i_1_CO_UNCONNECTED\(3 downto 2),
      CO(1) => \cont_reg[24]_i_1_n_2\,
      CO(0) => \cont_reg[24]_i_1_n_3\,
      CYINIT => '0',
      DI(3 downto 0) => B"0000",
      O(3) => \NLW_cont_reg[24]_i_1_O_UNCONNECTED\(3),
      O(2) => \cont_reg[24]_i_1_n_5\,
      O(1) => \cont_reg[24]_i_1_n_6\,
      O(0) => \cont_reg[24]_i_1_n_7\,
      S(3) => '0',
      S(2) => \cont[24]_i_2_n_0\,
      S(1) => \cont[24]_i_3_n_0\,
      S(0) => \cont[24]_i_4_n_0\
    );
\cont_reg[25]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => \cont_reg[24]_i_1_n_6\,
      Q => cont_reg(25)
    );
\cont_reg[26]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => \cont_reg[24]_i_1_n_5\,
      Q => cont_reg(26)
    );
\cont_reg[2]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => \cont_reg[0]_i_1_n_5\,
      Q => cont_reg(2)
    );
\cont_reg[3]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => \cont_reg[0]_i_1_n_4\,
      Q => cont_reg(3)
    );
\cont_reg[4]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => \cont_reg[4]_i_1_n_7\,
      Q => cont_reg(4)
    );
\cont_reg[4]_i_1\: unisim.vcomponents.CARRY4
     port map (
      CI => \cont_reg[0]_i_1_n_0\,
      CO(3) => \cont_reg[4]_i_1_n_0\,
      CO(2) => \cont_reg[4]_i_1_n_1\,
      CO(1) => \cont_reg[4]_i_1_n_2\,
      CO(0) => \cont_reg[4]_i_1_n_3\,
      CYINIT => '0',
      DI(3 downto 0) => B"0000",
      O(3) => \cont_reg[4]_i_1_n_4\,
      O(2) => \cont_reg[4]_i_1_n_5\,
      O(1) => \cont_reg[4]_i_1_n_6\,
      O(0) => \cont_reg[4]_i_1_n_7\,
      S(3) => \cont[4]_i_2_n_0\,
      S(2) => \cont[4]_i_3_n_0\,
      S(1) => \cont[4]_i_4_n_0\,
      S(0) => \cont[4]_i_5_n_0\
    );
\cont_reg[5]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => \cont_reg[4]_i_1_n_6\,
      Q => cont_reg(5)
    );
\cont_reg[6]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => \cont_reg[4]_i_1_n_5\,
      Q => cont_reg(6)
    );
\cont_reg[7]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => \cont_reg[4]_i_1_n_4\,
      Q => cont_reg(7)
    );
\cont_reg[8]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => \cont_reg[8]_i_1_n_7\,
      Q => cont_reg(8)
    );
\cont_reg[8]_i_1\: unisim.vcomponents.CARRY4
     port map (
      CI => \cont_reg[4]_i_1_n_0\,
      CO(3) => \cont_reg[8]_i_1_n_0\,
      CO(2) => \cont_reg[8]_i_1_n_1\,
      CO(1) => \cont_reg[8]_i_1_n_2\,
      CO(0) => \cont_reg[8]_i_1_n_3\,
      CYINIT => '0',
      DI(3 downto 0) => B"0000",
      O(3) => \cont_reg[8]_i_1_n_4\,
      O(2) => \cont_reg[8]_i_1_n_5\,
      O(1) => \cont_reg[8]_i_1_n_6\,
      O(0) => \cont_reg[8]_i_1_n_7\,
      S(3) => \cont[8]_i_2_n_0\,
      S(2) => \cont[8]_i_3_n_0\,
      S(1) => \cont[8]_i_4_n_0\,
      S(0) => \cont[8]_i_5_n_0\
    );
\cont_reg[9]\: unisim.vcomponents.FDCE
    generic map(
      INIT => '0'
    )
        port map (
      C => clk,
      CE => '1',
      CLR => rst,
      D => \cont_reg[8]_i_1_n_6\,
      Q => cont_reg(9)
    );
end STRUCTURE;
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity design_1_div_50_50_0_0 is
  port (
    clk : in STD_LOGIC;
    rst : in STD_LOGIC;
    clk_div : out STD_LOGIC
  );
  attribute NotValidForBitStream : boolean;
  attribute NotValidForBitStream of design_1_div_50_50_0_0 : entity is true;
  attribute CHECK_LICENSE_TYPE : string;
  attribute CHECK_LICENSE_TYPE of design_1_div_50_50_0_0 : entity is "design_1_div_50_50_0_0,div_50_50,{}";
  attribute downgradeipidentifiedwarnings : string;
  attribute downgradeipidentifiedwarnings of design_1_div_50_50_0_0 : entity is "yes";
  attribute ip_definition_source : string;
  attribute ip_definition_source of design_1_div_50_50_0_0 : entity is "module_ref";
  attribute x_core_info : string;
  attribute x_core_info of design_1_div_50_50_0_0 : entity is "div_50_50,Vivado 2026.1";
end design_1_div_50_50_0_0;

architecture STRUCTURE of design_1_div_50_50_0_0 is
  attribute x_interface_info : string;
  attribute x_interface_info of clk : signal is "xilinx.com:signal:clock:1.0 clk CLK";
  attribute x_interface_mode : string;
  attribute x_interface_mode of clk : signal is "slave clk";
  attribute x_interface_parameter : string;
  attribute x_interface_parameter of clk : signal is "XIL_INTERFACENAME clk, ASSOCIATED_RESET rst, FREQ_HZ 100000000, FREQ_TOLERANCE_HZ 0, PHASE 0.0, CLK_DOMAIN design_1_clk_0, INSERT_VIP 0";
  attribute x_interface_info of rst : signal is "xilinx.com:signal:reset:1.0 rst RST";
  attribute x_interface_mode of rst : signal is "slave rst";
  attribute x_interface_parameter of rst : signal is "XIL_INTERFACENAME rst, POLARITY ACTIVE_LOW, INSERT_VIP 0";
begin
U0: entity work.design_1_div_50_50_0_0_div_50_50
     port map (
      clk => clk,
      clk_div => clk_div,
      rst => rst
    );
end STRUCTURE;
