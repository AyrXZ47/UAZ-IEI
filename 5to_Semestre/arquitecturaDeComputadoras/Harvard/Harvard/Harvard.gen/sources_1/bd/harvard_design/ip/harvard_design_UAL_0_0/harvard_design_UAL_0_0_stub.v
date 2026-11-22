// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
// Date        : Sat Nov 21 18:12:07 2026
// Host        : nixos-laptop running 64-bit unknown
// Command     : write_verilog -force -mode synth_stub
//               /tmp/opencode/harvard_fix/Harvard/Harvard.gen/sources_1/bd/harvard_design/ip/harvard_design_UAL_0_0/harvard_design_UAL_0_0_stub.v
// Design      : harvard_design_UAL_0_0
// Purpose     : Stub declaration of top-level module interface
// Device      : xc7a35tcpg236-1
// --------------------------------------------------------------------------------

// This empty module with port declaration file causes synthesis tools to infer a black box for IP.
// The synthesis directives are for Synopsys Synplify support to prevent IO buffer insertion.
// Please paste the declaration into a Verilog source file or add the file as an additional source.
(* CHECK_LICENSE_TYPE = "harvard_design_UAL_0_0,UAL,{}" *) (* CORE_GENERATION_INFO = "harvard_design_UAL_0_0,UAL,{x_ipProduct=Vivado 2026.1,x_ipVendor=xilinx.com,x_ipLibrary=module_ref,x_ipName=UAL,x_ipVersion=1.0,x_ipCoreRevision=1,x_ipLanguage=VERILOG,x_ipSimLanguage=MIXED}" *) (* DowngradeIPIdentifiedWarnings = "yes" *) 
(* IP_DEFINITION_SOURCE = "module_ref" *) (* X_CORE_INFO = "UAL,Vivado 2026.1" *) 
module harvard_design_UAL_0_0(A, B, op, res, acarreo, cero)
/* synthesis syn_black_box black_box_pad_pin="A[3:0],B[3:0],op[2:0],res[3:0],acarreo,cero" */;
  input [3:0]A;
  input [3:0]B;
  input [2:0]op;
  output [3:0]res;
  output acarreo;
  output cero;
endmodule
