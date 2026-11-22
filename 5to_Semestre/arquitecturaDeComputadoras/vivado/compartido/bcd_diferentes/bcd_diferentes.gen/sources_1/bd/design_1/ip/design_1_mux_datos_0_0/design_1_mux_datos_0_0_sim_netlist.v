// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
// Date        : Sat Oct 24 17:45:26 2026
// Host        : nixos-laptop running 64-bit unknown
// Command     : write_verilog -force -mode funcsim {/home/yovick/repos/UAZ-IEI/5to
//               Semestre/arquitecturaDeComputadoras/vivado/compartido/bcd_diferentes/bcd_diferentes.gen/sources_1/bd/design_1/ip/design_1_mux_datos_0_0/design_1_mux_datos_0_0_sim_netlist.v}
// Design      : design_1_mux_datos_0_0
// Purpose     : This verilog netlist is a functional simulation representation of the design and should not be modified
//               or synthesized. This netlist cannot be used for SDF annotated simulation.
// Device      : xc7a100tcsg324-1
// --------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

(* CHECK_LICENSE_TYPE = "design_1_mux_datos_0_0,mux_datos,{}" *) (* downgradeipidentifiedwarnings = "yes" *) (* ip_definition_source = "module_ref" *) 
(* x_core_info = "mux_datos,Vivado 2026.1" *) 
(* NotValidForBitStream *)
module design_1_mux_datos_0_0
   (sw,
    sel,
    sal);
  input [15:0]sw;
  input [2:0]sel;
  output [3:0]sal;

  wire [3:0]sal;
  wire [2:0]sel;
  wire [15:0]sw;

  design_1_mux_datos_0_0_mux_datos U0
       (.sal(sal),
        .sel(sel),
        .sw(sw));
endmodule

(* ORIG_REF_NAME = "mux_datos" *) 
module design_1_mux_datos_0_0_mux_datos
   (sal,
    sel,
    sw);
  output [3:0]sal;
  input [2:0]sel;
  input [15:0]sw;

  wire [3:0]sal;
  wire \sal[0]_INST_0_i_1_n_0 ;
  wire \sal[0]_INST_0_i_2_n_0 ;
  wire \sal[1]_INST_0_i_1_n_0 ;
  wire \sal[1]_INST_0_i_2_n_0 ;
  wire \sal[2]_INST_0_i_1_n_0 ;
  wire \sal[2]_INST_0_i_2_n_0 ;
  wire \sal[3]_INST_0_i_1_n_0 ;
  wire \sal[3]_INST_0_i_2_n_0 ;
  wire [2:0]sel;
  wire [15:0]sw;

  MUXF7 \sal[0]_INST_0 
       (.I0(\sal[0]_INST_0_i_1_n_0 ),
        .I1(\sal[0]_INST_0_i_2_n_0 ),
        .O(sal[0]),
        .S(sel[2]));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \sal[0]_INST_0_i_1 
       (.I0(sw[12]),
        .I1(sw[8]),
        .I2(sel[1]),
        .I3(sw[4]),
        .I4(sel[0]),
        .I5(sw[0]),
        .O(\sal[0]_INST_0_i_1_n_0 ));
  LUT5 #(
    .INIT(32'hFCBB3088)) 
    \sal[0]_INST_0_i_2 
       (.I0(sw[8]),
        .I1(sel[1]),
        .I2(sw[4]),
        .I3(sel[0]),
        .I4(sw[0]),
        .O(\sal[0]_INST_0_i_2_n_0 ));
  MUXF7 \sal[1]_INST_0 
       (.I0(\sal[1]_INST_0_i_1_n_0 ),
        .I1(\sal[1]_INST_0_i_2_n_0 ),
        .O(sal[1]),
        .S(sel[2]));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \sal[1]_INST_0_i_1 
       (.I0(sw[13]),
        .I1(sw[9]),
        .I2(sel[1]),
        .I3(sw[5]),
        .I4(sel[0]),
        .I5(sw[1]),
        .O(\sal[1]_INST_0_i_1_n_0 ));
  LUT5 #(
    .INIT(32'hFCBB3088)) 
    \sal[1]_INST_0_i_2 
       (.I0(sw[9]),
        .I1(sel[1]),
        .I2(sw[5]),
        .I3(sel[0]),
        .I4(sw[1]),
        .O(\sal[1]_INST_0_i_2_n_0 ));
  MUXF7 \sal[2]_INST_0 
       (.I0(\sal[2]_INST_0_i_1_n_0 ),
        .I1(\sal[2]_INST_0_i_2_n_0 ),
        .O(sal[2]),
        .S(sel[2]));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \sal[2]_INST_0_i_1 
       (.I0(sw[14]),
        .I1(sw[10]),
        .I2(sel[1]),
        .I3(sw[6]),
        .I4(sel[0]),
        .I5(sw[2]),
        .O(\sal[2]_INST_0_i_1_n_0 ));
  LUT5 #(
    .INIT(32'hFCBB3088)) 
    \sal[2]_INST_0_i_2 
       (.I0(sw[10]),
        .I1(sel[1]),
        .I2(sw[6]),
        .I3(sel[0]),
        .I4(sw[2]),
        .O(\sal[2]_INST_0_i_2_n_0 ));
  MUXF7 \sal[3]_INST_0 
       (.I0(\sal[3]_INST_0_i_1_n_0 ),
        .I1(\sal[3]_INST_0_i_2_n_0 ),
        .O(sal[3]),
        .S(sel[2]));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \sal[3]_INST_0_i_1 
       (.I0(sw[15]),
        .I1(sw[11]),
        .I2(sel[1]),
        .I3(sw[7]),
        .I4(sel[0]),
        .I5(sw[3]),
        .O(\sal[3]_INST_0_i_1_n_0 ));
  LUT5 #(
    .INIT(32'hFCBB3088)) 
    \sal[3]_INST_0_i_2 
       (.I0(sw[11]),
        .I1(sel[1]),
        .I2(sw[7]),
        .I3(sel[0]),
        .I4(sw[3]),
        .O(\sal[3]_INST_0_i_2_n_0 ));
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
