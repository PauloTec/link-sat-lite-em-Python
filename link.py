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
RaioT = 6378.173; #Raio da terra em Km
CentroM = 42158; #Centro de massa em Km
pi = 3.14; #Pi em radianos
c = (3*10^8); #Velocidade da luz em m/s
n = 0.6; #Factor de rendimento
e = 2.7; #Euler
k =(1.38*10^-23); #Constante Bolztman
Latu = 1.5; #Perdas de tracking na atmosfera/desvio das antenas Uplink em dB
Latd = 1.2; #Perdas de tracking na atmosfera/desvio das antenas Downlink em dB

# Constante de Atenuação
Paup = 0.08; # Perda ou Atenuação Atmosférica é tabelado, calculado através da frequencia do uplink (Fu)
Padw = 0.05; #Perda ou Atenuação Atmosférica é tabelado, calculado através da frequencia do Downlink (Fd)
hr = 5; #Altitude da Chuva em Km
hs =1.3 ; #Altitude da Estação Terrena em relação ao nível do mar, Para Angola varia de 1.2 Km à 1.5 Km
Aespu = 3.3; #Atenuação Específica Calculado atraves da frequencia Fu
Roo1= 65; #Taxa de precipitação ou Queda de chuva
Aespd = 2.5; #Atenuação Específica Calculado atraves da frequencia Fd
Opt=0.1; #Erro Máximo de Apontamento em Graus

# Valores de Temperatura
Tsky = 8.5; #Temperatura do ceu Porque o AngElev = 29.0º Segundo a Tabela K
Tsky1 = 13; #Porque o AngElev = 33.1º Segundo a Tabela K
TG = 10; #Temperatura do Ruido do Solo Porque 10º <AngElev< 90º
Tf = 290; #Temperatura Termodinamica da Conexão
Tr = 150; #Temperatura do ruido Equivalente na entrada do receptor
Tm = 275; #Temperatura Termodinamica de Percipitação entre 260k e 280k

# Constantes de Comunicação Digital ################
Rb = 60; #Taxa de Bit Uplink Mbps
Rb1 = 36; #Taxa de Bit Downlink Mbps
Serv = 64; #Serviço para transmissão de dados em Kbps
Nc = 32; #Número de Canais
Lfrx = 1; #Perda No Receptor em dB
Lftx = 0.5; #Perda no Transmissor em dB

# Percentagem de Chuva ############
pu=0.01; #Percentagem Duração maxima chuva no Ascendente,porcentagem por ano
pd=0.01; #Percentagem Duração maxima chuva no descendente, porcentagem por ano