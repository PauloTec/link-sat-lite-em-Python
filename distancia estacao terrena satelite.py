import math

#CONSTANTES DO SISTEMA
RaioTerra = 6378.173 #Raio da terra em Km
CentroMassa = 42158 #Centro de massa em Km
velocidadeLuz = 300000000 #velocidade da luz

#-- 1º LOCALIZAÇÃO DAS ESTAÇÕES
nomeEstacaoA = input('Nome da localização da estaçao terrena - ')

#-- 1.1º Latitudes e longitudes das estações
latitudeEstacaoTerrenaA = int(input("Insere a latitude da estação terrena: "))
longitudeEstacaoTerrenaA = int(input("Insere a longitude da estação terrena: "))

#-- 1.2º Latitudes e longitudes do satélite
longitudeSatelite = int(input("Insere a longitude do satélite: "))

#CALCULO DA DISTÂNCIA ENTRE A ESTAÇÃO TERRENA E O SATÉLITE
aux1 = math.pow(RaioTerra,2) + math.pow(CentroMassa,2)
aux2 = 2*RaioTerra*CentroMassa
aux3 = math.cos(latitudeEstacaoTerrenaA)*math.cos(longitudeEstacaoTerrenaA-longitudeSatelite)

distancia_sat_EstTerrenaA = math.sqrt(aux1 - (aux2*aux3))

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

#CALCULO DO AZIMUTE DAS ESTAÇÕES TERRENAS
#----Estação A
auxAzimute1 = math.cos(longitudeEstacaoTerrenaA-longitudeSatelite)
auxAzimute11 = math.pow(auxAzimute1, 2)

auxAzimute2 = math.cos(latitudeEstacaoTerrenaA)
auxAzimute22 = math.pow(auxAzimute2, 2)
auxAzimute23 = auxAzimute11*auxAzimute22
auxAzimute3 = math.sqrt(1-(auxAzimute23))

azimute = (auxAzimute1*math.sin(latitudeEstacaoTerrenaA))/auxAzimute3
azimuteA = 180 - math.acos(azimute)

print("---------------------------------------------------------------------------------")
print("Latitude Estação terrena ",nomeEstacaoA,"= ",latitudeEstacaoTerrenaA,"º")
print("Longitude Estação terrena ",nomeEstacaoA,"= ",longitudeEstacaoTerrenaA,"º")
print("Longitude Do Satélite = ",longitudeSatelite)
print()
print("Distância Entre Estação terrena ",nomeEstacaoA," e o Satélite = ", distancia_sat_EstTerrenaA,"km")
print("-----------------")
print("Ângulo de Elevação",nomeEstacaoA," = ",anguloElevacaoA,"º")
print("-----------------")
print("Azimute da Estação ",nomeEstacaoA," = ",azimuteA,"º")

