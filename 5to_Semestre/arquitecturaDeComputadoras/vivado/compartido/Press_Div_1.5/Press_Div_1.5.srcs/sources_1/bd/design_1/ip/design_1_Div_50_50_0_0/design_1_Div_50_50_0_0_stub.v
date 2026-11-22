// Copyright 1986-2017 Xilinx, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2017.4.1 (win64) Build 2117270 Tue Jan 30 15:32:00 MST 2018
// Date        : Sat Oct 10 17:21:21 2026
// Host        : txinerlaptop running 64-bit major release  (build 9200)
// Command     : write_verilog -force -mode synth_stub {c:/Users/janag/Documents/IEI/Arquitectura de
//               Computadoras/Proy_23400357/Press_Div/Press_Div.srcs/sources_1/bd/design_1/ip/design_1_Div_50_50_0_0/design_1_Div_50_50_0_0_stub.v}
// Design      : design_1_Div_50_50_0_0
// Purpose     : Stub declaration of top-level module interface
// Device      : xc7a100tcsg324-1
// --------------------------------------------------------------------------------

// This empty module with port declaration file causes synthesis tools to infer a black box for IP.
// The synthesis directives are for Synopsys Synplify support to prevent IO buffer insertion.
// Please paste the declaration into a Verilog source file or add the file as an additional source.
(* x_core_info = "Div_50_50,Vivado 2017.4.1" *)
module design_1_Div_50_50_0_0(clk, rst, clk_div)
/* synthesis syn_black_box black_box_pad_pin="clk,rst,clk_div" */;
  input clk;
  input rst;
  output clk_div;
endmodule
