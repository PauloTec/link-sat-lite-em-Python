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

latitudeEstacaoTerrenaB = int(input("Insere a latitude da estação terrena 1: "))
longitudeEstacaoTerrenaB = int(input("Insere a longitude da estação terrena 1: "))

#-- 1.2º Latitudes e longitudes do satélite
longitudeSatelite = int(input("Insere a longitude do satélite: "))

#CALCULO DA DISTÂNCIA ENTRE A ESTAÇÃO TERRENA E O SATÉLITE
aux1 = math.pow(RaioTerra,2) + math.pow(CentroMassa,2)
aux2 = 2*RaioTerra*CentroMassa
aux3 = math.cos(latitudeEstacaoTerrenaA)*math.cos(longitudeEstacaoTerrenaA-longitudeSatelite)
aux4 = math.cos(latitudeEstacaoTerrenaB)*math.cos(longitudeEstacaoTerrenaB-longitudeSatelite)

distancia_sat_EstTerrenaA = math.sqrt(aux1 - (aux2*aux3))
distancia_sat_EstTerrenaB = math.sqrt(aux1 - (aux2*aux4))

#CALCULO DO ÂNGULO DE ELEVAÇÃO DAS ESTAÇÕES TERRENAS
#----Estação A
auxiliar1 = CentroMassa/RaioTerra
auxiliar11 = math.cos(latitudeEstacaoTerrenaA)*math.cos(longitudeEstacaoTerrenaA-longitudeSatelite)
auxiliar12 = math.pow(auxiliar1,2) #Quadrado do auxiliar 1

elevacaoA = (aux1*auxiliar11-1)/(math.sqrt(1+(auxiliar12))-(2*auxiliar1*auxiliar11))
anguloElevacaoA = 90-math.acos(elevacaoA)

#----Estação B
auxiliar13 = math.cos(latitudeEstacaoTerrenaB)*math.cos(longitudeEstacaoTerrenaB-longitudeSatelite)

elevacaoB = (aux1*auxiliar13-1)/(math.sqrt(1+(auxiliar12))-(2*auxiliar1*auxiliar13))
anguloElevacaoB = 90-math.acos(elevacaoB)

#-----------------------
#CALCULO DO AZIMUTE DAS ESTAÇÕES TERRENAS
a = math.cos(longitudeEstacaoTerrenaA-longitudeSatelite)*math.sin(latitudeEstacaoTerrenaA)
b = math.cos(latitudeEstacaoTerrenaA)*math.cos(longitudeSatelite-longitudeEstacaoTerrenaA)
azim = a/b
azimuteA = 180 - math.acos(azim)

#-- X - PARÂMETROS DO SISTEMA
frequenciaUplink = input('Digite a Frequencia de uplink Fu =  ')
frequenciaDownlink = input('Digite a Frequencia de Downlink  Fd =  ')
print('')

#densidadeFluxoPorTransponder = input('Digite a Densidade de fluxo no Satélite p/ Sat Transponder =   ')
#fatorMeritoSatelite = input('Digite o Factor de Mérito Antena do Satélite, Uplink (relGTu) =  ')

#EIRP_satelite = input('Digite EIRP de Saturação do Satélite (EIRPsat) =  ')

#backOffEntrada = input('Digite Back off de entrada do Satélite (BOin) =  ')
#backOffSaida = input('Digite Back off de Saída do Satélite (BOout) = ')

#bitErrorRate = input('Digite Probabilidade ou Erro de Bit (BER)')

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


print("---------------------------------------------------------------------------------")
print("Latitude Estação terrena - ",latitudeEstacaoTerrenaA,"º")
print("Longitude Estação terrena - ",longitudeEstacaoTerrenaA,"º")
print("Longitude Do Satélite - ",longitudeSatelite,"º")
print()
print("Distância Entre Estação terrena A e o Satélite - ", distancia_sat_EstTerrenaA,"km")
print("Distância Entre Estação terrena B e o Satélite - ", distancia_sat_EstTerrenaB,"km")