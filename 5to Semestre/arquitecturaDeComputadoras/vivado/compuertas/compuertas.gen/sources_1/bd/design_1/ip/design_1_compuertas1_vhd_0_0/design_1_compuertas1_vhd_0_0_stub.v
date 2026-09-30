// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
// Date        : Sat Sep 26 17:45:40 2026
// Host        : nixos-laptop running 64-bit unknown
// Command     : write_verilog -force -mode synth_stub {/home/yovick/repos/UAZ-IEI/5to
//               Semestre/arquitecturaDeComputadoras/vivado/compuertas/compuertas.gen/sources_1/bd/design_1/ip/design_1_compuertas1_vhd_0_0/design_1_compuertas1_vhd_0_0_stub.v}
// Design      : design_1_compuertas1_vhd_0_0
// Purpose     : Stub declaration of top-level module interface
// Device      : xc7a35tcpg236-1
// --------------------------------------------------------------------------------

// This empty module with port declaration file causes synthesis tools to infer a black box for IP.
// The synthesis directives are for Synopsys Synplify support to prevent IO buffer insertion.
// Please paste the declaration into a Verilog source file or add the file as an additional source.
(* CHECK_LICENSE_TYPE = "design_1_compuertas1_vhd_0_0,compuertas1_vhd,{}" *) (* core_generation_info = "design_1_compuertas1_vhd_0_0,compuertas1_vhd,{x_ipProduct=Vivado 2026.1,x_ipVendor=xilinx.com,x_ipLibrary=module_ref,x_ipName=compuertas1_vhd,x_ipVersion=1.0,x_ipCoreRevision=1,x_ipLanguage=VHDL,x_ipSimLanguage=MIXED}" *) (* downgradeipidentifiedwarnings = "yes" *) 
(* ip_definition_source = "module_ref" *) (* x_core_info = "compuertas1_vhd,Vivado 2026.1" *) 
module design_1_compuertas1_vhd_0_0(A, B, sel, sal)
/* synthesis syn_black_box black_box_pad_pin="A,B,sel[2:0],sal" */;
  input A;
  input B;
  input [2:0]sel;
  output sal;
endmodule
