// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
// Date        : Sat Nov 21 18:12:07 2026
// Host        : nixos-laptop running 64-bit unknown
// Command     : write_verilog -force -mode funcsim
//               /tmp/opencode/harvard_fix/Harvard/Harvard.gen/sources_1/bd/harvard_design/ip/harvard_design_UAL_0_0/harvard_design_UAL_0_0_sim_netlist.v
// Design      : harvard_design_UAL_0_0
// Purpose     : This verilog netlist is a functional simulation representation of the design and should not be modified
//               or synthesized. This netlist cannot be used for SDF annotated simulation.
// Device      : xc7a35tcpg236-1
// --------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

(* CHECK_LICENSE_TYPE = "harvard_design_UAL_0_0,UAL,{}" *) (* DowngradeIPIdentifiedWarnings = "yes" *) (* IP_DEFINITION_SOURCE = "module_ref" *) 
(* X_CORE_INFO = "UAL,Vivado 2026.1" *) 
(* NotValidForBitStream *)
module harvard_design_UAL_0_0
   (A,
    B,
    op,
    res,
    acarreo,
    cero);
  input [3:0]A;
  input [3:0]B;
  input [2:0]op;
  output [3:0]res;
  output acarreo;
  output cero;

  wire [3:0]A;
  wire [3:0]B;
  wire acarreo;
  wire acarreo_INST_0_i_1_n_0;
  wire acarreo_INST_0_i_2_n_0;
  wire cero;
  wire cero_INST_0_i_1_n_0;
  wire [2:0]op;
  wire [3:0]res;
  wire \res[1]_INST_0_i_1_n_0 ;
  wire \res[1]_INST_0_i_2_n_0 ;
  wire \res[2]_INST_0_i_1_n_0 ;
  wire \res[2]_INST_0_i_2_n_0 ;
  wire \res[2]_INST_0_i_3_n_0 ;
  wire \res[2]_INST_0_i_4_n_0 ;
  wire \res[3]_INST_0_i_1_n_0 ;
  wire \res[3]_INST_0_i_2_n_0 ;
  wire \res[3]_INST_0_i_3_n_0 ;
  wire \res[3]_INST_0_i_4_n_0 ;
  wire \res[3]_INST_0_i_5_n_0 ;

  MUXF7 acarreo_INST_0
       (.I0(acarreo_INST_0_i_1_n_0),
        .I1(acarreo_INST_0_i_2_n_0),
        .O(acarreo),
        .S(op[2]));
  LUT6 #(
    .INIT(64'h000000000CE8CFE8)) 
    acarreo_INST_0_i_1
       (.I0(\res[3]_INST_0_i_4_n_0 ),
        .I1(B[3]),
        .I2(A[3]),
        .I3(op[0]),
        .I4(\res[3]_INST_0_i_3_n_0 ),
        .I5(op[1]),
        .O(acarreo_INST_0_i_1_n_0));
  LUT6 #(
    .INIT(64'h0001FFFF80000000)) 
    acarreo_INST_0_i_2
       (.I0(A[3]),
        .I1(A[1]),
        .I2(A[0]),
        .I3(A[2]),
        .I4(op[1]),
        .I5(op[0]),
        .O(acarreo_INST_0_i_2_n_0));
  LUT6 #(
    .INIT(64'h0000000000440347)) 
    cero_INST_0
       (.I0(\res[2]_INST_0_i_2_n_0 ),
        .I1(op[2]),
        .I2(\res[2]_INST_0_i_1_n_0 ),
        .I3(\res[3]_INST_0_i_2_n_0 ),
        .I4(\res[3]_INST_0_i_1_n_0 ),
        .I5(cero_INST_0_i_1_n_0),
        .O(cero));
  LUT4 #(
    .INIT(16'hFEAE)) 
    cero_INST_0_i_1
       (.I0(res[0]),
        .I1(\res[1]_INST_0_i_1_n_0 ),
        .I2(op[2]),
        .I3(\res[1]_INST_0_i_2_n_0 ),
        .O(cero_INST_0_i_1_n_0));
  LUT5 #(
    .INIT(32'h50EF47A8)) 
    \res[0]_INST_0 
       (.I0(op[2]),
        .I1(op[0]),
        .I2(op[1]),
        .I3(A[0]),
        .I4(B[0]),
        .O(res[0]));
  MUXF7 \res[1]_INST_0 
       (.I0(\res[1]_INST_0_i_1_n_0 ),
        .I1(\res[1]_INST_0_i_2_n_0 ),
        .O(res[1]),
        .S(op[2]));
  LUT6 #(
    .INIT(64'hBEAAC9DDC9DD1400)) 
    \res[1]_INST_0_i_1 
       (.I0(op[1]),
        .I1(op[0]),
        .I2(A[0]),
        .I3(B[0]),
        .I4(B[1]),
        .I5(A[1]),
        .O(\res[1]_INST_0_i_1_n_0 ));
  LUT5 #(
    .INIT(32'h84877B78)) 
    \res[1]_INST_0_i_2 
       (.I0(A[0]),
        .I1(op[1]),
        .I2(op[0]),
        .I3(B[1]),
        .I4(A[1]),
        .O(\res[1]_INST_0_i_2_n_0 ));
  MUXF7 \res[2]_INST_0 
       (.I0(\res[2]_INST_0_i_1_n_0 ),
        .I1(\res[2]_INST_0_i_2_n_0 ),
        .O(res[2]),
        .S(op[2]));
  LUT6 #(
    .INIT(64'hBFBAE0E5E0E51510)) 
    \res[2]_INST_0_i_1 
       (.I0(op[1]),
        .I1(\res[2]_INST_0_i_3_n_0 ),
        .I2(op[0]),
        .I3(\res[2]_INST_0_i_4_n_0 ),
        .I4(B[2]),
        .I5(A[2]),
        .O(\res[2]_INST_0_i_1_n_0 ));
  LUT6 #(
    .INIT(64'hE070E07F1F8F1F80)) 
    \res[2]_INST_0_i_2 
       (.I0(A[0]),
        .I1(A[1]),
        .I2(op[1]),
        .I3(op[0]),
        .I4(B[2]),
        .I5(A[2]),
        .O(\res[2]_INST_0_i_2_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair0" *) 
  LUT4 #(
    .INIT(16'hDD4D)) 
    \res[2]_INST_0_i_3 
       (.I0(B[1]),
        .I1(A[1]),
        .I2(B[0]),
        .I3(A[0]),
        .O(\res[2]_INST_0_i_3_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair0" *) 
  LUT4 #(
    .INIT(16'hE888)) 
    \res[2]_INST_0_i_4 
       (.I0(B[1]),
        .I1(A[1]),
        .I2(A[0]),
        .I3(B[0]),
        .O(\res[2]_INST_0_i_4_n_0 ));
  MUXF7 \res[3]_INST_0 
       (.I0(\res[3]_INST_0_i_1_n_0 ),
        .I1(\res[3]_INST_0_i_2_n_0 ),
        .O(res[3]),
        .S(op[2]));
  LUT6 #(
    .INIT(64'hBFBAE0E5E0E51510)) 
    \res[3]_INST_0_i_1 
       (.I0(op[1]),
        .I1(\res[3]_INST_0_i_3_n_0 ),
        .I2(op[0]),
        .I3(\res[3]_INST_0_i_4_n_0 ),
        .I4(B[3]),
        .I5(A[3]),
        .O(\res[3]_INST_0_i_1_n_0 ));
  LUT5 #(
    .INIT(32'h888BBBB8)) 
    \res[3]_INST_0_i_2 
       (.I0(\res[3]_INST_0_i_5_n_0 ),
        .I1(op[1]),
        .I2(op[0]),
        .I3(B[3]),
        .I4(A[3]),
        .O(\res[3]_INST_0_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hD4DD4444DDDDD4DD)) 
    \res[3]_INST_0_i_3 
       (.I0(B[2]),
        .I1(A[2]),
        .I2(A[0]),
        .I3(B[0]),
        .I4(A[1]),
        .I5(B[1]),
        .O(\res[3]_INST_0_i_3_n_0 ));
  LUT6 #(
    .INIT(64'hEEEEE888E8888888)) 
    \res[3]_INST_0_i_4 
       (.I0(B[2]),
        .I1(A[2]),
        .I2(B[0]),
        .I3(A[0]),
        .I4(A[1]),
        .I5(B[1]),
        .O(\res[3]_INST_0_i_4_n_0 ));
  LUT5 #(
    .INIT(32'hBFFD4002)) 
    \res[3]_INST_0_i_5 
       (.I0(op[0]),
        .I1(A[1]),
        .I2(A[0]),
        .I3(A[2]),
        .I4(A[3]),
        .O(\res[3]_INST_0_i_5_n_0 ));
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
