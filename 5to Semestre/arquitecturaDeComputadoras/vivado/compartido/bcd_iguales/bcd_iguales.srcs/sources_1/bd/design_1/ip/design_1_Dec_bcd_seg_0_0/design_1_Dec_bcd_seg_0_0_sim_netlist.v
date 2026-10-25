// Copyright 1986-2017 Xilinx, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2017.4.1 (win64) Build 2117270 Tue Jan 30 15:32:00 MST 2018
// Date        : Sat Oct 10 14:49:58 2026
// Host        : txinerlaptop running 64-bit major release  (build 9200)
// Command     : write_verilog -force -mode funcsim {c:/Users/janag/Documents/IEI/Arquitectura de
//               Computadoras/Proy_23400357/bcd_iguales/bcd_iguales.srcs/sources_1/bd/design_1/ip/design_1_Dec_bcd_seg_0_0/design_1_Dec_bcd_seg_0_0_sim_netlist.v}
// Design      : design_1_Dec_bcd_seg_0_0
// Purpose     : This verilog netlist is a functional simulation representation of the design and should not be modified
//               or synthesized. This netlist cannot be used for SDF annotated simulation.
// Device      : xc7a100tcsg324-1
// --------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

(* CHECK_LICENSE_TYPE = "design_1_Dec_bcd_seg_0_0,Dec_bcd_seg,{}" *) (* downgradeipidentifiedwarnings = "yes" *) (* x_core_info = "Dec_bcd_seg,Vivado 2017.4.1" *) 
(* NotValidForBitStream *)
module design_1_Dec_bcd_seg_0_0
   (num,
    display,
    an,
    seg);
  input [3:0]num;
  input [7:0]display;
  output [7:0]an;
  output [7:0]seg;

  wire \<const1> ;
  wire [7:0]display;
  wire [3:0]num;
  wire [7:1]\^seg ;

  assign an[7:0] = display;
  assign seg[7:1] = \^seg [7:1];
  assign seg[0] = \<const1> ;
  VCC VCC
       (.P(\<const1> ));
  LUT4 #(
    .INIT(16'h4025)) 
    \seg[1]_INST_0 
       (.I0(num[3]),
        .I1(num[0]),
        .I2(num[2]),
        .I3(num[1]),
        .O(\^seg [1]));
  LUT4 #(
    .INIT(16'h5190)) 
    \seg[2]_INST_0 
       (.I0(num[3]),
        .I1(num[2]),
        .I2(num[0]),
        .I3(num[1]),
        .O(\^seg [2]));
  LUT4 #(
    .INIT(16'h5710)) 
    \seg[3]_INST_0 
       (.I0(num[3]),
        .I1(num[1]),
        .I2(num[2]),
        .I3(num[0]),
        .O(\^seg [3]));
  LUT4 #(
    .INIT(16'hC214)) 
    \seg[4]_INST_0 
       (.I0(num[3]),
        .I1(num[2]),
        .I2(num[0]),
        .I3(num[1]),
        .O(\^seg [4]));
  LUT4 #(
    .INIT(16'hA210)) 
    \seg[5]_INST_0 
       (.I0(num[3]),
        .I1(num[0]),
        .I2(num[1]),
        .I3(num[2]),
        .O(\^seg [5]));
  LUT4 #(
    .INIT(16'hAC48)) 
    \seg[6]_INST_0 
       (.I0(num[3]),
        .I1(num[2]),
        .I2(num[0]),
        .I3(num[1]),
        .O(\^seg [6]));
  LUT4 #(
    .INIT(16'h2094)) 
    \seg[7]_INST_0 
       (.I0(num[3]),
        .I1(num[2]),
        .I2(num[0]),
        .I3(num[1]),
        .O(\^seg [7]));
endmodule
`ifndef GLBL
`define GLBL
`timescale  1 ps / 1 ps

module glbl ();

    parameter ROC_WIDTH = 100000;
    parameter TOC_WIDTH = 0;

//--------   STARTUP Globals --------------
    wire GSR;
    wire GTS;
    wire GWE;
    wire PRLD;
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

endmodule
`endif
