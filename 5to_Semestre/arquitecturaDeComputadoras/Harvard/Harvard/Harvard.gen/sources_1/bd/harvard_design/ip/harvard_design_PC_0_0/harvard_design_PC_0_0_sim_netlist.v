// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
// Date        : Sat Nov 21 18:12:06 2026
// Host        : nixos-laptop running 64-bit unknown
// Command     : write_verilog -force -mode funcsim
//               /tmp/opencode/harvard_fix/Harvard/Harvard.gen/sources_1/bd/harvard_design/ip/harvard_design_PC_0_0/harvard_design_PC_0_0_sim_netlist.v
// Design      : harvard_design_PC_0_0
// Purpose     : This verilog netlist is a functional simulation representation of the design and should not be modified
//               or synthesized. This netlist cannot be used for SDF annotated simulation.
// Device      : xc7a35tcpg236-1
// --------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

(* CHECK_LICENSE_TYPE = "harvard_design_PC_0_0,PC,{}" *) (* DowngradeIPIdentifiedWarnings = "yes" *) (* IP_DEFINITION_SOURCE = "module_ref" *) 
(* X_CORE_INFO = "PC,Vivado 2026.1" *) 
(* NotValidForBitStream *)
module harvard_design_PC_0_0
   (clk,
    rst,
    incremento,
    Dir);
  (* X_INTERFACE_INFO = "xilinx.com:signal:clock:1.0 clk CLK" *) (* X_INTERFACE_MODE = "slave" *) (* X_INTERFACE_PARAMETER = "XIL_INTERFACENAME clk, ASSOCIATED_RESET rst, FREQ_HZ 100000000, FREQ_TOLERANCE_HZ 0, PHASE 0.0, CLK_DOMAIN harvard_design_clk, INSERT_VIP 0" *) input clk;
  (* X_INTERFACE_INFO = "xilinx.com:signal:reset:1.0 rst RST" *) (* X_INTERFACE_MODE = "slave" *) (* X_INTERFACE_PARAMETER = "XIL_INTERFACENAME rst, POLARITY ACTIVE_LOW, INSERT_VIP 0" *) input rst;
  input incremento;
  output [3:0]Dir;

  wire [3:0]Dir;
  wire clk;
  wire incremento;
  wire rst;

  harvard_design_PC_0_0_PC inst
       (.Dir(Dir),
        .clk(clk),
        .incremento(incremento),
        .rst(rst));
endmodule

(* ORIG_REF_NAME = "PC" *) 
module harvard_design_PC_0_0_PC
   (Dir,
    incremento,
    clk,
    rst);
  output [3:0]Dir;
  input incremento;
  input clk;
  input rst;

  wire [3:0]Dir;
  wire clk;
  wire incremento;
  wire [3:0]plusOp;
  wire rst;

  (* SOFT_HLUTNM = "soft_lutpair1" *) 
  LUT1 #(
    .INIT(2'h1)) 
    \cont[0]_i_1 
       (.I0(Dir[0]),
        .O(plusOp[0]));
  (* SOFT_HLUTNM = "soft_lutpair1" *) 
  LUT2 #(
    .INIT(4'h6)) 
    \cont[1]_i_1 
       (.I0(Dir[0]),
        .I1(Dir[1]),
        .O(plusOp[1]));
  (* SOFT_HLUTNM = "soft_lutpair0" *) 
  LUT3 #(
    .INIT(8'h78)) 
    \cont[2]_i_1 
       (.I0(Dir[0]),
        .I1(Dir[1]),
        .I2(Dir[2]),
        .O(plusOp[2]));
  (* SOFT_HLUTNM = "soft_lutpair0" *) 
  LUT4 #(
    .INIT(16'h7F80)) 
    \cont[3]_i_1 
       (.I0(Dir[1]),
        .I1(Dir[0]),
        .I2(Dir[2]),
        .I3(Dir[3]),
        .O(plusOp[3]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[0] 
       (.C(clk),
        .CE(incremento),
        .CLR(rst),
        .D(plusOp[0]),
        .Q(Dir[0]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[1] 
       (.C(clk),
        .CE(incremento),
        .CLR(rst),
        .D(plusOp[1]),
        .Q(Dir[1]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[2] 
       (.C(clk),
        .CE(incremento),
        .CLR(rst),
        .D(plusOp[2]),
        .Q(Dir[2]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[3] 
       (.C(clk),
        .CE(incremento),
        .CLR(rst),
        .D(plusOp[3]),
        .Q(Dir[3]));
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
