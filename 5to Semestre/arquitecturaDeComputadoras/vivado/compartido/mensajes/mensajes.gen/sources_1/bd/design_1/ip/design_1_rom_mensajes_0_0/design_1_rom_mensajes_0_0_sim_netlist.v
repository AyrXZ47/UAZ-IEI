// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
// Date        : Fri Oct 30 21:50:18 2026
// Host        : nixos-pc running 64-bit unknown
// Command     : write_verilog -force -mode funcsim {/home/yovick/repos/UAZ-IEI/5to
//               Semestre/arquitecturaDeComputadoras/vivado/compartido/mensajes/mensajes.gen/sources_1/bd/design_1/ip/design_1_rom_mensajes_0_0/design_1_rom_mensajes_0_0_sim_netlist.v}
// Design      : design_1_rom_mensajes_0_0
// Purpose     : This verilog netlist is a functional simulation representation of the design and should not be modified
//               or synthesized. This netlist cannot be used for SDF annotated simulation.
// Device      : xc7a100tcsg324-1
// --------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

(* CHECK_LICENSE_TYPE = "design_1_rom_mensajes_0_0,rom_mensajes,{}" *) (* downgradeipidentifiedwarnings = "yes" *) (* ip_definition_source = "module_ref" *) 
(* x_core_info = "rom_mensajes,Vivado 2026.1" *) 
(* NotValidForBitStream *)
module design_1_rom_mensajes_0_0
   (sel,
    dir,
    seg);
  input sel;
  input [2:0]dir;
  output [7:0]seg;

  wire [2:0]dir;
  wire [7:0]seg;
  wire sel;

  design_1_rom_mensajes_0_0_rom_mensajes U0
       (.dir(dir),
        .seg(seg[5:0]),
        .sel(sel));
  LUT4 #(
    .INIT(16'h004B)) 
    \seg[6]_INST_0 
       (.I0(dir[1]),
        .I1(dir[0]),
        .I2(dir[2]),
        .I3(sel),
        .O(seg[6]));
  LUT2 #(
    .INIT(4'h2)) 
    \seg[7]_INST_0 
       (.I0(dir[0]),
        .I1(sel),
        .O(seg[7]));
endmodule

(* ORIG_REF_NAME = "rom_mensajes" *) 
module design_1_rom_mensajes_0_0_rom_mensajes
   (seg,
    sel,
    dir);
  output [5:0]seg;
  input sel;
  input [2:0]dir;

  wire [2:0]dir;
  wire [5:0]seg;
  wire sel;

  (* SOFT_HLUTNM = "soft_lutpair2" *) 
  LUT4 #(
    .INIT(16'hBFFF)) 
    \seg[0]_INST_0 
       (.I0(sel),
        .I1(dir[2]),
        .I2(dir[0]),
        .I3(dir[1]),
        .O(seg[0]));
  (* SOFT_HLUTNM = "soft_lutpair0" *) 
  LUT4 #(
    .INIT(16'h17E0)) 
    \seg[1]_INST_0 
       (.I0(sel),
        .I1(dir[1]),
        .I2(dir[2]),
        .I3(dir[0]),
        .O(seg[1]));
  (* SOFT_HLUTNM = "soft_lutpair0" *) 
  LUT4 #(
    .INIT(16'hCF82)) 
    \seg[2]_INST_0 
       (.I0(sel),
        .I1(dir[1]),
        .I2(dir[2]),
        .I3(dir[0]),
        .O(seg[2]));
  (* SOFT_HLUTNM = "soft_lutpair1" *) 
  LUT4 #(
    .INIT(16'h7831)) 
    \seg[3]_INST_0 
       (.I0(sel),
        .I1(dir[2]),
        .I2(dir[0]),
        .I3(dir[1]),
        .O(seg[3]));
  (* SOFT_HLUTNM = "soft_lutpair1" *) 
  LUT4 #(
    .INIT(16'h0790)) 
    \seg[4]_INST_0 
       (.I0(sel),
        .I1(dir[1]),
        .I2(dir[2]),
        .I3(dir[0]),
        .O(seg[4]));
  (* SOFT_HLUTNM = "soft_lutpair2" *) 
  LUT4 #(
    .INIT(16'h8542)) 
    \seg[5]_INST_0 
       (.I0(sel),
        .I1(dir[0]),
        .I2(dir[2]),
        .I3(dir[1]),
        .O(seg[5]));
endmodule
`ifndef GLBL
`define GLBL
`timescale  1 ps / 1 ps

module glbl ();

    parameter ROC_WIDTH = 100000;
    parameter TOC_WIDTH = 0;
    parameter GRES_WIDTH = 10000;
    parameter GRES_START = 10000;

//--------   STARTUP Globals --------------
    wire GSR;
    wire GTS;
    wire GWE;
    wire PRLD;
    wire GRESTORE;
    tri1 p_up_tmp;
    tri (weak1, strong0) PLL_LOCKG = p_up_tmp;

    wire PROGB_GLBL;
    wire CCLKO_GLBL;
    wire FCSBO_GLBL;
    wire [3:0] DO_GLBL;
    wire [3:0] DI_GLBL;
   
    reg GSR_int;
    reg GTS_int;
    reg PRLD_int;
    reg GRESTORE_int;

//--------   JTAG Globals --------------
    wire JTAG_TDO_GLBL;
    wire JTAG_TCK_GLBL;
    wire JTAG_TDI_GLBL;
    wire JTAG_TMS_GLBL;
    wire JTAG_TRST_GLBL;

    reg JTAG_CAPTURE_GLBL;
    reg JTAG_RESET_GLBL;
    reg JTAG_SHIFT_GLBL;
    reg JTAG_UPDATE_GLBL;
    reg JTAG_RUNTEST_GLBL;

    reg JTAG_SEL1_GLBL = 0;
    reg JTAG_SEL2_GLBL = 0 ;
    reg JTAG_SEL3_GLBL = 0;
    reg JTAG_SEL4_GLBL = 0;

    reg JTAG_USER_TDO1_GLBL = 1'bz;
    reg JTAG_USER_TDO2_GLBL = 1'bz;
    reg JTAG_USER_TDO3_GLBL = 1'bz;
    reg JTAG_USER_TDO4_GLBL = 1'bz;

    assign (strong1, weak0) GSR = GSR_int;
    assign (strong1, weak0) GTS = GTS_int;
    assign (weak1, weak0) PRLD = PRLD_int;
    assign (strong1, weak0) GRESTORE = GRESTORE_int;

    initial begin
	GSR_int = 1'b1;
	PRLD_int = 1'b1;
	#(ROC_WIDTH)
	GSR_int = 1'b0;
	PRLD_int = 1'b0;
    end

    initial begin
	GTS_int = 1'b1;
	#(TOC_WIDTH)
	GTS_int = 1'b0;
    end

    initial begin 
	GRESTORE_int = 1'b0;
	#(GRES_START);
	GRESTORE_int = 1'b1;
	#(GRES_WIDTH);
	GRESTORE_int = 1'b0;
    end

endmodule
`endif
