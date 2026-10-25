// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
// Date        : Sat Oct 24 17:45:26 2026
// Host        : nixos-laptop running 64-bit unknown
// Command     : write_verilog -force -mode funcsim {/home/yovick/repos/UAZ-IEI/5to
//               Semestre/arquitecturaDeComputadoras/vivado/compartido/bcd_diferentes/bcd_diferentes.gen/sources_1/bd/design_1/ip/design_1_pres_500hz_0_0/design_1_pres_500hz_0_0_sim_netlist.v}
// Design      : design_1_pres_500hz_0_0
// Purpose     : This verilog netlist is a functional simulation representation of the design and should not be modified
//               or synthesized. This netlist cannot be used for SDF annotated simulation.
// Device      : xc7a100tcsg324-1
// --------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

(* CHECK_LICENSE_TYPE = "design_1_pres_500hz_0_0,pres_500hz,{}" *) (* downgradeipidentifiedwarnings = "yes" *) (* ip_definition_source = "module_ref" *) 
(* x_core_info = "pres_500hz,Vivado 2026.1" *) 
(* NotValidForBitStream *)
module design_1_pres_500hz_0_0
   (clk,
    rst,
    clk_pres);
  (* x_interface_info = "xilinx.com:signal:clock:1.0 clk CLK" *) (* x_interface_mode = "slave clk" *) (* x_interface_parameter = "XIL_INTERFACENAME clk, ASSOCIATED_RESET rst, FREQ_HZ 100000000, FREQ_TOLERANCE_HZ 0, PHASE 0.0, CLK_DOMAIN design_1_clk_0, INSERT_VIP 0" *) input clk;
  (* x_interface_info = "xilinx.com:signal:reset:1.0 rst RST" *) (* x_interface_mode = "slave rst" *) (* x_interface_parameter = "XIL_INTERFACENAME rst, POLARITY ACTIVE_LOW, INSERT_VIP 0" *) input rst;
  output clk_pres;

  wire clk;
  wire clk_pres;
  wire rst;

  design_1_pres_500hz_0_0_pres_500hz U0
       (.clk(clk),
        .clk_pres(clk_pres),
        .rst(rst));
endmodule

(* ORIG_REF_NAME = "pres_500hz" *) 
module design_1_pres_500hz_0_0_pres_500hz
   (clk_pres,
    clk,
    rst);
  output clk_pres;
  input clk;
  input rst;

  wire clk;
  wire clk_pres;
  wire clk_pres_0;
  wire clk_pres_i_2_n_0;
  wire clk_pres_i_3_n_0;
  wire clk_pres_i_4_n_0;
  wire clk_pres_i_5_n_0;
  wire [14:0]cont;
  wire [14:0]cont_1;
  wire \cont_reg[12]_i_2_n_0 ;
  wire \cont_reg[12]_i_2_n_1 ;
  wire \cont_reg[12]_i_2_n_2 ;
  wire \cont_reg[12]_i_2_n_3 ;
  wire \cont_reg[14]_i_2_n_3 ;
  wire \cont_reg[4]_i_2_n_0 ;
  wire \cont_reg[4]_i_2_n_1 ;
  wire \cont_reg[4]_i_2_n_2 ;
  wire \cont_reg[4]_i_2_n_3 ;
  wire \cont_reg[8]_i_2_n_0 ;
  wire \cont_reg[8]_i_2_n_1 ;
  wire \cont_reg[8]_i_2_n_2 ;
  wire \cont_reg[8]_i_2_n_3 ;
  wire [14:1]data0;
  wire rst;
  wire [3:1]\NLW_cont_reg[14]_i_2_CO_UNCONNECTED ;
  wire [3:2]\NLW_cont_reg[14]_i_2_O_UNCONNECTED ;

  (* SOFT_HLUTNM = "soft_lutpair0" *) 
  LUT1 #(
    .INIT(2'h1)) 
    clk_pres_i_1
       (.I0(clk_pres_i_2_n_0),
        .O(clk_pres_0));
  LUT6 #(
    .INIT(64'hFFFFFFFFEFFFFFFF)) 
    clk_pres_i_2
       (.I0(clk_pres_i_3_n_0),
        .I1(clk_pres_i_4_n_0),
        .I2(cont[14]),
        .I3(cont[13]),
        .I4(cont[0]),
        .I5(clk_pres_i_5_n_0),
        .O(clk_pres_i_2_n_0));
  LUT4 #(
    .INIT(16'hDFFF)) 
    clk_pres_i_3
       (.I0(cont[5]),
        .I1(cont[6]),
        .I2(cont[8]),
        .I3(cont[7]),
        .O(clk_pres_i_3_n_0));
  LUT4 #(
    .INIT(16'hFFF7)) 
    clk_pres_i_4
       (.I0(cont[2]),
        .I1(cont[1]),
        .I2(cont[4]),
        .I3(cont[3]),
        .O(clk_pres_i_4_n_0));
  LUT4 #(
    .INIT(16'hFFFE)) 
    clk_pres_i_5
       (.I0(cont[10]),
        .I1(cont[9]),
        .I2(cont[12]),
        .I3(cont[11]),
        .O(clk_pres_i_5_n_0));
  FDCE clk_pres_reg
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(clk_pres_0),
        .Q(clk_pres));
  LUT1 #(
    .INIT(2'h1)) 
    \cont[0]_i_1 
       (.I0(cont[0]),
        .O(cont_1[0]));
  (* SOFT_HLUTNM = "soft_lutpair5" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \cont[10]_i_1 
       (.I0(clk_pres_i_2_n_0),
        .I1(data0[10]),
        .O(cont_1[10]));
  (* SOFT_HLUTNM = "soft_lutpair5" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \cont[11]_i_1 
       (.I0(clk_pres_i_2_n_0),
        .I1(data0[11]),
        .O(cont_1[11]));
  (* SOFT_HLUTNM = "soft_lutpair6" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \cont[12]_i_1 
       (.I0(clk_pres_i_2_n_0),
        .I1(data0[12]),
        .O(cont_1[12]));
  (* SOFT_HLUTNM = "soft_lutpair6" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \cont[13]_i_1 
       (.I0(clk_pres_i_2_n_0),
        .I1(data0[13]),
        .O(cont_1[13]));
  LUT2 #(
    .INIT(4'h8)) 
    \cont[14]_i_1 
       (.I0(clk_pres_i_2_n_0),
        .I1(data0[14]),
        .O(cont_1[14]));
  (* SOFT_HLUTNM = "soft_lutpair0" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \cont[1]_i_1 
       (.I0(clk_pres_i_2_n_0),
        .I1(data0[1]),
        .O(cont_1[1]));
  (* SOFT_HLUTNM = "soft_lutpair1" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \cont[2]_i_1 
       (.I0(clk_pres_i_2_n_0),
        .I1(data0[2]),
        .O(cont_1[2]));
  (* SOFT_HLUTNM = "soft_lutpair1" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \cont[3]_i_1 
       (.I0(clk_pres_i_2_n_0),
        .I1(data0[3]),
        .O(cont_1[3]));
  (* SOFT_HLUTNM = "soft_lutpair2" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \cont[4]_i_1 
       (.I0(clk_pres_i_2_n_0),
        .I1(data0[4]),
        .O(cont_1[4]));
  (* SOFT_HLUTNM = "soft_lutpair2" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \cont[5]_i_1 
       (.I0(clk_pres_i_2_n_0),
        .I1(data0[5]),
        .O(cont_1[5]));
  (* SOFT_HLUTNM = "soft_lutpair3" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \cont[6]_i_1 
       (.I0(clk_pres_i_2_n_0),
        .I1(data0[6]),
        .O(cont_1[6]));
  (* SOFT_HLUTNM = "soft_lutpair3" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \cont[7]_i_1 
       (.I0(clk_pres_i_2_n_0),
        .I1(data0[7]),
        .O(cont_1[7]));
  (* SOFT_HLUTNM = "soft_lutpair4" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \cont[8]_i_1 
       (.I0(clk_pres_i_2_n_0),
        .I1(data0[8]),
        .O(cont_1[8]));
  (* SOFT_HLUTNM = "soft_lutpair4" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \cont[9]_i_1 
       (.I0(clk_pres_i_2_n_0),
        .I1(data0[9]),
        .O(cont_1[9]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[0] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(cont_1[0]),
        .Q(cont[0]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[10] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(cont_1[10]),
        .Q(cont[10]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[11] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(cont_1[11]),
        .Q(cont[11]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[12] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(cont_1[12]),
        .Q(cont[12]));
  (* ADDER_THRESHOLD = "35" *) 
  CARRY4 \cont_reg[12]_i_2 
       (.CI(\cont_reg[8]_i_2_n_0 ),
        .CO({\cont_reg[12]_i_2_n_0 ,\cont_reg[12]_i_2_n_1 ,\cont_reg[12]_i_2_n_2 ,\cont_reg[12]_i_2_n_3 }),
        .CYINIT(1'b0),
        .DI({1'b0,1'b0,1'b0,1'b0}),
        .O(data0[12:9]),
        .S(cont[12:9]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[13] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(cont_1[13]),
        .Q(cont[13]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[14] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(cont_1[14]),
        .Q(cont[14]));
  (* ADDER_THRESHOLD = "35" *) 
  CARRY4 \cont_reg[14]_i_2 
       (.CI(\cont_reg[12]_i_2_n_0 ),
        .CO({\NLW_cont_reg[14]_i_2_CO_UNCONNECTED [3:1],\cont_reg[14]_i_2_n_3 }),
        .CYINIT(1'b0),
        .DI({1'b0,1'b0,1'b0,1'b0}),
        .O({\NLW_cont_reg[14]_i_2_O_UNCONNECTED [3:2],data0[14:13]}),
        .S({1'b0,1'b0,cont[14:13]}));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[1] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(cont_1[1]),
        .Q(cont[1]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[2] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(cont_1[2]),
        .Q(cont[2]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[3] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(cont_1[3]),
        .Q(cont[3]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[4] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(cont_1[4]),
        .Q(cont[4]));
  (* ADDER_THRESHOLD = "35" *) 
  CARRY4 \cont_reg[4]_i_2 
       (.CI(1'b0),
        .CO({\cont_reg[4]_i_2_n_0 ,\cont_reg[4]_i_2_n_1 ,\cont_reg[4]_i_2_n_2 ,\cont_reg[4]_i_2_n_3 }),
        .CYINIT(cont[0]),
        .DI({1'b0,1'b0,1'b0,1'b0}),
        .O(data0[4:1]),
        .S(cont[4:1]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[5] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(cont_1[5]),
        .Q(cont[5]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[6] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(cont_1[6]),
        .Q(cont[6]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[7] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(cont_1[7]),
        .Q(cont[7]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[8] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(cont_1[8]),
        .Q(cont[8]));
  (* ADDER_THRESHOLD = "35" *) 
  CARRY4 \cont_reg[8]_i_2 
       (.CI(\cont_reg[4]_i_2_n_0 ),
        .CO({\cont_reg[8]_i_2_n_0 ,\cont_reg[8]_i_2_n_1 ,\cont_reg[8]_i_2_n_2 ,\cont_reg[8]_i_2_n_3 }),
        .CYINIT(1'b0),
        .DI({1'b0,1'b0,1'b0,1'b0}),
        .O(data0[8:5]),
        .S(cont[8:5]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[9] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(cont_1[9]),
        .Q(cont[9]));
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
