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
auxiliar12 = math.pow(auxiliar1,2)

elevacaoA = (aux1*auxiliar11-1)/(math.sqrt(1+(auxiliar12))-(2*auxiliar1*auxiliar11))
anguloElevacaoA = 90-math.acos(elevacaoA)

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

print("---------------------------------------------------------------------------------")
print("Latitude Estação terrena - ",latitudeEstacaoTerrenaA,"º")
print("Longitude Estação terrena - ",longitudeEstacaoTerrenaA,"º")
print("Longitude Do Satélite - ",longitudeSatelite,"º")
print()
print("Distância Entre Estação terrena A e o Satélite - ", distancia_sat_EstTerrenaA,"km")
print("Distância Entre Estação terrena B e o Satélite - ", distancia_sat_EstTerrenaB,"km")