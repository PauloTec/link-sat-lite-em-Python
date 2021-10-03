import math

#CONSTANTES DO SISTEMA
RaioTerra = 6378.173 #Raio da terra em Km
CentroMassa = 42158 #Centro de massa em Km
velocidadeLuz = 300000000 #velocidade da luz

#-- 1º LOCALIZAÇÃO DAS ESTAÇÕES
nomeEstacaoA = input('Nome da localização da estaçao A - ')
nomeEstacaoB = input('Nome da localização da estaçao B - ')

#-- 1.1º Latitudes e longitudes das estações
latitudeEstacaoTerrenaA = int(input("Insere a latitude da estação terrena 1: "))
longitudeEstacaoTerrenaA = int(input("Insere a longitude da estação terrena 1: "))

latitudeEstacaoTerrenaB = int(input("Insere a latitude da estação terrena 2: "))
longitudeEstacaoTerrenaB = int(input("Insere a longitude da estação terrena 2: "))

#-- 1.2º Latitudes e longitudes do satélite
longitudeSatelite = int(input("Insere a longitude do satélite: "))

#CALCULO DA DISTÂNCIA ENTRE A ESTAÇÃO TERRENA E O SATÉLITE
aux1 = math.pow(RaioTerra,2) + math.pow(CentroMassa,2)
aux2 = 2*RaioTerra*CentroMassa
aux3 = math.cos(latitudeEstacaoTerrenaA)*math.cos(longitudeEstacaoTerrenaA-longitudeSatelite)
aux4 = math.cos(latitudeEstacaoTerrenaB)*math.cos(longitudeEstacaoTerrenaB-longitudeSatelite)

distancia_sat_EstTerrenaA = math.sqrt(aux1 - (aux2*aux3))
distancia_sat_EstTerrenaB = math.sqrt(aux1 - (aux2*aux4))

print("---------------------------------------------------------------------------------")
print("Latitude Estação terrena = ",latitudeEstacaoTerrenaA,"º")
print("Longitude Estação terrena = ",longitudeEstacaoTerrenaA,"º")
print("Longitude Do Satélite = ",longitudeSatelite,"º")
print()
print("Distância Entre Estação terrena A e o Satélite = ", distancia_sat_EstTerrenaA,"km")
print("Distância Entre Estação terrena B e o Satélite = ", distancia_sat_EstTerrenaB,"km")