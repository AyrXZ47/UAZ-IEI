// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
// Date        : Sat Nov 21 18:12:42 2026
// Host        : nixos-laptop running 64-bit unknown
// Command     : write_verilog -force -mode funcsim
//               /tmp/opencode/harvard_fix/Harvard/Harvard.gen/sources_1/bd/harvard_design/ip/harvard_design_mux_datos_0_0/harvard_design_mux_datos_0_0_sim_netlist.v
// Design      : harvard_design_mux_datos_0_0
// Purpose     : This verilog netlist is a functional simulation representation of the design and should not be modified
//               or synthesized. This netlist cannot be used for SDF annotated simulation.
// Device      : xc7a35tcpg236-1
// --------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

(* CHECK_LICENSE_TYPE = "harvard_design_mux_datos_0_0,mux_datos,{}" *) (* DowngradeIPIdentifiedWarnings = "yes" *) (* IP_DEFINITION_SOURCE = "module_ref" *) 
(* X_CORE_INFO = "mux_datos,Vivado 2026.1" *) 
(* NotValidForBitStream *)
module harvard_design_mux_datos_0_0
   (A,
    B,
    dir,
    datoRam,
    sel,
    sal);
  input [3:0]A;
  input [3:0]B;
  input [3:0]dir;
  input [3:0]datoRam;
  input [1:0]sel;
  output [3:0]sal;

  wire [3:0]A;
  wire [3:0]B;
  wire [3:0]datoRam;
  wire [3:0]dir;
  wire [3:0]sal;
  wire [1:0]sel;

  harvard_design_mux_datos_0_0_mux_datos inst
       (.A(A),
        .B(B),
        .datoRam(datoRam),
        .dir(dir),
        .sal(sal),
        .sel(sel));
endmodule

(* ORIG_REF_NAME = "mux_datos" *) 
module harvard_design_mux_datos_0_0_mux_datos
   (sal,
    B,
    A,
    datoRam,
    sel,
    dir);
  output [3:0]sal;
  input [3:0]B;
  input [3:0]A;
  input [3:0]datoRam;
  input [1:0]sel;
  input [3:0]dir;

  wire [3:0]A;
  wire [3:0]B;
  wire [3:0]datoRam;
  wire [3:0]dir;
  wire [3:0]sal;
  wire [1:0]sel;

  LUT6 #(
    .INIT(64'hF0AAFFCCF0AA00CC)) 
    \sal[0]_INST_0 
       (.I0(B[0]),
        .I1(A[0]),
        .I2(datoRam[0]),
        .I3(sel[1]),
        .I4(sel[0]),
        .I5(dir[0]),
        .O(sal[0]));
  LUT6 #(
    .INIT(64'hF0AAFFCCF0AA00CC)) 
    \sal[1]_INST_0 
       (.I0(B[1]),
        .I1(A[1]),
        .I2(datoRam[1]),
        .I3(sel[1]),
        .I4(sel[0]),
        .I5(dir[1]),
        .O(sal[1]));
  LUT6 #(
    .INIT(64'hF0AAFFCCF0AA00CC)) 
    \sal[2]_INST_0 
       (.I0(B[2]),
        .I1(A[2]),
        .I2(datoRam[2]),
        .I3(sel[1]),
        .I4(sel[0]),
        .I5(dir[2]),
        .O(sal[2]));
  LUT6 #(
    .INIT(64'hF0AAFFCCF0AA00CC)) 
    \sal[3]_INST_0 
       (.I0(B[3]),
        .I1(A[3]),
        .I2(datoRam[3]),
        .I3(sel[1]),
        .I4(sel[0]),
        .I5(dir[3]),
        .O(sal[3]));
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
