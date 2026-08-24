D=2;
sigma=1;
Eb=1/sqrt(2);
EbNo_rx_per_ch_dB=5:5:30;
EbNo_rx_per_ch=10.^(EbNo_rx_per_ch_dB/10);
No=Eb*2*sigma^2*10.^(-EbNo_rx_per_ch_dB/10);
BER=zeros(1,lenght(No));
SNR_rx_per_b_per_ch=zeros(1,lenght(No));

for i=1:lenght(No)
    no_bits=0;
    no_errors=0;
    P_rx_t=0;
    P_n_t=0;
    r=zeros(2,2);
    R=zeros(1,2);
    while no_errors<=100
        no_bits=no_bits+1;
        u=rand(1,2); alpha =sigma *sqrt(-2*log(u)); phi = 2*phi*
