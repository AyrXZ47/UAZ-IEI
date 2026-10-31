// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
// Date        : Fri Oct 30 21:50:18 2026
// Host        : nixos-pc running 64-bit unknown
// Command     : write_verilog -force -mode funcsim {/home/yovick/repos/UAZ-IEI/5to
//               Semestre/arquitecturaDeComputadoras/vivado/compartido/mensajes/mensajes.gen/sources_1/bd/design_1/ip/design_1_dec_an_0_0/design_1_dec_an_0_0_sim_netlist.v}
// Design      : design_1_dec_an_0_0
// Purpose     : This verilog netlist is a functional simulation representation of the design and should not be modified
//               or synthesized. This netlist cannot be used for SDF annotated simulation.
// Device      : xc7a100tcsg324-1
// --------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

(* CHECK_LICENSE_TYPE = "design_1_dec_an_0_0,dec_an,{}" *) (* downgradeipidentifiedwarnings = "yes" *) (* ip_definition_source = "module_ref" *) 
(* x_core_info = "dec_an,Vivado 2026.1" *) 
(* NotValidForBitStream *)
module design_1_dec_an_0_0
   (ent,
    sal);
  input [2:0]ent;
  output [7:0]sal;

  wire [2:0]ent;
  wire [7:0]sal;

  design_1_dec_an_0_0_dec_an U0
       (.ent(ent),
        .sal(sal));
endmodule

(* ORIG_REF_NAME = "dec_an" *) 
module design_1_dec_an_0_0_dec_an
   (sal,
    ent);
  output [7:0]sal;
  input [2:0]ent;

  wire [2:0]ent;
  wire [7:0]sal;

  (* SOFT_HLUTNM = "soft_lutpair0" *) 
  LUT3 #(
    .INIT(8'hFE)) 
    \sal[0]_INST_0 
       (.I0(ent[1]),
        .I1(ent[2]),
        .I2(ent[0]),
        .O(sal[0]));
  (* SOFT_HLUTNM = "soft_lutpair0" *) 
  LUT3 #(
    .INIT(8'hEF)) 
    \sal[1]_INST_0 
       (.I0(ent[1]),
        .I1(ent[2]),
        .I2(ent[0]),
        .O(sal[1]));
  (* SOFT_HLUTNM = "soft_lutpair1" *) 
  LUT3 #(
    .INIT(8'hEF)) 
    \sal[2]_INST_0 
       (.I0(ent[2]),
        .I1(ent[0]),
        .I2(ent[1]),
        .O(sal[2]));
  (* SOFT_HLUTNM = "soft_lutpair1" *) 
  LUT3 #(
    .INIT(8'hF7)) 
    \sal[3]_INST_0 
       (.I0(ent[1]),
        .I1(ent[0]),
        .I2(ent[2]),
        .O(sal[3]));
  (* SOFT_HLUTNM = "soft_lutpair2" *) 
  LUT3 #(
    .INIT(8'hEF)) 
    \sal[4]_INST_0 
       (.I0(ent[1]),
        .I1(ent[0]),
        .I2(ent[2]),
        .O(sal[4]));
  (* SOFT_HLUTNM = "soft_lutpair2" *) 
  LUT3 #(
    .INIT(8'hF7)) 
    \sal[5]_INST_0 
       (.I0(ent[2]),
        .I1(ent[0]),
        .I2(ent[1]),
        .O(sal[5]));
  (* SOFT_HLUTNM = "soft_lutpair3" *) 
  LUT3 #(
    .INIT(8'hF7)) 
    \sal[6]_INST_0 
       (.I0(ent[1]),
        .I1(ent[2]),
        .I2(ent[0]),
        .O(sal[6]));
  (* SOFT_HLUTNM = "soft_lutpair3" *) 
  LUT3 #(
    .INIT(8'h7F)) 
    \sal[7]_INST_0 
       (.I0(ent[2]),
        .I1(ent[0]),
        .I2(ent[1]),
        .O(sal[7]));
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
