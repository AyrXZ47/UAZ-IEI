// Copyright 1986-2017 Xilinx, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2017.4.1 (win64) Build 2117270 Tue Jan 30 15:32:00 MST 2018
// Date        : Sat Sep 26 16:05:29 2026
// Host        : txinerlaptop running 64-bit major release  (build 9200)
// Command     : write_verilog -force -mode synth_stub {c:/Users/janag/Documents/IEI/Arquitectura de
//               Computadoras/Proy_23400357/project_23400357/project_23400357.srcs/sources_1/bd/PRUEBA_DESING/ip/PRUEBA_DESING_FUENTE_PRUEBA_0_0/PRUEBA_DESING_FUENTE_PRUEBA_0_0_stub.v}
// Design      : PRUEBA_DESING_FUENTE_PRUEBA_0_0
// Purpose     : Stub declaration of top-level module interface
// Device      : xc7a100tcsg324-1
// --------------------------------------------------------------------------------

// This empty module with port declaration file causes synthesis tools to infer a black box for IP.
// The synthesis directives are for Synopsys Synplify support to prevent IO buffer insertion.
// Please paste the declaration into a Verilog source file or add the file as an additional source.
(* x_core_info = "FUENTE_PRUEBA,Vivado 2017.4.1" *)
module PRUEBA_DESING_FUENTE_PRUEBA_0_0(SW, LED)
/* synthesis syn_black_box black_box_pad_pin="SW[15:0],LED[15:0]" */;
  input [15:0]SW;
  output [15:0]LED;
endmodule
