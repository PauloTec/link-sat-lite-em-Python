import math
print('----------------------------------------------')
print('     KUNDIAMA, TECNOLOGIA E INOVAÇÃO')
print('')
print('         CURSO DE TELECOMUNICAÇÕES')
print('')
print('         CÁLCULO DE LIGAÇÃO POR SATÉLITE ')
print('')
print('         Engº DIASSILUA PAULO SIMÃO')
print('----------------------------------------------')

#CONSTANTES DO SISTEMA

RaioTerra = 6378.173 #Raio da terra em Km
CentroMassa = 42158 #Centro de massa em Km

#CALCULO DA DISTÂNCIA ENTRE A ESTAÇÃO TERRENA E O SATÉLITE

latitudeEstacaoTerrena = int(input("Insere a latitude da estação terrena: "))
print()
longitudeEstacaoTerrena = int(input("Insere a longitude da estação terrena: "))
print()
longitudeSatelite = int(input("Insere a longitude do satélite: "))
print()

aux1 = math.pow(RaioTerra,2) + math.pow(CentroMassa,2)
aux2 = 2*RaioTerra*CentroMassa
aux3 = math.cos(latitudeEstacaoTerrena)*math.cos(longitudeEstacaoTerrena-longitudeSatelite)

distancia_sat_EstTerrena = math.sqrt(aux1 - (aux2*aux3))

print("---------------------------------------------------------------------------------")
print("Latitude Estação terrena - ",latitudeEstacaoTerrena,"º")
print("Longitude Estação terrena - ",longitudeEstacaoTerrena,"º")
print("Longitude Do Satélite - ",longitudeSatelite,"º")
print()
print("Distância Entre Estação terrena e o Satélite - ", distancia_sat_EstTerrena,"km")