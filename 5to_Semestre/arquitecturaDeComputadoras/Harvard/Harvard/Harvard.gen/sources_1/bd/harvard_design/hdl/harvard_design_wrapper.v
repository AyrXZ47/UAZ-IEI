//Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
//Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
//--------------------------------------------------------------------------------
//Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
//Date        : Sat Nov 21 18:10:43 2026
//Host        : nixos-laptop running 64-bit unknown
//Command     : generate_target harvard_design_wrapper.bd
//Design      : harvard_design_wrapper
//Purpose     : IP block netlist
//--------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

module harvard_design_wrapper
   (an,
    btnU,
    clk,
    led1,
    led2,
    rst,
    seg,
    sw1,
    sw2,
    sw3);
  output [3:0]an;
  input btnU;
  input clk;
  output led1;
  output led2;
  input rst;
  output [7:0]seg;
  input [3:0]sw1;
  input [3:0]sw2;
  input [3:0]sw3;

  wire [3:0]an;
  wire btnU;
  wire clk;
  wire led1;
  wire led2;
  wire rst;
  wire [7:0]seg;
  wire [3:0]sw1;
  wire [3:0]sw2;
  wire [3:0]sw3;

  harvard_design harvard_design_i
       (.an(an),
        .btnU(btnU),
        .clk(clk),
        .led1(led1),
        .led2(led2),
        .rst(rst),
        .seg(seg),
        .sw1(sw1),
        .sw2(sw2),
        .sw3(sw3));
endmodule
