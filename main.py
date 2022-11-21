#-----------------------------------------------------------------------------#
#=============================================================================#
#-----------------------------------------------------------------------------#

# Projeto - Bolão da Copa do Mundo
# Novembro 2022

#-----------------------------------------------------------------------------#
#=============================================================================#
#-----------------------------------------------------------------------------#

# importanto bibliotecas
import streamlit as st
import sqlite3
import pandas as pd
import webbrowser
from datetime import date, datetime, time
from datetime import date, datetime, time,timedelta
from time import strftime
import time
import pytz
#import flag
#import emoji
import numpy as np # biblioteca Python usada para trabalhar com arrays
#import matplotlib.pyplot as plt # biblioteca para criar visualizações estáticas, animadas e interativas em Python
#from os import write
#from numpy.core.fromnumeric import size
#import Controllers.clientecontroller as clientecontroller
#import models.cliente as cliente
import pandas as pd
#import plotly.figure_factory as ff
from PIL import Image

#-----------------------------------------------------------------------------#
#=============================================================================#
#-----------------------------------------------------------------------------#

# funções

def grupos():
    
    '''
    
    Definição dos grupos da copa do mundo 2022
    
    '''
    
    grupos = np.array([['Catar','Equador','Senegal','Holanda','A'],
                       ['Inglaterra','Irã','Estados Unidos','País de Gales','B'],
                       ['Argentina','Arábia Saudita','México','Polônia','C'],
                       ['França','Austrália','Dinamarca','Tunísia','D'],
                       ['Espanha','Costa Rica','Alemanha','Japão','E'],
                       ['Bélgica','Canadá','Marrocos','Croácia','F'],
                       ['Brasil','Sérvia','Suíça','Camarões','G'],
                       ['Portugal','Gana','Uruguai','Coreia do Sul','H']]) # grupos da copa do mundo 2022
    
    return grupos

def listaSelecoes():

    '''

    Lista das seleções da copa do mundo 2022

    '''

    selecoes = ['Catar','Equador','Senegal','Holanda',
                'Inglaterra','Irã','Estados Unidos','País de Gales',
                'Argentina','Arábia Saudita','México','Polônia',
                'França','Austrália','Dinamarca','Tunísia',
                'Espanha','Costa Rica','Alemanha','Japão',
                'Bélgica','Canadá','Marrocos','Croácia',
                'Brasil','Sérvia','Suíça','Camarões',
                'Portugal','Gana','Uruguai','Coreia do Sul'] # seleções da copa do mundo 2022
    
    return selecoes

def cadastroApostador(login,senha):
    
    '''
    Cadastro do usuário e apostador:
    login, senha, pontos, cravadas, acertos, erros, nadas, não apostas, ...
    tabela do apostador.
    '''

    pontos     = 0
    cravadas   = 0
    acertos    = 0
    erros      = 0
    nadas      = 0
    naoapostas = 0

    apostador = [login, senha, pontos, cravadas, acertos, erros, nadas, naoapostas]
    numeroApostasIniciais = 20
    numeroApostasPrimeiraFase = 96
    numeroTotal = numeroApostasIniciais + numeroApostasPrimeiraFase
    for aposta in range(numeroTotal):
        apostador.append('')
    
    return apostador

def fazerApostaPrimeiraFase(cadastroApostador, nomeGrupo, nomeJogo, golMandante, golVisitante):

    # apostas - colocar botões
    '''
    
    Aposta em jogos da primeira fase:
    
    cadastro do apostador.
        
    nomes dos grupos: grupo A = 0; grupo B = 1; grupo C = 2; grupo D = 3; grupo E = 4; grupo F = 5; grupo G = 6; grupo H = 7.
    
    nomes dos jogos: jogo 1 = 0; jogo 2 = 1; jogo 3 = 2; jogo 4 = 3; jogo 5 = 4; jogo 6 = 5.
    
    gols do mandante e do visitante.    
    
    '''
    
    #-------------------------------------------------------------------------#        
    
    # rodada e jogo
    #nomeRodada = int(input('Qual rodada você quer apostar? '))
    if nomeJogo == 0 or nomeJogo == 1:
        nomeRodada = 1
    elif nomeJogo == 2 or nomeJogo == 3:
        nomeRodada = 2
    elif nomeJogo == 4 or nomeJogo == 5:
        nomeRodada = 3
    
    
    if nomeRodada == 1:
        # Time i1 = 0
        # Time i2 = 1
        # Time i3 = 2
        # Time i4 = 3
        # rodada 1: Time i1 x Time i2
        # rodada 1: Time i3 x Time i4
        time1 = 0
        time2 = 1
        time3 = 2
        time4 = 3
        if nomeJogo == 0:
            print('')
            print('Jogo 1')
            print('%s X %s'%(grupos()[nomeGrupo][time1], grupos()[nomeGrupo][time2]))
        elif nomeJogo == 1:
            print('')
            print('Jogo 2')
            print('%s X %s'%(grupos()[nomeGrupo][time3], grupos()[nomeGrupo][time4]))
    
    elif nomeRodada == 2:
        # Time i1 = 0
        # Time i2 = 1
        # Time i3 = 2
        # Time i4 = 3
        # rodada 2: Time i1 x Time i3
        # rodada 2: Time i2 x Time i4
        time1 = 0
        time2 = 2
        time3 = 1
        time4 = 3
        if nomeJogo == 2:
            print('')
            print('Jogo 3')
            print('%s X %s'%(grupos()[nomeGrupo][time1], grupos()[nomeGrupo][time2]))
        elif nomeJogo == 3:
            print('')
            print('Jogo 4')
            print('%s X %s'%(grupos()[nomeGrupo][time3], grupos()[nomeGrupo][time4]))

    elif nomeRodada == 3:
        # Time i1 = 0
        # Time i2 = 1
        # Time i3 = 2
        # Time i4 = 3
        # rodada 3: Time i4 x Time i1
        # rodada 3: Time i2 x Time i3
        time1 = 3
        time2 = 0
        time3 = 1
        time4 = 2
        if nomeJogo == 4:
            print('')
            print('Jogo 5')
            print('%s X %s'%(grupos()[nomeGrupo][time1], grupos()[nomeGrupo][time2]))
        elif nomeJogo == 5:
            print('')
            print('Jogo 6')
            print('%s X %s'%(grupos()[nomeGrupo][time3], grupos()[nomeGrupo][time4]))

    #-------------------------------------------------------------------------#

    # colocando o resultado no cadastro do usuário
    #cadastroApostador[-1][nomeGrupo][nomeJogo-1][0], cadastroApostador[-1][nomeGrupo][nomeJogo-1][1] = golMandante, golVisitante
    #cadastroApostador[-1][nomeGrupo][nomeJogo][0], cadastroApostador[-1][nomeGrupo][nomeJogo][1] = golMandante, golVisitante
    cadastroApostador[28+2*6*nomeGrupo+2*nomeJogo], cadastroApostador[28+2*6*nomeGrupo+2*nomeJogo+1] = golMandante, golVisitante
    
    print('')
    print('Aposta realizada!')
    if nomeJogo == 0 or nomeJogo == 2 or nomeJogo == 4:
        #print('%s %d X %d %s'%(selecoes()[nomeGrupo][time1][0],golMandante,golVisitante,selecoes()[nomeGrupo][time2][0]))
        print('%s %d X %d %s'%(grupos()[nomeGrupo][time1],golMandante,golVisitante,grupos()[nomeGrupo][time2]))
    elif nomeJogo == 1 or nomeJogo == 3 or nomeJogo == 5:
        #print('%s %d X %d %s'%(selecoes()[nomeGrupo][time3][0],golMandante,golVisitante,selecoes()[nomeGrupo][time4][0]))
        print('%s %d X %d %s'%(grupos()[nomeGrupo][time3],golMandante,golVisitante,grupos()[nomeGrupo][time4]))

    return cadastroApostador

def apostaPodio(usuario,apostaCampeao,apostaViceCampeao,apostaTerceiroColocado):
    
    # apostas podio
    usuario[9] = listaSelecoes().index(apostaCampeao) #apostaCampeao
    usuario[10] = listaSelecoes().index(apostaViceCampeao) #apostaViceCampeao
    usuario[11] = listaSelecoes().index(apostaTerceiroColocado) #apostaTerceiroColocado

    return

def apostaGrupos(usuario,nomeGrupo,apostaPrimeiroGrupo,apostaSegundoGrupo):
    
    # apostas grupos
    if nomeGrupo == 0:
        usuario[12] = listaSelecoes().index(apostaPrimeiroGrupo) #apostaPrimeiroGrupo
        usuario[13] = listaSelecoes().index(apostaSegundoGrupo) #apostaSegundoGrupo
    elif nomeGrupo == 1:
        usuario[14] = listaSelecoes().index(apostaPrimeiroGrupo) #apostaPrimeiroGrupo
        usuario[15] = listaSelecoes().index(apostaSegundoGrupo) #apostaSegundoGrupo
    elif nomeGrupo == 2:
        usuario[16] = listaSelecoes().index(apostaPrimeiroGrupo) #apostaPrimeiroGrupo
        usuario[17] = listaSelecoes().index(apostaSegundoGrupo) #apostaSegundoGrupo
    elif nomeGrupo == 3:
        usuario[18] = listaSelecoes().index(apostaPrimeiroGrupo) #apostaPrimeiroGrupo
        usuario[19] = listaSelecoes().index(apostaSegundoGrupo) #apostaSegundoGrupo
    elif nomeGrupo == 4:
        usuario[20] = listaSelecoes().index(apostaPrimeiroGrupo) #apostaPrimeiroGrupo
        usuario[21] = listaSelecoes().index(apostaSegundoGrupo) #apostaSegundoGrupo
    elif nomeGrupo == 5:
        usuario[22] = listaSelecoes().index(apostaPrimeiroGrupo) #apostaPrimeiroGrupo
        usuario[23] = listaSelecoes().index(apostaSegundoGrupo) #apostaSegundoGrupo
    elif nomeGrupo == 6:
        usuario[24] = listaSelecoes().index(apostaPrimeiroGrupo) #apostaPrimeiroGrupo
        usuario[25] = listaSelecoes().index(apostaSegundoGrupo) #apostaSegundoGrupo
    elif nomeGrupo == 7:
        usuario[26] = listaSelecoes().index(apostaPrimeiroGrupo) #apostaPrimeiroGrupo
        usuario[27] = listaSelecoes().index(apostaSegundoGrupo) #apostaSegundoGrupo

    return

def horarioJogo(anoJogo,mesJogo,diaJogo,horaJogo,minutoJogo):
    # data e horário atual
    dataHoraMinutoAtual = datetime.strptime(datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%d/%m/%y %H:%M'), '%d/%m/%y %H:%M')
        
    #data_atual = datetime.now()
    #data_string = data_atual.strftime('%d/%m/%y %H:%M')
    #dataHoraMinutoAtual =datetime.strptime(data_string, '%d/%m/%y %H:%M')

    #print(dataHoraMinutoAtual)
    #print('')
    dataHoraMinutoJogo = datetime(anoJogo,mesJogo,diaJogo,horaJogo,minutoJogo)
    
    #print(dataHoraMinutoJogo)
    #print('')
    if dataHoraMinutoAtual >= dataHoraMinutoJogo:
        inicioJogo = False
        #print('acabou!')
    else:
        inicioJogo = True
        #print('Dá uma seguradinha ..')
    
    return inicioJogo

def horarioJogoGrupo(nomeGrupo,nomeJogo):
    
    # datas e horários dos jogos da primeira fase
    
    if nomeGrupo == 0:
        # Grupo A
        if nomeJogo == 0:
            # Catar x Equador
            #inicioJogo = horarioJogo(2022,11,20,13,0)
            inicioJogo = horarioJogo(2022,11,20,23,0)
        elif nomeJogo == 1:
            # Senegal X Holanda
            inicioJogo = horarioJogo(2022,11,21,13,0)
        elif nomeJogo == 2:
            # Catar X Senegal
            inicioJogo = horarioJogo(2022,11,25,10,0)
        elif nomeJogo == 3:
            # Holanda X Equador
            inicioJogo = horarioJogo(2022,11,25,13,0)
        elif nomeJogo == 4:
            # Holanda X Catar
            inicioJogo = horarioJogo(2022,11,29,12,0)
        elif nomeJogo == 5:
            # Equador X Senegal
            inicioJogo = horarioJogo(2022,11,29,12,0)
    
    elif nomeGrupo == 1:
        # Grupo B
        if nomeJogo == 0:
            # Inglaterra X Irã
            inicioJogo = horarioJogo(2022,11,21,10,0)
        elif nomeJogo == 1:
            # Estados Unidos X País de Gales
            inicioJogo = horarioJogo(2022,11,21,16,0)
        elif nomeJogo == 2:
            # Inglaterra X Estados Unidos
            inicioJogo = horarioJogo(2022,11,25,16,0)
        elif nomeJogo == 3:
            # País de Gales X Irã
            inicioJogo = horarioJogo(2022,11,25,7,0)
        elif nomeJogo == 4:
            # País de Gales X Inglaterra
            inicioJogo = horarioJogo(2022,11,29,16,0)
        elif nomeJogo == 5:
            # Irã X Estados Unidos
            inicioJogo = horarioJogo(2022,11,29,16,0)
    
    elif nomeGrupo == 2:
        # Grupo C
        if nomeJogo == 0:
            # Argentina X Arábia Saudita
            inicioJogo = horarioJogo(2022,11,22,7,0)
        elif nomeJogo == 1:
            # México X Polônia
            inicioJogo = horarioJogo(2022,11,22,13,0)
        elif nomeJogo == 2:
            # Argentina X México
            inicioJogo = horarioJogo(2022,11,26,16,0)
        elif nomeJogo == 3:
            # Polônia X Arábia Saudita
            inicioJogo = horarioJogo(2022,11,26,10,0)
        elif nomeJogo == 4:
            # Polônia X Argentina
            inicioJogo = horarioJogo(2022,11,30,16,0)
        elif nomeJogo == 5:
            # Arábia Saudita
            inicioJogo = horarioJogo(2022,11,30,16,0)
    
    elif nomeGrupo == 3:
        # Grupo D
        if nomeJogo == 0:
            # França X Austrália
            inicioJogo = horarioJogo(2022,11,22,16,0)
        elif nomeJogo == 1:
            # Dinamarca X Tunísia
            inicioJogo = horarioJogo(2022,11,22,10,0)
        elif nomeJogo == 2:
            # França X Dinamarca
            inicioJogo = horarioJogo(2022,11,26,13,0)
        elif nomeJogo == 3:
            # Tunísia X Austrália
            inicioJogo = horarioJogo(2022,11,26,7,0)
        elif nomeJogo == 4:
            # Tunísia X França
            inicioJogo = horarioJogo(2022,11,30,12,0)
        elif nomeJogo == 5:
            # Austrália X Dinamarca
            inicioJogo = horarioJogo(2022,11,30,12,0)
    
    elif nomeGrupo == 4:
        # Grupo E
        if nomeJogo == 0:
            # Espanha X Costa Rica
            inicioJogo = horarioJogo(2022,11,23,13,0)
        elif nomeJogo == 1:
            # Alemanha X Japão
            inicioJogo = horarioJogo(2022,11,23,10,0)
        elif nomeJogo == 2:
            # Espanha X Alemanha
            inicioJogo = horarioJogo(2022,11,27,16,0)
        elif nomeJogo == 3:
            # Japão X Costa Rica
            inicioJogo = horarioJogo(2022,11,27,7,0)
        elif nomeJogo == 4:
            # Japão X Espanha
            inicioJogo = horarioJogo(2022,12,1,16,0)
        elif nomeJogo == 5:
            # Costa Rica X Alemanha
            inicioJogo = horarioJogo(2022,12,1,16,0)
    
    elif nomeGrupo == 5:
        # Grupo F
        if nomeJogo == 0:
            # Bélgica X Canadá
            inicioJogo = horarioJogo(2022,11,23,16,0)
        elif nomeJogo == 1:
            # Marrocos X Croácia
            inicioJogo = horarioJogo(2022,11,23,7,0)
        elif nomeJogo == 2:
            # Bélgica X Marrocos
            inicioJogo = horarioJogo(2022,11,27,10,0)
        elif nomeJogo == 3:
            # Croácia X Canadá
            inicioJogo = horarioJogo(2022,11,27,13,0)
        elif nomeJogo == 4:
            # Croácia X Bélgica
            inicioJogo = horarioJogo(2022,12,1,12,0)
        elif nomeJogo == 5:
            # Canadá X Marrocos
            inicioJogo = horarioJogo(2022,12,1,12,0)
    
    elif nomeGrupo == 6:
        # Grupo G
        if nomeJogo == 0:
            # Brasil X Sérvia
            inicioJogo = horarioJogo(2022,11,24,16,0)
        elif nomeJogo == 1:
            # Suíça X Camarões
            inicioJogo = horarioJogo(2022,11,24,7,0)
        elif nomeJogo == 2:
            # Brasil X Suíça
            inicioJogo = horarioJogo(2022,11,28,13,0)
        elif nomeJogo == 3:
            # Camarões X Sérvia
            inicioJogo = horarioJogo(2022,11,28,7,0)
        elif nomeJogo == 4:
            # Camarões X Brasil
            inicioJogo = horarioJogo(2022,12,2,16,0)
        elif nomeJogo == 5:
            # Sérvia X Suíça
            inicioJogo = horarioJogo(2022,12,2,16,0)
    
    elif nomeGrupo == 7:
        # Grupo H
        if nomeJogo == 0:
            # Portugal x Gana
            inicioJogo = horarioJogo(2022,11,24,13,0)
        elif nomeJogo == 1:
            # Uruguai X Coreia do Sul
            inicioJogo = horarioJogo(2022,11,24,10,0)
        elif nomeJogo == 2:
            # Portugal X Uruguai
            inicioJogo = horarioJogo(2022,11,28,16,0)
        elif nomeJogo == 3:
            # Coreia do Sul X Gana
            inicioJogo = horarioJogo(2022,11,28,10,0)
        elif nomeJogo == 4:
            # Coreia do Sul x Portugal
            inicioJogo = horarioJogo(2022,12,2,12,0)
        elif nomeJogo == 5:
            # Gana X Uruguai
            inicioJogo = horarioJogo(2022,12,2,12,0)
            #inicioJogo = horarioJogo(2022,11,20,9,0)
    
    return inicioJogo

def dataHorarioJogoGrupo(nomeGrupo,nomeJogo):
    
    # datas e horários dos jogos da primeira fase
    
    if nomeGrupo == 0:
        # Grupo A
        if nomeJogo == 0:
            # Catar x Equador
            #inicioJogo = datetime(2022,11,20,13,0)
            inicioJogo = datetime(2022,11,20,23,0)
        elif nomeJogo == 1:
            # Senegal X Holanda
            inicioJogo = datetime(2022,11,21,13,0)
        elif nomeJogo == 2:
            # Catar X Senegal
            inicioJogo = datetime(2022,11,25,10,0)
        elif nomeJogo == 3:
            # Holanda X Equador
            inicioJogo = datetime(2022,11,25,13,0)
        elif nomeJogo == 4:
            # Holanda X Catar
            inicioJogo = datetime(2022,11,29,12,0)
        elif nomeJogo == 5:
            # Equador X Senegal
            inicioJogo = datetime(2022,11,29,12,0)
    
    elif nomeGrupo == 1:
        # Grupo B
        if nomeJogo == 0:
            # Inglaterra X Irã
            inicioJogo = datetime(2022,11,21,10,0)
        elif nomeJogo == 1:
            # Estados Unidos X País de Gales
            inicioJogo = datetime(2022,11,21,16,0)
        elif nomeJogo == 2:
            # Inglaterra X Estados Unidos
            inicioJogo = datetime(2022,11,25,16,0)
        elif nomeJogo == 3:
            # País de Gales X Irã
            inicioJogo = datetime(2022,11,25,7,0)
        elif nomeJogo == 4:
            # País de Gales X Inglaterra
            inicioJogo = datetime(2022,11,29,16,0)
        elif nomeJogo == 5:
            # Irã X Estados Unidos
            inicioJogo = datetime(2022,11,29,16,0)
    
    elif nomeGrupo == 2:
        # Grupo C
        if nomeJogo == 0:
            # Argentina X Arábia Saudita
            inicioJogo = datetime(2022,11,22,7,0)
        elif nomeJogo == 1:
            # México X Polônia
            inicioJogo = datetime(2022,11,22,13,0)
        elif nomeJogo == 2:
            # Argentina X México
            inicioJogo = datetime(2022,11,26,16,0)
        elif nomeJogo == 3:
            # Polônia X Arábia Saudita
            inicioJogo = datetime(2022,11,26,10,0)
        elif nomeJogo == 4:
            # Polônia X Argentina
            inicioJogo = datetime(2022,11,30,16,0)
        elif nomeJogo == 5:
            # Arábia Saudita
            inicioJogo = datetime(2022,11,30,16,0)
    
    elif nomeGrupo == 3:
        # Grupo D
        if nomeJogo == 0:
            # França X Austrália
            inicioJogo = datetime(2022,11,22,16,0)
        elif nomeJogo == 1:
            # Dinamarca X Tunísia
            inicioJogo = datetime(2022,11,22,10,0)
        elif nomeJogo == 2:
            # França X Dinamarca
            inicioJogo = datetime(2022,11,26,13,0)
        elif nomeJogo == 3:
            # Tunísia X Austrália
            inicioJogo = datetime(2022,11,26,7,0)
        elif nomeJogo == 4:
            # Tunísia X França
            inicioJogo = datetime(2022,11,30,12,0)
        elif nomeJogo == 5:
            # Austrália X Dinamarca
            inicioJogo = datetime(2022,11,30,12,0)
    
    elif nomeGrupo == 4:
        # Grupo E
        if nomeJogo == 0:
            # Espanha X Costa Rica
            inicioJogo = datetime(2022,11,23,13,0)
        elif nomeJogo == 1:
            # Alemanha X Japão
            inicioJogo = datetime(2022,11,23,10,0)
        elif nomeJogo == 2:
            # Espanha X Alemanha
            inicioJogo = datetime(2022,11,27,16,0)
        elif nomeJogo == 3:
            # Japão X Costa Rica
            inicioJogo = datetime(2022,11,27,7,0)
        elif nomeJogo == 4:
            # Japão X Espanha
            inicioJogo = datetime(2022,12,1,16,0)
        elif nomeJogo == 5:
            # Costa Rica X Alemanha
            inicioJogo = datetime(2022,12,1,16,0)
    
    elif nomeGrupo == 5:
        # Grupo F
        if nomeJogo == 0:
            # Bélgica X Canadá
            inicioJogo = datetime(2022,11,23,16,0)
        elif nomeJogo == 1:
            # Marrocos X Croácia
            inicioJogo = datetime(2022,11,23,7,0)
        elif nomeJogo == 2:
            # Bélgica X Marrocos
            inicioJogo = datetime(2022,11,27,10,0)
        elif nomeJogo == 3:
            # Croácia X Canadá
            inicioJogo = datetime(2022,11,27,13,0)
        elif nomeJogo == 4:
            # Croácia X Bélgica
            inicioJogo = datetime(2022,12,1,12,0)
        elif nomeJogo == 5:
            # Canadá X Marrocos
            inicioJogo = datetime(2022,12,1,12,0)
    
    elif nomeGrupo == 6:
        # Grupo G
        if nomeJogo == 0:
            # Brasil X Sérvia
            inicioJogo = datetime(2022,11,24,16,0)
        elif nomeJogo == 1:
            # Suíça X Camarões
            inicioJogo = datetime(2022,11,24,7,0)
        elif nomeJogo == 2:
            # Brasil X Suíça
            inicioJogo = datetime(2022,11,28,13,0)
        elif nomeJogo == 3:
            # Camarões X Sérvia
            inicioJogo = datetime(2022,11,28,7,0)
        elif nomeJogo == 4:
            # Camarões X Brasil
            inicioJogo = datetime(2022,12,2,16,0)
        elif nomeJogo == 5:
            # Sérvia X Suíça
            inicioJogo = datetime(2022,12,2,16,0)
    
    elif nomeGrupo == 7:
        # Grupo H
        if nomeJogo == 0:
            # Portugal x Gana
            inicioJogo = datetime(2022,11,24,13,0)
        elif nomeJogo == 1:
            # Uruguai X Coreia do Sul
            inicioJogo = datetime(2022,11,24,10,0)
        elif nomeJogo == 2:
            # Portugal X Uruguai
            inicioJogo = datetime(2022,11,28,16,0)
        elif nomeJogo == 3:
            # Coreia do Sul X Gana
            inicioJogo = datetime(2022,11,28,10,0)
        elif nomeJogo == 4:
            # Coreia do Sul x Portugal
            inicioJogo = datetime(2022,12,2,12,0)
        elif nomeJogo == 5:
            # Gana X Uruguai
            inicioJogo = datetime(2022,12,2,12,0)

    return inicioJogo

def resumoApostas():

    apostas1 = []
    apostas2 = []
    apostas3 = []
    for j in range(1, len(usuariosLista), 1):
        if usuariosLista[j][9] != '':
            apostas1.append(listaSelecoes()[int(usuariosLista[j][9])])
        else:
            apostas1.append('Não apostou.')
            
        if usuariosLista[j][10] != '':
            apostas2.append(listaSelecoes()[int(usuariosLista[j][10])])
        else:
            apostas2.append('Não apostou.')
            
        if usuariosLista[j][11] != '':
            apostas3.append(listaSelecoes()[int(usuariosLista[j][11])])
        else:
            apostas3.append('Não apostou.')

    dadosApostasIniciais = np.array([apostas1,apostas2,apostas3])
    rotuloColuna = np.delete(np.array(usuariosLista)[:,0], 0)
    rotuloLinha  = ['Campeão','Vice-campeão','Terceiro colocado']
    ncoluna = len(rotuloColuna)
    nlinha  = len(rotuloLinha)

    espacos = ncoluna*[0.25]
    
    #figura = plt.figure(figsize = (6,1))
    figura = st.pyplot(figsize = (6,1))
    
    font = {'family':'serif', 'color':'black', 'weight':'normal', 'size':24}
    #plt.title('Apostas Iniciais', fontdict = font)
    st.pyplot.title('Apostas Iniciais', fontdict = font)
    
    #tabela = plt.table(cellText = dadosApostasIniciais,
    tabela = st.pyplot.table(cellText = dadosApostasIniciais,
                       colWidths = espacos,#[0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
                       #colWidths = [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
                       rowLabels = rotuloLinha,
                       colLabels = rotuloColuna)
    
    celula = tabela.properties()["celld"]
    for coluna in range(ncoluna):
        for linha in range(nlinha+1):
            celula[linha, coluna]._loc = 'center'
                       
    tabela.auto_set_font_size(False)
    tabela.set_fontsize(20)
    tabela.scale(2, 4)
    #plt.axis('off')
    st.pyplot.axis('off')
    #plt.show()
    
    return figura

#-----------------------------------------------------------------------------#
#=============================================================================#
#-----------------------------------------------------------------------------#

#st.title('Bolão')

#-----------------------------------------------------------------------------#

# DB Management
dados = sqlite3.connect('dados10.db')
d = dados.cursor()

def cria_tabela_usuarios():
    d.execute("CREATE TABLE IF NOT EXISTS tabela(login TEXT, senha TEXT)")

def adicionar_dados_usuarios(login, senha):
    d.execute("INSERT INTO tabela(login, senha) VALUES(?, ?)", (login, senha))
    dados.commit()

def login_usuario(username,password):
    d.execute('SELECT * FROM tabela WHERE login = ? AND senha = ?',(username,password))
    dado = d.fetchall()
    return dado

def todos_os_usuarios():
    d.execute('SELECT * FROM tabela')
    dado = d.fetchall()
    return dado

def usuarioMestre():
    cria_tabela_usuarios()
    usuariosLista = []
    # definindo a lista de usuarios e o usuario mestre
    if len(todos_os_usuarios()) == 0:
        cadastro = cadastroApostador('usuarioMestre','appBolao')
        np.save('usuarioMestre',cadastro)
        usuariosLista.append(cadastro)
        adicionar_dados_usuarios('usuarioMestre','appBolao')
        st.success('O usuário mestre foi criado.')
    else:
        for i in range(len(todos_os_usuarios())):
            usuario = np.load(str(np.array(todos_os_usuarios())[:,0][i])+'.npy')
            usuariosLista.append(usuario)

    return usuariosLista

def contagemRegressiva(ano,mes,dia,hora,minuto):
    '''
    A entrada com a data e hora do jogo e
    a saída a contagem regressiva
    '''
    # data e horário do jogo
    #dataHoraJogo = datetime(2022,11,24,16,0)
    dataHoraJogo = datetime(ano,mes,dia,hora,minuto)
    
    # data e horário atual
    data_atual = datetime.now()
    data_string = data_atual.strftime('%d/%m/%y %H:%M')
    data_convertida =datetime.strptime(data_string, '%d/%m/%y %H:%M')
    
    # looping para contar os minutos que faltam
    tempo = 0
    while dataHoraJogo != data_convertida:
        data_convertida = data_convertida + timedelta(minutes= 1)
        tempo = tempo + 1
            
    # O tempo precisa ser em segundos
    while tempo: 
        mins, secs = divmod(tempo, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        tempo -= 1
        
    return tempo

#-----------------------------------------------------------------------------#

# criando o usuario mestre
usuariosLista = usuarioMestre()

def main():
    
    #st.title('Bolão')
    ''' Simple Login App '''
    menu = ['Home','Cadastro','Login']
    choice = st.sidebar.selectbox('Menu',menu)

    #-----------------------------------------------------------------------------#

    if choice == 'Home':
        
        st.subheader('Acesso do administrador')
        
        username = st.text_input('Nome de usuário')
        password = st.text_input('Senha', type = 'password')
        #if username == usuarioLista[0][0] and password == usuarioLista[0][1]:
        if username == 'usuarioMestre' and password == 'appBolao':
            #task = st.selectbox('Task',['Add Post','Analytics','Profiles'])
            task = st.sidebar.selectbox('Task',['Add Post','Analytics','Profiles'])

            if task == 'Add Post':
                st.subheader('Add Your Post')
            elif task == 'Analytics':
                st.title('Analytics')
            elif task == 'Profiles':
                st.subheader('User Profiles')
                #user_result = view_all_users() # lista com todos os usuários
                #clean_db = pd.DataFrame(user_result, columns = ['Username','Password'])
                #clean_db = pd.DataFrame(user_result)
                #st.dataframe(clean_db)
                #st.subheader(user_result[0])
                #st.subheader(user_result[0][0])
                #st.subheader(user_result[0][1])
                #st.subheader(user_result[1])
                #st.subheader(user_result[2])
                #st.subheader(user_result[3])
                #st.subheader(user_result[4])
                #dados = login_user(user_result[0][0],user_result[0][1])
                #st.subheader(np.array(view_all_users())[:,0])

                todos_usuarios = todos_os_usuarios() # lista com todos os usuários
                clean_db = pd.DataFrame(todos_usuarios)
                st.dataframe(clean_db)
                #st.subheader(np.array(todos_os_usuarios())[0][0])
                #st.subheader(np.array(todos_os_usuarios())[:,0][0])
                #st.subheader(np.where(np.array(todos_os_usuarios())[:,0] == 'usuarioTeste1')[0][0])
                #st.subheader(todos_os_usuarios())
                st.subheader(usuariosLista)
        else:
            st.subheader('Você não tem acesso')

    #-----------------------------------------------------------------------------#

    elif choice == 'Cadastro':
        st.subheader('Criar nova conta')
        new_user = st.text_input('Nome de usuário')
        new_password = st.text_input('Senha', type = 'password')

        if st.button('Cadastrar'):
            cria_tabela_usuarios()
            #create_usertable()
            #add_userdata(new_user,new_password)
            #st.success('You have sucessfully created an valid Account')
            #st.info('Go to login Menu to login')
            if new_user == '' or new_password == '':
                st.error('Preencha todos os campos para realizar o cadastro.')
            else:
                for usuarios in range(len(todos_os_usuarios())):
                    if new_user == np.array(todos_os_usuarios())[:,0][usuarios]:
                        st.error('Esse usuário já existe.')
                        st.warning('Tente outro nome de usuário')
                        break
                    elif usuarios == len(todos_os_usuarios())-1:
                        cadastro = cadastroApostador(new_user,new_password)
                        np.save(str(new_user),cadastro)
                        usuariosLista.append(cadastro)
                        adicionar_dados_usuarios(new_user,new_password)
                        
                        st.success('Você criou uma conta válida com sucesso')
                        st.info('Vá ao Menu para fazer login')
    
    #-----------------------------------------------------------------------------#

    elif choice == 'Login':
        username = st.sidebar.text_input('Nome de usuário')
        password = st.sidebar.text_input('Senha', type = 'password')

        if st.sidebar.checkbox('Login'):
            # pegar o índice do usuario
            indiceUsuario = np.where(np.array(todos_os_usuarios())[:,0] == username)[0][0]
            usuario = usuariosLista[indiceUsuario]
            #st.subheader(listaSelecoes()[int(usuariosLista[0][9])])
            #cria_tabela_usuarios()

            result = login_usuario(username,password)
            if result:
                st.sidebar.success('Você está logado como {}'.format(username))
                task = st.sidebar.selectbox(label = 'Selecionar o campeonato', options = ['Copa do Mundo 2022','Outros'], index = 1)
                
                if task == 'Copa do Mundo 2022':
                    st.title('Bolão da Copa do Mundo 2022')
                    task1 = st.sidebar.selectbox(label = 'Selecionar o campeonato', options = ['Apostas iniciais','Apostas fase de grupos','Apostas nas fases eliminatórias','Resumo das apostas','Links externos'], index = 0)
                    
                    if task1 == 'Apostas iniciais':                        
                        inicioCopa = horarioJogo(2022,11,21,23,0)
                        #st.subheader(inicioCopa)
                        #st.subheader(datetime.strptime(datetime.now().strftime('%d/%m/%y %H:%M'), '%d/%m/%y %H:%M'))

                        opcoesBolao = ['Campeão do mundo','Vice de nada','cara que não sabe de futebol, mas não vai ser o pior do bolão','Pangaré do futebol']
                        opcoes = [0,1,2,3,4]
                        with st.form(key = 'include_bolao'):
                            apostaBolao = st.selectbox('Selecione a posição que ficará no bolão', options = opcoesBolao, index = 3)
                            botaoBolao = st.form_submit_button(label = 'Apostar')
                        if botaoBolao and inicioCopa:
                            usuario[8] = opcoes[opcoesBolao.index(apostaBolao)]
                            np.save(str(username),usuario)
                        if usuario[8] != '':
                            st.subheader('Aposta registrada!')
                            st.write(f'Você vai ser o {opcoesBolao[int(usuario[8])]} !')
                        
                        #-----------------------------------------------------------------------------#

                        st.title('Apostas iniciais - 13:00 20/11/2022')
                        with st.form(key = 'include_campeao'):
                            apostaCampeao = st.selectbox('Quem será o campeão da Copa do Mundo 2022?', options = listaSelecoes(), index = 0)
                            apostaViceCampeao = st.selectbox('Quem será o vice campeão da Copa do Mundo 2022?', options = listaSelecoes(), index = 0)
                            apostaTerceiroColocado = st.selectbox('Quem será o terceiro colocado da Copa do Mundo 2022?', options = listaSelecoes(), index = 0)
                            botaoApostaCampeao = st.form_submit_button(label = 'Apostar')
                        if botaoApostaCampeao and inicioCopa:
                            apostaPodio(usuario,apostaCampeao,apostaViceCampeao,apostaTerceiroColocado)
                            np.save(str(username),usuario)
                        if usuario[9] != '':
                            st.subheader('Apostas registradas!')
                            st.write(f'Aposta campeão: {listaSelecoes()[int(usuario[9])]}')
                            st.write(f'Aposta vice campeão: {listaSelecoes()[int(usuario[10])]}')
                            st.write(f'Aposta terceiro colocado: {listaSelecoes()[int(usuario[11])]}')
                        
                        #-----------------------------------------------------------------------------#

                        for nomeGrupo in range(len(grupos()[:,0])):
                            st.subheader(f'Grupo {grupos()[nomeGrupo][-1]}')
                            with st.form(key = 'include_aposta_grupo_'+str(grupos()[nomeGrupo][-1])):
                                apostaPrimeiro = st.selectbox('Quem será o primeiro colocado?', options = np.delete(grupos()[nomeGrupo],-1), index = 0)
                                apostaSegundo  = st.selectbox('Quem será o segundo colocado?', options = np.delete(grupos()[nomeGrupo],-1), index = 0)
                                botaoApostaGrupos = st.form_submit_button(label = 'Apostar no grupo '+str(grupos()[nomeGrupo][-1]))
                            if botaoApostaGrupos and inicioCopa:
                                apostaGrupos(usuario,nomeGrupo,apostaPrimeiro,apostaSegundo)
                                np.save(str(username),usuario)
                            if usuario[2*nomeGrupo+12] != '':
                                st.subheader('Apostas registradas!')
                                st.write(f'Aposta primeiro colocado: {listaSelecoes()[int(usuario[2*nomeGrupo+12])]}')
                                st.write(f'Aposta primeiro colocado: {listaSelecoes()[int(usuario[2*nomeGrupo+13])]}')

                        #-----------------------------------------------------------------------------#

                    elif task1 == 'Apostas fase de grupos':
                        st.title('Fase de Grupos')

                        for nomeGrupo in range(len(grupos()[:,0])):

                            st.subheader(f'Grupo {grupos()[nomeGrupo][-1]}')
                            # Datas e horários dos jogos

                            for nomeJogo in range(6):
                                with st.form(key = 'include_aposta_jogo_'+str(nomeJogo+1)+'do_grupo_'+str(grupos()[nomeGrupo][-1])):

                                    #aposta_jogo_primeira_fase = st.selectbox('Escolha o jogo que deseja apostar', options = ['Jogo 1: ','Jogo 2: ','Jogo 3: ','Jogo 4: ','Jogo 5: ','Jogo 6: '], index = 0)
                                    #if aposta_jogo_primeira_fase == 'Jogo 2: ':
                                    #    aposta_selecao_1 = st.number_input(label = 'Seleção 4', min_value = 0, max_value = 20, step = 1, format = '%d')                                
                                    #st.subheader(f'Grupo {grupos()[nomeGrupo][-1]} - Jogo {nomeJogo+1} - RELÓGIO TIC TAC')
                                    st.subheader(f'Grupo {grupos()[nomeGrupo][-1]} - Jogo {nomeJogo+1} - {dataHorarioJogoGrupo(nomeGrupo,nomeJogo)}')
                                    
                                    # rodada e jogo
                                    #nomeRodada = int(input('Qual rodada você quer apostar? '))
                                    if nomeJogo == 0 or nomeJogo == 1:
                                        nomeRodada = 1
                                    elif nomeJogo == 2 or nomeJogo == 3:
                                        nomeRodada = 2
                                    elif nomeJogo == 4 or nomeJogo == 5:
                                        nomeRodada = 3
                                    
                                    if nomeRodada == 1:
                                        # Time i1 = 0
                                        # Time i2 = 1
                                        # Time i3 = 2
                                        # Time i4 = 3
                                        # rodada 1: Time i1 x Time i2
                                        # rodada 1: Time i3 x Time i4
                                        time1 = 0
                                        time2 = 1
                                        time3 = 2
                                        time4 = 3
                                        if nomeJogo == 0:
                                            #print('')
                                            #print('Jogo 1')
                                            #print('%s X %s'%(grupos()[nomeGrupo][time1], grupos()[nomeGrupo][time2]))
                                            aposta_selecao_1 = st.number_input(label = grupos()[nomeGrupo][time1], min_value = 0, max_value = 10, step = 1, format = '%d')
                                            aposta_selecao_2 = st.number_input(label = grupos()[nomeGrupo][time2], min_value = 0, max_value = 10, step = 1, format = '%d')
                                            botao_jogo_1 = st.form_submit_button(label = f'Apostar no jogo {nomeJogo+1}')
                                            inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                                            #if botao_jogo_1:
                                            if botao_jogo_1 and inicioJogo:
                                                fazerApostaPrimeiraFase(usuario,nomeGrupo,nomeJogo,aposta_selecao_1,aposta_selecao_2)
                                                np.save(str(username),usuario)
                                            if usuario[28+2*6*nomeGrupo+2*nomeJogo] != '':
                                                st.subheader('Aposta registrada!')
                                                #st.write(f'{grupos()[nomeGrupo][time1]} {aposta_selecao_1} X {aposta_selecao_2} {grupos()[nomeGrupo][time2]}')
                                                st.write(f'{grupos()[nomeGrupo][time1]} {usuario[28+2*6*nomeGrupo+2*nomeJogo]} X {usuario[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time2]}')

                                        elif nomeJogo == 1:
                                            #print('')
                                            #print('Jogo 2')
                                            #print('%s X %s'%(grupos()[nomeGrupo][time3], grupos()[nomeGrupo][time4]))
                                            aposta_selecao_3 = st.number_input(label = grupos()[nomeGrupo][time3], min_value = 0, max_value = 10, step = 1, format = '%d')
                                            aposta_selecao_4 = st.number_input(label = grupos()[nomeGrupo][time4], min_value = 0, max_value = 10, step = 1, format = '%d')
                                            botao_jogo_2 = st.form_submit_button(label = f'Apostar no jogo {nomeJogo+1}')
                                            inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                                            #if botao_jogo_2:
                                            if botao_jogo_2 and inicioJogo:
                                                fazerApostaPrimeiraFase(usuario,nomeGrupo,nomeJogo,aposta_selecao_3,aposta_selecao_4)
                                                np.save(str(username),usuario)
                                            if usuario[28+2*6*nomeGrupo+2*nomeJogo] != '':
                                                st.subheader('Aposta registrada!')
                                                #st.write(f'{grupos()[nomeGrupo][time3]} {aposta_selecao_3} X {aposta_selecao_4} {grupos()[nomeGrupo][time4]}')
                                                st.write(f'{grupos()[nomeGrupo][time3]} {usuario[28+2*6*nomeGrupo+2*nomeJogo]} X {usuario[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time4]}')
                                    
                                    elif nomeRodada == 2:
                                        # Time i1 = 0
                                        # Time i2 = 1
                                        # Time i3 = 2
                                        # Time i4 = 3
                                        # rodada 2: Time i1 x Time i3
                                        # rodada 2: Time i2 x Time i4
                                        # rodada 2: Time i4 x Time i2 ALTERADA
                                        time1 = 0
                                        time2 = 2
                                        time3 = 3
                                        time4 = 1
                                        if nomeJogo == 2:
                                            #print('')
                                            #print('Jogo 3')
                                            #print('%s X %s'%(grupos()[nomeGrupo][time1], grupos()[nomeGrupo][time2]))
                                            aposta_selecao_1 = st.number_input(label = grupos()[nomeGrupo][time1], min_value = 0, max_value = 10, step = 1, format = '%d')
                                            aposta_selecao_2 = st.number_input(label = grupos()[nomeGrupo][time2], min_value = 0, max_value = 10, step = 1, format = '%d')
                                            botao_jogo_3 = st.form_submit_button(label = f'Apostar no jogo {nomeJogo+1}')
                                            inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                                            #if botao_jogo_3:
                                            if botao_jogo_3 and inicioJogo:
                                                fazerApostaPrimeiraFase(usuario,nomeGrupo,nomeJogo,aposta_selecao_1,aposta_selecao_2)
                                                np.save(str(username),usuario)
                                            if usuario[28+2*6*nomeGrupo+2*nomeJogo] != '':
                                                st.subheader('Aposta registrada!')
                                                #st.write(f'{grupos()[nomeGrupo][time1]} {aposta_selecao_1} X {aposta_selecao_2} {grupos()[nomeGrupo][time2]}')
                                                st.write(f'{grupos()[nomeGrupo][time1]} {usuario[28+2*6*nomeGrupo+2*nomeJogo]} X {usuario[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time2]}')

                                        elif nomeJogo == 3:
                                            #print('')
                                            #print('Jogo 4')
                                            #print('%s X %s'%(grupos()[nomeGrupo][time3], grupos()[nomeGrupo][time4]))
                                            aposta_selecao_3 = st.number_input(label = grupos()[nomeGrupo][time3], min_value = 0, max_value = 10, step = 1, format = '%d')
                                            aposta_selecao_4 = st.number_input(label = grupos()[nomeGrupo][time4], min_value = 0, max_value = 10, step = 1, format = '%d')
                                            botao_jogo_4 = st.form_submit_button(label = f'Apostar no jogo {nomeJogo+1}')
                                            inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                                            #if botao_jogo_4:
                                            if botao_jogo_4 and inicioJogo:
                                                fazerApostaPrimeiraFase(usuario,nomeGrupo,nomeJogo,aposta_selecao_3,aposta_selecao_4)
                                                np.save(str(username),usuario)
                                            if usuario[28+2*6*nomeGrupo+2*nomeJogo] != '':
                                                st.subheader('Aposta registrada!')
                                                #st.write(f'{grupos()[nomeGrupo][time3]} {aposta_selecao_3} X {aposta_selecao_4} {grupos()[nomeGrupo][time4]}')
                                                st.write(f'{grupos()[nomeGrupo][time3]} {usuario[28+2*6*nomeGrupo+2*nomeJogo]} X {usuario[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time4]}')

                                    elif nomeRodada == 3:
                                        # Time i1 = 0
                                        # Time i2 = 1
                                        # Time i3 = 2
                                        # Time i4 = 3
                                        # rodada 3: Time i4 x Time i1
                                        # rodada 3: Time i2 x Time i3
                                        time1 = 3
                                        time2 = 0
                                        time3 = 1
                                        time4 = 2
                                        if nomeJogo == 4:
                                            #print('')
                                            #print('Jogo 5')
                                            #print('%s X %s'%(grupos()[nomeGrupo][time1], grupos()[nomeGrupo][time2]))
                                            aposta_selecao_1 = st.number_input(label = grupos()[nomeGrupo][time1], min_value = 0, max_value = 10, step = 1, format = '%d')
                                            aposta_selecao_2 = st.number_input(label = grupos()[nomeGrupo][time2], min_value = 0, max_value = 10, step = 1, format = '%d')
                                            botao_jogo_5 = st.form_submit_button(label = f'Apostar no jogo {nomeJogo+1}')
                                            inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                                            #if botao_jogo_5:
                                            if botao_jogo_5 and inicioJogo:
                                                fazerApostaPrimeiraFase(usuario,nomeGrupo,nomeJogo,aposta_selecao_1,aposta_selecao_2)
                                                np.save(str(username),usuario)
                                            if usuario[28+2*6*nomeGrupo+2*nomeJogo] != '':
                                                st.subheader('Aposta registrada!')
                                                #st.write(f'{grupos()[nomeGrupo][time1]} {aposta_selecao_1} X {aposta_selecao_2} {grupos()[nomeGrupo][time2]}')
                                                st.write(f'{grupos()[nomeGrupo][time1]} {usuario[28+2*6*nomeGrupo+2*nomeJogo]} X {usuario[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time2]}')

                                        elif nomeJogo == 5:
                                            #print('')
                                            #print('Jogo 6')
                                            #print('%s X %s'%(grupos()[nomeGrupo][time3], grupos()[nomeGrupo][time4]))
                                            aposta_selecao_3 = st.number_input(label = grupos()[nomeGrupo][time3], min_value = 0, max_value = 10, step = 1, format = '%d')
                                            aposta_selecao_4 = st.number_input(label = grupos()[nomeGrupo][time4], min_value = 0, max_value = 10, step = 1, format = '%d')
                                            botao_jogo_6 = st.form_submit_button(label = f'Apostar no jogo {nomeJogo+1}')
                                            inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                                            #if botao_jogo_6:
                                            if botao_jogo_6 and inicioJogo:
                                                fazerApostaPrimeiraFase(usuario,nomeGrupo,nomeJogo,aposta_selecao_3,aposta_selecao_4)
                                                np.save(str(username),usuario)
                                            if usuario[28+2*6*nomeGrupo+2*nomeJogo] != '':
                                                st.subheader('Aposta registrada!')
                                                #st.write(f'{grupos()[nomeGrupo][time3]} {aposta_selecao_3} X {aposta_selecao_4} {grupos()[nomeGrupo][time4]}')
                                                st.write(f'{grupos()[nomeGrupo][time3]} {usuario[28+2*6*nomeGrupo+2*nomeJogo]} X {usuario[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time4]}')
                                            
                    elif task1 == 'Resumo das apostas':
                        st.header('Resumo das apostas')
                        #figuraInicial = resumoApostas()
                        #st.pyplot(figuraInicial)
                        
                        #def criandoTabs():
                        tabs = []
                        for tab in range(len(usuariosLista)):
                            tabs.append(np.array(usuariosLista)[tab][0])
                        tabs[0] = 'Bolão'
                        tabs = st.tabs(tabs)
                        for usuario in range(len(usuariosLista)):
                            if usuario == 0:
                                with tabs[usuario]:
                                    st.header(f'Resumo das apostas do Bolão')
                                    st.image("https://static.streamlit.io/examples/owl.jpg", width = 200)
                                    #df = pd.DataFrame(np.random.randn(10, 5), columns=('col %d' % i for i in range(5)))
                                    #df = pd.DataFrame(np.array([[listaSelecoes()[int(np.array(usuariosLista)[usuario][9])], listaSelecoes()[int(np.array(usuariosLista)[usuario][10])], listaSelecoes()[int(np.array(usuariosLista)[usuario][11])]]]),
                                    df = pd.DataFrame(np.array([[1,2,3],[4,5,6]]),
                                                      columns = ('Campeão','Vice-campeão','Terceiro colocado'))
                                    st.table(df)
                            else:
                                with tabs[usuario]:
                                    st.header(f'Resumo das apostas - {np.array(usuariosLista)[usuario][0]}')
                                    #image = Image.open('CampoSLpaper.png')
                                    #st.image(image, caption='Sunrise by the mountains')
                                    
                                    if np.array(usuariosLista)[usuario][9] != '':
                                        apostaCampeao = listaSelecoes()[int(np.array(usuariosLista)[usuario][9])]
                                    else:
                                        apostaCampeao = 'Não apostou no campeão'
                                        
                                    if np.array(usuariosLista)[usuario][10] != '':
                                        apostaViceCampeao = listaSelecoes()[int(np.array(usuariosLista)[usuario][10])]
                                    else:
                                        apostaViceCampeao = 'Não apostou no vice-campeão'
                                        
                                    if np.array(usuariosLista)[usuario][11] != '':
                                        apostaTerceiroColocado = listaSelecoes()[int(np.array(usuariosLista)[usuario][11])]
                                    else:
                                        apostaTerceiroColocado = 'Não apostou no terceiro colocado'
                                        
                                    df1 = pd.DataFrame(np.array([[apostaCampeao,apostaViceCampeao,apostaTerceiroColocado],
                                                        ['Fase de grupos','Fase de grupos','Fase de grupos']]),
                                                        columns = ('Campeão','Vice-campeão','Terceiro colocado'))
                                    df1.index = [f'Aposta - {np.array(usuariosLista)[usuario][0]}','Periodo da aposta']
                                    st.table(df1)

                                    apostasGrupos = []
                                    #for apostaGrupo in range(12, 28, 1):
                                    for apostaGrupo in range(12, 28, 2):
                                        if np.array(usuariosLista)[usuario][apostaGrupo] != '':
                                            apostasGrupos.append([listaSelecoes()[int(np.array(usuariosLista)[usuario][apostaGrupo])],listaSelecoes()[int(np.array(usuariosLista)[usuario][apostaGrupo+1])]])
                                        else:
                                            apostasGrupos.append(['Não apostou','Não apostou'])
                                    st.subheader(apostasGrupos)

                                    df2 = pd.DataFrame(np.array([[apostaTerceiroColocado,apostaTerceiroColocado],
                                                                 ['Fase de grupos','Fase de grupos'],
                                                                 ['Fase de grupos','Fase de grupos'],
                                                                 ['Fase de grupos','Fase de grupos'],
                                                                 ['Fase de grupos','Fase de grupos'],
                                                                 ['Fase de grupos','Fase de grupos'],
                                                                 ['Fase de grupos','Fase de grupos'],
                                                                 ['Fase de grupos','Fase de grupos']]),
                                                        columns = (f'Primeiro colocado - {np.array(usuariosLista)[usuario][0]}',f'Segundo colocado - {np.array(usuariosLista)[usuario][0]}'))
                                    #df2.index = [f'Aposta - {np.array(usuariosLista)[usuario][0]}','Periodo da aposta']
                                    df2.index = ['Grupo A','Grupo B','Grupo C','Grupo D','Grupo E','Grupo F','Grupo G','Grupo H']
                                    st.table(df2)
                                    
                                    st.image("https://static.streamlit.io/examples/cat.jpg", width = 200)
                            
                    elif task1 == 'Links externos':

                        classificacaoGE = 'https://ge.globo.com/futebol/copa-do-mundo/2022/'
                        if st.button('Classificação Globo Esporte'):
                            webbrowser.open_new_tab(classificacaoGE)
                        
                        simuladorGE = 'https://interativos.ge.globo.com/futebol/copa-do-mundo/especial/simulador-da-copa-do-mundo-2022'
                        if st.button('Simulador Globo Esporte'):
                            webbrowser.open_new_tab(simuladorGE)

                elif task == 'Outros':
                    st.title('Dá uma seguradinha que estamos começando ainda ... 🎈')

            else:
                st.error('Usuário/senha inválidos')
            
if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------------#
#=============================================================================#
#-----------------------------------------------------------------------------#
