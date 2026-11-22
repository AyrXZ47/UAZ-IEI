--Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
--Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
----------------------------------------------------------------------------------
--Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
--Date        : Fri Oct 30 21:49:54 2026
--Host        : nixos-pc running 64-bit unknown
--Command     : generate_target design_1.bd
--Design      : design_1
--Purpose     : IP block netlist
----------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity design_1 is
  port (
    AN : out STD_LOGIC_VECTOR ( 7 downto 0 );
    CLK100MHZ : in STD_LOGIC;
    SW : in STD_LOGIC_VECTOR ( 0 to 0 );
    rst : in STD_LOGIC;
    seg : out STD_LOGIC_VECTOR ( 7 downto 0 )
  );
  attribute CORE_GENERATION_INFO : string;
  attribute CORE_GENERATION_INFO of design_1 : entity is "design_1,IP_Integrator,{x_ipVendor=xilinx.com,x_ipLibrary=BlockDiagram,x_ipName=design_1,x_ipVersion=1.00.a,x_ipLanguage=VHDL}";
  attribute HW_HANDOFF : string;
  attribute HW_HANDOFF of design_1 : entity is "design_1.hwdef";
end design_1;

architecture STRUCTURE of design_1 is
  component design_1_pres_500hz_0_0 is
  port (
    clk : in STD_LOGIC;
    rst : in STD_LOGIC;
    clk_pres : out STD_LOGIC
  );
  end component design_1_pres_500hz_0_0;
  component design_1_contador_0_0 is
  port (
    clk : in STD_LOGIC;
    rst : in STD_LOGIC;
    display : out STD_LOGIC_VECTOR ( 2 downto 0 )
  );
  end component design_1_contador_0_0;
  component design_1_dec_an_0_0 is
  port (
    ent : in STD_LOGIC_VECTOR ( 2 downto 0 );
    sal : out STD_LOGIC_VECTOR ( 7 downto 0 )
  );
  end component design_1_dec_an_0_0;
  component design_1_rom_mensajes_0_0 is
  port (
    sel : in STD_LOGIC;
    dir : in STD_LOGIC_VECTOR ( 2 downto 0 );
    seg : out STD_LOGIC_VECTOR ( 7 downto 0 )
  );
  end component design_1_rom_mensajes_0_0;
  signal contador_0_display : STD_LOGIC_VECTOR ( 2 downto 0 );
  signal pres_500hz_0_clk_pres : STD_LOGIC;
  attribute X_INTERFACE_INFO : string;
  attribute X_INTERFACE_INFO of CLK100MHZ : signal is "xilinx.com:signal:clock:1.0 CLK.CLK100MHZ CLK";
  attribute X_INTERFACE_PARAMETER : string;
  attribute X_INTERFACE_PARAMETER of CLK100MHZ : signal is "XIL_INTERFACENAME CLK.CLK100MHZ, ASSOCIATED_RESET rst, CLK_DOMAIN design_1_CLK100MHZ, FREQ_HZ 100000000, FREQ_TOLERANCE_HZ 0, INSERT_VIP 0, PHASE 0.0";
begin
contador_0: component design_1_contador_0_0
     port map (
      clk => pres_500hz_0_clk_pres,
      display(2 downto 0) => contador_0_display(2 downto 0),
      rst => rst
    );
dec_an_0: component design_1_dec_an_0_0
     port map (
      ent(2 downto 0) => contador_0_display(2 downto 0),
      sal(7 downto 0) => AN(7 downto 0)
    );
pres_500hz_0: component design_1_pres_500hz_0_0
     port map (
      clk => CLK100MHZ,
      clk_pres => pres_500hz_0_clk_pres,
      rst => rst
    );
rom_mensajes_0: component design_1_rom_mensajes_0_0
     port map (
      dir(2 downto 0) => contador_0_display(2 downto 0),
      seg(7 downto 0) => seg(7 downto 0),
      sel => SW(0)
    );
end STRUCTURE;
