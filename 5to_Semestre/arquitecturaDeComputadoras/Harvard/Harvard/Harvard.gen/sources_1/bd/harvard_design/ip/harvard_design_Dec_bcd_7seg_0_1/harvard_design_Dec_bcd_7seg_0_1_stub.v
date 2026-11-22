// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
// Date        : Sat Nov 21 18:11:25 2026
// Host        : nixos-laptop running 64-bit unknown
// Command     : write_verilog -force -mode synth_stub
//               /tmp/opencode/harvard_fix/Harvard/Harvard.gen/sources_1/bd/harvard_design/ip/harvard_design_Dec_bcd_7seg_0_1/harvard_design_Dec_bcd_7seg_0_1_stub.v
// Design      : harvard_design_Dec_bcd_7seg_0_1
// Purpose     : Stub declaration of top-level module interface
// Device      : xc7a35tcpg236-1
// --------------------------------------------------------------------------------

// This empty module with port declaration file causes synthesis tools to infer a black box for IP.
// The synthesis directives are for Synopsys Synplify support to prevent IO buffer insertion.
// Please paste the declaration into a Verilog source file or add the file as an additional source.
(* CHECK_LICENSE_TYPE = "harvard_design_Dec_bcd_7seg_0_1,Dec_bcd_7seg,{}" *) (* CORE_GENERATION_INFO = "harvard_design_Dec_bcd_7seg_0_1,Dec_bcd_7seg,{x_ipProduct=Vivado 2026.1,x_ipVendor=xilinx.com,x_ipLibrary=module_ref,x_ipName=Dec_bcd_7seg,x_ipVersion=1.0,x_ipCoreRevision=1,x_ipLanguage=VERILOG,x_ipSimLanguage=MIXED}" *) (* DowngradeIPIdentifiedWarnings = "yes" *) 
(* IP_DEFINITION_SOURCE = "module_ref" *) (* X_CORE_INFO = "Dec_bcd_7seg,Vivado 2026.1" *) 
module harvard_design_Dec_bcd_7seg_0_1(num, seg)
/* synthesis syn_black_box black_box_pad_pin="num[3:0],seg[7:0]" */;
  input [3:0]num;
  output [7:0]seg;
endmodule
