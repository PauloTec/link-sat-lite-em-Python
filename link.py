import math

print('|-------------------------------------------------------------|')
print('|              Kundiama, Tecnologia e Inovação                |')
print('|            Telecomunicações - Radiocomunicação              |')

print('|                                                             |')
print('|    Cálculo de Ligação Por Satélite entre Zona 1 e Zona 2  |')
print('|                                                             |')

print('| Elaborado por:                                              |')
print('|            Engº Diassilua Paulo Simão (10093)               |')
print('|                                                             |')

print('| Em memória: Professor Dr. Engº Alberto Amaral Lopes         |')
print('|-------------------------------------------------------------|')

#CONSTANTES DO SISTEMA
RaioTerra = 6378.173 #Raio da terra em Km
CentroMassa = 42158 #Centro de massa em Km
velocidadeLuz = 300000000 #velocidade da luz

FactorRendimento = 0.6
La = 0.045    #Atenuação Atmosférica é tabelado, cálculado através da frequencia do uplink (Fu)
La1 = 0.04   # Atenuação Atmosférica é tabelado, cálculado através da frequencia do Downlink (Fd)
hr = 5       # altitude da Chuva em Km
hs =1.2   #Altitude da Estação Terrena em relação ao nível do mar, Para Angola varia de 1.5 Km à 1.5 Km
Aesp = 2.5  #Atenuação Específica Caçulado atraves da frequencia Fu
Roo1= 50   #Taxa de precipitação ou Queda de chuva
Aesp1 = 1.2 #Atenuação Específica Calculado atraves da frequencia Fd
Roo11= 30.2  #Taxa de precipitação ou Queda de chuva
euler = 2.7 #Constante de euler

#---------------------- INSERIR DADOS PARA O CÁLCULO

#-- 1º LOCALIZAÇÃO DAS ESTAÇÕES
nomeEstacaoA = input('Nome da localização da estaçao A - ')
nomeEstacaoB = input('Nome da localização da estaçao B - ')

#-- 1.1º Latitudes e longitudes das estações
latitudeEstacaoTerrenaA = int(input("Insere a latitude da estação terrena 1: "))
longitudeEstacaoTerrenaA = int(input("Insere a longitude da estação terrena 1: "))

latitudeEstacaoTerrenaB = int(input("Insere a latitude da estação terrena 2: "))
longitudeEstacaoTerrenaB = int(input("Insere a longitude da estação terrena 2: "))

#-- 1.2º Latitudes e longitudes do satélite
nomeSatelite = input('Qual é o nome do satélite: ')
longitudeSatelite = int(input("Insera a longitude do satélite: "))

#CALCULO DA DISTÂNCIA ENTRE A ESTAÇÃO TERRENA E O SATÉLITE
aux1 = math.pow(RaioTerra,2) + math.pow(CentroMassa,2)
aux2 = 2*RaioTerra*CentroMassa
aux3 = math.cos(latitudeEstacaoTerrenaA)*math.cos(longitudeEstacaoTerrenaA-longitudeSatelite)
aux4 = math.cos(latitudeEstacaoTerrenaB)*math.cos(longitudeEstacaoTerrenaB-longitudeSatelite)

distancia_sat_EstTerrenaA = math.sqrt(aux1 - (aux2*aux3))
distancia_sat_EstTerrenaB = math.sqrt(aux1 - (aux2*aux4))

#CALCULO DO ÂNGULO DE ELEVAÇÃO DAS ESTAÇÕES TERRENAS
#----Estação A
auxAngElev1 = CentroMassa/RaioTerra
auxAngElev2 = math.cos(latitudeEstacaoTerrenaA)
auxAngElev3 = math.cos(longitudeEstacaoTerrenaA-longitudeSatelite)
auxAngElev4 = math.pow(auxAngElev1,2) #Quadrado do auxiliar 1

auxAngElev5 = (auxAngElev1*auxAngElev2*auxAngElev3)-1
auxAngElev6 = 1+auxAngElev4
auxAngElev7 = 2*auxAngElev1*auxAngElev2*auxAngElev3

elevacaoA = auxAngElev5/math.sqrt(auxAngElev6-auxAngElev7)

anguloElevacaoA = 90-math.acos(elevacaoA)

#----Estação B
auxAngElev2B = math.cos(latitudeEstacaoTerrenaB)
auxAngElev3B = math.cos(longitudeEstacaoTerrenaB-longitudeSatelite)

auxAngElev5B = (auxAngElev1*auxAngElev2B*auxAngElev3B)-1
auxAngElev7B = 2*auxAngElev1*auxAngElev2B*auxAngElev3B

elevacaoB = auxAngElev5B/math.sqrt(auxAngElev6-auxAngElev7B)

anguloElevacaoB = 90-math.acos(elevacaoB)

#-----------------------
#CALCULO DO AZIMUTE DAS ESTAÇÕES TERRENAS
#----Estação A
auxAzimute1 = math.cos(longitudeEstacaoTerrenaA-longitudeSatelite)
auxAzimute11 = math.pow(auxAzimute1, 2)

auxAzimute2 = math.cos(latitudeEstacaoTerrenaA)
auxAzimute22 = math.pow(auxAzimute2, 2)
auxAzimute23 = auxAzimute11*auxAzimute22
auxAzimute3 = math.sqrt(1-(auxAzimute23))

azimute = (auxAzimute1*math.sin(latitudeEstacaoTerrenaA))/auxAzimute3
azimuteEstacaoA = 180 - math.acos(azimute)

#----Estação B
auxAzimute1B = math.cos(longitudeEstacaoTerrenaB-longitudeSatelite)
auxAzimute11B = math.pow(auxAzimute1B, 2)

auxAzimute2B = math.cos(latitudeEstacaoTerrenaB)
auxAzimute22B = math.pow(auxAzimute2B, 2)
auxAzimute23B = auxAzimute11*auxAzimute22B
auxAzimute3B = math.sqrt(1-(auxAzimute23B))

azimuteB = (auxAzimute1B*math.sin(latitudeEstacaoTerrenaB))/auxAzimute3B
azimuteEstacaoB = 180 - math.acos(azimuteB)

#-- X - PARÂMETROS DO SISTEMA
frequenciaUplink = int(input('Digite a Frequencia de uplink Fu =  '))
frequenciaDownlink = int(input('Digite a Frequencia de Downlink  Fd =  '))
print('')

#densidadeFluxoPorTransponder = input('Digite a Densidade de fluxo no Satélite p/ Sat Transponder =   ')
#fatorMeritoSatelite = input('Digite o Factor de Mérito Antena do Satélite, Uplink (relGTu) =  ')

#EIRP_satelite = input('Digite EIRP de Saturação do Satélite (EIRPsat) =  ')

backOffEntrada = int(input('Digite Back off de entrada do Satélite (BOin) =  '))
backOffSaida = int(input('Digite Back off de Saída do Satélite (BOout) = '))

#bitErrorRate = input('Digite Probabilidade ou Erro de Bit (BER)')

#-----------------------------------------------------------------
# ATENUAÇÃO NO ESPAÇO LIVRE
#-----------------------------------------------------------------

#-- 2º CÁLCULO DA ATENUAÇÃO NO PERCURSO DE SUBIDA SEM CHUVA
auxilio = velocidadeLuz/frequenciaUplink
atenEspacoLivre = (4*math.pi*distancia_sat_EstTerrenaA*1000)/(math.pow(auxilio,2))

#Conversão em dB
atenEspacoLivre_dB = 10*math.log10(atenEspacoLivre)

#Atenuação total sem chuva
atenEspacoLivre_semChuva = atenEspacoLivre_dB + La

#-- 2.1º CÁLCULO DA ATENUAÇÃO NO PERCURSO DE DESCIDA SEM CHUVA
auxilio = velocidadeLuz/frequenciaDownlink
atenEspacoLivre2 = (4*math.pi*distancia_sat_EstTerrenaB*1000)/(math.pow(auxilio,2))

#Conversão em dB
atenEspacoLivre_dB2 = 10*math.log10(atenEspacoLivre2)

#Atenuação total sem chuva
atenEspacoLivre_semChuva2 = atenEspacoLivre_dB2 + La

# 3º INCLINAÇÃO DO PERCURSO NA CHUVA
inclinacaoPercursoChuvaA = ((hr-hs)*1000)/math.sin(anguloElevacaoA)
inclinacaoPercursoChuvaB = ((hr-hs)*1000)/math.sin(anguloElevacaoB)
#Hr - altitude da Chuva em Km, ver nas constantes acima
#Hs - Altitude da Estação Terrena em relação ao nível do mar, Para Angola varia de 1.5 Km à 1.5 Km, ver nas constantes acima

#Conversão em dB
inclinacaoPercursoChuvaA_dB = 10*math.log10(inclinacaoPercursoChuvaA)
inclinacaoPercursoChuvaB_dB = 10*math.log10(inclinacaoPercursoChuvaB)

# 4º DISTÂNCIA DA CHUVA COM TAXA PLUVIOMÉTRICA
taxaPluvometrica = 50 #corresponde ao R0,001; ver na definição das constantes
aux = (-0.015)*taxaPluvometrica
distanciaChuva = 35*math.pow(euler,aux)

# 4.1º DISTÂNCIA DA CHUVA PARA R DE 1%
auxiliando = (inclinacaoPercursoChuvaA/distanciaChuva)*math.cos(anguloElevacaoA)
auxiliando2 = (inclinacaoPercursoChuvaB/distanciaChuva)*math.cos(anguloElevacaoB)
distanciaChuva_R001_A = 1/(1+auxiliando)
distanciaChuva_R001_B = 1/(1+auxiliando2)

#5º CÁLCULO DA ATENUAÇÃO NO PERCURSO DE DESCIDA COM CHUVA
#Estação A
auxiliando1 = Aesp * inclinacaoPercursoChuvaA_dB * distanciaChuva_R001_A
auxiliando1_dB = 10*math.log10(auxiliando1)

atenEspacoLivre_comChuva_A = La + inclinacaoPercursoChuvaA_dB + auxiliando1_dB

#Estação B
auxiliando2 = Aesp * inclinacaoPercursoChuvaB_dB * distanciaChuva_R001_B
auxiliando2_dB = 10*math.log10(auxiliando2)

atenEspacoLivre_comChuva_B = La + inclinacaoPercursoChuvaB_dB + auxiliando2_dB

#6º CÁLCULO DA PERDA NA TRANSMISSÃO
erroMaximoApontamento = 0.1 #Encontrar na definição de constantes
auxiliando3 = (erroMaximoApontamento*distancia_sat_EstTerrenaA*frequenciaUplink)/(70*velocidadeLuz)

perdaTx = 12*math.pow(auxiliando3,2)
#Em db
perdaTx_dB = 10*math.log10(perdaTx)

#6.1º CÁLCULO DA PERDA NA RECEPÇÃO
auxiliando4 = (erroMaximoApontamento*distancia_sat_EstTerrenaB*frequenciaDownlink)/(70*velocidadeLuz)

perdaRx = 12*math.pow(auxiliando4,2)
#Em db
perdaRx_dB = 10*math.log10(perdaRx)

#7º CÁLCULO DA DISPONIBILIDADE DO LINK
pu=0.005
pd=0.005
p=pu+pd

disponibilidadeLink = 1 - (p/100)

#8º CÁLCULO DA DISPONIBILIDADE DO SISTEMA
disponibilidadeSatelite=0.9999
Pa=0.9999

disponibilidadeSistema = Pa * disponibilidadeSatelite * disponibilidadeLink

#9º CÁLCULO DA INDISPONIBILIDADE DO SISTEMA EM HORAS
indisponibilidade=(1-disponibilidadeSistema)*(365*24)

#10º CÁLCULO DA TEMPERATURA DO SISTEMA
#TG e Tsky,obtido de acordo o ângulo de elevação em graus TG - 10º <AngElev < 90º e Tsky - ângulo de elevação = 68.2º Segundo a Tabela.
TG = 10
Tsky = 16
temperaturaSistema = TG + Tsky

#11º CÁLCULO DA TAXA DE TRANSMISSÃO
#Serviço para transmissão de dados em Kbps = 64 e Número de canais = 32.
servicoTx = 64
numCanais = 32
taxtaTransmissao = servicoTx * numCanais

#12º CÁLCULO DE SINAL RUÍDO
k = 1.38*math.pow(10, -23)
k1=10*math.log10(1/k)

EIRP = 51 #EIRP de saturação do Satélite
relGTu =3.2 #Factor de Mérito Antena do Satélite (relGTu)

#C_No = EIRP - atenEspacoLivre_comChuva_A + relGTu + k1

#13º CÁLCULO DE GANHO DO SISTEMA NA RECEPÇÃO
Grx = relGTu + 10*math.log10(temperaturaSistema)
Grx_watts = math.pow(10, (Grx/10))

#13.1º CÁLCULO DE GANHO DO SISTEMA NA TRANSMISSÃO
ganhoTx = (20*math.log10(frequenciaUplink))-(20*math.log10(frequenciaDownlink))+Grx
Gtx_watts = math.pow(10, ganhoTx/10)

#14º CÁLCULO DO DIÂMETRO DA ANTENA NA TRANSMISSÃO
auxiliando3 = (Gtx_watts/FactorRendimento)*velocidadeLuz
auxiliando4 = math.pi * frequenciaUplink

diametroTx = math.sqrt(auxiliando3/auxiliando4)

#14.1º CÁLCULO DO DIÂMETRO DA ANTENA NA RECEPÇÃO
auxiliando5 = (Grx_watts/FactorRendimento)*velocidadeLuz
auxiliando6 = math.pi * frequenciaDownlink

diametroRx = math.sqrt(auxiliando5/auxiliando6)

#15º CÁLCULO DO GANHO ESPECÍFICO DA ANTENA NA TRANSMISSÃO DE ACORDO O DIAMETRO DA ANTENA
auxiliando7 = math.pi*diametroTx*frequenciaUplink/velocidadeLuz
GanhoEspTx = FactorRendimento*math.pow(auxiliando7,2)

#Conversão em dB
GanhoEspTx_dB = 10*math.log10(GanhoEspTx)

#15.1º CÁLCULO DO GANHO ESPECÍFICO DA ANTENA NA RECEPÇÃO DE ACORDO O DIAMETRO DA ANTENA
auxiliando8 = math.pi*diametroRx*frequenciaDownlink/velocidadeLuz
GanhoEspRx = FactorRendimento*math.pow(auxiliando8,2)

#Conversão em dB
GanhoEspRx_dB = 10*math.log10(GanhoEspRx)

#16º CÁLCULO DO EIRP NA TRANSMISSÃO E NA RECEPÇÃO
densidadeFluxo = -91 #Inserido pelo usuário
Latu = 1.5 #Perda colocar na definição das constantes do sistema
Latd = 1.2 #Perda colocar na definição das constantes do sistema

#Na transmissão
EIRP_tx = densidadeFluxo + 10*math.log10(4*math.pi*math.pow(diametroTx,2)) + Latu + backOffEntrada

#Na recepção
EIRP_rx = densidadeFluxo + 10*math.log10(4*math.pi*math.pow(diametroRx,2)) + Latd + backOffSaida

#17º CÁLCULO DE POTÊNCIA NA TRANSMISSÃO
PotenciaTx = EIRP_tx - ganhoTx
PotenciaTx_watts = math.pow(10, PotenciaTx/10)

#valor absoluto em watts
auxiliando1111 = PotenciaTx_watts*math.pow(10, -6)
PotenciaTx_watts_absoluto = abs(round(auxiliando1111))

#17.1º CÁLCULO DE POTÊNCIA NA RECEPÇÃO
PotenciaRx = EIRP_rx - Grx
PotenciaRx_watts = math.pow(10, PotenciaRx/10)

print("---------------------------------------------------------------------------------")
print("     IMPRESSÃO DE DADOS                                                          ")
print("---------------------------------------------------------------------------------")
print("Latitude Estação terrena",nomeEstacaoA," = ",latitudeEstacaoTerrenaA,"º")
print("Latitude Estação terrena",nomeEstacaoA," = ",longitudeEstacaoTerrenaA,"º")
print("-----------------")
print("Longitude Estação terrena ",nomeEstacaoB," = ",latitudeEstacaoTerrenaB,"º")
print("Latitude Estação terrena",nomeEstacaoB," = ",longitudeEstacaoTerrenaB,"º")
print("-----------------")
print("Longitude Do Satélite = ",longitudeSatelite,"º")
print()
print("-----------------")
print("Distância Entre Estação terrena A",nomeEstacaoA," e o Satélite = ", distancia_sat_EstTerrenaA,"km")
print("Distância Entre Estação terrena B",nomeEstacaoB," e o Satélite = ", distancia_sat_EstTerrenaB,"km")
print()
print("-----------------")
print("Ângulo de Elevação",nomeEstacaoA," = ",anguloElevacaoA,"º")
print("Ângulo de Elevação",nomeEstacaoB," = ",anguloElevacaoB,"º")

print("-----------------")
print("Azimute da Estação ",nomeEstacaoA," = ",azimuteEstacaoA,"º")
print("Azimute da Estação ",nomeEstacaoA," = ",azimuteEstacaoB,"º")

print("-----------------------------------------------------------------")
print("             ATENUAÇÃO NO ESPAÇO LIVRE                           ")
print("-----------------------------------------------------------------")

print("----- Percurso sem chuva                          ")

print("SUBIDA SEM CHUVA")
print("Atenuação no percurso de Subida sem Chuva ",atenEspacoLivre)
print("Equivalência em dB =",atenEspacoLivre_dB)
print("Atenuação Total no percurso sem Chuva=",atenEspacoLivre_semChuva)

print("DESCIDA SEM CHUVA")
print("Atenuação no percurso de descida sem Chuva ",atenEspacoLivre2)
print("Equivalência em dB =",atenEspacoLivre_dB2)
print("Atenuação Total no percurso sem Chuva=",atenEspacoLivre_semChuva2)

print()
print("----- Percurso com chuva                          ")
print("-----------------")
print("INCLINAÇÃO DO PERCURSO COM CHUVA")
print("Para estação A =",inclinacaoPercursoChuvaA)
print("Equivalência na estação A em dB",inclinacaoPercursoChuvaA_dB)

print()
print("Para estação B",inclinacaoPercursoChuvaB)
print("Equivalência na estação B em dB",inclinacaoPercursoChuvaB_dB)

print()
print("DISTÂNCIA DA CHUVA PARA R DE 1%")
print("Para estação A =",distanciaChuva_R001_A)
print("Para estação B =",distanciaChuva_R001_B)

print()
print("ATENUAÇÃO NO PERCURSO COM CHUVA")

print("Para estação A =",atenEspacoLivre_comChuva_A)
print("Para estação B =",atenEspacoLivre_comChuva_B)

print("-----------------------------------------------------------------")
print("             PERDA NA TRANSMISSÃO E NA RECEPÇÃO                  ")
print("-----------------------------------------------------------------")

print()
print("Perda na transmissão = ",perdaTx)
print("Equivalente em dB = ",perdaTx_dB)

print()
print("Perda na recepção = ",perdaRx)
print("Equivalente em dB = ",perdaRx_dB)

print("-----------------------------------------------------------------")
print("             DISPONIBILIDADE DO LINK                  ")
print("-----------------------------------------------------------------")
print()
print("Disponibilidade de link = ",disponibilidadeLink)

