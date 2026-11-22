// Copyright 1986-2017 Xilinx, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2017.4.1 (win64) Build 2117270 Tue Jan 30 15:32:00 MST 2018
// Date        : Sat Oct 10 17:21:21 2026
// Host        : txinerlaptop running 64-bit major release  (build 9200)
// Command     : write_verilog -force -mode funcsim -rename_top decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix -prefix
//               decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix_ design_1_Div_50_50_0_0_sim_netlist.v
// Design      : design_1_Div_50_50_0_0
// Purpose     : This verilog netlist is a functional simulation representation of the design and should not be modified
//               or synthesized. This netlist cannot be used for SDF annotated simulation.
// Device      : xc7a100tcsg324-1
// --------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

module decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix_Div_50_50
   (clk_div,
    clk,
    rst);
  output clk_div;
  input clk;
  input rst;

  wire cambio_i_1_n_0;
  wire cambio_i_3_n_0;
  wire cambio_i_4_n_0;
  wire cambio_i_5_n_0;
  wire cambio_i_6_n_0;
  wire cambio_i_7_n_0;
  wire cambio_i_8_n_0;
  wire clk;
  wire clk_div;
  wire \cont[0]_i_2_n_0 ;
  wire \cont[0]_i_3_n_0 ;
  wire \cont[0]_i_4_n_0 ;
  wire \cont[0]_i_5_n_0 ;
  wire \cont[0]_i_6_n_0 ;
  wire \cont[12]_i_2_n_0 ;
  wire \cont[12]_i_3_n_0 ;
  wire \cont[12]_i_4_n_0 ;
  wire \cont[12]_i_5_n_0 ;
  wire \cont[16]_i_2_n_0 ;
  wire \cont[16]_i_3_n_0 ;
  wire \cont[16]_i_4_n_0 ;
  wire \cont[16]_i_5_n_0 ;
  wire \cont[20]_i_2_n_0 ;
  wire \cont[20]_i_3_n_0 ;
  wire \cont[20]_i_4_n_0 ;
  wire \cont[20]_i_5_n_0 ;
  wire \cont[24]_i_2_n_0 ;
  wire \cont[24]_i_3_n_0 ;
  wire \cont[24]_i_4_n_0 ;
  wire \cont[4]_i_2_n_0 ;
  wire \cont[4]_i_3_n_0 ;
  wire \cont[4]_i_4_n_0 ;
  wire \cont[4]_i_5_n_0 ;
  wire \cont[8]_i_2_n_0 ;
  wire \cont[8]_i_3_n_0 ;
  wire \cont[8]_i_4_n_0 ;
  wire \cont[8]_i_5_n_0 ;
  wire [26:0]cont_reg;
  wire \cont_reg[0]_i_1_n_0 ;
  wire \cont_reg[0]_i_1_n_1 ;
  wire \cont_reg[0]_i_1_n_2 ;
  wire \cont_reg[0]_i_1_n_3 ;
  wire \cont_reg[0]_i_1_n_4 ;
  wire \cont_reg[0]_i_1_n_5 ;
  wire \cont_reg[0]_i_1_n_6 ;
  wire \cont_reg[0]_i_1_n_7 ;
  wire \cont_reg[12]_i_1_n_0 ;
  wire \cont_reg[12]_i_1_n_1 ;
  wire \cont_reg[12]_i_1_n_2 ;
  wire \cont_reg[12]_i_1_n_3 ;
  wire \cont_reg[12]_i_1_n_4 ;
  wire \cont_reg[12]_i_1_n_5 ;
  wire \cont_reg[12]_i_1_n_6 ;
  wire \cont_reg[12]_i_1_n_7 ;
  wire \cont_reg[16]_i_1_n_0 ;
  wire \cont_reg[16]_i_1_n_1 ;
  wire \cont_reg[16]_i_1_n_2 ;
  wire \cont_reg[16]_i_1_n_3 ;
  wire \cont_reg[16]_i_1_n_4 ;
  wire \cont_reg[16]_i_1_n_5 ;
  wire \cont_reg[16]_i_1_n_6 ;
  wire \cont_reg[16]_i_1_n_7 ;
  wire \cont_reg[20]_i_1_n_0 ;
  wire \cont_reg[20]_i_1_n_1 ;
  wire \cont_reg[20]_i_1_n_2 ;
  wire \cont_reg[20]_i_1_n_3 ;
  wire \cont_reg[20]_i_1_n_4 ;
  wire \cont_reg[20]_i_1_n_5 ;
  wire \cont_reg[20]_i_1_n_6 ;
  wire \cont_reg[20]_i_1_n_7 ;
  wire \cont_reg[24]_i_1_n_2 ;
  wire \cont_reg[24]_i_1_n_3 ;
  wire \cont_reg[24]_i_1_n_5 ;
  wire \cont_reg[24]_i_1_n_6 ;
  wire \cont_reg[24]_i_1_n_7 ;
  wire \cont_reg[4]_i_1_n_0 ;
  wire \cont_reg[4]_i_1_n_1 ;
  wire \cont_reg[4]_i_1_n_2 ;
  wire \cont_reg[4]_i_1_n_3 ;
  wire \cont_reg[4]_i_1_n_4 ;
  wire \cont_reg[4]_i_1_n_5 ;
  wire \cont_reg[4]_i_1_n_6 ;
  wire \cont_reg[4]_i_1_n_7 ;
  wire \cont_reg[8]_i_1_n_0 ;
  wire \cont_reg[8]_i_1_n_1 ;
  wire \cont_reg[8]_i_1_n_2 ;
  wire \cont_reg[8]_i_1_n_3 ;
  wire \cont_reg[8]_i_1_n_4 ;
  wire \cont_reg[8]_i_1_n_5 ;
  wire \cont_reg[8]_i_1_n_6 ;
  wire \cont_reg[8]_i_1_n_7 ;
  wire load;
  wire rst;
  wire [3:2]\NLW_cont_reg[24]_i_1_CO_UNCONNECTED ;
  wire [3:3]\NLW_cont_reg[24]_i_1_O_UNCONNECTED ;

  LUT2 #(
    .INIT(4'h6)) 
    cambio_i_1
       (.I0(load),
        .I1(clk_div),
        .O(cambio_i_1_n_0));
  LUT6 #(
    .INIT(64'h8000000000000000)) 
    cambio_i_2
       (.I0(cambio_i_3_n_0),
        .I1(cambio_i_4_n_0),
        .I2(cambio_i_5_n_0),
        .I3(cambio_i_6_n_0),
        .I4(cambio_i_7_n_0),
        .I5(cambio_i_8_n_0),
        .O(load));
  LUT6 #(
    .INIT(64'h8000000000000000)) 
    cambio_i_3
       (.I0(cont_reg[20]),
        .I1(cont_reg[21]),
        .I2(cont_reg[22]),
        .I3(cont_reg[23]),
        .I4(cont_reg[26]),
        .I5(cont_reg[24]),
        .O(cambio_i_3_n_0));
  LUT4 #(
    .INIT(16'h1000)) 
    cambio_i_4
       (.I0(cont_reg[1]),
        .I1(cont_reg[0]),
        .I2(cont_reg[13]),
        .I3(cont_reg[8]),
        .O(cambio_i_4_n_0));
  LUT4 #(
    .INIT(16'h8000)) 
    cambio_i_5
       (.I0(cont_reg[18]),
        .I1(cont_reg[16]),
        .I2(cont_reg[15]),
        .I3(cont_reg[14]),
        .O(cambio_i_5_n_0));
  LUT6 #(
    .INIT(64'h0000000000000001)) 
    cambio_i_6
       (.I0(cont_reg[10]),
        .I1(cont_reg[11]),
        .I2(cont_reg[12]),
        .I3(cont_reg[17]),
        .I4(cont_reg[25]),
        .I5(cont_reg[19]),
        .O(cambio_i_6_n_0));
  LUT3 #(
    .INIT(8'h01)) 
    cambio_i_7
       (.I0(cont_reg[4]),
        .I1(cont_reg[3]),
        .I2(cont_reg[2]),
        .O(cambio_i_7_n_0));
  LUT4 #(
    .INIT(16'h0001)) 
    cambio_i_8
       (.I0(cont_reg[9]),
        .I1(cont_reg[7]),
        .I2(cont_reg[6]),
        .I3(cont_reg[5]),
        .O(cambio_i_8_n_0));
  FDCE #(
    .INIT(1'b0)) 
    cambio_reg
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(cambio_i_1_n_0),
        .Q(clk_div));
  LUT2 #(
    .INIT(4'h2)) 
    \cont[0]_i_2 
       (.I0(cont_reg[0]),
        .I1(load),
        .O(\cont[0]_i_2_n_0 ));
  LUT2 #(
    .INIT(4'h2)) 
    \cont[0]_i_3 
       (.I0(cont_reg[3]),
        .I1(load),
        .O(\cont[0]_i_3_n_0 ));
  LUT2 #(
    .INIT(4'h2)) 
    \cont[0]_i_4 
       (.I0(cont_reg[2]),
        .I1(load),
        .O(\cont[0]_i_4_n_0 ));
  LUT2 #(
    .INIT(4'h2)) 
    \cont[0]_i_5 
       (.I0(cont_reg[1]),
        .I1(load),
        .O(\cont[0]_i_5_n_0 ));
  LUT2 #(
    .INIT(4'h1)) 
    \cont[0]_i_6 
       (.I0(cont_reg[0]),
        .I1(load),
        .O(\cont[0]_i_6_n_0 ));
  LUT2 #(
    .INIT(4'h2)) 
    \cont[12]_i_2 
       (.I0(cont_reg[15]),
        .I1(load),
        .O(\cont[12]_i_2_n_0 ));
  LUT2 #(
    .INIT(4'h2)) 
    \cont[12]_i_3 
       (.I0(cont_reg[14]),
        .I1(load),
        .O(\cont[12]_i_3_n_0 ));
  LUT2 #(
    .INIT(4'h2)) 
    \cont[12]_i_4 
       (.I0(cont_reg[13]),
        .I1(load),
        .O(\cont[12]_i_4_n_0 ));
  LUT2 #(
    .INIT(4'h2)) 
    \cont[12]_i_5 
       (.I0(cont_reg[12]),
        .I1(load),
        .O(\cont[12]_i_5_n_0 ));
  LUT2 #(
    .INIT(4'h2)) 
    \cont[16]_i_2 
       (.I0(cont_reg[19]),
        .I1(load),
        .O(\cont[16]_i_2_n_0 ));
  LUT2 #(
    .INIT(4'h2)) 
    \cont[16]_i_3 
       (.I0(cont_reg[18]),
        .I1(load),
        .O(\cont[16]_i_3_n_0 ));
  LUT2 #(
    .INIT(4'h2)) 
    \cont[16]_i_4 
       (.I0(cont_reg[17]),
        .I1(load),
        .O(\cont[16]_i_4_n_0 ));
  LUT2 #(
    .INIT(4'h2)) 
    \cont[16]_i_5 
       (.I0(cont_reg[16]),
        .I1(load),
        .O(\cont[16]_i_5_n_0 ));
  LUT2 #(
    .INIT(4'h2)) 
    \cont[20]_i_2 
       (.I0(cont_reg[23]),
        .I1(load),
        .O(\cont[20]_i_2_n_0 ));
  LUT2 #(
    .INIT(4'h2)) 
    \cont[20]_i_3 
       (.I0(cont_reg[22]),
        .I1(load),
        .O(\cont[20]_i_3_n_0 ));
  LUT2 #(
    .INIT(4'h2)) 
    \cont[20]_i_4 
       (.I0(cont_reg[21]),
        .I1(load),
        .O(\cont[20]_i_4_n_0 ));
  LUT2 #(
    .INIT(4'h2)) 
    \cont[20]_i_5 
       (.I0(cont_reg[20]),
        .I1(load),
        .O(\cont[20]_i_5_n_0 ));
  LUT2 #(
    .INIT(4'h2)) 
    \cont[24]_i_2 
       (.I0(cont_reg[26]),
        .I1(load),
        .O(\cont[24]_i_2_n_0 ));
  LUT2 #(
    .INIT(4'h2)) 
    \cont[24]_i_3 
       (.I0(cont_reg[25]),
        .I1(load),
        .O(\cont[24]_i_3_n_0 ));
  LUT2 #(
    .INIT(4'h2)) 
    \cont[24]_i_4 
       (.I0(cont_reg[24]),
        .I1(load),
        .O(\cont[24]_i_4_n_0 ));
  LUT2 #(
    .INIT(4'h2)) 
    \cont[4]_i_2 
       (.I0(cont_reg[7]),
        .I1(load),
        .O(\cont[4]_i_2_n_0 ));
  LUT2 #(
    .INIT(4'h2)) 
    \cont[4]_i_3 
       (.I0(cont_reg[6]),
        .I1(load),
        .O(\cont[4]_i_3_n_0 ));
  LUT2 #(
    .INIT(4'h2)) 
    \cont[4]_i_4 
       (.I0(cont_reg[5]),
        .I1(load),
        .O(\cont[4]_i_4_n_0 ));
  LUT2 #(
    .INIT(4'h2)) 
    \cont[4]_i_5 
       (.I0(cont_reg[4]),
        .I1(load),
        .O(\cont[4]_i_5_n_0 ));
  LUT2 #(
    .INIT(4'h2)) 
    \cont[8]_i_2 
       (.I0(cont_reg[11]),
        .I1(load),
        .O(\cont[8]_i_2_n_0 ));
  LUT2 #(
    .INIT(4'h2)) 
    \cont[8]_i_3 
       (.I0(cont_reg[10]),
        .I1(load),
        .O(\cont[8]_i_3_n_0 ));
  LUT2 #(
    .INIT(4'h2)) 
    \cont[8]_i_4 
       (.I0(cont_reg[9]),
        .I1(load),
        .O(\cont[8]_i_4_n_0 ));
  LUT2 #(
    .INIT(4'h2)) 
    \cont[8]_i_5 
       (.I0(cont_reg[8]),
        .I1(load),
        .O(\cont[8]_i_5_n_0 ));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[0] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(\cont_reg[0]_i_1_n_7 ),
        .Q(cont_reg[0]));
  CARRY4 \cont_reg[0]_i_1 
       (.CI(1'b0),
        .CO({\cont_reg[0]_i_1_n_0 ,\cont_reg[0]_i_1_n_1 ,\cont_reg[0]_i_1_n_2 ,\cont_reg[0]_i_1_n_3 }),
        .CYINIT(1'b0),
        .DI({1'b0,1'b0,1'b0,\cont[0]_i_2_n_0 }),
        .O({\cont_reg[0]_i_1_n_4 ,\cont_reg[0]_i_1_n_5 ,\cont_reg[0]_i_1_n_6 ,\cont_reg[0]_i_1_n_7 }),
        .S({\cont[0]_i_3_n_0 ,\cont[0]_i_4_n_0 ,\cont[0]_i_5_n_0 ,\cont[0]_i_6_n_0 }));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[10] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(\cont_reg[8]_i_1_n_5 ),
        .Q(cont_reg[10]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[11] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(\cont_reg[8]_i_1_n_4 ),
        .Q(cont_reg[11]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[12] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(\cont_reg[12]_i_1_n_7 ),
        .Q(cont_reg[12]));
  CARRY4 \cont_reg[12]_i_1 
       (.CI(\cont_reg[8]_i_1_n_0 ),
        .CO({\cont_reg[12]_i_1_n_0 ,\cont_reg[12]_i_1_n_1 ,\cont_reg[12]_i_1_n_2 ,\cont_reg[12]_i_1_n_3 }),
        .CYINIT(1'b0),
        .DI({1'b0,1'b0,1'b0,1'b0}),
        .O({\cont_reg[12]_i_1_n_4 ,\cont_reg[12]_i_1_n_5 ,\cont_reg[12]_i_1_n_6 ,\cont_reg[12]_i_1_n_7 }),
        .S({\cont[12]_i_2_n_0 ,\cont[12]_i_3_n_0 ,\cont[12]_i_4_n_0 ,\cont[12]_i_5_n_0 }));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[13] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(\cont_reg[12]_i_1_n_6 ),
        .Q(cont_reg[13]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[14] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(\cont_reg[12]_i_1_n_5 ),
        .Q(cont_reg[14]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[15] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(\cont_reg[12]_i_1_n_4 ),
        .Q(cont_reg[15]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[16] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(\cont_reg[16]_i_1_n_7 ),
        .Q(cont_reg[16]));
  CARRY4 \cont_reg[16]_i_1 
       (.CI(\cont_reg[12]_i_1_n_0 ),
        .CO({\cont_reg[16]_i_1_n_0 ,\cont_reg[16]_i_1_n_1 ,\cont_reg[16]_i_1_n_2 ,\cont_reg[16]_i_1_n_3 }),
        .CYINIT(1'b0),
        .DI({1'b0,1'b0,1'b0,1'b0}),
        .O({\cont_reg[16]_i_1_n_4 ,\cont_reg[16]_i_1_n_5 ,\cont_reg[16]_i_1_n_6 ,\cont_reg[16]_i_1_n_7 }),
        .S({\cont[16]_i_2_n_0 ,\cont[16]_i_3_n_0 ,\cont[16]_i_4_n_0 ,\cont[16]_i_5_n_0 }));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[17] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(\cont_reg[16]_i_1_n_6 ),
        .Q(cont_reg[17]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[18] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(\cont_reg[16]_i_1_n_5 ),
        .Q(cont_reg[18]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[19] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(\cont_reg[16]_i_1_n_4 ),
        .Q(cont_reg[19]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[1] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(\cont_reg[0]_i_1_n_6 ),
        .Q(cont_reg[1]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[20] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(\cont_reg[20]_i_1_n_7 ),
        .Q(cont_reg[20]));
  CARRY4 \cont_reg[20]_i_1 
       (.CI(\cont_reg[16]_i_1_n_0 ),
        .CO({\cont_reg[20]_i_1_n_0 ,\cont_reg[20]_i_1_n_1 ,\cont_reg[20]_i_1_n_2 ,\cont_reg[20]_i_1_n_3 }),
        .CYINIT(1'b0),
        .DI({1'b0,1'b0,1'b0,1'b0}),
        .O({\cont_reg[20]_i_1_n_4 ,\cont_reg[20]_i_1_n_5 ,\cont_reg[20]_i_1_n_6 ,\cont_reg[20]_i_1_n_7 }),
        .S({\cont[20]_i_2_n_0 ,\cont[20]_i_3_n_0 ,\cont[20]_i_4_n_0 ,\cont[20]_i_5_n_0 }));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[21] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(\cont_reg[20]_i_1_n_6 ),
        .Q(cont_reg[21]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[22] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(\cont_reg[20]_i_1_n_5 ),
        .Q(cont_reg[22]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[23] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(\cont_reg[20]_i_1_n_4 ),
        .Q(cont_reg[23]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[24] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(\cont_reg[24]_i_1_n_7 ),
        .Q(cont_reg[24]));
  CARRY4 \cont_reg[24]_i_1 
       (.CI(\cont_reg[20]_i_1_n_0 ),
        .CO({\NLW_cont_reg[24]_i_1_CO_UNCONNECTED [3:2],\cont_reg[24]_i_1_n_2 ,\cont_reg[24]_i_1_n_3 }),
        .CYINIT(1'b0),
        .DI({1'b0,1'b0,1'b0,1'b0}),
        .O({\NLW_cont_reg[24]_i_1_O_UNCONNECTED [3],\cont_reg[24]_i_1_n_5 ,\cont_reg[24]_i_1_n_6 ,\cont_reg[24]_i_1_n_7 }),
        .S({1'b0,\cont[24]_i_2_n_0 ,\cont[24]_i_3_n_0 ,\cont[24]_i_4_n_0 }));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[25] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(\cont_reg[24]_i_1_n_6 ),
        .Q(cont_reg[25]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[26] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(\cont_reg[24]_i_1_n_5 ),
        .Q(cont_reg[26]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[2] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(\cont_reg[0]_i_1_n_5 ),
        .Q(cont_reg[2]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[3] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(\cont_reg[0]_i_1_n_4 ),
        .Q(cont_reg[3]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[4] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(\cont_reg[4]_i_1_n_7 ),
        .Q(cont_reg[4]));
  CARRY4 \cont_reg[4]_i_1 
       (.CI(\cont_reg[0]_i_1_n_0 ),
        .CO({\cont_reg[4]_i_1_n_0 ,\cont_reg[4]_i_1_n_1 ,\cont_reg[4]_i_1_n_2 ,\cont_reg[4]_i_1_n_3 }),
        .CYINIT(1'b0),
        .DI({1'b0,1'b0,1'b0,1'b0}),
        .O({\cont_reg[4]_i_1_n_4 ,\cont_reg[4]_i_1_n_5 ,\cont_reg[4]_i_1_n_6 ,\cont_reg[4]_i_1_n_7 }),
        .S({\cont[4]_i_2_n_0 ,\cont[4]_i_3_n_0 ,\cont[4]_i_4_n_0 ,\cont[4]_i_5_n_0 }));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[5] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(\cont_reg[4]_i_1_n_6 ),
        .Q(cont_reg[5]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[6] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(\cont_reg[4]_i_1_n_5 ),
        .Q(cont_reg[6]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[7] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(\cont_reg[4]_i_1_n_4 ),
        .Q(cont_reg[7]));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[8] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(\cont_reg[8]_i_1_n_7 ),
        .Q(cont_reg[8]));
  CARRY4 \cont_reg[8]_i_1 
       (.CI(\cont_reg[4]_i_1_n_0 ),
        .CO({\cont_reg[8]_i_1_n_0 ,\cont_reg[8]_i_1_n_1 ,\cont_reg[8]_i_1_n_2 ,\cont_reg[8]_i_1_n_3 }),
        .CYINIT(1'b0),
        .DI({1'b0,1'b0,1'b0,1'b0}),
        .O({\cont_reg[8]_i_1_n_4 ,\cont_reg[8]_i_1_n_5 ,\cont_reg[8]_i_1_n_6 ,\cont_reg[8]_i_1_n_7 }),
        .S({\cont[8]_i_2_n_0 ,\cont[8]_i_3_n_0 ,\cont[8]_i_4_n_0 ,\cont[8]_i_5_n_0 }));
  FDCE #(
    .INIT(1'b0)) 
    \cont_reg[9] 
       (.C(clk),
        .CE(1'b1),
        .CLR(rst),
        .D(\cont_reg[8]_i_1_n_6 ),
        .Q(cont_reg[9]));
endmodule

(* CHECK_LICENSE_TYPE = "design_1_Div_50_50_0_0,Div_50_50,{}" *) (* downgradeipidentifiedwarnings = "yes" *) (* x_core_info = "Div_50_50,Vivado 2017.4.1" *) 
(* NotValidForBitStream *)
module decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix
   (clk,
    rst,
    clk_div);
  (* x_interface_info = "xilinx.com:signal:clock:1.0 clk CLK" *) (* x_interface_parameter = "XIL_INTERFACENAME clk, ASSOCIATED_RESET rst, FREQ_HZ 100000000, PHASE 0.000, CLK_DOMAIN design_1_clk_0" *) input clk;
  (* x_interface_info = "xilinx.com:signal:reset:1.0 rst RST" *) (* x_interface_parameter = "XIL_INTERFACENAME rst, POLARITY ACTIVE_LOW" *) input rst;
  output clk_div;

  wire clk;
  wire clk_div;
  wire rst;

  decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix_Div_50_50 U0
       (.clk(clk),
        .clk_div(clk_div),
        .rst(rst));
endmodule
`ifndef GLBL
`define GLBL
`timescale  1 ps / 1 ps

module glbl ();

    parameter ROC_WIDTH = 100000;
    parameter TOC_WIDTH = 0;

//--------   STARTUP Globals --------------
    wire GSR;
    wire GTS;
    wire GWE;
    wire PRLD;
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

endmodule
`endif
