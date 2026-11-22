## UniversidadAutónomadeZacatecas

## łFranciscoGarcíaSalinasž

## UnidadAcadémicadeIngenieríaEléctrica

## ManualdePrácticas

## TecnologíasCelulares

## Dr.VíktorIvánRodríguezAbdalá

## 28deseptiembrede2026

TecnologíasCelulares

ManualdePrácticas

## Índice

1.Introducción

7

2.ObjetivosGenerales

7

3.EquipoRequerido

7

4.ConőguracióndelRTL-SDRenMATLAB

8

5.Práctica 1. Exploración de redes celulares utilizando RTL-SDR y MATLAB

9 5.1.ObjetivoGeneral.................................

9 5.2.ObjetivosEspecíőcos...............................

9 5.3.Introducción....................................

9 5.4.FundamentoTeórico

...............................

9 5.5.MaterialyEquipo .................................

10 5.6.Procedimiento...................................

10 5.6.1.

Conőguracióndelreceptor........................

10 5.6.2.

Capturademuestras...........................

10 5.6.3.

Obtencióndelespectro..........................

11 5.6.4.

Espectrograma

..............................

11 5.7.ExploracióndeBandas..............................

11 5.8.RegistroExperimental..............................

12 5.9.ResultadosEsperados...............................

12 5.10. AnálisisdeResultados..............................

12 5.11. Cuestionario....................................

13 5.12. Entregables

....................................

13

6.Práctica2.Generaciónyanálisisdesecuenciaspseudoaleatorias(PN)

14 6.1.ObjetivoGeneral.................................

14 6.2.ObjetivosEspecíőcos...............................

14 6.3.Introducción....................................

14 6.4.FundamentoTeórico

...............................

14 6.5.MaterialyEquipo .................................

15 6.6.GeneracióndeunaSecuenciaPN

........................

15 6.7.ConversiónBipolar................................

15 6.8.Histograma

....................................

16 6.9.Autocorrelación..................................

16 6.10. CorrelaciónCruzada

...............................

16 6.11. PropiedadesdeBalance

.............................

17 6.12. LongituddeSecuencia..............................

17 6.13. ResultadosEsperados...............................

18 6.14. AnálisisdeResultados..............................

18 6.15. Cuestionario....................................

18 6.16. Entregables

....................................

18

1

TecnologíasCelulares

ManualdePrácticas

7.Práctica3.ImplementacióndeunsistemaDSSS

20 7.1.ObjetivoGeneral.................................

20 7.2.ObjetivosEspecíőcos...............................

20 7.3.Introducción....................................

20 7.4.FundamentoTeórico

...............................

20 7.5.MaterialyEquipo .................................

21 7.6.GeneracióndeDatos...............................

21 7.7.GeneracióndelCódigoPN............................

21 7.8.ProcesodeDispersión

..............................

21 7.9.VisualizaciónTemporal..............................

22 7.10. EspectrodelaSeñal

...............................

22 7.11. CanalAWGN...................................

22 7.12. ProcesodeDesdispersión.............................

22 7.13. Decisión......................................

23 7.14. CálculodeBER..................................

23 7.15. AnálisisparaDistintosValoresdeSNR.....................

23 7.16. ResultadosEsperados...............................

24 7.17. AnálisisdeResultados..............................

24 7.18. Cuestionario....................................

24 7.19. Entregables

....................................

24

8.Práctica4.ImplementacióndeunsistemaFHSS

25 8.1.ObjetivoGeneral.................................

25 8.2.ObjetivosEspecíőcos...............................

25 8.3.Introducción....................................

25 8.4.FundamentoTeórico

...............................

25 8.5.MaterialyEquipo .................................

26 8.6.GeneracióndeDatos...............................

26 8.7.DeőnicióndeFrecuenciasdeSalto........................

26 8.8.GeneracióndelaSecuenciadeSalto.......................

26 8.9.RepresentaciónTemporal.............................

27 8.10. CanalconInterferencia..............................

27 8.11. VisualizacióndeInterferencia

..........................

27 8.12. Detección

.....................................

28 8.13. CálculodeBER..................................

28 8.14. ComparaciónconSistemaConvencional .....................

28 8.15. ProbabilidaddeError

..............................

28 8.16. ResultadosEsperados...............................

29 8.17. AnálisisdeResultados..............................

29 8.18. Cuestionario....................................

29 8.19. Entregables

....................................

30

2

TecnologíasCelulares

ManualdePrácticas

9.Práctica5.GeneracióndeunaseñalOFDM

31 9.1.ObjetivoGeneral.................................

31 9.2.ObjetivosEspecíőcos...............................

31 9.3.Introducción....................................

31 9.4.FundamentoTeórico

...............................

31 9.5.MaterialyEquipo .................................

32 9.6.GeneracióndeBits................................

32 9.7.ModulaciónQPSK

................................

32 9.8.AsignacióndeSubportadoras

..........................

32 9.9.GeneracióndelaSeñalOFDM..........................

33 9.10. ConversiónSerie-Paralelo.............................

33 9.11. VisualizaciónTemporal..............................

33 9.12. ConstelaciónQPSK................................

33 9.13. EspectroOFDM

.................................

34 9.14. VisualizacióndeSubportadoras.........................

34 9.15. AnálisisdeOrtogonalidad

............................

34 9.16. ResultadosEsperados...............................

35 9.17. AnálisisdeResultados..............................

35 9.18. Cuestionario....................................

35 9.19. Entregables

....................................

35

10.Práctica6.DemodulacióndeseñalesOFDM

36 10.1. ObjetivoGeneral.................................

36 10.2. ObjetivosEspecíőcos...............................

36 10.3. Introducción....................................

36 10.4. FundamentoTeórico

...............................

36 10.5. MaterialyEquipo .................................

37 10.6. GeneracióndeDatos...............................

37 10.7. ModulaciónQPSK

................................

37 10.8. GeneraciónOFDM................................

37 10.9. CanalAWGN...................................

37 10.10.ConversiónSerie-Paralelo.............................

38 10.11.DemodulaciónOFDM

..............................

38 10.12.ConstelaciónRecibida

..............................

38 10.13.DetecciónQPSK

.................................

38 10.14.CálculodeBER..................................

39 10.15.CurvaBERvsSNR................................

39 10.16.GráőcaBER ....................................

39 10.17.ResultadosEsperados...............................

40 10.18.AnálisisdeResultados..............................

40 10.19.Cuestionario....................................

40 10.20.Entregables

....................................

41

3

TecnologíasCelulares

ManualdePrácticas

11.Práctica7.Usodelpreőjocíclicoparaeliminarladispersióndelcanal

42 11.1. ObjetivoGeneral.................................

42 11.2. ObjetivosEspecíőcos...............................

42 11.3. Introducción....................................

42 11.4. FundamentoTeórico

...............................

42 11.5. MaterialyEquipo .................................

43 11.6. GeneracióndeDatos...............................

43 11.7. ModulaciónQPSK

................................

43 11.8. GeneraciónOFDM................................

43 11.9. CanalMultitrayectoria..............................

43 11.10.Caso1.SinPreőjoCíclico............................

43 11.11.Recepción.....................................

44 11.12.Detección

.....................................

44 11.13.BERSinPreőjo..................................

44 11.14.Caso2.ConPreőjoCíclico............................

44 11.15.Transmisión....................................

45 11.16.Recepción.....................................

45 11.17.Detección

.....................................

45 11.18.BERConPreőjo

.................................

46 11.19.ComparacióndeResultados

...........................

46 11.20.ConstelaciónRecibida

..............................

46 11.21.ResultadosEsperados...............................

46 11.22.AnálisisdeResultados..............................

47 11.23.Cuestionario....................................

47 11.24.Entregables

....................................

47

12.Práctica8.RelacióndepotenciapicoapromedioensistemasOFDM

48 12.1. ObjetivoGeneral.................................

48 12.2. ObjetivosEspecíőcos...............................

48 12.3. Introducción....................................

48 12.4. FundamentoTeórico

...............................

48 12.5. MaterialyEquipo .................................

49 12.6. GeneracióndeDatos...............................

49 12.7. ModulaciónQPSK

................................

49 12.8. GeneraciónOFDM................................

49 12.9. VisualizaciónTemporal..............................

49 12.10.PotenciaInstantánea...............................

50 12.11.CálculodePAPR.................................

50 12.12.ComparaciónparaDiferentesNúmerosdeSubportadoras...........

50 12.13.GráőcadePAPR.................................

51 12.14.CCDFdelaPAPR................................

51 12.15.ResultadosEsperados...............................

52 12.16.AnálisisdeResultados..............................

53 12.17.Cuestionario....................................

53 12.18.Entregables

....................................

53

4

TecnologíasCelulares

ManualdePrácticas

13.Práctica9.ModeladodecanalesMIMOycapacidaddesistemasdeantena múltiple

54 13.1. ObjetivoGeneral.................................

54 13.2. ObjetivosEspecíőcos...............................

54 13.3. Introducción....................................

54 13.4. FundamentoTeórico

...............................

54 13.5. MaterialyEquipo .................................

55 13.6. GeneracióndeunCanalMIMO2x2.......................

55 13.7. CálculodeCapacidad...............................

55 13.8. CapacidaddeunSistemaSISO

.........................

56 13.9. CapacidadversusSNR..............................

56 13.10.GráőcadeCapacidad...............................

56 13.11.ComparacióndeConőguraciones

........................

57 13.12.DistribucióndeValoresSingulares........................

57 13.13.ResultadosEsperados...............................

58 13.14.AnálisisdeResultados..............................

58 13.15.Cuestionario....................................

58 13.16.Entregables

....................................

58

14.Práctica10.DeteccióndesímbolosensistemasMIMOutilizandoZFy MMSE

59 14.1. ObjetivoGeneral.................................

59 14.2. ObjetivosEspecíőcos...............................

59 14.3. Introducción....................................

59 14.4. FundamentoTeórico

...............................

59 14.5. MaterialyEquipo .................................

60 14.6. ParámetrosdeSimulación

............................

60 14.7. GeneracióndeBits................................

60 14.8. AgrupaciónporAntenas.............................

60 14.9. CanalMIMO

...................................

61 14.10.Transmisión....................................

61 14.11.Ruido

.......................................

61 14.12.DetectorZF....................................

61 14.13.BERparaZF...................................

61 14.14.DetectorMMSE..................................

62 14.15.BERparaMMSE.................................

62 14.16.ComparaciónparaDistintosValoresdeSNR..................

62 14.17.GráőcaBER ....................................

62 14.18.ConstelacionesRecuperadas...........................

63 14.19.ResultadosEsperados...............................

63 14.20.AnálisisdeResultados..............................

63 14.21.Cuestionario....................................

64 14.22.Entregables

....................................

64

5

TecnologíasCelulares

ManualdePrácticas

15.Práctica11.CódigoEspacio-TiempodeAlamoutiparasistemasMIMO

65 15.1. ObjetivoGeneral.................................

65 15.2. ObjetivosEspecíőcos...............................

65 15.3. Introducción....................................

65 15.4. FundamentoTeórico

...............................

65 15.5. MaterialyEquipo .................................

66 15.6. GeneracióndeDatos...............................

66 15.7. AgrupacióndeSímbolos

.............................

66 15.8. CodiőcaciónAlamouti

..............................

66 15.9. CanalRayleigh

..................................

66 15.10.Transmisión....................................

67 15.11.AdicióndeRuido.................................

67 15.12.DecodiőcaciónAlamouti.............................

67 15.13.Detección

.....................................

68 15.14.BER........................................

68 15.15.ComparaciónconSistemaSISO.........................

68 15.16.GráőcaBER ....................................

69 15.17.ResultadosEsperados...............................

69 15.18.AnálisisdeResultados..............................

70 15.19.Cuestionario....................................

70 15.20.Entregables

....................................

70

16.Práctica12.Proyectointegrador:caracterizaciónexperimentaldeunared LTEutilizandoRTL-SDRyMATLAB

71 16.1. ObjetivoGeneral.................................

71 16.2. ObjetivosEspecíőcos...............................

71 16.3. Introducción....................................

71 16.4. FundamentoTeórico

...............................

71 16.5. MaterialyEquipo .................................

72 16.6. EscenariosdeMedición..............................

72 16.7. ConőguracióndelReceptor............................

72 16.8. CapturadeDatos.................................

72 16.9. AnálisisEspectral.................................

73 16.10.DensidadEspectraldePotencia.........................

73 16.11.Espectrograma

..................................

73 16.12.EstimacióndePotenciaRecibida

........................

74 16.13.ComparacióndeMediciones...........................

74 16.14.AnálisisOFDM..................................

74 16.15.CapacidadAproximada..............................

74 16.16.ResultadosEsperados...............................

75 16.17.AnálisisdeResultados..............................

75 16.18.ProductoFinal

..................................

75 16.19.EstructuradelReporte..............................

76 16.20.CriteriosdeEvaluación..............................

76

6

TecnologíasCelulares

ManualdePrácticas

## 1.

## Introducción

Lastecnologíascelularesmodernasutilizanunacombinacióndetécnicasavanzadasde modulación,accesomúltiple,espectrodisperso,OFDMysistemasMIMOparaproporcionar serviciosdecomunicacionesdealtacapacidad.

Elpresentemanualtienecomoobjetivocomplementarloscontenidosteóricosdelaasig- naturamedianteactividadesprácticasdesarrolladasutilizandoMATLAByreceptoresRTL- SDR.

Lasprácticaspermitiránestudiarexperimentalmenteaspectosrelacionadoscon:

Redescelulares2G,3Gy4G.

Espectrodisperso.

OFDM.

SistemasMIMO.

CaracterizacióndeseñalesLTE.

## 2.

## ObjetivosGenerales

1.AnalizarseñalescelularesrealesmedianteMATLAByRTL-SDR.

2.ImplementarsistemasDSSSyFHSS.

3.DesarrollartransmisoresyreceptoresOFDM.

4.SimularsistemasMIMO.

5.Relacionarlosconceptosteóricosconseñalesrealespresentesenelespectroradioeléc- trico.

## 3.

## EquipoRequerido

Computadorapersonal.

MATLAB.

CommunicationsToolbox.

SignalProcessingToolbox.

CommunicationsToolboxSupportPackageforRTL-SDRRadio.

RTL-SDRV4.

Antenatelescópica.

7

TecnologíasCelulares

ManualdePrácticas

## 4.

## ConőguracióndelRTL-SDRenMATLAB

VeriőquelainstalacióndelsoporteparaRTL-SDRmediante:

info=sdrinfo(’RTL -SDR’) 1 Sieldispositivoesdetectadocorrectamente,MATLABmostrarálainformacióncorres- pondientealreceptorconectado.

8

TecnologíasCelulares

ManualdePrácticas

## 5.

## Práctica1.Exploraciónderedescelularesutilizando

## RTL-SDRyMATLAB

## 5.1.

## ObjetivoGeneral

Identiőcarycaracterizarseñalesderedescelularespresentesenelentornomediantela adquisiciónyanálisisdeseñalesutilizandounreceptorRTL-SDRyMATLAB.

## 5.2.

## ObjetivosEspecíőcos

Identiőcarbandascelularespresentesenelentorno.

Medirfrecuenciascentralesyanchosdebanda.

Obtenerespectrosdeseñalescelulares.

FamiliarizarseconelusodelRTL-SDRenaplicacionescelulares.

Comparardiferentesportadorasobservadas.

## 5.3.

## Introducción

Lasredescelularesutilizanbandaslicenciadasdelespectroradioeléctricoparaproporcio- narserviciosmóviles.

Dependiendodeloperadorydelageneracióntecnológica,puedenobservarsediferentes portadorasdistribuidasenbandascomo:

700MHz.

850MHz.

1900MHz.

AWS.

2.6GHz.

Estasseñalespresentananchosdebandaconsiderablementemayoresquelosservicios convencionalesderadioyconstituyenejemplosrealesdesistemascelularesmodernos.

## 5.4.

## FundamentoTeórico

Una señal adquirida mediante un receptor SDR se representa mediante muestras comple- jas:

x[n] = I[n] + jQ[n] LaTransformadaDiscretadeFourierpermiteobtenersurepresentaciónespectral:

9

TecnologíasCelulares

ManualdePrácticas

N−1

x[n]e−j2πkn/N

X[k] = 

n=0

Ladensidadespectraldepotenciapermiteidentiőcar:

Frecuenciacentral.

Anchodebanda.

Potenciarelativa.

Otrasseñalespresentesenelentorno.

## 5.5.

## MaterialyEquipo

Computadorapersonal.

MATLAB.

RTL-SDR.

Antena.

## 5.6.

## Procedimiento

5.6.1.

Conőguracióndelreceptor

ConőgureelRTL-SDRparalabandadeinterés.

rx=comm. SDRRTLReceiver ;

1

2

rx. CenterFrequency=850e6;

3

4

rx.SampleRate=2.4e6;

5

6

rx. SamplesPerFrame=262144;

7

8

rx. EnableTunerAGC=true;

9

5.6.2.

Capturademuestras

Adquieraunbloquededatos.

[data ,len]=rx();

1

2

release(rx);

3

10

TecnologíasCelulares

ManualdePrácticas

5.6.3.

Obtencióndelespectro

Fs=rx.SampleRate;

1

2

N=length(data);

3

4

X=fftshift(fft(data));

5

6

f=linspace(-Fs/2,Fs/2,N);

7

8

PSD=20* log10(abs(X));

9

10

figure 11

12

plot(f/1e6 ,PSD) 13

14

gridon 15

16

xlabel(’Frecuencia␣(MHz)’) 17

ylabel(’Magnitud␣(dB)’) 18

19

title(’Espectro␣observado ’) 20

5.6.4.

Espectrograma

figure 1

2

spectrogram(data ,...

3

1024 ,...

4

512 ,...

5

1024 ,...

6

Fs ,...

7

’centered ’) 8

9

title(’Espectrograma ’) 10

colorbar 11

## 5.7.

## ExploracióndeBandas

Repitalasmedicionesparalassiguientesfrecuencias:

11

TecnologíasCelulares

ManualdePrácticas

Tabla1:Bandassugeridasparaexploración.

FrecuenciaCentral

Servicio 700MHz

LTE 850MHz

LTE 1900MHz

LTE/PCS 2100MHz

AWS 2600MHz

LTE

## 5.8.

## RegistroExperimental

Completelasiguientetabla.

Tabla2:Señalesidentiőcadas.

Frecuencia

AnchodeBanda

Potencia

Observaciones

## 5.9.

## ResultadosEsperados

Elestudiantedeberáobtener:

Espectrosdeseñalescelularesreales.

Estimacionesdefrecuenciacentral.

Estimacionesdeanchodebanda.

Comparaciónentrediferentesbandascelulares.

## 5.10.

## AnálisisdeResultados

Discuta:

1.£Québandascelularesfueronidentiőcadas?

2.£Quédiferenciasexistenentrelasseñalesobservadas?

3.£Cuálbandapresentómayorocupaciónespectral?

4.£SeobservaronotrosserviciosademásdeLTE?

12

TecnologíasCelulares

ManualdePrácticas

## 5.11.

## Cuestionario

1.£Quéesunaredcelular?

2.£Quédiferenciaexisteentre2G,3Gy4G?

3.£Porquéseutilizanbandaslicenciadas?

4.£Quéinformaciónpuedeobtenerseapartirdelespectro?

5.£QuélimitacionestieneelRTL-SDRparaanalizarseñalesLTE?

## 5.12.

## Entregables

1.Objetivo.

2.Fundamentoteórico.

3.Desarrolloexperimental.

4.CódigoMATLAB.

5.Capturasespectrales.

6.Tabladeresultados.

7.Respuestasalcuestionario.

8.Conclusiones.

13

TecnologíasCelulares

ManualdePrácticas

## 6.

## Práctica2.Generaciónyanálisisdesecuenciaspseu-

## doaleatorias(PN)

## 6.1.

## ObjetivoGeneral

Generarsecuenciaspseudoaleatoriasutilizandoregistrosdecorrimientoconretroalimen- taciónlineal(LFSR)yanalizarsuspropiedadesdecorrelaciónmedianteMATLAB.

## 6.2.

## ObjetivosEspecíőcos

ComprenderelfuncionamientodeungeneradorLFSR.

GenerarsecuenciasPNdelongitudmáxima.

AnalizarlaspropiedadesestadísticasdelassecuenciasPN.

Obtenerfuncionesdeautocorrelaciónycorrelacióncruzada.

IdentiőcaraplicacionesdelassecuenciasPNensistemascelulares.

## 6.3.

## Introducción

Lassecuenciaspseudoaleatorias(PN)constituyenlabasedelossistemasdeespectro dispersoutilizadosentecnologíascelularesdetercerageneración.

Estassecuenciaspresentanpropiedadessimilaresalasdelruidoaleatorio,aunqueson generadasmedianteprocesosdeterminísticos.

Entresusprincipalesaplicacionesdestacan:

SistemasDSSS.

CDMA.

Sincronización.

Identiőcacióndeusuarios.

Enmascaramientodeseñales.

## 6.4.

## FundamentoTeórico

N= 2m−1 UnasecuenciaPNpuedegenerarseutilizandounRegistrodeCorrimientoconRetroali- mentaciónLineal(LFSR).

Lalongitudmáximadeunasecuenciageneradaconunregistrodemetapases:

(1) Porejemplo:

14

TecnologíasCelulares

ManualdePrácticas

Tabla3:LongituddesecuenciasPN.

m

LongitudN

3

7

4

15

5

31

6

63

7

127

8

255

Una característica importante de las secuencias PN es su función de autocorrelación apro-

ximadamenteimpulsiva.

## 6.5.

## MaterialyEquipo

Computadorapersonal.

MATLAB.

## 6.6.

## GeneracióndeunaSecuenciaPN

ConsidereunLFSRdecincoetapas.

m=5;

1

2

pn=comm.PNSequence(...

3

’Polynomial ’ ,[520],...

4

’SamplesPerFrame ’ ,31);

5

6

x=pn();

7

Visualicelasecuenciaobtenida.

figure 1

2

stem(x,’filled ’) 3

4

gridon 5

6

xlabel(’Indice ’) 7

ylabel(’Valor ’) 8

9

title(’Secuencia␣PN’) 10

## 6.7.

## ConversiónBipolar

Conviertalasecuenciaarepresentaciónbipolar.

15

TecnologíasCelulares

ManualdePrácticas

xb=2*x-1;

1

Veriőquequelasecuenciaúnicamentecontenga:

{−1, +1}

## 6.8.

## Histograma

Obtengaladistribuciónestadística.

figure 1

2

histogram(xb) 3

4

gridon 5

6

title(’Distribucion ␣de␣la␣secuencia␣PN’) 7

## 6.9.

## Autocorrelación

Calculelaautocorrelación.

R=xcorr(xb ,’coeff ’);

1

2

figure 3

4

stem(R) 5

6

gridon 7

8

xlabel(’Retardo ’) 9

ylabel(’Correlacion ’) 10

11

title(’Autocorrelacion ’) 12

Observelapresenciadeunpicodominanteenelorigen.

## 6.10.

## CorrelaciónCruzada

Genereunasegundasecuencia.

pn2=comm.PNSequence(...

1

’Polynomial ’ ,[540],...

2

’SamplesPerFrame ’ ,31);

3

4

y=pn2();

5

6

yb=2*y-1;

7

16

TecnologíasCelulares

ManualdePrácticas

Calculelacorrelacióncruzada.

Rc=xcorr(xb ,yb ,’coeff ’);

1

2

figure 3

4

stem(Rc) 5

6

gridon 7

8

xlabel(’Retardo ’) 9

ylabel(’Correlacion ’) 10

11

title(’Correlacion␣cruzada ’) 12

## 6.11.

## PropiedadesdeBalance

Determinelacantidaddeunosyceros.

Nunos=sum(x);

1

2

Nceros=length(x)-Nunos;

3

Registrelosresultados.

## 6.12.

## LongituddeSecuencia

Repitaelexperimentoutilizando:

m = 4

m = 5

m = 6

m = 7

CompletelaTablasiguiente.

Tabla4:LongituddesecuenciasPN.

m LongitudTeórica

LongitudObservada

4

5

6

7

17

TecnologíasCelulares

ManualdePrácticas

## 6.13.

## ResultadosEsperados

Elestudiantedeberáobtener:

SecuenciasPNdelongitudmáxima.

Funcionesdeautocorrelación.

Funcionesdecorrelacióncruzada.

Veriőcaciónexperimentaldelaspropiedadesestadísticas.

## 6.14.

## AnálisisdeResultados

Discuta:

1.£PorquélassecuenciasPNsonútilesenespectrodisperso?

2.£Quécaracterísticaspresentalaautocorrelación?

3.£PorquélacorrelacióncruzadaesimportanteenCDMA?

4.£Cómocambialalongituddelasecuenciaalaumentarm?

## 6.15.

## Cuestionario

1.£QuéesunasecuenciaPN?

2.£QuéesunLFSR?

3.£Quésigniőcasecuenciadelongitudmáxima?

4.£PorquélassecuenciasPNsondeterminísticasperoparecenaleatorias?

5.£Cuáleslaventajadeunaautocorrelaciónimpulsiva?

6.£PorquéseutilizansecuenciasPNensistemascelulares?

## 6.16.

## Entregables

1.Objetivo.

2.Fundamentoteórico.

3.CódigoMATLAB.

4.Secuenciasgeneradas.

5.Autocorrelación.

6.Correlacióncruzada.

18

TecnologíasCelulares

ManualdePrácticas

7.Tabladeresultados.

8.Respuestasalcuestionario.

9.Conclusiones.

19

TecnologíasCelulares

ManualdePrácticas

## 7.

## Práctica3.ImplementacióndeunsistemaDSSS

## 7.1.

## ObjetivoGeneral

Implementarunsistemadeespectrodispersoporsecuenciadirecta(DSSS)utilizando MATLAByevaluarsudesempeñofrentealruido.

## 7.2.

## ObjetivosEspecíőcos

ImplementaruntransmisorDSSS.

GenerarunasecuenciaPNdedispersión.

Analizarelensanchamientoespectraldelaseñaltransmitida.

Implementarlarecuperacióndedatosmediantecorrelación.

Evaluarelefectodelruidosobrelatransmisión.

## 7.3.

## Introducción

Los sistemas DSSS (Direct Sequence Spread Spectrum) multiplican una señal de informa- ciónporunasecuenciapseudoaleatoriadealtavelocidaddenominadacódigodedispersión.

Elresultadoesunaseñalconunanchodebandaconsiderablementemayorqueeldela señaloriginal.

EstatécnicafueampliamenteutilizadaensistemascelularesCDMAypermite:

Incrementarlainmunidadalruido.

Reducirelefectodeinterferencias.

Permitiraccesomúltiplemediantecódigos.

## 7.4.

## FundamentoTeórico

LaseñalDSSSpuederepresentarsecomo s(t) = b(t)c(t) (2) donde:

b(t)representalainformación.

c(t)representalasecuenciaPN.

Lagananciadeprocesamientoestádeőnidapor Gp=Rc (3) Rb donde:

20

TecnologíasCelulares

ManualdePrácticas

Rceslavelocidaddelcódigo.

Rbeslavelocidaddelosdatos.

## 7.5.

## MaterialyEquipo

Computadorapersonal.

MATLAB.

## 7.6.

## GeneracióndeDatos

Genereunasecuenciabinariaaleatoria.

Nb=100;

1

2

bits=randi ([01],Nb ,1);

3

Conviertaarepresentaciónbipolar.

b=2* bits-1;

1

## 7.7.

## GeneracióndelCódigoPN

GenereunasecuenciaPNdelongitud31.

pn=comm.PNSequence(...

1

’Polynomial ’ ,[520],...

2

’SamplesPerFrame ’ ,31);

3

4

c=pn();

5

6

c=2*c-1;

7

## 7.8.

## ProcesodeDispersión

MultipliquecadasímboloporelcódigoPN.

spreadSignal=[];

1

2

fork=1: length(b) 3

4

spreadSignal=...

5

[spreadSignal;b(k)*c];

6

7

end 8

21

TecnologíasCelulares

ManualdePrácticas

## 7.9.

## VisualizaciónTemporal

figure 1

2

plot(spreadSignal) 3

4

gridon 5

6

xlabel(’Chip ’) 7

ylabel(’Amplitud ’) 8

9

title(’Senal␣DSSS ’) 10

## 7.10.

## EspectrodelaSeñal

Obtengaelespectro.

N=length(spreadSignal );

1

2

X=fftshift(fft(spreadSignal));

3

4

PSD=20* log10(abs(X));

5

6

figure 7

8

plot(PSD) 9

10

gridon 11

12

title(’Espectro␣de␣la␣senal␣DSSS ’) 13

Compareconelespectrodelaseñaloriginal.

## 7.11.

## CanalAWGN

Incorporeruidogaussiano.

EbN0=5;

1

2

rx=awgn(spreadSignal ,...

3

EbN0 ,...

4

’measured ’);

5

## 7.12.

## ProcesodeDesdispersión

Recuperelosdatosoriginales.

22

TecnologíasCelulares

ManualdePrácticas

bitsRx=[];

1

2

fork=1:Nb 3

4

inicio=(k-1) *31+1;

5

6

fin=k*31;

7

8

bloque=rx(inicio:fin);

9

10

z=sum(bloque .*c);

11

12

bitsRx=[bitsRx;z];

13

14

end 15

## 7.13.

## Decisión

bitsHat=bitsRx>0;

1

## 7.14.

## CálculodeBER

BER=sum(bits~=bitsHat)/Nb 1

## 7.15.

## AnálisisparaDistintosValoresdeSNR

Repitalasimulaciónpara:

0,2,4,6,8y10dB

Completelasiguientetabla.

Tabla5:DesempeñodelsistemaDSSS.

Eb/N0(dB)

BER

0

2

4

6

8

10

23

TecnologíasCelulares

ManualdePrácticas

## 7.16.

## ResultadosEsperados

Elestudiantedeberáobservar:

Ensanchamientoespectral.

Recuperacióncorrectadelosdatos.

DisminucióndelaBERalaumentarlaSNR.

GananciadeprocesamientoproporcionadaporDSSS.

## 7.17.

## AnálisisdeResultados

Discuta:

1.£Cómocambiaelespectrodespuésdelprocesodedispersión?

2.£CuáleslafuncióndelcódigoPN?

3.£Porquéserecuperanlosdatosmediantecorrelación?

4.£Quéocurrecuandoaumentalalongituddelcódigo?

## 7.18.

## Cuestionario

1.£QuéesDSSS?

2.£Quéeslagananciadeprocesamiento?

3.£PorquéDSSSofreceinmunidadalruido?

4.£QuéaplicacionestuvoDSSSensistemascelulares?

5.£CuálesladiferenciaentreDSSSyFHSS?

## 7.19.

## Entregables

1.Objetivo.

2.Fundamentoteórico.

3.CódigoMATLAB.

4.Señaldispersada.

5.Espectroobtenido.

6.ResultadosBER.

7.Tabladeresultados.

8.Respuestasalcuestionario.

9.Conclusiones.

24

TecnologíasCelulares

ManualdePrácticas

## 8.

## Práctica4.ImplementacióndeunsistemaFHSS

## 8.1.

## ObjetivoGeneral

Implementarunsistemadeespectrodispersoporsaltoenfrecuencia(FHSS)utilizando MATLAByanalizarsudesempeñoenpresenciadeinterferencia.

## 8.2.

## ObjetivosEspecíőcos

ImplementarunsistemaFHSS.

Generarsecuenciasdesaltopseudoaleatorias.

AnalizarelcomportamientoespectraldelasseñalesFHSS.

Comparareldesempeñoconunatransmisiónconvencional.

Evaluarelefectodeinterferenciasdebandaparcial.

## 8.3.

## Introducción

LossistemasFHSS(FrequencyHoppingSpreadSpectrum)transmitenlainformaciónuti- lizandounasecuenciapseudoaleatoriadefrecuenciasportadoras.

Durante la transmisión, la frecuencia cambia periódicamente siguiendo un patrón conocido tantoporeltransmisorcomoporelreceptor.

Estatécnicapresentaventajasimportantes:

Robustezfrenteainterferencias.

Mayorresistenciaalbloqueodefrecuencia.

Bajaprobabilidaddeinterceptación.

Diversidadenfrecuencia.

FHSSfueutilizadoenBluetoothclásicoyendiversossistemasmilitaresydecomunica- cionesseguras.

## 8.4.

## FundamentoTeórico

SiexistenMfrecuenciasdisponibles:

f1, f2, . . . , fM lasecuenciadesaltoseleccionaunafrecuenciaparacadasímbolotransmitido.

UnasecuenciaFHpuederepresentarsecomo:

fh(k) = fm(k) donde:

25

TecnologíasCelulares

ManualdePrácticas

m(k)eselíndicegeneradoporunasecuenciaPN.

fh(k)eslafrecuenciautilizadaduranteelsaltok.

Ladiversidadenfrecuenciapermitereducirelimpactodeinterferenciaslocalizadas.

## 8.5.

## MaterialyEquipo

Computadorapersonal.

MATLAB.

## 8.6.

## GeneracióndeDatos

Genereunasecuenciabinariaaleatoria.

Nb=200;

1

2

bits=randi ([01],Nb ,1);

3

4

b=2* bits-1;

5

## 8.7.

## DeőnicióndeFrecuenciasdeSalto

Deőnaochocanalesposibles.

f=[12345678];

1

## 8.8.

## GeneracióndelaSecuenciadeSalto

Genereunasecuenciapseudoaleatoria.

hops=randi ([18],Nb ,1);

1

Visualicelasecuencia.

figure 1

2

stairs(hops) 3

4

gridon 5

6

xlabel(’Simbolo ’) 7

ylabel(’Canal ’) 8

9

title(’Secuencia␣FH’) 10

26

TecnologíasCelulares

ManualdePrácticas

## 8.9.

## RepresentaciónTemporal

ConstruyaunarepresentaciónsimpliőcadadelsistemaFHSS.

fhSignal=hops.*b;

1

Graőquelaseñal.

figure 1

2

stairs(fhSignal) 3

4

gridon 5

6

xlabel(’Simbolo ’) 7

ylabel(’Frecuencia␣seleccionada ’) 8

9

title(’Transmision␣FHSS ’) 10

## 8.10.

## CanalconInterferencia

Introduzcainterferenciaenunapartedelespectro.

Supongaqueelcanal4presentainterferenciaintensa.

rx=fhSignal;

1

2

interferencia=(hops==4);

3

4

rx(interferencia)=...

5

rx(interferencia)+8* randn(...

6

sum( interferencia ) ,1);

7

## 8.11.

## VisualizacióndeInterferencia

figure 1

2

plot(rx) 3

4

gridon 5

6

xlabel(’Simbolo ’) 7

ylabel(’Amplitud ’) 8

9

title(’Senal␣afectada␣por␣interferencia ’) 10

27

TecnologíasCelulares

ManualdePrácticas

## 8.12.

## Detección

Realiceunadetecciónsimple.

bitsHat=sign(rx);

1

2

bitsHat(bitsHat <0) =0;

3

4

bitsHat(bitsHat >0) =1;

5

## 8.13.

## CálculodeBER

BER=...

1

sum(bits~=bitsHat)/Nb 2

## 8.14.

## ComparaciónconSistemaConvencional

GenereunatransmisiónsinFHSS.

x=b;

1

2

x( interferencia )=...

3

x( interferencia )+...

4

8* randn(...

5

sum( interferencia ) ,1);

6

7

bitsHat2=sign(x);

8

9

bitsHat2(bitsHat2 <0) =0;

10

11

bitsHat2(bitsHat2 >0) =1;

12

13

BERconv=...

14

sum(bits~=bitsHat2)/Nb 15

Compare:

BERdelsistemaFHSS.

BERdelsistemaconvencional.

## 8.15.

## ProbabilidaddeError

Repitaelexperimentoparadiferentesnivelesdeinterferencia:

AI= 2,4,6,8,10

Obtengalasiguientetabla.

28

TecnologíasCelulares

ManualdePrácticas

Tabla6:Desempeñofrenteainterferencia.

Interferencia

BERFHSS

BERConvencional 2 4 6 8 10

## 8.16.

## ResultadosEsperados

Elestudiantedeberáobservar:

Secuenciasdesaltopseudoaleatorias.

RobustezdelsistemaFHSS.

Menordegradaciónanteinterferencialocalizada.

Beneőciodeladiversidadenfrecuencia.

## 8.17.

## AnálisisdeResultados

Discuta:

1.£Cómoafectalainterferenciaacadasistema?

2.£PorquéFHSSesmásrobusto?

3.£Quéocurresiseincrementaelnúmerodefrecuenciasdisponibles?

4.£Cómoinŕuyelasecuenciadesaltoeneldesempeño?

## 8.18.

## Cuestionario

1.£QuéesFHSS?

2.£CuáleslaprincipaldiferenciaentreFHSSyDSSS?

3.£Quépapeldesempeñalasecuenciapseudoaleatoria?

4.£PorquéFHSSproporcionadiversidadenfrecuencia?

5.£QuéaplicacionescomercialesutilizanFHSS?

29

TecnologíasCelulares

ManualdePrácticas

## 8.19.

## Entregables

1.Objetivo.

2.Fundamentoteórico.

3.CódigoMATLAB.

4.Secuenciadesaltogenerada.

5.ResultadosBER.

6.ComparaciónFHSSvsconvencional.

7.Tabladeresultados.

8.Respuestasalcuestionario.

9.Conclusiones.

30

TecnologíasCelulares

ManualdePrácticas

## 9.

## Práctica5.GeneracióndeunaseñalOFDM

## 9.1.

## ObjetivoGeneral

Implementar un transmisor OFDM en MATLAB y analizar las características temporales yespectralesdelaseñalgenerada.

## 9.2.

## ObjetivosEspecíőcos

Comprenderelprincipiodemodulaciónmultiportadora.

ImplementaruntransmisorOFDMbasadoenIFFT.

Analizarlaortogonalidadentresubportadoras.

ObtenerlaseñalOFDMeneldominiodeltiempo.

Visualizarelespectrodelaseñaltransmitida.

## 9.3.

## Introducción

OrthogonalFrequencyDivisionMultiplexing(OFDM)eslatécnicadetransmisiónutili- zadaensistemasmodernoscomo:

LTE.

WiFi.

DVB-T.

WiMAX.

5GNR.

OFDMdivideunŕujodedatosdealtavelocidadenmúltiplesŕujosparalelosdemenor tasa,transmitidossimultáneamentemediantesubportadorasortogonales.

Laortogonalidadpermitequelassubportadorassesuperponganespectralmentesinpro- ducirinterferenciaentreellas.

## 9.4.

## FundamentoTeórico

N−1 UnaseñalOFDMestáformadaporlasumadeNsubportadoras:

Xkej2πkt/T s(t) =  (4) k=0 donde:

Xkrepresentaelsímbolotransmitidoenlasubportadorak.

31

TecnologíasCelulares

ManualdePrácticas

Nrepresentaelnúmerodesubportadoras.

TrepresentaladuracióndelsímboloOFDM.

N−1

LaimplementaciónprácticaserealizamedianteunaIFFT:

x[n] =1

Xkej2πkn/N  (5)

N

k=0

## 9.5.

## MaterialyEquipo

Computadorapersonal.

MATLAB.

## 9.6.

## GeneracióndeBits

Genereunasecuenciabinariaaleatoria.

Nb=1024;

1

2

bits=randi ([01],Nb ,1);

3

## 9.7.

## ModulaciónQPSK

ConviertalosbitsasímbolosQPSK.

bits2=reshape(bits ,2 ,[]) ’;

1

2

sym=(2* bits2 (: ,1) -1)+...

3

1j*(2* bits2 (: ,2) -1);

4

5

sym=sym/sqrt (2);

6

## 9.8.

## AsignacióndeSubportadoras

Considere:

N= 64

subportadorasOFDM.

Nfft=64;

1

Organicelossímbolos.

X=reshape(sym ,...

1

Nfft ,...

2

[]);

3

32

TecnologíasCelulares

ManualdePrácticas

## 9.9.

## GeneracióndelaSeñalOFDM

ObtengacadasímboloOFDMmedianteIFFT.

x=ifft(X,Nfft);

1

## 9.10.

## ConversiónSerie-Paralelo

Obtengalaseñaltransmitida.

tx=x(:);

1

## 9.11.

## VisualizaciónTemporal

Graőquelaparterealdelaseñal.

figure 1

2

plot(real(tx)) 3

4

gridon 5

6

xlabel(’Muestra ’) 7

ylabel(’Amplitud ’) 8

9

title(’Senal␣OFDM ’) 10

## 9.12.

## ConstelaciónQPSK

Visualicelossímbolostransmitidos.

figure 1

2

plot(real(sym) ,...

3

imag(sym),’.’) 4

5

gridon 6

7

axissquare 8

9

xlabel(’I’) 10

ylabel(’Q’) 11

12

title(’Constelacion ␣QPSK ’) 13

33

TecnologíasCelulares

ManualdePrácticas

## 9.13.

## EspectroOFDM

Obtengaelespectrodelaseñal.

N=length(tx);

1

2

Xf=fftshift(fft(tx));

3

4

PSD=20* log10(abs(Xf));

5

6

figure 7

8

plot(PSD) 9

10

gridon 11

12

title(’Espectro␣OFDM ’) 13

xlabel(’Frecuencia ’) 14

ylabel(’Magnitud␣(dB)’) 15

## 9.14.

## VisualizacióndeSubportadoras

Observelassubportadorasutilizadas.

figure 1

2

stem(abs(X(: ,1))) 3

4

gridon 5

6

xlabel(’Subportadora ’) 7

ylabel(’Magnitud ’) 8

9

title(’Simbolo␣OFDM ’) 10

## 9.15.

## AnálisisdeOrtogonalidad

Seleccionedossubportadorasconsecutivas.

n=0:Nfft -1;

1

2

s1=exp(1j*2*pi*5*n/Nfft);

3

4

s2=exp(1j*2*pi*6*n/Nfft);

5

6

producto=sum(s1.* conj(s2)) 7

Veriőquequeelproductointernoseacercanoacero.

34

TecnologíasCelulares

ManualdePrácticas

## 9.16.

## ResultadosEsperados

Elestudiantedeberáobtener:

SeñalesOFDMgeneradasmedianteIFFT.

ConstelaciónQPSK.

EspectroOFDM.

Veriőcacióndeortogonalidad.

## 9.17.

## AnálisisdeResultados

Discuta:

1.£Porquélassubportadorasnointerőerenentresí?

2.£CuáleslafuncióndelaIFFT?

3.£QuédiferenciasexistenentreOFDMyunatransmisiónmonocanal?

4.£Cómocambiaelespectroalaumentarelnúmerodesubportadoras?

## 9.18.

## Cuestionario

1.£QuéesOFDM?

2.£Porquéseutilizansubportadorasortogonales?

3.£CuáleslafuncióndelaIFFT?

4.£QuéventajasofreceOFDMencanalesselectivosenfrecuencia?

5.£QuétecnologíasutilizanOFDMactualmente?

## 9.19.

## Entregables

1.Objetivo.

2.Fundamentoteórico.

3.CódigoMATLAB.

4.SeñalOFDMgenerada.

5.ConstelaciónQPSK.

6.EspectroOFDM.

7.Veriőcacióndeortogonalidad.

8.Respuestasalcuestionario.

9.Conclusiones.

35

TecnologíasCelulares

ManualdePrácticas

## 10.

## Práctica6.DemodulacióndeseñalesOFDM

## 10.1.

## ObjetivoGeneral

ImplementarunreceptorOFDMenMATLABpararecuperarinformacióntransmitida mediante un sistema multiportadora y evaluar su desempeño mediante la tasa de error de bit (BER).

## 10.2.

## ObjetivosEspecíőcos

ImplementarlarecepcióndesímbolosOFDM.

RecuperarlassubportadorasmedianteFFT.

RealizarlademodulaciónQPSK.

CalcularlaBERdelsistema.

AnalizarelefectodelruidosobrelatransmisiónOFDM.

## 10.3.

## Introducción

EnunsistemaOFDM,lainformacióntransmitidaenmúltiplessubportadorasdeberecu- perarseenelreceptormedianteunaFFT.

LaFFTpermitesepararlassubportadorasortogonalesyrecuperarlossímbolostransmi- tidos.

Eldesempeñodelsistemasueleevaluarsemediantelatasadeerrordebit(BER)para distintosvaloresderelaciónseñalaruido.

## 10.4.

## FundamentoTeórico

ElreceptorOFDMrealizalassiguientesoperaciones:

r[n] →FFT→Xk→Deteccin →Bits N−1 r[n]e−j2πkn/N LaFFTsedeőnecomo

X[k] =  n=0 Latasadeerrordebitsecalculamediante

BER =Ne Nb

donde:

Neeselnúmerodebitserróneos.

Nbeseltotaldebitstransmitidos.

36

TecnologíasCelulares

ManualdePrácticas

## 10.5.

## MaterialyEquipo

Computadorapersonal.

MATLAB.

## 10.6.

## GeneracióndeDatos

Nb=4096;

1

2

bits=randi ([01],Nb ,1);

3

## 10.7.

## ModulaciónQPSK

bits2=reshape(bits ,2 ,[]) ’;

1

2

sym=(2* bits2 (: ,1) -1)+...

3

1j*(2* bits2 (: ,2) -1);

4

5

sym=sym/sqrt (2);

6

## 10.8.

## GeneraciónOFDM

Nfft=64;

1

2

X=reshape(sym ,Nfft ,[]);

3

4

tx=ifft(X,Nfft);

5

6

tx=tx(:);

7

## 10.9.

## CanalAWGN

Seleccioneinicialmente:

Eb/N0= 10dB

EbN0=10;

1

2

rx=awgn(tx ,EbN0 ,’measured ’);

3

37

TecnologíasCelulares

ManualdePrácticas

## 10.10.

## ConversiónSerie-Paralelo

rxMatrix=reshape(rx ,...

1

Nfft ,...

2

[]);

3

## 10.11.

## DemodulaciónOFDM

ApliqueFFT.

Y=fft(rxMatrix ,Nfft);

1

Obtengalossímbolosrecibidos.

symRx=Y(:);

1

## 10.12.

## ConstelaciónRecibida

figure 1

2

plot(real(symRx) ,...

3

imag(symRx),’.’) 4

5

gridon 6

7

axissquare 8

9

xlabel(’I’) 10

ylabel(’Q’) 11

12

title(’Constelacion ␣recibida ’) 13

## 10.13.

## DetecciónQPSK

bitsHat=zeros(Nb ,1);

1

2

bitsHat (1:2: end)=...

3

real(symRx) >0;

4

5

bitsHat (2:2: end)=...

6

imag(symRx) >0;

7

38

TecnologíasCelulares

ManualdePrácticas

## 10.14.

## CálculodeBER

BER=...

1

sum(bits~=bitsHat)...

2

/Nb 3

## 10.15.

## CurvaBERvsSNR

Evalúe:

Eb/N0= 0, 2, 4, 6, 8, 10, 12, 14

EbN0dB=0:2:14;

1

2

BER=zeros(size(EbN0dB));

3

4

fork=1: length(EbN0dB) 5

6

rx=awgn(tx ,...

7

EbN0dB(k) ,...

8

’measured ’);

9

10

rxMatrix=...

11

reshape(rx ,Nfft ,[]);

12

13

Y=fft(rxMatrix ,Nfft);

14

15

symRx=Y(:);

16

17

bitsHat=zeros(Nb ,1);

18

19

bitsHat (1:2: end)=...

20

real(symRx) >0;

21

22

bitsHat (2:2: end)=...

23

imag(symRx) >0;

24

25

BER(k)=...

26

sum(bits ~= bitsHat)/Nb;

27

28

end 29

## 10.16.

## GráőcaBER

figure 1

2

39

TecnologíasCelulares

ManualdePrácticas

semilogy(EbN0dB ,...

3 BER ,...

4 ’o-’) 5 6 gridon 7 8 xlabel(’E_b/N_0␣(dB)’) 9 ylabel(’BER’) 10 11 title(’BER␣de␣sistema␣OFDM ’) 12

## 10.17.

## ResultadosEsperados

Elestudiantedeberáobtener:

Recuperacióncorrectadelossímbolostransmitidos.

ConstelacionesOFDMrecibidas.

BERparadiferentesSNR.

Curvasdedesempeñodelsistema.

## 10.18.

## AnálisisdeResultados

Discuta:

1.£Cómoafectaelruidoalaconstelación?

2.£QuéocurreconlaBERalincrementarlaSNR?

3.£PorquélaFFTpermitesepararlassubportadoras?

4.£Quédiferenciasexistiríansilassubportadorasnofueranortogonales?

## 10.19.

## Cuestionario

1.£CuáleslafuncióndelaFFTenunreceptorOFDM?

2.£QuérepresentalaBER?

3.£PorquéOFDMutilizamúltiplessubportadoras?

4.£CómoseinterpretaunaconstelaciónQPSKrecibida?

5.£QuéfactoreslimitaneldesempeñodeunsistemaOFDM?

40

TecnologíasCelulares

ManualdePrácticas

## 10.20.

## Entregables

1.Objetivo.

2.Fundamentoteórico.

3.CódigoMATLAB.

4.Constelaciónrecibida.

5.CálculodeBER.

6.CurvaBERvsSNR.

7.Respuestasalcuestionario.

8.Conclusiones.

41

TecnologíasCelulares

ManualdePrácticas

## 11.

## Práctica7.Usodelpreőjocíclicoparaeliminarla

## dispersióndelcanal

## 11.1.

## ObjetivoGeneral

Analizarelefectodeladispersióntemporalproducidaporuncanalmultitrayectoria sobreseñalesOFDMeimplementarelusodelpreőjocíclicoparamitigarlainterferencia entresímbolos.

## 11.2.

## ObjetivosEspecíőcos

Modelaruncanalmultitrayectoria.

Analizarlainterferenciaentresímbolos(ISI).

ImplementarelpreőjocíclicoenunsistemaOFDM.

Comparareldesempeñoconysinpreőjocíclico.

Evaluarlatasadeerrordebitenamboscasos.

## 11.3.

## Introducción

Loscanalesinalámbricospresentanmúltiplestrayectoriasdepropagacióndebidoala reŕexión,difracciónydispersióndelasondaselectromagnéticas.

Estastrayectoriasproducendiferentesretardosquepuedengenerarinterferenciaentre símbolosconsecutivos.

OFDMcombateesteproblemaagregandounpreőjocíclicoaliniciodecadasímbolo transmitido.

Elpreőjocíclicotransformalaconvoluciónlinealdelcanalenunaconvolucióncircular, permitiendoquelaFFTrecuperecorrectamentelainformacióntransmitida.

## 11.4.

## FundamentoTeórico

LaseñalOFDMtransmitidapuederepresentarsecomo

x[n] = IFFT{X[k]}

ElpreőjocíclicoseconstruyecopiandolasúltimasmuestrasdelsímboloOFDMalinicio L−1 delmismo.

Sielcanaltieneunarespuestaimpulsional

h[n] =

hlδ[n −l]  l=0 lalongituddelpreőjocíclicodebeseralmenosigualalmáximoretardopresenteenel canal.

42

TecnologíasCelulares

ManualdePrácticas

## 11.5.

## MaterialyEquipo

Computadorapersonal.

MATLAB.

## 11.6.

## GeneracióndeDatos

Nb=4096;

1

2

bits=randi ([01],Nb ,1);

3

## 11.7.

## ModulaciónQPSK

bits2=reshape(bits ,2 ,[]) ’;

1

2

sym=(2* bits2 (: ,1) -1)+...

3

1j*(2* bits2 (: ,2) -1);

4

5

sym=sym/sqrt (2);

6

## 11.8.

## GeneraciónOFDM

Nfft=64;

1

2

X=reshape(sym ,Nfft ,[]);

3

4

x=ifft(X,Nfft);

5

## 11.9.

## CanalMultitrayectoria

Considereelsiguientecanal:

h = [10.60.3] (6)

h=[10.60.3];

1

## 11.10.

## Caso1.SinPreőjoCíclico

Generelaseñaltransmitida.

tx1=x(:);

1

Propaguelaseñalporelcanal.

43

TecnologíasCelulares

ManualdePrácticas

rx1=conv(tx1 ,h);

1

Agregueruido.

rx1=awgn(rx1 ,...

1

15 ,...

2

’measured ’);

3

## 11.11.

## Recepción

rx1=rx1 (1: length(tx1));

1

2

rxMatrix=...

3

reshape(rx1 ,Nfft ,[]);

4

5

Y=fft(rxMatrix ,Nfft);

6

7

symRx=Y(:);

8

## 11.12.

## Detección

bitsHat=zeros(Nb ,1);

1

2

bitsHat (1:2: end)=...

3

real(symRx) >0;

4

5

bitsHat (2:2: end)=...

6

imag(symRx) >0;

7

## 11.13.

## BERSinPreőjo

BERsin=...

1

sum(bitsHat ~= bits)/Nb 2

## 11.14.

## Caso2.ConPreőjoCíclico

Seleccione:

NCP= 16

Ncp=16;

1

Genereelpreőjo.

44

TecnologíasCelulares

ManualdePrácticas

xcp=[x(end -Ncp +1:end ,:);

1

x];

2

## 11.15.

## Transmisión

tx2=xcp (:);

1

2

rx2=conv(tx2 ,h);

3

4

rx2=awgn(rx2 ,...

5

15 ,...

6

’measured ’);

7

## 11.16.

## Recepción

Reconstruyalamatriz.

rxMatrix=...

1

reshape(rx2 (1: length(tx2)) ,...

2

Nfft+Ncp ,...

3

[]);

4

Remuevaelpreőjo.

rxMatrix=...

1

rxMatrix(Ncp +1:end ,:);

2

ObtengalaFFT.

Y=fft(rxMatrix ,Nfft);

1

2

symRx=Y(:);

3

## 11.17.

## Detección

bitsHat=zeros(Nb ,1);

1

2

bitsHat (1:2: end)=...

3

real(symRx) >0;

4

5

bitsHat (2:2: end)=...

6

imag(symRx) >0;

7

45

TecnologíasCelulares

ManualdePrácticas

## 11.18.

## BERConPreőjo

BERcon=...

1

sum(bitsHat ~= bits)/Nb 2

## 11.19.

## ComparacióndeResultados

Construyalatabla:

Tabla7:Comparacióndedesempeño.

Conőguración

BER

Sinpreőjocíclico

Conpreőjocíclico

## 11.20.

## ConstelaciónRecibida

Graőquelasconstelaciones.

figure 1

2

plot(real(symRx) ,...

3

imag(symRx),’.’) 4

5

gridon 6

7

axissquare 8

9

xlabel(’I’) 10

ylabel(’Q’) 11

12

title(’Constelacion ␣recibida ’) 13

## 11.21.

## ResultadosEsperados

Elestudiantedeberáobservar:

Degradaciónnotablesinpreőjocíclico.

Mejorrecuperacióndesímbolosconpreőjocíclico.

MenorBERcuandoseempleapreőjo.

Reduccióndelainterferenciaentresímbolos.

46

TecnologíasCelulares

ManualdePrácticas

## 11.22.

## AnálisisdeResultados

Discuta:

1.£Quéefectoproducelamultitrayectoria?

2.£CómoafectalaISIalossímbolosOFDM?

3.£Porquéelpreőjocíclicomejoraeldesempeño?

4.£Quéocurresielretardodelcanalsuperalalongituddelpreőjo?

## 11.23.

## Cuestionario

1.£Quéeslainterferenciaentresímbolos?

2.£Cuáleslafuncióndelpreőjocíclico?

3.£PorquéLTEutilizapreőjocíclico?

4.£Quérelaciónexisteentrelalongituddelpreőjoyelretardomáximodelcanal?

5.£Quécostotieneagregarunpreőjocíclico?

## 11.24.

## Entregables

1.Objetivo.

2.Fundamentoteórico.

3.CódigoMATLAB.

4.Canalutilizado.

5.BERconysinpreőjo.

6.Constelacionesobtenidas.

7.Tablacomparativa.

8.Respuestasalcuestionario.

9.Conclusiones.

47

TecnologíasCelulares

ManualdePrácticas

## 12.

## Práctica8.Relacióndepotenciapicoapromedioen

## sistemasOFDM

## 12.1.

## ObjetivoGeneral

Analizar la relación de potencia pico a promedio (PAPR) de señales OFDM y estudiar su dependenciaconelnúmerodesubportadoras.

## 12.2.

## ObjetivosEspecíőcos

GenerarseñalesOFDMcondiferentenúmerodesubportadoras.

Calcularlapotenciapico.

Calcularlapotenciapromedio.

DeterminarlarelaciónPAPR.

AnalizarelimpactodePAPRentransmisoresinalámbricos.

## 12.3.

## Introducción

UnadelasprincipalesdesventajasdeOFDMeslaelevadarelacióndepotenciapicoa promedio(PAPR).

Debidoaquelaseñaltransmitidaresultadelasumademúltiplessubportadoras,pueden ocurririnstantesenloscualesvariascomponentessesumanconstructivamenteproduciendo amplitudeselevadas.

Los altos valores de PAPR obligan a los ampliőcadores de potencia a operar con márgenes adicionalesdelinealidad,reduciendolaeőcienciaenergéticadelostransmisores.

EsteproblemaesparticularmenteimportanteensistemasLTE,WiFiy5G.

## 12.4.

## FundamentoTeórico

LaPAPRsedeőnecomo PAPR =m´ax{|x[n]|2} (7) E{|x[n]|2} donde:

m´ax{|x[n]|2}correspondealapotenciapico.

E{|x[n]|2}correspondealapotenciapromedio.

FrecuentementelaPAPRseexpresaendecibeles:

PAPRdB= 10 log10(PAPR) (8)

48

TecnologíasCelulares

ManualdePrácticas

## 12.5.

## MaterialyEquipo

Computadorapersonal.

MATLAB.

## 12.6.

## GeneracióndeDatos

Genereunasecuenciabinariaaleatoria.

Nb=4096;

1

2

bits=randi ([01],Nb ,1);

3

## 12.7.

## ModulaciónQPSK

bits2=reshape(bits ,2 ,[]) ’;

1

2

sym=(2* bits2 (: ,1) -1)+...

3

1j*(2* bits2 (: ,2) -1);

4

5

sym=sym/sqrt (2);

6

## 12.8.

## GeneraciónOFDM

Utiliceinicialmente:

NF FT= 64

Nfft=64;

1

2

X=reshape(sym ,...

3

Nfft ,...

4

[]);

5

6

x=ifft(X,Nfft);

7

8

tx=x(:);

9

## 12.9.

## VisualizaciónTemporal

figure 1

2

plot(real(tx)) 3

4

49

TecnologíasCelulares

ManualdePrácticas

gridon 5

6

xlabel(’Muestra ’) 7

ylabel(’Amplitud ’) 8

9

title(’Senal␣OFDM ’) 10

Observelapresenciadepicoselevados.

## 12.10.

## PotenciaInstantánea

Calculelapotenciainstantánea.

P=abs(tx).^2;

1

Graőqueelresultado.

figure 1

2

plot(P) 3

4

gridon 5

6

xlabel(’Muestra ’) 7

ylabel(’Potencia ’) 8

9

title(’Potencia␣instantanea ’) 10

## 12.11.

## CálculodePAPR

Obtenga:

Ppeak=max(P);

1

2

Pavg=mean(P);

3

4

PAPR=Ppeak/Pavg;

5

6

PAPRdB=10* log10(PAPR) 7

Registreelvalorobtenido.

## 12.12.

## ComparaciónparaDiferentesNúmerosdeSubportadoras

Repitaelexperimentopara:

NF FT= 16,32,64,128,256

Completelasiguientetabla.

50

TecnologíasCelulares

ManualdePrácticas

Tabla8:VariacióndePAPR.

NF FT PAPR(dB)

16

32

64

128

256

## 12.13.

## GráőcadePAPR

NfftVec=[163264128256];

1

2

PAPRvec=[];

3

4

figure 5

6

plot(NfftVec ,...

7

PAPRvec ,...

8

’o-’,’LineWidth ’ ,2) 9

10

gridon 11

12

xlabel(’Numero␣de␣subportadoras ’) 13

ylabel(’PAPR␣(dB)’) 14

15

title(’PAPR␣en␣funcion␣de␣N_{FFT}’) 16

## 12.14.

## CCDFdelaPAPR

ObtengalafunciónCCDF.

paprSamples=zeros (1000 ,1);

1

2

fork=1:1000 3

4

bits=randi ([01] ,128 ,1);

5

6

bits2=reshape(bits ,2 ,[]) ’;

7

8

sym=(2* bits2 (: ,1) -1)+...

9

1j*(2* bits2 (: ,2) -1);

10

11

sym=sym/sqrt (2);

12

13

tx=ifft(sym);

14

51

TecnologíasCelulares

ManualdePrácticas

15

p=abs(tx).^2;

16

17

paprSamples(k)=...

18

10* log10(max(p)/mean(p));

19

20

end 21

ConstruyalaCCDF.

thresholds=0:0.1:15;

1

2

ccdf=zeros(size(thresholds));

3

4

fori=1: length(thresholds) 5

6

ccdf(i)=...

7

mean(paprSamples>...

8

thresholds(i));

9

10

end 11

12

figure 13

14

semilogy(thresholds ,...

15

ccdf ,...

16

’LineWidth ’ ,2) 17

18

gridon 19

20

xlabel(’PAPR␣(dB)’) 21

ylabel(’CCDF ’) 22

23

title(’Distribucion ␣CCDF ’) 24

## 12.15.

## ResultadosEsperados

Elestudiantedeberáobservar:

Potenciasinstantáneaselevadas.

AumentodePAPRconelnúmerodesubportadoras.

DistribuciónestadísticadePAPR.

NaturalezaprobabilísticadelospicosOFDM.

52

TecnologíasCelulares

ManualdePrácticas

## 12.16.

## AnálisisdeResultados

Discuta:

1.£PorquéOFDMpresentavaloreselevadosdePAPR?

2.£Quéocurrealincrementarelnúmerodesubportadoras?

3.£CómoafectalaPAPRalosampliőcadoresdepotencia?

4.£QuéimpactotienelaPAPRsobrelaeőcienciaenergética?

## 12.17.

## Cuestionario

1.£QuéeslaPAPR?

2.£PorquéesunproblemaenOFDM?

3.£QuésistemasdecomunicaciónutilizanOFDM?

4.£Quésucedesielampliőcadoroperaensaturación?

5.£QuétécnicasexistenparareducirlaPAPR?

## 12.18.

## Entregables

1.Objetivo.

2.Fundamentoteórico.

3.CódigoMATLAB.

4.Potenciainstantánea.

5.PAPRcalculada.

6.Tablacomparativa.

7.CCDFobtenida.

8.Respuestasalcuestionario.

9.Conclusiones.

53

TecnologíasCelulares

ManualdePrácticas

## 13.

## Práctica9.ModeladodecanalesMIMOycapacidad

## desistemasdeantenamúltiple

## 13.1.

## ObjetivoGeneral

ModelarsistemasMIMOenMATLAByevaluarlacapacidaddecanalparadiferentes conőguracionesdeantenas.

## 13.2.

## ObjetivosEspecíőcos

ModelarcanalesMIMORayleigh.

Generarmatricesdecanalaleatorias.

CompararsistemasSISOyMIMO.

Calcularlacapacidaddecanal.

Analizarlainŕuenciadelnúmerodeantenassobrelacapacidad.

## 13.3.

## Introducción

Los sistemas MIMO (MultipleInputMultipleOutput) utilizan múltiples antenas en trans- misión y recepción para incrementar la capacidad y conőabilidad de los enlaces inalámbricos.

LastecnologíascelularesmodernascomoLTEy5GincorporantécnicasMIMOpara aumentarsigniőcativamentelastasasdetransmisiónsinrequeriranchodebandaadicional.

UnadelasprincipalesventajasdeMIMOeslaposibilidaddetransmitirmúltiplesŕujos deinformaciónsimultáneamenteatravésdelcanalinalámbrico.

## 13.4.

## FundamentoTeórico

ElmodelobasedeunsistemaMIMOseexpresacomo y = Hx + n (9) donde:

xeselvectortransmitido.

yeselvectorrecibido.

nrepresentaelruido.

Hrepresentalamatrizdecanal.

54

TecnologíasCelulares

ManualdePrácticas

ParaunsistemaconNtantenastransmisorasyNrantenasreceptoras,

H ∈CNr×Nt

LacapacidadteóricadeuncanalMIMOvienedadapor

I +ρ



HHH

C= log2 (10)

Nt

donde:

ρrepresentalaSNRlineal.

Ieslamatrizidentidad.

## 13.5.

## MaterialyEquipo

Computadorapersonal.

MATLAB.

## 13.6.

## GeneracióndeunCanalMIMO2x2

ConsidereunsistemaMIMOcondosantenastransmisorasydosreceptoras.

Nt=2;

1

Nr=2;

2

3

H=(randn(Nr ,Nt)+...

4

1j*randn(Nr ,Nt))/sqrt (2) 5

Visualicelamatrizgenerada.

## 13.7.

## CálculodeCapacidad

Seleccioneinicialmente

SNR = 10 dB

snrDB=10;

1

2

rho=10^( snrDB /10);

3

Calculelacapacidad.

C=log2(det(...

1

eye(Nr)+...

2

(rho/Nt)*(H*H’))) 3

Registreelresultado.

55

TecnologíasCelulares

ManualdePrácticas

## 13.8.

## CapacidaddeunSistemaSISO

Paracomparacióncalcule

CSISO= log2(1 + ρ) (11)

Csiso=log2 (1+ rho) 1

Compareambosresultados.

## 13.9.

## CapacidadversusSNR

Obtengalacapacidadpara:

SNR = 0,5,10,15,20,25,30

snrDB=0:5:30;

1

2

Cmimo=zeros(size(snrDB));

3

4

fork=1: length(snrDB) 5

6

rho=...

7

10^( snrDB(k)/10);

8

9

H=...

10

(randn(Nr ,Nt)+...

11

1j*randn(Nr ,Nt))/sqrt (2);

12

13

Cmimo(k)=...

14

real(log2(det(...

15

eye(Nr)+...

16

(rho/Nt)*(H*H’))));

17

18

end 19

## 13.10.

## GráőcadeCapacidad

Csiso=log2(...

1

1+10.^( snrDB /10));

2

3

figure 4

5

plot(snrDB ,...

6

Cmimo ,...

7

’o-’,’LineWidth ’ ,2) 8

9

56

TecnologíasCelulares

ManualdePrácticas

holdon 10

11

plot(snrDB ,...

12

Csiso ,...

13

’s-’,’LineWidth ’ ,2) 14

15

gridon 16

17

xlabel(’SNR␣(dB)’) 18

ylabel(’Capacidad␣(bps/Hz)’) 19

20

legend(’MIMO␣2x2’ ,...

21

’SISO ’) 22

23

title(’Capacidad␣de␣canal ’) 24

## 13.11.

## ComparacióndeConőguraciones

Repitaelanálisispara:

SISO(1x1)

MIMO2x2

MIMO4x4

Tabla9:Capacidadparadistintasconőguraciones.

SNR(dB)

1x1

2x2

4x4

0

5

10

15

20

25

30

## 13.12.

## DistribucióndeValoresSingulares

Obtengalosvaloressingularesdelcanal.

s=svd(H) 1

Analicecómoserelacionanconlacapacidadobtenida.

57

TecnologíasCelulares

ManualdePrácticas

## 13.13.

## ResultadosEsperados

Elestudiantedeberáobservar:

Aumentodecapacidadalincrementarelnúmerodeantenas.

CrecimientocasilinealdecapacidadparaconőguracionesMIMO.

GananciasigniőcativarespectoasistemasSISO.

DependenciadelacapacidadconlaSNR.

## 13.14.

## AnálisisdeResultados

Discuta:

1.£PorquéMIMOincrementalacapacidad?

2.£CómoinŕuyelaSNRsobreeldesempeño?

3.£Quésucedealduplicarelnúmerodeantenas?

4.£Quérepresentanfísicamentelosvaloressingularesdelamatrizdecanal?

## 13.15.

## Cuestionario

1.£QuésigniőcaMIMO?

2.£CuálesladiferenciaentreSISOyMIMO?

3.£Quéeslacapacidaddecanal?

4.£PorquéLTEutilizaMIMO?

5.£Quéventajaofreceunsistema4x4respectoaunsistema2x2?

## 13.16.

## Entregables

1.Objetivo.

2.Fundamentoteórico.

3.CódigoMATLAB.

4.Curvasdecapacidad.

5.ComparaciónSISO/MIMO.

6.Tabladeresultados.

7.Respuestasalcuestionario.

8.Conclusiones.

58

TecnologíasCelulares

ManualdePrácticas

## 14.

## Práctica10.DeteccióndesímbolosensistemasMI-

## MOutilizandoZFyMMSE

## 14.1.

## ObjetivoGeneral

Implementar detectores Zero-Forcing (ZF) y Minimum Mean Square Error (MMSE) para unsistemaMIMOycompararsudesempeñomediantesimulacionesdeBER.

## 14.2.

## ObjetivosEspecíőcos

ImplementarunsistemaMIMO2x2.

ModelaruncanalRayleighMIMO.

ImplementareldetectorZF.

ImplementareldetectorMMSE.

Compararlatasadeerrordeambosdetectores.

## 14.3.

## Introducción

UnodelosprincipalesdesafíosensistemasMIMOconsisteensepararlossímbolostrans- mitidossimultáneamentedesdemúltiplesantenas.

Losdetectoreslinealesmásutilizadosson:

ZeroForcing(ZF).

MinimumMeanSquareError(MMSE).

EldetectorZFeliminacompletamentelainterferenciaentreŕujosespaciales,mientras queeldetectorMMSEconsiderasimultáneamentelainterferenciayelruido.

## 14.4.

## FundamentoTeórico

UnsistemaMIMOpuederepresentarsecomo y = Hx + n donde:

xeselvectortransmitido.

yeselvectorrecibido.

Heslamatrizdecanal.

nesruidoAWGN.

59

TecnologíasCelulares

ManualdePrácticas

WZF= (HHH)−1HH

EldetectorZFutiliza

−1

mientrasqueeldetectorMMSEutiliza

 HHH +1

HH WMMSE=

ρI

dondeρrepresentalaSNRlineal.

## 14.5.

## MaterialyEquipo

Computadorapersonal.

MATLAB.

## 14.6.

## ParámetrosdeSimulación

Considere:

SistemaMIMO2x2.

ModulaciónBPSK.

CanalRayleigh.

Nt=2;

1

2

Nr=2;

3

4

Nb=10000;

5

## 14.7.

## GeneracióndeBits

bits=randi ([01],Nb ,1);

1

2

x=2* bits-1;

3

## 14.8.

## AgrupaciónporAntenas

x=reshape(x,Nt ,[]);

1

60

TecnologíasCelulares

ManualdePrácticas

## 14.9.

## CanalMIMO

H=(randn(Nr ,Nt)+...

1

1j*randn(Nr ,Nt))/sqrt (2);

2

## 14.10.

## Transmisión

y=H*x;

1

## 14.11.

## Ruido

Seleccioneinicialmente:

Eb/N0= 10 dB

EbN0=10;

1

2

sigma=...

3

sqrt (10^( - EbN0 /10));

4

5

n=sigma *(...

6

randn(size(y))+...

7

1j*randn(size(y))...

8

)/sqrt (2);

9

10

y=y+n;

11

## 14.12.

## DetectorZF

Obtengalamatrizdedetección.

Wzf=inv(H’*H)*H’;

1

Recuperelossímbolos.

xzf=Wzf*y;

1

Decisión:

bitsZF=real(xzf) >0;

1

## 14.13.

## BERparaZF

BERzf=...

1

sum(bitsZF (:)~= bits)/Nb 2

61

TecnologíasCelulares

ManualdePrácticas

## 14.14.

## DetectorMMSE

Calcule:

rho=10^( EbN0 /10);

1

2

Wmmse=...

3

inv(H’*H+...

4

(1/ rho)*eye(Nt))*H’;

5

Recupere:

xmmse=Wmmse*y;

1

Decisión:

bitsMMSE=...

1

real(xmmse) >0;

2

## 14.15.

## BERparaMMSE

BERmmse=...

1

sum(bitsMMSE (:)~= bits)/Nb 2

## 14.16.

## ComparaciónparaDistintosValoresdeSNR

Considere:

0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20

dB.

ObtengalaBERparaambosdetectores.

## 14.17.

## GráőcaBER

figure 1

2

semilogy(EbN0dB ,...

3

BER_ZF ,...

4

’o-’,’LineWidth ’ ,2) 5

6

holdon 7

8

semilogy(EbN0dB ,...

9

BER_MMSE ,...

10

’s-’,’LineWidth ’ ,2) 11

12

gridon 13

62

TecnologíasCelulares

ManualdePrácticas

14

xlabel(’E_b/N_0␣(dB)’) 15

ylabel(’BER’) 16

17

legend(’ZF’,’MMSE ’) 18

19

title(’Comparacion␣de␣detectores ’) 20

## 14.18.

## ConstelacionesRecuperadas

Graőquelasseñalesdetectadas.

figure 1

2

plot(real(xzf (:)) ,...

3

imag(xzf (:)),’.’) 4

5

gridon 6

7

title(’Constelacion ␣ZF’) 8

figure 1

2

plot(real(xmmse (:)) ,...

3

imag(xmmse (:)),’.’) 4

5

gridon 6

7

title(’Constelacion ␣MMSE ’) 8

## 14.19.

## ResultadosEsperados

RecuperacióndesímbolosensistemasMIMO.

Comparacióndedetectoreslineales.

MejordesempeñodeMMSEparabajasSNR.

CurvasBERvsSNR.

## 14.20.

## AnálisisdeResultados

Discuta:

1.£PorquéMMSEsuelesuperaraZF?

2.£Enquécondicionesambosdetectorespresentandesempeñossimilares?

63

TecnologíasCelulares

ManualdePrácticas

3.£Cómoafectaelruidoacadadetector?

4.£Quéventajasofrececadamétodo?

## 14.21.

## Cuestionario

1.£QuéhaceeldetectorZF?

2.£QuédesventajapresentaZF?

3.£QuéventajatieneMMSE?

4.£PorquéMMSEconsideralapotenciaderuido?

5.£CuáldetectorutilizaLTEcontécnicasavanzadasderecepción?

## 14.22.

## Entregables

1.Objetivo.

2.Fundamentoteórico.

3.CódigoMATLAB.

4.BERparaZF.

5.BERparaMMSE.

6.CurvasBER.

7.Constelacionesobtenidas.

8.Respuestasalcuestionario.

9.Conclusiones.

64

TecnologíasCelulares

ManualdePrácticas

## 15.

## Práctica 11. Código Espacio-Tiempo de Alamouti pa-

## rasistemasMIMO

## 15.1.

## ObjetivoGeneral

Implementarunsistemadetransmisiónutilizandoelcódigoespacio-tiempodeAlamouti yevaluarlamejoraendesempeñorespectoaunsistemaSISOconvencional.

## 15.2.

## ObjetivosEspecíőcos

ImplementaruntransmisorAlamouti2x1.

ModelaruncanalRayleigh.

ImplementareldecodiőcadorAlamouti.

ComparareldesempeñoconunsistemaSISO.

Analizarlagananciadediversidad.

## 15.3.

## Introducción

Loscódigosespacio-tiempofuerondesarrolladosparaaprovecharladiversidadespacial proporcionadapormúltiplesantenas.

UnodelosesquemasmásutilizadoseselcódigodeAlamouti,debidoaque:

Proporcionadiversidaddeordendos.

Mantienelatasaunitaria.

Poseeundecodiőcadorlinealsencillo.

Fueincorporadoendiversosestándaresinalámbricos.

## 15.4.

## FundamentoTeórico

Paradossímboloscomplejos:

s1 y −s∗ s2 lamatrizdetransmisiónAlamouties S = s1

s2  s∗ 2

1

65

TecnologíasCelulares

ManualdePrácticas

Durantedosintervalosdetiemposetransmitenambossímbolosdesdedosantenasdife-

rentes.

Laortogonalidaddelamatrizpermiteunadetecciónsencillaenelreceptor.

## 15.5.

## MaterialyEquipo

Computadorapersonal.

MATLAB.

## 15.6.

## GeneracióndeDatos

Nb=10000;

1

2

bits=randi ([01],Nb ,1);

3

4

x=2* bits-1;

5

## 15.7.

## AgrupacióndeSímbolos

x=reshape(x,2 ,[]);

1

Cadacolumnacontiene:

[s1s2]

## 15.8.

## CodiőcaciónAlamouti

s1=x(1,:);

1

2

s2=x(2,:);

3

4

X1=[s1;

5

-s2];

6

7

X2=[s2;

8

s1];

9

## 15.9.

## CanalRayleigh

Generecoeőcientesindependientes.

h1=(randn (1, length(s1))+...

1

1j*randn (1, length(s1)))/sqrt (2);

2

3

66

TecnologíasCelulares

ManualdePrácticas

h2=(randn (1, length(s1))+...

4

1j*randn (1, length(s1)))/sqrt (2);

5

## 15.10.

## Transmisión

Primerintervalo:

r1=h1.*s1+...

1

h2.*s2;

2

Segundointervalo:

r2=-h1.* conj(s2)+...

1

h2.* conj(s1);

2

## 15.11.

## AdicióndeRuido

EbN0=10;

1

2

sigma=...

3

sqrt (10^( - EbN0 /10));

4

5

n1=sigma *( randn(size(r1))+...

6

1j*randn(size(r1)))/sqrt (2);

7

8

n2=sigma *( randn(size(r2))+...

9

1j*randn(size(r2)))/sqrt (2);

10

11

r1=r1+n1;

12

13

r2=r2+n2;

14

## 15.12.

## DecodiőcaciónAlamouti

Obtengalasestimaciones.

s1Hat=...

1

conj(h1).*r1+...

2

h2.* conj(r2);

3

4

s2Hat=...

5

conj(h2).*r1-...

6

h1.* conj(r2);

7

Normalice.

67

TecnologíasCelulares

ManualdePrácticas

ganancia=...

1

abs(h1).^2+...

2

abs(h2).^2;

3

4

s1Hat=s1Hat ./ ganancia;

5

6

s2Hat=s2Hat ./ ganancia;

7

## 15.13.

## Detección

bits1=real(s1Hat) >0;

1

2

bits2=real(s2Hat) >0;

3

Reconstruyaelvectordebits.

bitsHat=zeros(Nb ,1);

1

2

bitsHat (1:2: end)=bits1;

3

4

bitsHat (2:2: end)=bits2;

5

## 15.14.

## BER

BER=...

1

sum(bits ~= bitsHat)/Nb 2

## 15.15.

## ComparaciónconSistemaSISO

ImplementeunatransmisiónconvencionalBPSKsobrecanalRayleigh.

ObtengalaBERpara:

Eb/N0= 0, 2, 4, . . . , 20

dB.

Completelatabla.

68

TecnologíasCelulares

ManualdePrácticas

Tabla10:Comparacióndedesempeño.

Eb/N0(dB)

SISO

Alamouti

0

2

4

6

8

10

12

14

16

18

20

## 15.16.

## GráőcaBER

figure 1

2

semilogy(EbN0 ,...

3

BERsiso ,...

4

’o-’) 5

6

holdon 7

8

semilogy(EbN0 ,...

9

BERalamouti ,...

10

’s-’) 11

12

gridon 13

14

xlabel(’E_b/N_0␣(dB)’) 15

ylabel(’BER’) 16

17

legend(’SISO ’ ,...

18

’Alamouti ’) 19

20

title(’Ganancia␣de␣diversidad ’) 21

## 15.17.

## ResultadosEsperados

ImplementaciónfuncionaldelcódigoAlamouti.

ReducciónsigniőcativadelaBER.

Evidenciadegananciadediversidad.

69

TecnologíasCelulares

ManualdePrácticas

MejordesempeñorespectoaSISO.

## 15.18.

## AnálisisdeResultados

Discuta:

1.£QuégananciaproporcionaAlamouti?

2.£PorquélaBERdisminuye?

3.£Quésigniőcadiversidadespacial?

4.£Quéventajasofrecefrenteaincrementarlapotenciatransmitida?

## 15.19.

## Cuestionario

1.£Quéesuncódigoespacio-tiempo?

2.£QuéventajatieneelesquemadeAlamouti?

3.£Quéesladiversidadespacial?

4.£PorquélatasadelcódigoAlamoutiesunitaria?

5.£Quéaplicacionescelularesutilizantécnicassimilares?

## 15.20.

## Entregables

1.Objetivo.

2.Fundamentoteórico.

3.CódigoMATLAB.

4.BERdeAlamouti.

5.BERSISO.

6.Curvascomparativas.

7.Tabladeresultados.

8.Respuestasalcuestionario.

9.Conclusiones.

70

TecnologíasCelulares

ManualdePrácticas

## 16.

## Práctica12.Proyectointegrador:caracterizaciónex-

## perimentaldeunaredLTEutilizandoRTL-SDRy

## MATLAB

## 16.1.

## ObjetivoGeneral

CaracterizarexperimentalmenteseñalesLTEmediantelaadquisiciónyprocesamiento demuestrasIQutilizandounreceptorRTL-SDRyMATLAB,relacionandolosconceptos estudiadosduranteelcursodeTecnologíasCelulares.

## 16.2.

## ObjetivosEspecíőcos

IdentiőcarportadorasLTEpresentesenelentorno.

Analizarlaocupaciónespectraldeunaredcelular.

Estimaranchodebandayfrecuenciacentral.

RelacionarlaseñalobservadaconelmodeloOFDMestudiado.

Compararmedicionesrealizadasendiferentesubicaciones.

## 16.3.

## Introducción

LasredesLTEempleanOFDMenelenlacedescendenteytécnicasMIMOparaincre- mentarlacapacidadyeőcienciaespectral.

UtilizandounreceptorRTL-SDResposiblecapturarmuestrasIQdeseñalesLTEreales yrealizarunanálisisdetalladodesuscaracterísticasespectrales.

Enestaprácticasedesarrollaráunacampañademediciónparaidentiőcarycaracterizar redescelularespresentesenelentorno.

## 16.4.

## FundamentoTeórico

LaeőcienciaespectraldeunsistemaLTEdependede:

Anchodebandautilizado.

Númerodeantenas.

Relaciónseñalaruido.

Esquemademodulación.

Las señales LTEutilizan OFDM, por lo que suespectro presenta una estructura formada pormúltiplessubportadorasortogonales.

Laobservaciónexperimentaldedichasseñalespermiterelacionarconceptosteóricoscon implementacionesreales.

71

TecnologíasCelulares

ManualdePrácticas

## 16.5.

## MaterialyEquipo

Computadorapersonal.

MATLAB.

RTL-SDR.

Antenadebandaancha.

## 16.6.

## EscenariosdeMedición

Realicemedicionesenalmenostresubicacionesdistintas:

1.Exteriordelediőcio.

2.Interiordelaboratorio.

3.Pasilloocorredor.

Registrelascoordenadasodescripcióndecadapunto.

## 16.7.

## ConőguracióndelReceptor

Conőgureinicialmentelafrecuenciadeobservación.

rx=comm. SDRRTLReceiver ;

1

2

rx. CenterFrequency=850e6;

3

4

rx.SampleRate=2.4e6;

5

6

rx. SamplesPerFrame=262144;

7

8

rx. EnableTunerAGC=true;

9

## 16.8.

## CapturadeDatos

[data ,len]=rx();

1

2

release(rx);

3

Guardelasmuestrasadquiridasparasuanálisisposterior.

save

medicion1.matdata 1

72

TecnologíasCelulares

ManualdePrácticas

## 16.9.

## AnálisisEspectral

ObtengalaFFT.

Fs=rx.SampleRate;

1

2

N=length(data);

3

4

X=fftshift(fft(data));

5

6

f=linspace(-Fs/2 ,...

7

Fs/2 ,...

8

N);

9

10

figure 11

12

plot(f/1e6 ,...

13

20* log10(abs(X))) 14

15

gridon 16

17

xlabel(’Frecuencia␣(MHz)’) 18

ylabel(’Magnitud␣(dB)’) 19

20

title(’Espectro␣LTE’) 21

## 16.10.

## DensidadEspectraldePotencia

figure 1

2

pwelch(data ,...

3

4096 ,...

4

2048 ,...

5

4096 ,...

6

Fs ,...

7

’centered ’) 8

Analicelaocupaciónespectralobservada.

## 16.11.

## Espectrograma

figure 1

2

spectrogram(data ,...

3

1024 ,...

4

512 ,...

5

1024 ,...

6

73

TecnologíasCelulares

ManualdePrácticas

Fs ,...

7

’centered ’) 8

9

title(’Espectrograma ␣LTE’) 10

11

colorbar 12

## 16.12.

## EstimacióndePotenciaRecibida

Pr=mean(abs(data).^2);

1

2

Pr_dB=10* log10(Pr) 3

Repitaelprocedimientoparacadaubicación.

## 16.13.

## ComparacióndeMediciones

Completelasiguientetabla.

Tabla11:Medicionesrealizadas.

Ubicación

Frecuencia(MHz)

Potencia(dB)

Observaciones

Punto1

Punto2

Punto3

## 16.14.

## AnálisisOFDM

Utilizandoelespectroobtenido:

1.Identiőquelaestructuramultiportadora.

2.Estimeelanchodebandaocupado.

3.CompareconunaseñalOFDMsimuladaenprácticasanteriores.

## 16.15.

## CapacidadAproximada

AsumiendounaSNRestimadaexperimentalmente,calcule:

C= B log2(1 + SNR)

paraelcanalobservado.

Presentelosresultadosparacadaubicación.

74

TecnologíasCelulares

ManualdePrácticas

## 16.16.

## ResultadosEsperados

Elestudiantedeberáobtener:

CapturasIQdeunaredLTEreal.

Espectrosmedidosexperimentalmente.

Estimacionesdepotenciarecibida.

Comparaciónentrediferentesubicaciones.

RelaciónentreLTEyOFDM.

## 16.17.

## AnálisisdeResultados

Discuta:

1.£CuálfuelabandaLTEobservada?

2.£Quédiferenciasseobservaronentreubicaciones?

3.£Cómoinŕuyelapropagaciónenlapotenciarecibida?

4.£QuéevidenciasexperimentalesmuestranqueLTEutilizaOFDM?

5.£CómocontribuyeMIMOaldesempeñodeLTE?

## 16.18.

## ProductoFinal

Cadaequipodeberáentregar:

1.Reportetécnicocompleto.

2.Archivosdemedición.

3.CódigoMATLABdesarrollado.

4.Gráőcasobtenidas.

5.Presentaciónderesultados.

75

TecnologíasCelulares

ManualdePrácticas

## 16.19.

## EstructuradelReporte

1.Resumen.

2.Introducción.

3.Marcoteórico.

4.Metodología.

5.Escenariosdemedición.

6.Resultadosexperimentales.

7.Comparaciónentreubicaciones.

8.RelaciónconOFDMyMIMO.

9.Cálculodecapacidad.

10.Conclusiones.

11.Referencias.

## 16.20.

## CriteriosdeEvaluación

Tabla12:Rúbricadeevaluación.

Concepto

Ponderación Medicionesexperimentales

25 % ProcesamientoenMATLAB

20 % Análisistécnico

25 % Reporteescrito

20 % Presentación

10 %

76
