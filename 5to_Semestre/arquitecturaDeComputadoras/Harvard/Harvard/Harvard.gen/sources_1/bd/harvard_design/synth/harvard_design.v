//Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
//Copyright 2022-2026 Advanced Micro Devices, Inc. All Rights Reserved.
//--------------------------------------------------------------------------------
//Tool Version: Vivado v.2026.1 (lin64) Build 6511674 Tue Jun 16 11:01:26 MDT 2026
//Date        : Sat Nov 21 18:10:43 2026
//Host        : nixos-laptop running 64-bit unknown
//Command     : generate_target harvard_design.bd
//Design      : harvard_design
//Purpose     : IP block netlist
//--------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

(* CORE_GENERATION_INFO = "harvard_design,IP_Integrator,{x_ipVendor=xilinx.com,x_ipLibrary=BlockDiagram,x_ipName=harvard_design,x_ipVersion=1.00.a,x_ipLanguage=VERILOG}" *) (* HW_HANDOFF = "harvard_design.hwdef" *) 
module harvard_design
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
  (* X_INTERFACE_INFO = "xilinx.com:signal:clock:1.0 CLK.CLK CLK" *) (* X_INTERFACE_PARAMETER = "XIL_INTERFACENAME CLK.CLK, ASSOCIATED_RESET rst, CLK_DOMAIN harvard_design_clk, FREQ_HZ 100000000, FREQ_TOLERANCE_HZ 0, INSERT_VIP 0, PHASE 0.0" *) input clk;
  output led1;
  output led2;
  (* X_INTERFACE_INFO = "xilinx.com:signal:reset:1.0 RST.RST RST" *) (* X_INTERFACE_PARAMETER = "XIL_INTERFACENAME RST.RST, INSERT_VIP 0, POLARITY ACTIVE_LOW" *) input rst;
  output [7:0]seg;
  input [3:0]sw1;
  input [3:0]sw2;
  input [3:0]sw3;

  wire [3:0]M_RAM_0_dato_out;
  wire [2:0]M_ROM_0_dato;
  wire [3:0]Net;
  wire [3:0]PC_0_Dir;
  wire [3:0]UAL_0_res;
  wire [3:0]UC_0_A_out;
  wire [3:0]UC_0_B_out;
  wire UC_0_L_E;
  wire UC_0_incrementar;
  wire [2:0]UC_0_op_out;
  wire [3:0]an;
  wire boton_0_sal;
  wire btnU;
  wire clk;
  wire [1:0]contador_0_display;
  wire led1;
  wire led2;
  wire [3:0]mux_datos_0_sal;
  wire pres_500hz_0_clk_pres;
  wire rst;
  wire [7:0]seg;
  wire [3:0]sw1;
  wire [3:0]sw2;
  wire [3:0]sw3;

  harvard_design_Dec_bcd_7seg_0_1 Dec_bcd_7seg_0
       (.num(mux_datos_0_sal),
        .seg(seg));
  harvard_design_M_RAM_0_0 M_RAM_0
       (.L_E(UC_0_L_E),
        .clk(clk),
        .dato_in(UAL_0_res),
        .dato_out(M_RAM_0_dato_out),
        .dir_E(Net),
        .dir_L(sw3));
  harvard_design_M_ROM_0_0 M_ROM_0
       (.clk(clk),
        .dato(M_ROM_0_dato),
        .dir(Net));
  harvard_design_PC_0_0 PC_0
       (.Dir(PC_0_Dir),
        .clk(clk),
        .incremento(UC_0_incrementar),
        .rst(rst));
  harvard_design_UAL_0_0 UAL_0
       (.A(UC_0_A_out),
        .B(UC_0_B_out),
        .acarreo(led1),
        .cero(led2),
        .op(UC_0_op_out),
        .res(UAL_0_res));
  harvard_design_UC_0_0 UC_0
       (.A_in(sw1),
        .A_out(UC_0_A_out),
        .B_in(sw2),
        .B_out(UC_0_B_out),
        .L_E(UC_0_L_E),
        .clk(clk),
        .dir_in(PC_0_Dir),
        .dir_out(Net),
        .ejecutar(boton_0_sal),
        .incrementar(UC_0_incrementar),
        .op_in(M_ROM_0_dato),
        .op_out(UC_0_op_out),
        .rst(rst));
  harvard_design_boton_0_1 boton_0
       (.clk(clk),
        .ent(btnU),
        .rst(rst),
        .sal(boton_0_sal));
  harvard_design_contador_0_1 contador_0
       (.clk(pres_500hz_0_clk_pres),
        .display(contador_0_display),
        .rst(rst));
  harvard_design_dec_an_0_1 dec_an_0
       (.ent(contador_0_display),
        .sal(an));
  harvard_design_mux_datos_0_0 mux_datos_0
       (.A(UC_0_A_out),
        .B(UC_0_B_out),
        .datoRam(M_RAM_0_dato_out),
        .dir(PC_0_Dir),
        .sal(mux_datos_0_sal),
        .sel(contador_0_display));
  harvard_design_pres_500hz_0_0 pres_500hz_0
       (.clk(clk),
        .clk_pres(pres_500hz_0_clk_pres),
        .rst(rst));
endmodule
