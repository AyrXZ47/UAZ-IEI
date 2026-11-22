// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
// Date        : Sat Nov 21 18:11:25 2026
// Host        : nixos-laptop running 64-bit unknown
// Command     : write_verilog -force -mode funcsim
//               /tmp/opencode/harvard_fix/Harvard/Harvard.gen/sources_1/bd/harvard_design/ip/harvard_design_M_RAM_0_0/harvard_design_M_RAM_0_0_sim_netlist.v
// Design      : harvard_design_M_RAM_0_0
// Purpose     : This verilog netlist is a functional simulation representation of the design and should not be modified
//               or synthesized. This netlist cannot be used for SDF annotated simulation.
// Device      : xc7a35tcpg236-1
// --------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

(* CHECK_LICENSE_TYPE = "harvard_design_M_RAM_0_0,M_RAM,{}" *) (* DowngradeIPIdentifiedWarnings = "yes" *) (* IP_DEFINITION_SOURCE = "module_ref" *) 
(* X_CORE_INFO = "M_RAM,Vivado 2026.1" *) 
(* NotValidForBitStream *)
module harvard_design_M_RAM_0_0
   (clk,
    dir_E,
    dir_L,
    dato_in,
    dato_out,
    L_E);
  (* X_INTERFACE_INFO = "xilinx.com:signal:clock:1.0 clk CLK" *) (* X_INTERFACE_MODE = "slave" *) (* X_INTERFACE_PARAMETER = "XIL_INTERFACENAME clk, FREQ_HZ 100000000, FREQ_TOLERANCE_HZ 0, PHASE 0.0, CLK_DOMAIN harvard_design_clk, INSERT_VIP 0" *) input clk;
  input [3:0]dir_E;
  input [3:0]dir_L;
  input [3:0]dato_in;
  output [3:0]dato_out;
  input L_E;

  wire L_E;
  wire clk;
  wire [3:0]dato_in;
  wire [3:0]dato_out;
  wire [3:0]dir_E;
  wire [3:0]dir_L;

  harvard_design_M_RAM_0_0_M_RAM inst
       (.L_E(L_E),
        .clk(clk),
        .dato_in(dato_in),
        .dato_out(dato_out),
        .dir_E(dir_E),
        .dir_L(dir_L));
endmodule

(* ORIG_REF_NAME = "M_RAM" *) 
module harvard_design_M_RAM_0_0_M_RAM
   (dato_out,
    clk,
    L_E,
    dato_in,
    dir_L,
    dir_E);
  output [3:0]dato_out;
  input clk;
  input L_E;
  input [3:0]dato_in;
  input [3:0]dir_L;
  input [3:0]dir_E;

  wire L_E;
  wire clk;
  wire [3:0]dato_in;
  wire [3:0]dato_out;
  wire [3:0]dir_E;
  wire [3:0]dir_L;
  wire p_0_in;
  wire [3:0]p_0_out;
  wire [1:0]NLW_memoria_reg_0_15_0_3_DOC_UNCONNECTED;
  wire [1:0]NLW_memoria_reg_0_15_0_3_DOD_UNCONNECTED;

  LUT1 #(
    .INIT(2'h1)) 
    \dato_out[3]_i_1 
       (.I0(L_E),
        .O(p_0_in));
  FDRE \dato_out_reg[0] 
       (.C(clk),
        .CE(p_0_in),
        .D(p_0_out[0]),
        .Q(dato_out[0]),
        .R(1'b0));
  FDRE \dato_out_reg[1] 
       (.C(clk),
        .CE(p_0_in),
        .D(p_0_out[1]),
        .Q(dato_out[1]),
        .R(1'b0));
  FDRE \dato_out_reg[2] 
       (.C(clk),
        .CE(p_0_in),
        .D(p_0_out[2]),
        .Q(dato_out[2]),
        .R(1'b0));
  FDRE \dato_out_reg[3] 
       (.C(clk),
        .CE(p_0_in),
        .D(p_0_out[3]),
        .Q(dato_out[3]),
        .R(1'b0));
  (* METHODOLOGY_DRC_VIOS = "" *) 
  (* RTL_RAM_BITS = "64" *) 
  (* RTL_RAM_NAME = "harvard_design_M_RAM_0_0/inst/memoria_reg" *) 
  (* RTL_RAM_STYLE = "auto" *) 
  (* RTL_RAM_TYPE = "RAM_SDP" *) 
  (* ram_addr_begin = "0" *) 
  (* ram_addr_end = "15" *) 
  (* ram_offset = "0" *) 
  (* ram_slice_begin = "0" *) 
  (* ram_slice_end = "3" *) 
  RAM32M #(
    .INIT_A(64'h0000000000000000),
    .INIT_B(64'h0000000000000000),
    .INIT_C(64'h0000000000000000),
    .INIT_D(64'h0000000000000000)) 
    memoria_reg_0_15_0_3
       (.ADDRA({1'b0,dir_L}),
        .ADDRB({1'b0,dir_L}),
        .ADDRC({1'b0,dir_L}),
        .ADDRD({1'b0,dir_E}),
        .DIA(dato_in[1:0]),
        .DIB(dato_in[3:2]),
        .DIC({1'b0,1'b0}),
        .DID({1'b0,1'b0}),
        .DOA(p_0_out[1:0]),
        .DOB(p_0_out[3:2]),
        .DOC(NLW_memoria_reg_0_15_0_3_DOC_UNCONNECTED[1:0]),
        .DOD(NLW_memoria_reg_0_15_0_3_DOD_UNCONNECTED[1:0]),
        .WCLK(clk),
        .WE(L_E));
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
