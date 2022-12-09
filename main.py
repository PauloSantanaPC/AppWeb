#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#-----------------------------------------------------------------------------#
#=============================================================================#
#-----------------------------------------------------------------------------#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# Projeto - Bolão da Copa do Mundo
# Novembro 2022

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#-----------------------------------------------------------------------------#
#=============================================================================#
#-----------------------------------------------------------------------------#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# importanto bibliotecas
import streamlit as st
import sqlite3
import pandas as pd
import webbrowser
from datetime import date, datetime, time, timedelta
from time import strftime
import time
import pytz
import numpy as np # biblioteca Python usada para trabalhar com arrays
import pandas as pd

# pegando as funções externas
#from funcoes import *

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#-----------------------------------------------------------------------------#
#=============================================================================#
#-----------------------------------------------------------------------------#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


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

#-----------------------------------------------------------------------------#

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

#-----------------------------------------------------------------------------#

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
    numeroApostasFaseEliminatoria = 48
    numeroTotal = numeroApostasIniciais + numeroApostasPrimeiraFase + numeroApostasFaseEliminatoria
    for aposta in range(numeroTotal):
        apostador.append('')
    
    return apostador

#-----------------------------------------------------------------------------#

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

    cadastroApostador[28+2*6*nomeGrupo+2*nomeJogo], cadastroApostador[28+2*6*nomeGrupo+2*nomeJogo+1] = golMandante, golVisitante
    
    return cadastroApostador

#-----------------------------------------------------------------------------#

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

#-----------------------------------------------------------------------------#

def horarioJogo(anoJogo,mesJogo,diaJogo,horaJogo,minutoJogo):
    # data e horário atual
    dataHoraMinutoAtual = datetime.strptime(datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%d/%m/%y %H:%M'), '%d/%m/%y %H:%M')
    dataHoraMinutoJogo = datetime(anoJogo,mesJogo,diaJogo,horaJogo,minutoJogo)
    
    if dataHoraMinutoAtual >= dataHoraMinutoJogo:
        inicioJogo = False
    else:
        inicioJogo = True
    
    return inicioJogo

#-----------------------------------------------------------------------------#

def apostaPodio(usuario,apostaCampeao,apostaViceCampeao,apostaTerceiroColocado):
    
    # apostas podio
    usuario[9] = listaSelecoes().index(apostaCampeao) #apostaCampeao
    usuario[10] = listaSelecoes().index(apostaViceCampeao) #apostaViceCampeao
    usuario[11] = listaSelecoes().index(apostaTerceiroColocado) #apostaTerceiroColocado

    return

#-----------------------------------------------------------------------------#

def horarioJogoGrupo(nomeGrupo,nomeJogo):
    
    # datas e horários dos jogos da primeira fase
    if nomeGrupo == 0:
        # Grupo A
        if nomeJogo == 0:
            # Catar x Equador
            inicioJogo = horarioJogo(2022,11,20,13,0)
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
    
    return inicioJogo

#-----------------------------------------------------------------------------#

def dataHorarioJogoGrupo(nomeGrupo,nomeJogo):
    
    # datas e horários dos jogos da primeira fase
    if nomeGrupo == 0:
        # Grupo A
        if nomeJogo == 0:
            # Catar x Equador
            inicioJogo = datetime(2022,11,20,13,0)
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

#-----------------------------------------------------------------------------#

def classificacaoInicial():
    
    '''
    
    Classificação antes do início da copa do mundo
    
    '''
    
    #numeroSelecoes = len(grupos()[0])-1 # Número de times por grupo
    selecoes = [] # array das seleções
    pontosSelecao = 0
    jogos         = 0
    vitorias      = 0
    empates       = 0
    derrotas      = 0
    golsPro       = 0
    golsContra    = 0
    saldoGols     = 0
    
    # looping para montar os grupos
    for grupo in range(len(grupos())):
        s = []
        for selecao in range(len(grupos()[0])):
            s.append([grupos()[grupo][selecao], pontosSelecao, jogos, vitorias, empates, derrotas, golsPro, golsContra, saldoGols])
        selecoes.append(s)
    
    return selecoes

#-----------------------------------------------------------------------------#

def classificacaoFaseGrupos(selecoes, nomeGrupo, nomeJogo, golMandante, golVisitante):

    '''
    
    Classificação primeira fase:
    
    nomes dos grupos: grupo A = 0; grupo B = 1; grupo C = 2; grupo D = 3; grupo E = 4; grupo F = 5; grupo G = 6; grupo H = 7.
    
    nomes dos jogos: jogo 1 = 0; jogo 2 = 1; jogo 3 = 2; jogo 4 = 3; jogo 5 = 4; jogo 6 = 5.
    
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
            
            # gols
            selecoes[nomeGrupo][time1].append(golMandante)
            selecoes[nomeGrupo][time2].append(golVisitante)

            # Número de jogos
            selecoes[nomeGrupo][time1][2] = selecoes[nomeGrupo][time1][2]+1 # número de jogos que o time i1 fez
            selecoes[nomeGrupo][time2][2] = selecoes[nomeGrupo][time2][2]+1 # número de jogos que o time i2 fez
            # Gols pró
            selecoes[nomeGrupo][time1][6] = selecoes[nomeGrupo][time1][6]+selecoes[nomeGrupo][time1][-1] # gols que o time i1 fez
            selecoes[nomeGrupo][time2][6] = selecoes[nomeGrupo][time2][6]+selecoes[nomeGrupo][time2][-1] # gols que o time i2 fez
            # Gols contra
            selecoes[nomeGrupo][time1][7] = selecoes[nomeGrupo][time1][7]+selecoes[nomeGrupo][time2][-1] # gols que o time i1 tomou
            selecoes[nomeGrupo][time2][7] = selecoes[nomeGrupo][time2][7]+selecoes[nomeGrupo][time1][-1] # gols que o time i2 tomou
            # Saldo de gols
            selecoes[nomeGrupo][time1][8] = selecoes[nomeGrupo][time1][6]-selecoes[nomeGrupo][time1][7] # saldo de gols do time i1
            selecoes[nomeGrupo][time2][8] = selecoes[nomeGrupo][time2][6]-selecoes[nomeGrupo][time2][7] # saldo de gols do time i2

            # Jogo 1
            if selecoes[nomeGrupo][time1][-1]==selecoes[nomeGrupo][time2][-1]: # empate
                selecoes[nomeGrupo][time1][1] = selecoes[nomeGrupo][time1][1]+1 # soma um ponto
                selecoes[nomeGrupo][time2][1] = selecoes[nomeGrupo][time2][1]+1 # soma um ponto
                selecoes[nomeGrupo][time1][4] = selecoes[nomeGrupo][time1][4]+1 # mais um empate
                selecoes[nomeGrupo][time2][4] = selecoes[nomeGrupo][time2][4]+1 # mais um empate
            elif selecoes[nomeGrupo][time1][-1]>selecoes[nomeGrupo][time2][-1]: # vitoria mandante
                selecoes[nomeGrupo][time1][1] = selecoes[nomeGrupo][time1][1]+3 # soma três pontos
                selecoes[nomeGrupo][time2][1] = selecoes[nomeGrupo][time2][1]+0 # nenhum ponto
                selecoes[nomeGrupo][time1][3] = selecoes[nomeGrupo][time1][3]+1 # mais uma vitória
                selecoes[nomeGrupo][time2][5] = selecoes[nomeGrupo][time2][5]+1 # mais uma derrota
            elif selecoes[nomeGrupo][time1][-1]<selecoes[nomeGrupo][time2][-1]: # derrota mandante
                selecoes[nomeGrupo][time1][1] = selecoes[nomeGrupo][time1][1]+0 # nenhum ponto
                selecoes[nomeGrupo][time2][1] = selecoes[nomeGrupo][time2][1]+3 # soma três pontos
                selecoes[nomeGrupo][time1][5] = selecoes[nomeGrupo][time1][5]+1 # mais uma vitória
                selecoes[nomeGrupo][time2][3] = selecoes[nomeGrupo][time2][3]+1 # mais uma derrota

        elif nomeJogo == 1:
            
            # gols
            selecoes[nomeGrupo][time3].append(golMandante)
            selecoes[nomeGrupo][time4].append(golVisitante)
            
            # Número de jogos
            selecoes[nomeGrupo][time3][2] = selecoes[nomeGrupo][time3][2]+1 # número de jogos que o time i3 fez
            selecoes[nomeGrupo][time4][2] = selecoes[nomeGrupo][time4][2]+1 # número de jogos que o time i4 fez
            # Gols pró
            selecoes[nomeGrupo][time3][6] = selecoes[nomeGrupo][time3][6]+selecoes[nomeGrupo][time3][-1] # gols que o time i3 fez
            selecoes[nomeGrupo][time4][6] = selecoes[nomeGrupo][time4][6]+selecoes[nomeGrupo][time4][-1] # gols que o time i4 fez
            # Gols contra
            selecoes[nomeGrupo][time3][7] = selecoes[nomeGrupo][time3][7]+selecoes[nomeGrupo][time4][-1] # gols que o time i3 tomou
            selecoes[nomeGrupo][time4][7] = selecoes[nomeGrupo][time4][7]+selecoes[nomeGrupo][time3][-1] # gols que o time i4 tomou
            # Saldo de gols
            selecoes[nomeGrupo][time3][8] = selecoes[nomeGrupo][time3][6]-selecoes[nomeGrupo][time3][7] # saldo de gols do time i3
            selecoes[nomeGrupo][time4][8] = selecoes[nomeGrupo][time4][6]-selecoes[nomeGrupo][time4][7] # saldo de gols do time i4

            # Jogo 2
            if selecoes[nomeGrupo][time3][-1]==selecoes[nomeGrupo][time4][-1]: # empate
                selecoes[nomeGrupo][time3][1] = selecoes[nomeGrupo][time3][1]+1 # soma um ponto
                selecoes[nomeGrupo][time4][1] = selecoes[nomeGrupo][time4][1]+1 # soma um ponto
                selecoes[nomeGrupo][time3][4] = selecoes[nomeGrupo][time3][4]+1 # mais um empate
                selecoes[nomeGrupo][time4][4] = selecoes[nomeGrupo][time4][4]+1 # mais um empate
            elif selecoes[nomeGrupo][time3][-1]>selecoes[nomeGrupo][time4][-1]: # vitoria mandante
                selecoes[nomeGrupo][time3][1] = selecoes[nomeGrupo][time3][1]+3 # soma três pontos
                selecoes[nomeGrupo][time4][1] = selecoes[nomeGrupo][time4][1]+0 # nenhum ponto
                selecoes[nomeGrupo][time3][3] = selecoes[nomeGrupo][time3][3]+1 # mais uma vitória
                selecoes[nomeGrupo][time4][5] = selecoes[nomeGrupo][time4][5]+1 # mais uma derrota
            elif selecoes[nomeGrupo][time3][-1]<selecoes[nomeGrupo][time4][-1]: # derrota mandante
                selecoes[nomeGrupo][time3][1] = selecoes[nomeGrupo][time3][1]+0 # nenhum ponto
                selecoes[nomeGrupo][time4][1] = selecoes[nomeGrupo][time4][1]+3 # soma três pontos
                selecoes[nomeGrupo][time3][5] = selecoes[nomeGrupo][time3][5]+1 # mais uma vitória
                selecoes[nomeGrupo][time4][3] = selecoes[nomeGrupo][time4][3]+1 # mais uma derrota

    elif nomeRodada == 2:
        # Time i1 = 0
        # Time i2 = 1
        # Time i3 = 2
        # Time i4 = 3
        # rodada 2: Time i1 x Time i3
        # rodada 2: Time i2 x Time i4
        time1 = 0
        time2 = 2
        time3 = 3
        time4 = 1
        if nomeJogo == 2:
            
            # gols
            selecoes[nomeGrupo][time1].append(golMandante)
            selecoes[nomeGrupo][time2].append(golVisitante)

            # Número de jogos
            selecoes[nomeGrupo][time1][2] = selecoes[nomeGrupo][time1][2]+1 # número de jogos que o time i1 fez
            selecoes[nomeGrupo][time2][2] = selecoes[nomeGrupo][time2][2]+1 # número de jogos que o time i2 fez
            # Gols pró
            selecoes[nomeGrupo][time1][6] = selecoes[nomeGrupo][time1][6]+selecoes[nomeGrupo][time1][-1] # gols que o time i1 fez
            selecoes[nomeGrupo][time2][6] = selecoes[nomeGrupo][time2][6]+selecoes[nomeGrupo][time2][-1] # gols que o time i2 fez
            # Gols contra
            selecoes[nomeGrupo][time1][7] = selecoes[nomeGrupo][time1][7]+selecoes[nomeGrupo][time2][-1] # gols que o time i1 tomou
            selecoes[nomeGrupo][time2][7] = selecoes[nomeGrupo][time2][7]+selecoes[nomeGrupo][time1][-1] # gols que o time i2 tomou
            # Saldo de gols
            selecoes[nomeGrupo][time1][8] = selecoes[nomeGrupo][time1][6]-selecoes[nomeGrupo][time1][7] # saldo de gols do time i1
            selecoes[nomeGrupo][time2][8] = selecoes[nomeGrupo][time2][6]-selecoes[nomeGrupo][time2][7] # saldo de gols do time i2

            # Jogo 1
            if selecoes[nomeGrupo][time1][-1]==selecoes[nomeGrupo][time2][-1]: # empate
                selecoes[nomeGrupo][time1][1] = selecoes[nomeGrupo][time1][1]+1 # soma um ponto
                selecoes[nomeGrupo][time2][1] = selecoes[nomeGrupo][time2][1]+1 # soma um ponto
                selecoes[nomeGrupo][time1][4] = selecoes[nomeGrupo][time1][4]+1 # mais um empate
                selecoes[nomeGrupo][time2][4] = selecoes[nomeGrupo][time2][4]+1 # mais um empate
            elif selecoes[nomeGrupo][time1][-1]>selecoes[nomeGrupo][time2][-1]: # vitoria mandante
                selecoes[nomeGrupo][time1][1] = selecoes[nomeGrupo][time1][1]+3 # soma três pontos
                selecoes[nomeGrupo][time2][1] = selecoes[nomeGrupo][time2][1]+0 # nenhum ponto
                selecoes[nomeGrupo][time1][3] = selecoes[nomeGrupo][time1][3]+1 # mais uma vitória
                selecoes[nomeGrupo][time2][5] = selecoes[nomeGrupo][time2][5]+1 # mais uma derrota
            elif selecoes[nomeGrupo][time1][-1]<selecoes[nomeGrupo][time2][-1]: # derrota mandante
                selecoes[nomeGrupo][time1][1] = selecoes[nomeGrupo][time1][1]+0 # nenhum ponto
                selecoes[nomeGrupo][time2][1] = selecoes[nomeGrupo][time2][1]+3 # soma três pontos
                selecoes[nomeGrupo][time1][5] = selecoes[nomeGrupo][time1][5]+1 # mais uma vitória
                selecoes[nomeGrupo][time2][3] = selecoes[nomeGrupo][time2][3]+1 # mais uma derrota

        elif nomeJogo == 3:
            
            # gols
            selecoes[nomeGrupo][time3].append(golMandante)
            selecoes[nomeGrupo][time4].append(golVisitante)
            
            # Número de jogos
            selecoes[nomeGrupo][time3][2] = selecoes[nomeGrupo][time3][2]+1 # número de jogos que o time i3 fez
            selecoes[nomeGrupo][time4][2] = selecoes[nomeGrupo][time4][2]+1 # número de jogos que o time i4 fez
            # Gols pró
            selecoes[nomeGrupo][time3][6] = selecoes[nomeGrupo][time3][6]+selecoes[nomeGrupo][time3][-1] # gols que o time i3 fez
            selecoes[nomeGrupo][time4][6] = selecoes[nomeGrupo][time4][6]+selecoes[nomeGrupo][time4][-1] # gols que o time i4 fez
            # Gols contra
            selecoes[nomeGrupo][time3][7] = selecoes[nomeGrupo][time3][7]+selecoes[nomeGrupo][time4][-1] # gols que o time i3 tomou
            selecoes[nomeGrupo][time4][7] = selecoes[nomeGrupo][time4][7]+selecoes[nomeGrupo][time3][-1] # gols que o time i4 tomou
            # Saldo de gols
            selecoes[nomeGrupo][time3][8] = selecoes[nomeGrupo][time3][6]-selecoes[nomeGrupo][time3][7] # saldo de gols do time i3
            selecoes[nomeGrupo][time4][8] = selecoes[nomeGrupo][time4][6]-selecoes[nomeGrupo][time4][7] # saldo de gols do time i4

            # Jogo 2
            if selecoes[nomeGrupo][time3][-1]==selecoes[nomeGrupo][time4][-1]: # empate
                selecoes[nomeGrupo][time3][1] = selecoes[nomeGrupo][time3][1]+1 # soma um ponto
                selecoes[nomeGrupo][time4][1] = selecoes[nomeGrupo][time4][1]+1 # soma um ponto
                selecoes[nomeGrupo][time3][4] = selecoes[nomeGrupo][time3][4]+1 # mais um empate
                selecoes[nomeGrupo][time4][4] = selecoes[nomeGrupo][time4][4]+1 # mais um empate
            elif selecoes[nomeGrupo][time3][-1]>selecoes[nomeGrupo][time4][-1]: # vitoria mandante
                selecoes[nomeGrupo][time3][1] = selecoes[nomeGrupo][time3][1]+3 # soma três pontos
                selecoes[nomeGrupo][time4][1] = selecoes[nomeGrupo][time4][1]+0 # nenhum ponto
                selecoes[nomeGrupo][time3][3] = selecoes[nomeGrupo][time3][3]+1 # mais uma vitória
                selecoes[nomeGrupo][time4][5] = selecoes[nomeGrupo][time4][5]+1 # mais uma derrota
            elif selecoes[nomeGrupo][time3][-1]<selecoes[nomeGrupo][time4][-1]: # derrota mandante
                selecoes[nomeGrupo][time3][1] = selecoes[nomeGrupo][time3][1]+0 # nenhum ponto
                selecoes[nomeGrupo][time4][1] = selecoes[nomeGrupo][time4][1]+3 # soma três pontos
                selecoes[nomeGrupo][time3][5] = selecoes[nomeGrupo][time3][5]+1 # mais uma vitória
                selecoes[nomeGrupo][time4][3] = selecoes[nomeGrupo][time4][3]+1 # mais uma derrota

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
            
            # gols
            selecoes[nomeGrupo][time1].append(golMandante)
            selecoes[nomeGrupo][time2].append(golVisitante)

            # Número de jogos
            selecoes[nomeGrupo][time1][2] = selecoes[nomeGrupo][time1][2]+1 # número de jogos que o time i1 fez
            selecoes[nomeGrupo][time2][2] = selecoes[nomeGrupo][time2][2]+1 # número de jogos que o time i2 fez
            # Gols pró
            selecoes[nomeGrupo][time1][6] = selecoes[nomeGrupo][time1][6]+selecoes[nomeGrupo][time1][-1] # gols que o time i1 fez
            selecoes[nomeGrupo][time2][6] = selecoes[nomeGrupo][time2][6]+selecoes[nomeGrupo][time2][-1] # gols que o time i2 fez
            # Gols contra
            selecoes[nomeGrupo][time1][7] = selecoes[nomeGrupo][time1][7]+selecoes[nomeGrupo][time2][-1] # gols que o time i1 tomou
            selecoes[nomeGrupo][time2][7] = selecoes[nomeGrupo][time2][7]+selecoes[nomeGrupo][time1][-1] # gols que o time i2 tomou
            # Saldo de gols
            selecoes[nomeGrupo][time1][8] = selecoes[nomeGrupo][time1][6]-selecoes[nomeGrupo][time1][7] # saldo de gols do time i1
            selecoes[nomeGrupo][time2][8] = selecoes[nomeGrupo][time2][6]-selecoes[nomeGrupo][time2][7] # saldo de gols do time i2

            # Jogo 1
            if selecoes[nomeGrupo][time1][-1]==selecoes[nomeGrupo][time2][-1]: # empate
                selecoes[nomeGrupo][time1][1] = selecoes[nomeGrupo][time1][1]+1 # soma um ponto
                selecoes[nomeGrupo][time2][1] = selecoes[nomeGrupo][time2][1]+1 # soma um ponto
                selecoes[nomeGrupo][time1][4] = selecoes[nomeGrupo][time1][4]+1 # mais um empate
                selecoes[nomeGrupo][time2][4] = selecoes[nomeGrupo][time2][4]+1 # mais um empate
            elif selecoes[nomeGrupo][time1][-1]>selecoes[nomeGrupo][time2][-1]: # vitoria mandante
                selecoes[nomeGrupo][time1][1] = selecoes[nomeGrupo][time1][1]+3 # soma três pontos
                selecoes[nomeGrupo][time2][1] = selecoes[nomeGrupo][time2][1]+0 # nenhum ponto
                selecoes[nomeGrupo][time1][3] = selecoes[nomeGrupo][time1][3]+1 # mais uma vitória
                selecoes[nomeGrupo][time2][5] = selecoes[nomeGrupo][time2][5]+1 # mais uma derrota
            elif selecoes[nomeGrupo][time1][-1]<selecoes[nomeGrupo][time2][-1]: # derrota mandante
                selecoes[nomeGrupo][time1][1] = selecoes[nomeGrupo][time1][1]+0 # nenhum ponto
                selecoes[nomeGrupo][time2][1] = selecoes[nomeGrupo][time2][1]+3 # soma três pontos
                selecoes[nomeGrupo][time1][5] = selecoes[nomeGrupo][time1][5]+1 # mais uma vitória
                selecoes[nomeGrupo][time2][3] = selecoes[nomeGrupo][time2][3]+1 # mais uma derrota

        elif nomeJogo == 5:
            
            # gols
            selecoes[nomeGrupo][time3].append(golMandante)
            selecoes[nomeGrupo][time4].append(golVisitante)
            
            # Número de jogos
            selecoes[nomeGrupo][time3][2] = selecoes[nomeGrupo][time3][2]+1 # número de jogos que o time i3 fez
            selecoes[nomeGrupo][time4][2] = selecoes[nomeGrupo][time4][2]+1 # número de jogos que o time i4 fez
            # Gols pró
            selecoes[nomeGrupo][time3][6] = selecoes[nomeGrupo][time3][6]+selecoes[nomeGrupo][time3][-1] # gols que o time i3 fez
            selecoes[nomeGrupo][time4][6] = selecoes[nomeGrupo][time4][6]+selecoes[nomeGrupo][time4][-1] # gols que o time i4 fez
            # Gols contra
            selecoes[nomeGrupo][time3][7] = selecoes[nomeGrupo][time3][7]+selecoes[nomeGrupo][time4][-1] # gols que o time i3 tomou
            selecoes[nomeGrupo][time4][7] = selecoes[nomeGrupo][time4][7]+selecoes[nomeGrupo][time3][-1] # gols que o time i4 tomou
            # Saldo de gols
            selecoes[nomeGrupo][time3][8] = selecoes[nomeGrupo][time3][6]-selecoes[nomeGrupo][time3][7] # saldo de gols do time i3
            selecoes[nomeGrupo][time4][8] = selecoes[nomeGrupo][time4][6]-selecoes[nomeGrupo][time4][7] # saldo de gols do time i4

            # Jogo 2
            if selecoes[nomeGrupo][time3][-1]==selecoes[nomeGrupo][time4][-1]: # empate
                selecoes[nomeGrupo][time3][1] = selecoes[nomeGrupo][time3][1]+1 # soma um ponto
                selecoes[nomeGrupo][time4][1] = selecoes[nomeGrupo][time4][1]+1 # soma um ponto
                selecoes[nomeGrupo][time3][4] = selecoes[nomeGrupo][time3][4]+1 # mais um empate
                selecoes[nomeGrupo][time4][4] = selecoes[nomeGrupo][time4][4]+1 # mais um empate
            elif selecoes[nomeGrupo][time3][-1]>selecoes[nomeGrupo][time4][-1]: # vitoria mandante
                selecoes[nomeGrupo][time3][1] = selecoes[nomeGrupo][time3][1]+3 # soma três pontos
                selecoes[nomeGrupo][time4][1] = selecoes[nomeGrupo][time4][1]+0 # nenhum ponto
                selecoes[nomeGrupo][time3][3] = selecoes[nomeGrupo][time3][3]+1 # mais uma vitória
                selecoes[nomeGrupo][time4][5] = selecoes[nomeGrupo][time4][5]+1 # mais uma derrota
            elif selecoes[nomeGrupo][time3][-1]<selecoes[nomeGrupo][time4][-1]: # derrota mandante
                selecoes[nomeGrupo][time3][1] = selecoes[nomeGrupo][time3][1]+0 # nenhum ponto
                selecoes[nomeGrupo][time4][1] = selecoes[nomeGrupo][time4][1]+3 # soma três pontos
                selecoes[nomeGrupo][time3][5] = selecoes[nomeGrupo][time3][5]+1 # mais uma vitória
                selecoes[nomeGrupo][time4][3] = selecoes[nomeGrupo][time4][3]+1 # mais uma derrota

    return selecoes

#-----------------------------------------------------------------------------#

def resultadoJogo(golMandante, golVisitante):

    '''
    
    Resultado jogo
        
    '''
    
    #-------------------------------------------------------------------------#        
    
    vitoria = False
    empate  = False
    derrota = False

    if golMandante != '':    
        if golMandante == golVisitante: # empate
            empate = True
        elif golMandante > golVisitante: # vitoria mandante
            vitoria = True
        elif golMandante < golVisitante: # derrota mandante
            derrota = True

    return vitoria, empate, derrota

#-----------------------------------------------------------------------------#

def resultadoApostadorFaseGrupos(usuario,pontuacao,golMandanteApostador,golVisitanteApostador,golMandanteJogo,golVisitanteJogo):
    
    '''
    
    Função que contabiliza os pontos do usuario para um jogo na fase de grupos
    
    '''
    
    vitoria, empate, derrota = resultadoJogo(golMandanteJogo,golVisitanteJogo)
    vitoriaApostador, empateApostador, derrotaApostador = resultadoJogo(golMandanteApostador,golVisitanteApostador)
    if vitoria:
        if vitoriaApostador:
            if golMandanteJogo == golMandanteApostador and golVisitanteJogo == golVisitanteApostador:
                # cravada
                usuario[3] = int(usuario[3]) + 1
                usuario[2] = int(usuario[2]) + 10
                pontuacao += 10
            else:
                # acerto
                usuario[4] = int(usuario[4]) + 1
                usuario[2] = int(usuario[2]) + 7
                pontuacao += 7
        elif derrotaApostador:
            # erro
            usuario[5] = int(usuario[5]) + 1
            usuario[2] = int(usuario[2]) - 7
            pontuacao += -7
        elif empateApostador:
            # nada
            usuario[6] = int(usuario[6]) + 1
            usuario[2] = int(usuario[2]) + 0
            pontuacao += 0
        if golMandanteApostador == '':
            # não apostou
            usuario[7] = int(usuario[7]) + 1
            usuario[2] = int(usuario[2]) - 10
            pontuacao += -10
            
    #-------------------------------------------------------------------------#
            
    elif empate:
        if vitoriaApostador:
            # nada
            usuario[6] = int(usuario[6]) + 1
            usuario[2] = int(usuario[2]) + 0
            pontuacao += 0
        elif derrotaApostador:
            # nada
            usuario[6] = int(usuario[6]) + 1
            usuario[2] = int(usuario[2]) + 0
            pontuacao += 0
        elif empateApostador:
            if golMandanteJogo == golMandanteApostador and golVisitanteJogo == golVisitanteApostador:
                # cravada
                usuario[3] = int(usuario[3]) + 1
                usuario[2] = int(usuario[2]) + 10
                pontuacao += 10
            else:
                # acerto
                usuario[4] = int(usuario[4]) + 1
                usuario[2] = int(usuario[2]) + 7
                pontuacao += 7
        if golMandanteApostador == '':
            # não apostou
            usuario[7] = int(usuario[7]) + 1
            usuario[2] = int(usuario[2]) - 10
            pontuacao += -10
    
    #-------------------------------------------------------------------------#
    
    elif derrota:
        if vitoriaApostador:
            # erro
            usuario[5] = int(usuario[5]) + 1
            usuario[2] = int(usuario[2]) - 7
            pontuacao += -7
        elif derrotaApostador:
            if golMandanteJogo == golMandanteApostador and golVisitanteJogo == golVisitanteApostador:
                # cravada
                usuario[3] = int(usuario[3]) + 1
                usuario[2] = int(usuario[2]) + 10
                pontuacao += 10
            else:
                # acerto
                usuario[4] = int(usuario[4]) + 1
                usuario[2] = int(usuario[2]) + 7
                pontuacao += 7
        elif empateApostador:
            # nada
            usuario[6] = int(usuario[6]) + 1
            usuario[2] = int(usuario[2]) + 0
            pontuacao += 0
        if golMandanteApostador == '':
            # não apostou
            usuario[7] = int(usuario[7]) + 1
            usuario[2] = int(usuario[2]) - 10
            pontuacao += -10
            
    return usuario, pontuacao

#-----------------------------------------------------------------------------#

def resultadoApostadorFaseEliminatoria(usuario,pontuacao,golMandanteApostador,golVisitanteApostador,golMandanteJogo,golVisitanteJogo):
    
    '''
    
    Função que contabiliza os pontos do usuario para um jogo na fase eliminatoria
    
    '''
    
    vitoria, empate, derrota = resultadoJogo(golMandanteJogo,golVisitanteJogo)
    vitoriaApostador, empateApostador, derrotaApostador = resultadoJogo(golMandanteApostador,golVisitanteApostador)
    if vitoria:
        if vitoriaApostador:
            if golMandanteJogo == golMandanteApostador and golVisitanteJogo == golVisitanteApostador:
                # cravada
                usuario[3] = int(usuario[3]) + 1
                usuario[2] = int(usuario[2]) + 20
                pontuacao += 20
            else:
                # acerto
                usuario[4] = int(usuario[4]) + 1
                usuario[2] = int(usuario[2]) + 14
                pontuacao += 14
        elif derrotaApostador:
            # erro
            usuario[5] = int(usuario[5]) + 1
            usuario[2] = int(usuario[2]) - 14
            pontuacao += -14
        elif empateApostador:
            # nada
            usuario[6] = int(usuario[6]) + 1
            usuario[2] = int(usuario[2]) + 0
            pontuacao += 0
        if golMandanteApostador == '':
            # não apostou
            usuario[7] = int(usuario[7]) + 1
            usuario[2] = int(usuario[2]) - 20
            pontuacao += -20
            
    #-------------------------------------------------------------------------#
            
    elif empate:
        if vitoriaApostador:
            # nada
            usuario[6] = int(usuario[6]) + 1
            usuario[2] = int(usuario[2]) + 0
            pontuacao += 0
        elif derrotaApostador:
            # nada
            usuario[6] = int(usuario[6]) + 1
            usuario[2] = int(usuario[2]) + 0
            pontuacao += 0
        elif empateApostador:
            if golMandanteJogo == golMandanteApostador and golVisitanteJogo == golVisitanteApostador:
                # cravada
                usuario[3] = int(usuario[3]) + 1
                usuario[2] = int(usuario[2]) + 20
                pontuacao += 20
            else:
                # acerto
                usuario[4] = int(usuario[4]) + 1
                usuario[2] = int(usuario[2]) + 14
                pontuacao += 14
        if golMandanteApostador == '':
            # não apostou
            usuario[7] = int(usuario[7]) + 1
            usuario[2] = int(usuario[2]) - 20
            pontuacao += -20
    
    #-------------------------------------------------------------------------#
    
    elif derrota:
        if vitoriaApostador:
            # erro
            usuario[5] = int(usuario[5]) + 1
            usuario[2] = int(usuario[2]) - 14
            pontuacao += -14
        elif derrotaApostador:
            if golMandanteJogo == golMandanteApostador and golVisitanteJogo == golVisitanteApostador:
                # cravada
                usuario[3] = int(usuario[3]) + 1
                usuario[2] = int(usuario[2]) + 20
                pontuacao += 20
            else:
                # acerto
                usuario[4] = int(usuario[4]) + 1
                usuario[2] = int(usuario[2]) + 14
                pontuacao += 14
        elif empateApostador:
            # nada
            usuario[6] = int(usuario[6]) + 1
            usuario[2] = int(usuario[2]) + 0
            pontuacao += 0
        if golMandanteApostador == '':
            # não apostou
            usuario[7] = int(usuario[7]) + 1
            usuario[2] = int(usuario[2]) - 20
            pontuacao += -20
            
    return usuario, pontuacao

#-----------------------------------------------------------------------------#

def resultadoApostadorFaseEliminatoriaSelecao(usuario,pontuacao,selecaoApostador,selecaoClassificada):
    
    '''
    
    Função que contabiliza os pontos do usuario para um jogo na fase eliminatoria pela seleção classificada
    
    '''
    
    if selecaoClassificada == selecaoApostador:
        usuario[2] = int(usuario[2]) + 30
        pontuacao += 30
    else:
        usuario[2] = int(usuario[2]) + 0
        pontuacao += 0
            
    return usuario, pontuacao

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#-----------------------------------------------------------------------------#
#=============================================================================#
#-----------------------------------------------------------------------------#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def apostasIniciais(usuario,nomeUsuario):

    st.header('Apostas Campeão, Final da Copa do Mundo, Terceiro Colocado e Classificados nos Grupos')
    dataJanela = datetime(2022,12,9,12,0)
    st.subheader(f'Fim da Janela de Apostas - {dataJanela}')

    inicioJanela = horarioJogo(2022,12,9,12,0)
    inicioCopa   = horarioJogo(2023,11,22,10,0)
    opcoesBolao = ['Campeão do mundo','Vice de nada','cara que não sabe de futebol, mas não vai ser o pior do bolão','Pangaré do futebol']
    opcoes = [0,1,2,3,4]

    with st.form(key = 'include_bolao'):
        apostaBolao = st.selectbox('Selecione a posição que ficará no bolão', options = opcoesBolao, index = 3)
        botaoBolao = st.form_submit_button(label = 'Apostar')
    if botaoBolao and inicioCopa:
        usuario[8] = opcoes[opcoesBolao.index(apostaBolao)]
        np.save(str(nomeUsuario),usuario)
    if usuario[8] != '':
        st.subheader('Aposta registrada!')
        st.write(f'Você vai ser o {opcoesBolao[int(usuario[8])]} !')
    
    #-----------------------------------------------------------------------------#

    st.subheader('Apostas Campeão, Final da Copa do Mundo e Terceiro Colocado ')
    with st.form(key = 'include_campeao'):
        apostaCampeao = st.selectbox('Quem será o campeão da Copa do Mundo 2022?', options = listaSelecoes(), index = 0)
        apostaViceCampeao = st.selectbox('Quem será o vice campeão da Copa do Mundo 2022?', options = listaSelecoes(), index = 0)
        apostaTerceiroColocado = st.selectbox('Quem será o terceiro colocado da Copa do Mundo 2022?', options = listaSelecoes(), index = 0)
        botaoApostaCampeao = st.form_submit_button(label = 'Apostar')
    if botaoApostaCampeao and inicioJanela:
        apostaPodio(usuario,apostaCampeao,apostaViceCampeao,apostaTerceiroColocado)
        np.save(str(nomeUsuario),usuario)
    if usuario[9] != '':
        st.subheader('Apostas registradas!')
        st.write(f'Aposta campeão: {listaSelecoes()[int(usuario[9])]}')
        st.write(f'Aposta vice campeão: {listaSelecoes()[int(usuario[10])]}')
        st.write(f'Aposta terceiro colocado: {listaSelecoes()[int(usuario[11])]}')

    #-----------------------------------------------------------------------------#

    st.subheader('Classificados nos Grupos')
    for nomeGrupo in range(len(grupos()[:,0])):
        st.subheader(f'Grupo {grupos()[nomeGrupo][-1]}')
        with st.form(key = 'include_aposta_grupo_'+str(grupos()[nomeGrupo][-1])):
            apostaPrimeiro = st.selectbox('Quem será o primeiro colocado?', options = np.delete(grupos()[nomeGrupo],-1), index = 0)
            apostaSegundo  = st.selectbox('Quem será o segundo colocado?', options = np.delete(grupos()[nomeGrupo],-1), index = 0)
            botaoApostaGrupos = st.form_submit_button(label = 'Apostar no grupo '+str(grupos()[nomeGrupo][-1]))
        if botaoApostaGrupos and inicioCopa:
            apostaGrupos(usuario,nomeGrupo,apostaPrimeiro,apostaSegundo)
            np.save(str(nomeUsuario),usuario)
        if usuario[2*nomeGrupo+12] != '':
            st.subheader('Apostas registradas!')
            st.write(f'Aposta primeiro colocado: {listaSelecoes()[int(usuario[2*nomeGrupo+12])]}')
            st.write(f'Aposta primeiro colocado: {listaSelecoes()[int(usuario[2*nomeGrupo+13])]}')

    #-----------------------------------------------------------------------------#

    return usuario

#-----------------------------------------------------------------------------#

def apostasFaseGrupos(usuario,nomeUsuario,usuarioMestre):

    st.header('Fase de Grupos')
    classificacao = classificacaoInicial()

    for nomeGrupo in range(len(grupos()[:,0])):
        st.subheader(f'Grupo {grupos()[nomeGrupo][-1]}')
        
        # Datas e horários dos jogos
        for nomeJogo in range(6):
            with st.form(key = 'include_aposta_jogo_'+str(nomeJogo+1)+'do_grupo_'+str(grupos()[nomeGrupo][-1])):
                st.subheader(f'Grupo {grupos()[nomeGrupo][-1]} - Jogo {nomeJogo+1} - {dataHorarioJogoGrupo(nomeGrupo,nomeJogo)}')
                
                # rodada e jogo
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
                        #print('Jogo 1')
                        aposta_selecao_1 = st.number_input(label = grupos()[nomeGrupo][time1], min_value = 0, max_value = 10, step = 1, format = '%d')
                        aposta_selecao_2 = st.number_input(label = grupos()[nomeGrupo][time2], min_value = 0, max_value = 10, step = 1, format = '%d')
                        botao_jogo_1 = st.form_submit_button(label = f'Apostar no jogo {nomeJogo+1}')
                        inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                        #if botao_jogo_1:
                        if botao_jogo_1 and inicioJogo:
                            fazerApostaPrimeiraFase(usuario,nomeGrupo,nomeJogo,aposta_selecao_1,aposta_selecao_2)
                            np.save(str(nomeUsuario),usuario)
                        if usuario[28+2*6*nomeGrupo+2*nomeJogo] != '':
                            st.subheader('Aposta registrada!')
                            st.write(f'{grupos()[nomeGrupo][time1]} {usuario[28+2*6*nomeGrupo+2*nomeJogo]} X {usuario[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time2]}')
                        if usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo] != '':
                            st.subheader('Fim de jogo!')
                            st.write(f'{grupos()[nomeGrupo][time1]} {usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]} X {usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time2]}')
                            classificacao = classificacaoFaseGrupos(classificacao,nomeGrupo,nomeJogo,int(usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]),int(usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]))

                    elif nomeJogo == 1:
                        #print('Jogo 2')
                        aposta_selecao_3 = st.number_input(label = grupos()[nomeGrupo][time3], min_value = 0, max_value = 10, step = 1, format = '%d')
                        aposta_selecao_4 = st.number_input(label = grupos()[nomeGrupo][time4], min_value = 0, max_value = 10, step = 1, format = '%d')
                        botao_jogo_2 = st.form_submit_button(label = f'Apostar no jogo {nomeJogo+1}')
                        inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                        #if botao_jogo_2:
                        if botao_jogo_2 and inicioJogo:
                            fazerApostaPrimeiraFase(usuario,nomeGrupo,nomeJogo,aposta_selecao_3,aposta_selecao_4)
                            np.save(str(nomeUsuario),usuario)
                        if usuario[28+2*6*nomeGrupo+2*nomeJogo] != '':
                            st.subheader('Aposta registrada!')
                            #st.write(f'{grupos()[nomeGrupo][time3]} {aposta_selecao_3} X {aposta_selecao_4} {grupos()[nomeGrupo][time4]}')
                            st.write(f'{grupos()[nomeGrupo][time3]} {usuario[28+2*6*nomeGrupo+2*nomeJogo]} X {usuario[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time4]}')
                        if usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo] != '':
                            st.subheader('Fim de jogo!')
                            st.write(f'{grupos()[nomeGrupo][time3]} {usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]} X {usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time4]}')
                            classificacao = classificacaoFaseGrupos(classificacao,nomeGrupo,nomeJogo,int(usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]),int(usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]))

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
                    time3 = 1
                    time4 = 3
                    if nomeJogo == 2:
                        #print('Jogo 3')
                        aposta_selecao_1 = st.number_input(label = grupos()[nomeGrupo][time1], min_value = 0, max_value = 10, step = 1, format = '%d')
                        aposta_selecao_2 = st.number_input(label = grupos()[nomeGrupo][time2], min_value = 0, max_value = 10, step = 1, format = '%d')
                        botao_jogo_3 = st.form_submit_button(label = f'Apostar no jogo {nomeJogo+1}')
                        inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                        #if botao_jogo_3:
                        if botao_jogo_3 and inicioJogo:
                            fazerApostaPrimeiraFase(usuario,nomeGrupo,nomeJogo,aposta_selecao_1,aposta_selecao_2)
                            np.save(str(nomeUsuario),usuario)
                        if usuario[28+2*6*nomeGrupo+2*nomeJogo] != '':
                            st.subheader('Aposta registrada!')
                            #st.write(f'{grupos()[nomeGrupo][time1]} {aposta_selecao_1} X {aposta_selecao_2} {grupos()[nomeGrupo][time2]}')
                            st.write(f'{grupos()[nomeGrupo][time1]} {usuario[28+2*6*nomeGrupo+2*nomeJogo]} X {usuario[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time2]}')
                        if usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo] != '':
                            st.subheader('Fim de jogo!')
                            st.write(f'{grupos()[nomeGrupo][time1]} {usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]} X {usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time2]}')
                            classificacao = classificacaoFaseGrupos(classificacao,nomeGrupo,nomeJogo,int(usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]),int(usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]))

                    elif nomeJogo == 3:
                        #print('Jogo 4')
                        aposta_selecao_3 = st.number_input(label = grupos()[nomeGrupo][time3], min_value = 0, max_value = 10, step = 1, format = '%d')
                        aposta_selecao_4 = st.number_input(label = grupos()[nomeGrupo][time4], min_value = 0, max_value = 10, step = 1, format = '%d')
                        botao_jogo_4 = st.form_submit_button(label = f'Apostar no jogo {nomeJogo+1}')
                        inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                        #if botao_jogo_4:
                        if botao_jogo_4 and inicioJogo:
                            fazerApostaPrimeiraFase(usuario,nomeGrupo,nomeJogo,aposta_selecao_3,aposta_selecao_4)
                            np.save(str(nomeUsuario),usuario)
                        if usuario[28+2*6*nomeGrupo+2*nomeJogo] != '':
                            st.subheader('Aposta registrada!')
                            #st.write(f'{grupos()[nomeGrupo][time3]} {aposta_selecao_3} X {aposta_selecao_4} {grupos()[nomeGrupo][time4]}')
                            st.write(f'{grupos()[nomeGrupo][time3]} {usuario[28+2*6*nomeGrupo+2*nomeJogo]} X {usuario[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time4]}')
                        if usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo] != '':
                            st.subheader('Fim de jogo!')
                            st.write(f'{grupos()[nomeGrupo][time3]} {usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]} X {usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time4]}')
                            classificacao = classificacaoFaseGrupos(classificacao,nomeGrupo,nomeJogo,int(usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]),int(usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]))

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
                        #print('Jogo 5')
                        aposta_selecao_1 = st.number_input(label = grupos()[nomeGrupo][time1], min_value = 0, max_value = 10, step = 1, format = '%d')
                        aposta_selecao_2 = st.number_input(label = grupos()[nomeGrupo][time2], min_value = 0, max_value = 10, step = 1, format = '%d')
                        botao_jogo_5 = st.form_submit_button(label = f'Apostar no jogo {nomeJogo+1}')
                        inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                        #if botao_jogo_5:
                        if botao_jogo_5 and inicioJogo:
                            fazerApostaPrimeiraFase(usuario,nomeGrupo,nomeJogo,aposta_selecao_1,aposta_selecao_2)
                            np.save(str(nomeUsuario),usuario)
                        if usuario[28+2*6*nomeGrupo+2*nomeJogo] != '':
                            st.subheader('Aposta registrada!')
                            #st.write(f'{grupos()[nomeGrupo][time1]} {aposta_selecao_1} X {aposta_selecao_2} {grupos()[nomeGrupo][time2]}')
                            st.write(f'{grupos()[nomeGrupo][time1]} {usuario[28+2*6*nomeGrupo+2*nomeJogo]} X {usuario[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time2]}')
                        if usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo] != '':
                            st.subheader('Fim de jogo!')
                            st.write(f'{grupos()[nomeGrupo][time1]} {usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]} X {usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time2]}')
                            classificacao = classificacaoFaseGrupos(classificacao,nomeGrupo,nomeJogo,int(usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]),int(usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]))

                    elif nomeJogo == 5:
                        #print('Jogo 6')
                        aposta_selecao_3 = st.number_input(label = grupos()[nomeGrupo][time3], min_value = 0, max_value = 10, step = 1, format = '%d')
                        aposta_selecao_4 = st.number_input(label = grupos()[nomeGrupo][time4], min_value = 0, max_value = 10, step = 1, format = '%d')
                        botao_jogo_6 = st.form_submit_button(label = f'Apostar no jogo {nomeJogo+1}')
                        inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                        #if botao_jogo_6:
                        if botao_jogo_6 and inicioJogo:
                            fazerApostaPrimeiraFase(usuario,nomeGrupo,nomeJogo,aposta_selecao_3,aposta_selecao_4)
                            np.save(str(nomeUsuario),usuario)
                        if usuario[28+2*6*nomeGrupo+2*nomeJogo] != '':
                            st.subheader('Aposta registrada!')
                            #st.write(f'{grupos()[nomeGrupo][time3]} {aposta_selecao_3} X {aposta_selecao_4} {grupos()[nomeGrupo][time4]}')
                            st.write(f'{grupos()[nomeGrupo][time3]} {usuario[28+2*6*nomeGrupo+2*nomeJogo]} X {usuario[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time4]}')
                        if usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo] != '':
                            st.subheader('Fim de jogo!')
                            st.write(f'{grupos()[nomeGrupo][time3]} {usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]} X {usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time4]}')
                            classificacao = classificacaoFaseGrupos(classificacao,nomeGrupo,nomeJogo,int(usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]),int(usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]))
                            
    rotuloColuna = ['P',  # pontuação
                    'J',  # jogos
                    'V',  # vitórias
                    'E',  # empates
                    'D',  # derrotas
                    'GP', # gols pró
                    'GC', # gols contra
                    'SG'] # saldo de gols
    for contadorClassificacao in range(len(classificacao)):
        classificacao[contadorClassificacao].pop(-1)
        df = pd.DataFrame(np.array([[classificacao[contadorClassificacao][0][1],classificacao[contadorClassificacao][0][2],classificacao[contadorClassificacao][0][3],classificacao[contadorClassificacao][0][4],classificacao[contadorClassificacao][0][5],classificacao[contadorClassificacao][0][6],classificacao[contadorClassificacao][0][7],classificacao[contadorClassificacao][0][8]],
                                    [classificacao[contadorClassificacao][1][1],classificacao[contadorClassificacao][1][2],classificacao[contadorClassificacao][1][3],classificacao[contadorClassificacao][1][4],classificacao[contadorClassificacao][1][5],classificacao[contadorClassificacao][1][6],classificacao[contadorClassificacao][1][7],classificacao[contadorClassificacao][1][8]],
                                    [classificacao[contadorClassificacao][2][1],classificacao[contadorClassificacao][2][2],classificacao[contadorClassificacao][2][3],classificacao[contadorClassificacao][2][4],classificacao[contadorClassificacao][2][5],classificacao[contadorClassificacao][2][6],classificacao[contadorClassificacao][2][7],classificacao[contadorClassificacao][2][8]],
                                    [classificacao[contadorClassificacao][3][1],classificacao[contadorClassificacao][3][2],classificacao[contadorClassificacao][3][3],classificacao[contadorClassificacao][3][4],classificacao[contadorClassificacao][3][5],classificacao[contadorClassificacao][3][6],classificacao[contadorClassificacao][3][7],classificacao[contadorClassificacao][3][8]]
                                    ]),
                    columns = tuple(rotuloColuna)
        )
        df.index = [classificacao[contadorClassificacao][0][0],classificacao[contadorClassificacao][1][0],classificacao[contadorClassificacao][2][0],classificacao[contadorClassificacao][3][0]]
        st.table(df)

    return usuario

#-----------------------------------------------------------------------------#

def apostasOitavas(usuario,nomeUsuario,usuarioMestre):

    st.subheader('Oitavas de final')
    #-----------------------------
    opcoesOitavas1 = ['Holanda','Estados Unidos']
    opcoesOitavas2 = ['Argentina','Austrália']
    opcoesOitavas3 = ['Japão','Croácia']
    opcoesOitavas4 = ['Brasil','Coreia do Sul']
    opcoesOitavas5 = ['Inglaterra','Senegal']
    opcoesOitavas6 = ['França','Polônia']
    opcoesOitavas7 = ['Marrocos','Espanha']
    opcoesOitavas8 = ['Portugal','Suíça']
    opcoesOitavas  = [opcoesOitavas1,
                      opcoesOitavas2,
                      opcoesOitavas3,
                      opcoesOitavas4,
                      opcoesOitavas5,
                      opcoesOitavas6,
                      opcoesOitavas7,
                      opcoesOitavas8]
    #-----------------------------
    horarioOitavas1 = horarioJogo(2022,12,3,12,0)
    horarioOitavas2 = horarioJogo(2022,12,3,16,0)
    horarioOitavas3 = horarioJogo(2022,12,5,12,0)
    horarioOitavas4 = horarioJogo(2022,12,5,16,0)
    horarioOitavas5 = horarioJogo(2022,12,4,16,0)
    horarioOitavas6 = horarioJogo(2022,12,4,12,0)
    horarioOitavas7 = horarioJogo(2022,12,6,12,0)
    horarioOitavas8 = horarioJogo(2022,12,6,16,0)
    horarioOitavas  = [horarioOitavas1,
                       horarioOitavas2,
                       horarioOitavas3,
                       horarioOitavas4,
                       horarioOitavas5,
                       horarioOitavas6,
                       horarioOitavas7,
                       horarioOitavas8]
    #-----------------------------
    dataOitavas1 = datetime(2022,12,3,12,0)
    dataOitavas2 = datetime(2022,12,3,16,0)
    dataOitavas3 = datetime(2022,12,5,12,0)
    dataOitavas4 = datetime(2022,12,5,16,0)
    dataOitavas5 = datetime(2022,12,4,16,0)
    dataOitavas6 = datetime(2022,12,4,12,0)
    dataOitavas7 = datetime(2022,12,6,12,0)
    dataOitavas8 = datetime(2022,12,6,16,0)
    dataOitavas  = [dataOitavas1,
                    dataOitavas2,
                    dataOitavas3,
                    dataOitavas4,
                    dataOitavas5,
                    dataOitavas6,
                    dataOitavas7,
                    dataOitavas8]
    #-----------------------------
    for nomeJogo in range(8):
        st.subheader(f'Jogo {nomeJogo+1} - {opcoesOitavas[nomeJogo][0]} x {opcoesOitavas[nomeJogo][1]} - {dataOitavas[nomeJogo]}')
        with st.form(key = 'incluirApostaFaseEliminatoriasOitavasJogo'+str(nomeJogo+1)):
            apostaOitavas = st.selectbox('Qual será a seleção classificada?', options = opcoesOitavas[nomeJogo], index = 0)
            apostaOitavasSelecao1 = st.number_input(label = opcoesOitavas[nomeJogo][0], min_value = 0, max_value = 10, step = 1, format = '%d')
            apostaOitavasSelecao2 = st.number_input(label = opcoesOitavas[nomeJogo][1], min_value = 0, max_value = 10, step = 1, format = '%d')
            botaoApostaOitavas = st.form_submit_button(label = 'Apostar')
        if botaoApostaOitavas and horarioOitavas[nomeJogo]:
            if apostaOitavas == opcoesOitavas[nomeJogo][0] and apostaOitavasSelecao1 < apostaOitavasSelecao2 or apostaOitavas == opcoesOitavas[nomeJogo][1] and apostaOitavasSelecao2 < apostaOitavasSelecao1:
                st.subheader('Apostas INVÁLIDAS!')
                st.write(f'Tente realizar as apostas novamente.')
            else:
                usuario[124+3*nomeJogo], usuario[125+3*nomeJogo] = apostaOitavasSelecao1, apostaOitavasSelecao2
                usuario[126+3*nomeJogo] = listaSelecoes().index(apostaOitavas)
                np.save(str(nomeUsuario),usuario)
        elif botaoApostaOitavas and not horarioOitavas[nomeJogo]:
            st.subheader('O jogo já começou!')
            st.write(f'Você NÃO pode realizar as apostas.')
        if usuario[124+3*nomeJogo] != '' and usuario[126+3*nomeJogo] != '':
            st.subheader('Aposta registrada!')
            st.write(f'{opcoesOitavas[nomeJogo][0]} {usuario[124+3*nomeJogo]} X {usuario[125+3*nomeJogo]} {opcoesOitavas[nomeJogo][1]}')
            st.write(f'Aposta classificação: {listaSelecoes()[int(usuario[126+3*nomeJogo])]}')
        if usuarioMestre[124+3*nomeJogo] != '' and usuarioMestre[126+3*nomeJogo] != '':
            st.subheader('Fim de jogo!')
            st.write(f'{opcoesOitavas[nomeJogo][0]} {usuarioMestre[124+3*nomeJogo]} X {usuarioMestre[125+3*nomeJogo]} {opcoesOitavas[nomeJogo][1]}')
            st.write(f'Seleção classificada: {listaSelecoes()[int(usuarioMestre[126+3*nomeJogo])]}')

    return usuario

#-----------------------------------------------------------------------------#

def classificacaoDoBolao():

    dataHoraMinutoAtual = datetime.strptime(datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%d/%m/%y %H:%M'), '%d/%m/%y %H:%M')
    st.subheader(f'Classificação do Bolão - {dataHoraMinutoAtual}')

    opcoesBolao = ['Campeão do mundo','Vice de nada','cara que não sabe de futebol, mas não vai ser o pior do bolão','Pangaré do futebol']
    classificacaoBolao = []
    dadosClassificacao = []
    for contadorUsuario in range(1, len(listaUsuarios), 1):
        classificacaoBolao.append([listaUsuarios[contadorUsuario][0],listaUsuarios[contadorUsuario][2],listaUsuarios[contadorUsuario][3],listaUsuarios[contadorUsuario][4],listaUsuarios[contadorUsuario][5],listaUsuarios[contadorUsuario][6],listaUsuarios[contadorUsuario][7]])
        dadosClassificacao.append(np.delete(np.array(classificacaoBolao[contadorUsuario-1]),0,0))
    df = pd.DataFrame(np.array(dadosClassificacao),
                       columns = ('Pontos','Cravadas','Acertos','Erros','Nadas','Não apostas'))
    df.index = np.delete(np.array(listaUsuarios)[:,0],0)
    st.table(df)

    return

#-----------------------------------------------------------------------------#

def classificacaoBolaoGrupos():

    dataHoraMinutoAtual = datetime.strptime(datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%d/%m/%y %H:%M'), '%d/%m/%y %H:%M')
    
    #------------------                                    
    colunas = []
    opcoes = []
    apostasCampeao = []
    apostasViceCampeao = []
    apostasTerceiroColocado = []
    apostasGrupos = []
    opcoesBolao = ['Campeão do mundo','Vice de nada','cara que não sabe de futebol, mas não vai ser o pior do bolão','Pangaré do futebol']
    for contadorUsuario in range(1, len(listaUsuarios), 1):
        
        # Apostas Iniciais bolão, campeão, vice e terceiro
        colunas.append(np.array(listaUsuarios)[contadorUsuario][0])
        if listaUsuarios[contadorUsuario][8] != '':
            opcoes.append(f'Acha que vai ser o {opcoesBolao[int(listaUsuarios[contadorUsuario][8])]} !')
        else:
            opcoes.append(f'Não acha nada.')

        if np.array(listaUsuarios)[contadorUsuario][9] != '':
            apostasCampeao.append(listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][9])])
        else:
            apostasCampeao.append('Não apostou no campeão')

        if np.array(listaUsuarios)[contadorUsuario][10] != '':
            apostasViceCampeao.append(listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][10])])
        else:
            apostasViceCampeao.append('Não apostou no vice-campeão')

        if np.array(listaUsuarios)[contadorUsuario][11] != '':
            apostasTerceiroColocado.append(listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][11])])
        else:
            apostasTerceiroColocado.append('Não apostou no terceiro colocado')

        # apostas Iniciais Grupos
        listaApostasGruposUsuario = []
        for apostaGrupo in range(12, 28, 2):
            if np.array(listaUsuarios)[contadorUsuario][apostaGrupo] != '':
                listaApostasGruposUsuario.append([listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo])],listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo+1])]])
            else:
                listaApostasGruposUsuario.append(['Não apostou','Não apostou'])
        apostasGrupos.append(listaApostasGruposUsuario)

    classificadosGrupos = np.array(['Holanda','Senegal',
                                    'Inglaterra','Estados Unidos',
                                    'Argentina','Polônia',
                                    'França','Austrália',
                                    'Japão','Espanha',
                                    'Marrocos','Croácia',
                                    'Brasil','Suíça',
                                    'Portugal','Coreia do Sul'])
    
    apostadorPontuacaoApostasGrupos = []
    apostadorPontuacaoGrupos = []
    for contadorUsuario in range(1, len(listaUsuarios), 1):
        pontuacaoApostasGrupos = []
        pontuacaoGrupos = 0
        for apostaGrupo in range(12, 28, 2):
            if np.array(listaUsuarios)[contadorUsuario][apostaGrupo] != '':
                if listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo])] == classificadosGrupos[apostaGrupo-12] and listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo+1])] == classificadosGrupos[apostaGrupo+1-12]:
                    pontuacaoApostasGrupos.append([30,30])
                    pontuacaoGrupos += 60
                elif listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo])] == classificadosGrupos[apostaGrupo-12] and listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo+1])] != classificadosGrupos[apostaGrupo+1-12]:
                    pontuacaoApostasGrupos.append([30,0])
                    pontuacaoGrupos += 30
                elif listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo])] == classificadosGrupos[apostaGrupo+1-12] and listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo+1])] == classificadosGrupos[apostaGrupo-12]:
                    pontuacaoApostasGrupos.append([21,21])
                    pontuacaoGrupos += 42
                elif listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo])] == classificadosGrupos[apostaGrupo+1-12] and listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo+1])] != classificadosGrupos[apostaGrupo-12]:
                    pontuacaoApostasGrupos.append([21,0])
                    pontuacaoGrupos += 21
                elif listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo])] != classificadosGrupos[apostaGrupo-12] and listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo+1])] == classificadosGrupos[apostaGrupo+1-12]:
                    pontuacaoApostasGrupos.append([0,30])
                    pontuacaoGrupos += 30
                elif listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo])] != classificadosGrupos[apostaGrupo+1-12] and listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo+1])] == classificadosGrupos[apostaGrupo-12]:
                    pontuacaoApostasGrupos.append([0,21])
                    pontuacaoGrupos += 21
                elif listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo])] != classificadosGrupos[apostaGrupo-12] and listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo+1])] != classificadosGrupos[apostaGrupo+1-12]:
                    pontuacaoApostasGrupos.append([0,0])
                    pontuacaoGrupos += 0
            else:
                #pontuacaoApostasGrupos.append(['Não apostou','Não apostou'])
                pontuacaoApostasGrupos.append([0,0])
        apostadorPontuacaoApostasGrupos.append(pontuacaoApostasGrupos)
        apostadorPontuacaoGrupos.append(pontuacaoGrupos)
    
    #-------------------------------------------
    
    st.subheader(f'Apostas campeão, final e terceiro colocado - {dataHoraMinutoAtual}')
    colunas = tuple(colunas)
    dfa = pd.DataFrame(np.array([opcoes,apostasCampeao,apostasViceCampeao,apostasTerceiroColocado,]),
                      columns = colunas)
    dfa.index = ['Bolão','Campeão','Vice-campeão','Terceiro colocado']
    st.table(dfa)

    #-------------------------------------------
    
    st.subheader(f'Apostas classificados nos grupos')
    dfb = pd.DataFrame(np.array([np.array(apostadorPontuacaoGrupos),
                                 np.array(apostasGrupos)[:,0][:,0],np.array(np.array(apostadorPontuacaoApostasGrupos)[:,0][:,0]),
                                 np.array(apostasGrupos)[:,0][:,1],np.array(np.array(apostadorPontuacaoApostasGrupos)[:,0][:,1]), # grupo A
                                 np.array(apostasGrupos)[:,1][:,0],np.array(np.array(apostadorPontuacaoApostasGrupos)[:,1][:,0]),
                                 np.array(apostasGrupos)[:,1][:,1],np.array(np.array(apostadorPontuacaoApostasGrupos)[:,1][:,1]), # grupo B
                                 np.array(apostasGrupos)[:,2][:,0],np.array(np.array(apostadorPontuacaoApostasGrupos)[:,2][:,0]),
                                 np.array(apostasGrupos)[:,2][:,1],np.array(np.array(apostadorPontuacaoApostasGrupos)[:,2][:,1]), # grupo C
                                 np.array(apostasGrupos)[:,3][:,0],np.array(np.array(apostadorPontuacaoApostasGrupos)[:,3][:,0]),
                                 np.array(apostasGrupos)[:,3][:,1],np.array(np.array(apostadorPontuacaoApostasGrupos)[:,3][:,1]), # grupo D
                                 np.array(apostasGrupos)[:,4][:,0],np.array(np.array(apostadorPontuacaoApostasGrupos)[:,4][:,0]),
                                 np.array(apostasGrupos)[:,4][:,1],np.array(np.array(apostadorPontuacaoApostasGrupos)[:,4][:,1]), # grupo E
                                 np.array(apostasGrupos)[:,5][:,0],np.array(np.array(apostadorPontuacaoApostasGrupos)[:,5][:,0]),
                                 np.array(apostasGrupos)[:,5][:,1],np.array(np.array(apostadorPontuacaoApostasGrupos)[:,5][:,1]), # grupo F
                                 np.array(apostasGrupos)[:,6][:,0],np.array(np.array(apostadorPontuacaoApostasGrupos)[:,6][:,0]),
                                 np.array(apostasGrupos)[:,6][:,1],np.array(np.array(apostadorPontuacaoApostasGrupos)[:,6][:,1]), # grupo G
                                 np.array(apostasGrupos)[:,7][:,0],np.array(np.array(apostadorPontuacaoApostasGrupos)[:,7][:,0]),
                                 np.array(apostasGrupos)[:,7][:,1],np.array(np.array(apostadorPontuacaoApostasGrupos)[:,7][:,1])]), # grupo H
                      columns = colunas)
    dfb.index = ['Pontuação total',
                 '1° Grupo A','1° Grupo A - Pontuação',
                 '2° Grupo A','2° Grupo A - Pontuação',
                 '1° Grupo B','1° Grupo B - Pontuação',
                 '2° Grupo B','2° Grupo B - Pontuação',
                 '1° Grupo C','1° Grupo C - Pontuação',
                 '2° Grupo C','2° Grupo C - Pontuação',
                 '1° Grupo D','1° Grupo D - Pontuação',
                 '2° Grupo D','2° Grupo D - Pontuação',
                 '1° Grupo E','1° Grupo E - Pontuação',
                 '2° Grupo E','2° Grupo E - Pontuação',
                 '1° Grupo F','1° Grupo F - Pontuação',
                 '2° Grupo F','2° Grupo F - Pontuação',
                 '1° Grupo G','1° Grupo G - Pontuação',
                 '2° Grupo G','2° Grupo G - Pontuação',
                 '1° Grupo H','1° Grupo H - Pontuação',
                 '2° Grupo H','2° Grupo H - Pontuação']
    st.table(dfb)
    
    #-------------------------------------------

    return

#-----------------------------------------------------------------------------#

def apostasOitavasApostador(contadorUsuario):

    dataHoraMinutoAtual = datetime.strptime(datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%d/%m/%y %H:%M'), '%d/%m/%y %H:%M')

    #-----------------------------
    st.subheader('Oitavas de final')
    #-----------------------------

    opcoesOitavas1 = ['Holanda','Estados Unidos']
    opcoesOitavas2 = ['Argentina','Austrália']
    opcoesOitavas3 = ['Japão','Croácia']
    opcoesOitavas4 = ['Brasil','Coreia do Sul']
    opcoesOitavas5 = ['Inglaterra','Senegal']
    opcoesOitavas6 = ['França','Polônia']
    opcoesOitavas7 = ['Marrocos','Espanha']
    opcoesOitavas8 = ['Portugal','Suíça']
    opcoesOitavas  = [opcoesOitavas1,
                      opcoesOitavas2,
                      opcoesOitavas3,
                      opcoesOitavas4,
                      opcoesOitavas5,
                      opcoesOitavas6,
                      opcoesOitavas7,
                      opcoesOitavas8]
    
    #-----------------------------
    
    horarioOitavas1 = horarioJogo(2022,12,3,12,0)
    horarioOitavas2 = horarioJogo(2022,12,3,16,0)
    horarioOitavas3 = horarioJogo(2022,12,5,12,0)
    horarioOitavas4 = horarioJogo(2022,12,5,16,0)
    horarioOitavas5 = horarioJogo(2022,12,4,16,0)
    horarioOitavas6 = horarioJogo(2022,12,4,12,0)
    horarioOitavas7 = horarioJogo(2022,12,6,12,0)
    horarioOitavas8 = horarioJogo(2022,12,6,16,0)
    horarioOitavas  = [horarioOitavas1,
                       horarioOitavas2,
                       horarioOitavas3,
                       horarioOitavas4,
                       horarioOitavas5,
                       horarioOitavas6,
                       horarioOitavas7,
                       horarioOitavas8]

    #-----------------------------
    
    for nomeJogo in range(8):
        st.write(f'Jogo {nomeJogo+1} - {np.array(listaUsuarios)[contadorUsuario][0]}')
        if not horarioOitavas[nomeJogo]:
        #if horarioOitavas[nomeJogo]:
            if np.array(listaUsuarios)[contadorUsuario][124+3*nomeJogo] != '':
                st.write(f'{opcoesOitavas[nomeJogo][0]} {np.array(listaUsuarios)[contadorUsuario][124+3*nomeJogo]}x{np.array(listaUsuarios)[contadorUsuario][125+3*nomeJogo]} {opcoesOitavas[nomeJogo][1]}')
                st.write(f'Classificado: {listaSelecoes()[int(listaUsuarios[contadorUsuario][126+3*nomeJogo])]}')
            else:
                st.write(f'Aposta NÃO realizada.')
    
    #-------------------------------------------

    return

#-----------------------------------------------------------------------------#

def apostasPrincipaisApostador(contadorUsuario):

    dataHoraMinutoAtual = datetime.strptime(datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%d/%m/%y %H:%M'), '%d/%m/%y %H:%M')

    opcoesBolao = ['Campeão do mundo','Vice de nada','cara que não sabe de futebol, mas não vai ser o pior do bolão','Pangaré do futebol']
    if listaUsuarios[contadorUsuario][8] != '':
        st.subheader(f'Acha que vai ser o {opcoesBolao[int(listaUsuarios[contadorUsuario][8])]} !')
    
    if np.array(listaUsuarios)[contadorUsuario][9] != '':
        apostaCampeao = listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][9])]
    else:
        apostaCampeao = 'Não apostou no campeão'
        
    if np.array(listaUsuarios)[contadorUsuario][10] != '':
        apostaViceCampeao = listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][10])]
    else:
        apostaViceCampeao = 'Não apostou no vice-campeão'
        
    if np.array(listaUsuarios)[contadorUsuario][11] != '':
        apostaTerceiroColocado = listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][11])]
    else:
        apostaTerceiroColocado = 'Não apostou no terceiro colocado'
    
    st.subheader(f'Apostas principais - {dataHoraMinutoAtual}:')
    df = pd.DataFrame(np.array([[apostaCampeao,apostaViceCampeao,apostaTerceiroColocado]]),
                        columns = ('Campeão','Vice-campeão','Terceiro colocado'))
    df.index = [f'Aposta - {np.array(listaUsuarios)[contadorUsuario][0]}']
    st.table(df)

    return

#-----------------------------------------------------------------------------#

def apostasGruposApostador(contadorUsuario):

    dataHoraMinutoAtual = datetime.strptime(datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%d/%m/%y %H:%M'), '%d/%m/%y %H:%M')

    st.subheader(f'Apostas grupos - {dataHoraMinutoAtual}:')
    classificadosGrupos = np.array(['Holanda','Senegal',
                                    'Inglaterra','Estados Unidos',
                                    'Argentina','Polônia',
                                    'França','Austrália',
                                    'Japão','Espanha',
                                    'Marrocos','Croácia',
                                    'Brasil','Suíça',
                                    'Portugal','Coreia'])
    pontuacaoApostasGrupos = []
    pontuacaoGrupos = 0
    for apostaGrupo in range(12, 28, 2):
        if np.array(listaUsuarios)[contadorUsuario][apostaGrupo] != '':
            pontuacaoApostasGrupos.append([listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo])],listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo+1])]])
            if listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo])] == classificadosGrupos[apostaGrupo-12] and listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo+1])] == classificadosGrupos[apostaGrupo+1-12]:
                pontuacaoApostasGrupos.append([30,30])
                pontuacaoGrupos += 60
            elif listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo])] == classificadosGrupos[apostaGrupo-12] and listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo+1])] != classificadosGrupos[apostaGrupo+1-12]:
                pontuacaoApostasGrupos.append([30,0])
                pontuacaoGrupos += 30
            elif listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo])] == classificadosGrupos[apostaGrupo+1-12] and listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo+1])] == classificadosGrupos[apostaGrupo-12]:
                pontuacaoApostasGrupos.append([21,21])
                pontuacaoGrupos += 42
            elif listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo])] == classificadosGrupos[apostaGrupo+1-12] and listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo+1])] != classificadosGrupos[apostaGrupo-12]:
                pontuacaoApostasGrupos.append([21,0])
                pontuacaoGrupos += 21
            elif listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo])] != classificadosGrupos[apostaGrupo-12] and listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo+1])] == classificadosGrupos[apostaGrupo+1-12]:
                pontuacaoApostasGrupos.append([0,30])
                pontuacaoGrupos += 30
            elif listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo])] != classificadosGrupos[apostaGrupo+1-12] and listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo+1])] == classificadosGrupos[apostaGrupo-12]:
                pontuacaoApostasGrupos.append([0,21])
                pontuacaoGrupos += 21
            elif listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo])] != classificadosGrupos[apostaGrupo-12] and listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo+1])] != classificadosGrupos[apostaGrupo+1-12]:
                pontuacaoApostasGrupos.append([0,0])
                pontuacaoGrupos += 0
        else:
            pontuacaoApostasGrupos.append(['Não apostou','Não apostou'])
            pontuacaoApostasGrupos.append([0,0])

    df = pd.DataFrame(np.array(pontuacaoApostasGrupos),
                       columns = ('Primeiro colocado','Segundo colocado'))
    df.index = ['Grupo A - aposta',
                'Grupo A - pontuação',
                'Grupo B - aposta',
                'Grupo B - pontuação',
                'Grupo C - aposta',
                'Grupo C - pontuação',
                'Grupo D - aposta',
                'Grupo D - pontuação',
                'Grupo E - aposta',
                'Grupo E - pontuação',
                'Grupo F - aposta',
                'Grupo F - pontuação',
                'Grupo G - aposta',
                'Grupo G - pontuação',
                'Grupo H - aposta',
                'Grupo H - pontuação']
    st.table(df)
    st.subheader(f'Apostas dos classificados dos grupos: {pontuacaoGrupos} ponto(s)')

    return

#-----------------------------------------------------------------------------#

def apostasFaseGruposApostador(contadorUsuario):

    dataHoraMinutoAtual = datetime.strptime(datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%d/%m/%y %H:%M'), '%d/%m/%y %H:%M')

    st.subheader(f'Apostas jogos primeira fase - {dataHoraMinutoAtual}:')
    for contadorGrupo in range(8):
        st.write(f'Grupo {grupos()[:,4][contadorGrupo]} - {np.array(listaUsuarios)[contadorUsuario][0]}')
        for contadorJogo in range(6):
            # rodada e jogo
            if contadorJogo == 0 or contadorJogo == 1:
                nomeRodada = 1
            elif contadorJogo == 2 or contadorJogo == 3:
                nomeRodada = 2
            elif contadorJogo == 4 or contadorJogo == 5:
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
                if contadorJogo == 0:
                    timeMandante  = time1
                    timeVisitante = time2
                elif contadorJogo == 1:
                    timeMandante  = time3
                    timeVisitante = time4

            elif nomeRodada == 2:
                # Time i1 = 0
                # Time i2 = 1
                # Time i3 = 2
                # Time i4 = 3
                # rodada 2: Time i1 x Time i3
                # rodada 2: Time i2 x Time i4
                time1 = 0
                time2 = 2
                time3 = 3
                time4 = 1
                if contadorJogo == 2:
                    timeMandante  = time1
                    timeVisitante = time2
                elif contadorJogo == 3:
                    timeMandante  = time3
                    timeVisitante = time4

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
                if contadorJogo == 4:
                    timeMandante  = time1
                    timeVisitante = time2
                elif contadorJogo == 5:
                    timeMandante  = time3
                    timeVisitante = time4

            if not horarioJogoGrupo(contadorGrupo,contadorJogo):
                if np.array(listaUsuarios)[contadorUsuario][28+2*6*contadorGrupo+2*contadorJogo] != '':
                    st.write(f'Jogo {contadorJogo+1}: {grupos()[contadorGrupo][timeMandante]} {np.array(listaUsuarios)[contadorUsuario][28+2*6*contadorGrupo+2*contadorJogo]} x {np.array(listaUsuarios)[contadorUsuario][29+2*6*contadorGrupo+2*contadorJogo]} {grupos()[contadorGrupo][timeVisitante]}')
                else:
                    st.write(f'Jogo {contadorJogo+1}: Aposta NÃO realizada.')

    return

#-----------------------------------------------------------------------------#

def placarJogos(nomeUsuario):

    classificacao = classificacaoInicial()
    indiceUsuario = np.where(np.array(listaUsuarios)[:,0] == nomeUsuario)[0][0]
    usuario = listaUsuarios[indiceUsuario]
    for contadorUsuario in range(1, len(listaUsuarios), 1):
        listaUsuarios[contadorUsuario][2] = 0
        listaUsuarios[contadorUsuario][3] = 0
        listaUsuarios[contadorUsuario][4] = 0
        listaUsuarios[contadorUsuario][5] = 0
        listaUsuarios[contadorUsuario][6] = 0
        listaUsuarios[contadorUsuario][7] = 0
        np.save(str(listaUsuarios[contadorUsuario][0]),listaUsuarios[contadorUsuario])
    
    classificadosGrupos = np.array(['Holanda','Senegal',
                                    'Inglaterra','Estados Unidos',
                                    'Argentina','Polônia',
                                    'França','Austrália',
                                    'Japão','Espanha',
                                    'Marrocos','Croácia',
                                    'Brasil','Suíça',
                                    'Portugal','Coreia do Sul'])
    
    for contadorUsuario in range(1, len(listaUsuarios), 1):
        pontuacaoGrupos = 0
        for apostaGrupo in range(12, 28, 2):
            if np.array(listaUsuarios)[contadorUsuario][apostaGrupo] != '':
                if listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo])] == classificadosGrupos[apostaGrupo-12] and listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo+1])] == classificadosGrupos[apostaGrupo+1-12]:
                    pontuacaoGrupos += 60
                elif listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo])] == classificadosGrupos[apostaGrupo-12] and listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo+1])] != classificadosGrupos[apostaGrupo+1-12]:
                    pontuacaoGrupos += 30
                elif listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo])] == classificadosGrupos[apostaGrupo+1-12] and listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo+1])] == classificadosGrupos[apostaGrupo-12]:
                    pontuacaoGrupos += 42
                elif listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo])] == classificadosGrupos[apostaGrupo+1-12] and listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo+1])] != classificadosGrupos[apostaGrupo-12]:
                    pontuacaoGrupos += 21
                elif listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo])] != classificadosGrupos[apostaGrupo-12] and listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo+1])] == classificadosGrupos[apostaGrupo+1-12]:
                    pontuacaoGrupos += 30
                elif listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo])] != classificadosGrupos[apostaGrupo+1-12] and listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo+1])] == classificadosGrupos[apostaGrupo-12]:
                    pontuacaoGrupos += 21
                elif listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo])] != classificadosGrupos[apostaGrupo-12] and listaSelecoes()[int(np.array(listaUsuarios)[contadorUsuario][apostaGrupo+1])] != classificadosGrupos[apostaGrupo+1-12]:
                    pontuacaoGrupos += 0

        listaUsuarios[contadorUsuario][2] = int(listaUsuarios[contadorUsuario][2]) + pontuacaoGrupos
        np.save(str(listaUsuarios[contadorUsuario][0]),listaUsuarios[contadorUsuario])


    for nomeGrupo in range(len(grupos()[:,0])):
        st.subheader(f'Grupo {grupos()[nomeGrupo][-1]}')
        
        # Datas e horários dos jogos
        for nomeJogo in range(6):
            with st.form(key = 'include_aposta_jogo_'+str(nomeJogo+1)+'do_grupo_'+str(grupos()[nomeGrupo][-1])):
                st.subheader(f'Grupo {grupos()[nomeGrupo][-1]} - Jogo {nomeJogo+1} - {dataHorarioJogoGrupo(nomeGrupo,nomeJogo)}')

                # rodada e jogo
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
                        #print('Jogo 1')
                        placar_selecao_1 = st.number_input(label = grupos()[nomeGrupo][time1], min_value = 0, max_value = 10, step = 1, format = '%d')
                        placar_selecao_2 = st.number_input(label = grupos()[nomeGrupo][time2], min_value = 0, max_value = 10, step = 1, format = '%d')
                        botao_jogo_1 = st.form_submit_button(label = f'Postar placar do jogo {nomeJogo+1}')
                        inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                        if botao_jogo_1 and not inicioJogo:
                            fazerApostaPrimeiraFase(usuario,nomeGrupo,nomeJogo,placar_selecao_1,placar_selecao_2)
                            np.save(str(nomeUsuario),usuario)
                            st.subheader(f'Registrou.')
                        if usuario[28+2*6*nomeGrupo+2*nomeJogo] != '':
                            st.subheader('Fim de jogo!')
                            st.write(f'{grupos()[nomeGrupo][time1]} {usuario[28+2*6*nomeGrupo+2*nomeJogo]} X {usuario[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time2]}')
                            classificacao = classificacaoFaseGrupos(classificacao,nomeGrupo,nomeJogo,int(usuario[28+2*6*nomeGrupo+2*nomeJogo]),int(usuario[29+2*6*nomeGrupo+2*nomeJogo]))
                            if not inicioJogo:
                                for contadorUsuario in range(1, len(listaUsuarios), 1):
                                    pontuacaoJogo = 0
                                    listaUsuarios[contadorUsuario], pontuacao = resultadoApostadorFaseGrupos(listaUsuarios[contadorUsuario],pontuacaoJogo,listaUsuarios[contadorUsuario][28+2*6*nomeGrupo+2*nomeJogo],listaUsuarios[contadorUsuario][29+2*6*nomeGrupo+2*nomeJogo],usuario[28+2*6*nomeGrupo+2*nomeJogo],usuario[29+2*6*nomeGrupo+2*nomeJogo])
                                    st.subheader(f'A sua pontuação do {listaUsuarios[contadorUsuario][0]} foi: {pontuacao} ponto(s)')
                                    np.save(str(listaUsuarios[contadorUsuario][0]),listaUsuarios[contadorUsuario])

                    elif nomeJogo == 1:
                        #print('Jogo 2')
                        placar_selecao_3 = st.number_input(label = grupos()[nomeGrupo][time3], min_value = 0, max_value = 10, step = 1, format = '%d')
                        placar_selecao_4 = st.number_input(label = grupos()[nomeGrupo][time4], min_value = 0, max_value = 10, step = 1, format = '%d')
                        botao_jogo_2 = st.form_submit_button(label = f'Postar placar do jogo {nomeJogo+1}')
                        inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                        if botao_jogo_2 and not inicioJogo:
                            fazerApostaPrimeiraFase(usuario,nomeGrupo,nomeJogo,placar_selecao_3,placar_selecao_4)
                            np.save(str(nomeUsuario),usuario)
                            st.subheader(f'Registrou.')
                        if usuario[28+2*6*nomeGrupo+2*nomeJogo] != '':
                            st.subheader('Fim de jogo!')
                            st.write(f'{grupos()[nomeGrupo][time3]} {usuario[28+2*6*nomeGrupo+2*nomeJogo]} X {usuario[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time4]}')
                            classificacao = classificacaoFaseGrupos(classificacao,nomeGrupo,nomeJogo,int(usuario[28+2*6*nomeGrupo+2*nomeJogo]),int(usuario[29+2*6*nomeGrupo+2*nomeJogo]))
                            if not inicioJogo:
                                for contadorUsuario in range(1, len(listaUsuarios), 1):
                                    pontuacaoJogo = 0
                                    listaUsuarios[contadorUsuario], pontuacao = resultadoApostadorFaseGrupos(listaUsuarios[contadorUsuario],pontuacaoJogo,listaUsuarios[contadorUsuario][28+2*6*nomeGrupo+2*nomeJogo],listaUsuarios[contadorUsuario][29+2*6*nomeGrupo+2*nomeJogo],usuario[28+2*6*nomeGrupo+2*nomeJogo],usuario[29+2*6*nomeGrupo+2*nomeJogo])
                                    st.subheader(f'A sua pontuação do {listaUsuarios[contadorUsuario][0]} foi: {pontuacao} ponto(s)')
                                    np.save(str(listaUsuarios[contadorUsuario][0]),listaUsuarios[contadorUsuario])

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
                        #print('Jogo 3')
                        placar_selecao_1 = st.number_input(label = grupos()[nomeGrupo][time1], min_value = 0, max_value = 10, step = 1, format = '%d')
                        placar_selecao_2 = st.number_input(label = grupos()[nomeGrupo][time2], min_value = 0, max_value = 10, step = 1, format = '%d')
                        botao_jogo_3 = st.form_submit_button(label = f'Postar placar do jogo {nomeJogo+1}')
                        inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                        if botao_jogo_3 and not inicioJogo:
                            fazerApostaPrimeiraFase(usuario,nomeGrupo,nomeJogo,placar_selecao_1,placar_selecao_2)
                            np.save(str(nomeUsuario),usuario)
                            st.subheader(f'Registrou.')
                        if usuario[28+2*6*nomeGrupo+2*nomeJogo] != '':
                            st.subheader('Fim de jogo!')
                            st.write(f'{grupos()[nomeGrupo][time1]} {usuario[28+2*6*nomeGrupo+2*nomeJogo]} X {usuario[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time2]}')
                            classificacao = classificacaoFaseGrupos(classificacao,nomeGrupo,nomeJogo,int(usuario[28+2*6*nomeGrupo+2*nomeJogo]),int(usuario[29+2*6*nomeGrupo+2*nomeJogo]))
                            if not inicioJogo:
                                for contadorUsuario in range(1, len(listaUsuarios), 1):
                                    pontuacaoJogo = 0
                                    listaUsuarios[contadorUsuario], pontuacao = resultadoApostadorFaseGrupos(listaUsuarios[contadorUsuario],pontuacaoJogo,listaUsuarios[contadorUsuario][28+2*6*nomeGrupo+2*nomeJogo],listaUsuarios[contadorUsuario][29+2*6*nomeGrupo+2*nomeJogo],usuario[28+2*6*nomeGrupo+2*nomeJogo],usuario[29+2*6*nomeGrupo+2*nomeJogo])
                                    st.subheader(f'A sua pontuação do {listaUsuarios[contadorUsuario][0]} foi: {pontuacao} ponto(s)')
                                    np.save(str(listaUsuarios[contadorUsuario][0]),listaUsuarios[contadorUsuario])

                    elif nomeJogo == 3:
                        #print('Jogo 4')
                        placar_selecao_3 = st.number_input(label = grupos()[nomeGrupo][time3], min_value = 0, max_value = 10, step = 1, format = '%d')
                        placar_selecao_4 = st.number_input(label = grupos()[nomeGrupo][time4], min_value = 0, max_value = 10, step = 1, format = '%d')
                        botao_jogo_4 = st.form_submit_button(label = f'Postar placar do jogo {nomeJogo+1}')
                        inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                        if botao_jogo_4 and not inicioJogo:
                            fazerApostaPrimeiraFase(usuario,nomeGrupo,nomeJogo,placar_selecao_3,placar_selecao_4)
                            np.save(str(nomeUsuario),usuario)
                            st.subheader(f'Registrou.')
                        if usuario[28+2*6*nomeGrupo+2*nomeJogo] != '':
                            st.subheader('Fim de jogo!')
                            st.write(f'{grupos()[nomeGrupo][time4]} {usuario[28+2*6*nomeGrupo+2*nomeJogo]} X {usuario[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time3]}')
                            classificacao = classificacaoFaseGrupos(classificacao,nomeGrupo,nomeJogo,int(usuario[28+2*6*nomeGrupo+2*nomeJogo]),int(usuario[29+2*6*nomeGrupo+2*nomeJogo]))
                            if not inicioJogo:
                                for contadorUsuario in range(1, len(listaUsuarios), 1):
                                    pontuacaoJogo = 0
                                    listaUsuarios[contadorUsuario], pontuacao = resultadoApostadorFaseGrupos(listaUsuarios[contadorUsuario],pontuacaoJogo,listaUsuarios[contadorUsuario][28+2*6*nomeGrupo+2*nomeJogo],listaUsuarios[contadorUsuario][29+2*6*nomeGrupo+2*nomeJogo],usuario[28+2*6*nomeGrupo+2*nomeJogo],usuario[29+2*6*nomeGrupo+2*nomeJogo])
                                    st.subheader(f'A sua pontuação do {listaUsuarios[contadorUsuario][0]} foi: {pontuacao} ponto(s)')
                                    np.save(str(listaUsuarios[contadorUsuario][0]),listaUsuarios[contadorUsuario])

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
                        #print('Jogo 5')
                        placar_selecao_1 = st.number_input(label = grupos()[nomeGrupo][time1], min_value = 0, max_value = 10, step = 1, format = '%d')
                        placar_selecao_2 = st.number_input(label = grupos()[nomeGrupo][time2], min_value = 0, max_value = 10, step = 1, format = '%d')
                        botao_jogo_5 = st.form_submit_button(label = f'Postar placar do jogo {nomeJogo+1}')
                        inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                        if botao_jogo_5 and not inicioJogo:
                            fazerApostaPrimeiraFase(usuario,nomeGrupo,nomeJogo,placar_selecao_1,placar_selecao_2)
                            np.save(str(nomeUsuario),usuario)
                            st.subheader(f'Registrou.')
                        if usuario[28+2*6*nomeGrupo+2*nomeJogo] != '':
                            st.subheader('Fim de jogo!')
                            st.write(f'{grupos()[nomeGrupo][time1]} {usuario[28+2*6*nomeGrupo+2*nomeJogo]} X {usuario[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time2]}')
                            classificacao = classificacaoFaseGrupos(classificacao,nomeGrupo,nomeJogo,int(usuario[28+2*6*nomeGrupo+2*nomeJogo]),int(usuario[29+2*6*nomeGrupo+2*nomeJogo]))
                            if not inicioJogo:
                                for contadorUsuario in range(1, len(listaUsuarios), 1):
                                    pontuacaoJogo = 0
                                    listaUsuarios[contadorUsuario], pontuacao = resultadoApostadorFaseGrupos(listaUsuarios[contadorUsuario],pontuacaoJogo,listaUsuarios[contadorUsuario][28+2*6*nomeGrupo+2*nomeJogo],listaUsuarios[contadorUsuario][29+2*6*nomeGrupo+2*nomeJogo],usuario[28+2*6*nomeGrupo+2*nomeJogo],usuario[29+2*6*nomeGrupo+2*nomeJogo])
                                    st.subheader(f'A sua pontuação do {listaUsuarios[contadorUsuario][0]} foi: {pontuacao} ponto(s)')
                                    np.save(str(listaUsuarios[contadorUsuario][0]),listaUsuarios[contadorUsuario])

                    elif nomeJogo == 5:
                        #print('Jogo 6')
                        placar_selecao_3 = st.number_input(label = grupos()[nomeGrupo][time3], min_value = 0, max_value = 10, step = 1, format = '%d')
                        placar_selecao_4 = st.number_input(label = grupos()[nomeGrupo][time4], min_value = 0, max_value = 10, step = 1, format = '%d')
                        botao_jogo_6 = st.form_submit_button(label = f'Postar placar do jogo {nomeJogo+1}')
                        inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                        if botao_jogo_6 and not inicioJogo:
                            fazerApostaPrimeiraFase(usuario,nomeGrupo,nomeJogo,placar_selecao_3,placar_selecao_4)
                            np.save(str(nomeUsuario),usuario)
                            st.subheader(f'Registrou.')
                        if usuario[28+2*6*nomeGrupo+2*nomeJogo] != '':
                            st.subheader('Fim de jogo!')
                            st.write(f'{grupos()[nomeGrupo][time3]} {usuario[28+2*6*nomeGrupo+2*nomeJogo]} X {usuario[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time4]}')
                            classificacao = classificacaoFaseGrupos(classificacao,nomeGrupo,nomeJogo,int(usuario[28+2*6*nomeGrupo+2*nomeJogo]),int(usuario[29+2*6*nomeGrupo+2*nomeJogo]))
                            if not inicioJogo:
                                for contadorUsuario in range(1, len(listaUsuarios), 1):
                                    pontuacaoJogo = 0
                                    listaUsuarios[contadorUsuario], pontuacao = resultadoApostadorFaseGrupos(listaUsuarios[contadorUsuario],pontuacaoJogo,listaUsuarios[contadorUsuario][28+2*6*nomeGrupo+2*nomeJogo],listaUsuarios[contadorUsuario][29+2*6*nomeGrupo+2*nomeJogo],usuario[28+2*6*nomeGrupo+2*nomeJogo],usuario[29+2*6*nomeGrupo+2*nomeJogo])
                                    st.subheader(f'A sua pontuação do {listaUsuarios[contadorUsuario][0]} foi: {pontuacao} ponto(s)')
                                    np.save(str(listaUsuarios[contadorUsuario][0]),listaUsuarios[contadorUsuario])

    rotuloColuna = ['P',  # pontuação
                    'J',  # jogos
                    'V',  # vitórias
                    'E',  # empates
                    'D',  # derrotas
                    'GP', # gols pró
                    'GC', # gols contra
                    'SG'] # saldo de gols
    for contadorClassificacao in range(len(classificacao)):
        classificacao[contadorClassificacao].pop(-1)
        df = pd.DataFrame(np.array([[classificacao[contadorClassificacao][0][1],classificacao[contadorClassificacao][0][2],classificacao[contadorClassificacao][0][3],classificacao[contadorClassificacao][0][4],classificacao[contadorClassificacao][0][5],classificacao[contadorClassificacao][0][6],classificacao[contadorClassificacao][0][7],classificacao[contadorClassificacao][0][8]],
                                    [classificacao[contadorClassificacao][1][1],classificacao[contadorClassificacao][1][2],classificacao[contadorClassificacao][1][3],classificacao[contadorClassificacao][1][4],classificacao[contadorClassificacao][1][5],classificacao[contadorClassificacao][1][6],classificacao[contadorClassificacao][1][7],classificacao[contadorClassificacao][1][8]],
                                    [classificacao[contadorClassificacao][2][1],classificacao[contadorClassificacao][2][2],classificacao[contadorClassificacao][2][3],classificacao[contadorClassificacao][2][4],classificacao[contadorClassificacao][2][5],classificacao[contadorClassificacao][2][6],classificacao[contadorClassificacao][2][7],classificacao[contadorClassificacao][2][8]],
                                    [classificacao[contadorClassificacao][3][1],classificacao[contadorClassificacao][3][2],classificacao[contadorClassificacao][3][3],classificacao[contadorClassificacao][3][4],classificacao[contadorClassificacao][3][5],classificacao[contadorClassificacao][3][6],classificacao[contadorClassificacao][3][7],classificacao[contadorClassificacao][3][8]]
                                    ]),
                    columns = tuple(rotuloColuna)
        )
        df.index = [classificacao[contadorClassificacao][0][0],classificacao[contadorClassificacao][1][0],classificacao[contadorClassificacao][2][0],classificacao[contadorClassificacao][3][0]]
        st.table(df)
    
    st.subheader(listaUsuarios)
    classificacaoBolao = []
    dadosClassificacao = []
    for contadorUsuario in range(1, len(listaUsuarios), 1):
        classificacaoBolao.append([listaUsuarios[contadorUsuario][0],listaUsuarios[contadorUsuario][2],listaUsuarios[contadorUsuario][3],listaUsuarios[contadorUsuario][4],listaUsuarios[contadorUsuario][5],listaUsuarios[contadorUsuario][6],listaUsuarios[contadorUsuario][7]])
        dadosClassificacao.append(np.delete(np.array(classificacaoBolao[contadorUsuario-1]),0,0))
    df0 = pd.DataFrame(np.array(dadosClassificacao),
                       columns = ('Pontos','Cravadas','Acertos','Erros','Nadas','Não apostas'))
    df0.index = np.delete(np.array(listaUsuarios)[:,0],0)
    st.table(df0)
    
    st.header('Oitavas de final')
    #-----------------------------
    opcoesOitavas1 = ['Holanda','Estados Unidos']
    opcoesOitavas2 = ['Argentina','Austrália']
    opcoesOitavas3 = ['Japão','Croácia']
    opcoesOitavas4 = ['Brasil','Coreia do Sul']
    opcoesOitavas5 = ['Inglaterra','Senegal']
    opcoesOitavas6 = ['França','Polônia']
    opcoesOitavas7 = ['Marrocos','Espanha']
    opcoesOitavas8 = ['Portugal','Suíça']
    opcoesOitavas  = [opcoesOitavas1,
                      opcoesOitavas2,
                      opcoesOitavas3,
                      opcoesOitavas4,
                      opcoesOitavas5,
                      opcoesOitavas6,
                      opcoesOitavas7,
                      opcoesOitavas8]
    #-----------------------------
    horarioOitavas1 = horarioJogo(2022,12,3,12,0)
    horarioOitavas2 = horarioJogo(2022,12,3,16,0)
    horarioOitavas3 = horarioJogo(2022,12,5,12,0)
    horarioOitavas4 = horarioJogo(2022,12,5,16,0)
    horarioOitavas5 = horarioJogo(2022,12,4,16,0)
    horarioOitavas6 = horarioJogo(2022,12,4,12,0)
    horarioOitavas7 = horarioJogo(2022,12,6,12,0)
    horarioOitavas8 = horarioJogo(2022,12,6,16,0)
    horarioOitavas  = [horarioOitavas1,
                       horarioOitavas2,
                       horarioOitavas3,
                       horarioOitavas4,
                       horarioOitavas5,
                       horarioOitavas6,
                       horarioOitavas7,
                       horarioOitavas8]
    #-----------------------------
    dataOitavas1 = datetime(2022,12,3,12,0)
    dataOitavas2 = datetime(2022,12,3,16,0)
    dataOitavas3 = datetime(2022,12,5,12,0)
    dataOitavas4 = datetime(2022,12,5,16,0)
    dataOitavas5 = datetime(2022,12,4,16,0)
    dataOitavas6 = datetime(2022,12,4,12,0)
    dataOitavas7 = datetime(2022,12,6,12,0)
    dataOitavas8 = datetime(2022,12,6,16,0)
    dataOitavas  = [dataOitavas1,
                    dataOitavas2,
                    dataOitavas3,
                    dataOitavas4,
                    dataOitavas5,
                    dataOitavas6,
                    dataOitavas7,
                    dataOitavas8]

    for nomeJogo in range(8):
        st.subheader(f'Jogo {nomeJogo+1} - {opcoesOitavas[nomeJogo][0]} x {opcoesOitavas[nomeJogo][1]} - {dataOitavas[nomeJogo]}')
        with st.form(key = 'incluirApostaFaseEliminatoriasOitavasJogo'+str(nomeJogo+1)):
            placarOitavas = st.selectbox('Qual será a seleção classificada?', options = opcoesOitavas[nomeJogo], index = 0)
            placarOitavasSelecao1 = st.number_input(label = opcoesOitavas[nomeJogo][0], min_value = 0, max_value = 10, step = 1, format = '%d')
            placarOitavasSelecao2 = st.number_input(label = opcoesOitavas[nomeJogo][1], min_value = 0, max_value = 10, step = 1, format = '%d')
            botaoPlacarOitavas = st.form_submit_button(label = 'Placar')
        if botaoPlacarOitavas and not horarioOitavas[nomeJogo]:
            if placarOitavas == opcoesOitavas[nomeJogo][0] and placarOitavasSelecao1 < placarOitavasSelecao2 or placarOitavas == opcoesOitavas[nomeJogo][1] and placarOitavasSelecao2 < placarOitavasSelecao1:
                st.subheader('Placar INVÁLIDO!')
                st.write(f'Tente postar novamente.')
            else:
                usuario[124+3*nomeJogo], usuario[125+3*nomeJogo] = placarOitavasSelecao1, placarOitavasSelecao2
                usuario[126+3*nomeJogo] = listaSelecoes().index(placarOitavas)
                np.save(str(nomeUsuario),usuario)
        elif botaoPlacarOitavas and horarioOitavas[nomeJogo]:
            st.subheader('O jogo ainda não começou!')
            st.write(f'Você NÃO pode postar o placar.')
        if usuario[124+3*nomeJogo] != '' and usuario[126+3*nomeJogo] != '':
            st.subheader('Fim de Jogo!')
            st.subheader('Placar registrado.')
            st.write(f'{opcoesOitavas[nomeJogo][0]} {usuario[124+3*nomeJogo]} X {usuario[125+3*nomeJogo]} {opcoesOitavas[nomeJogo][1]}')
            st.write(f'Seleção classificada: {listaSelecoes()[int(usuario[126+3*nomeJogo])]}')
            if not horarioOitavas[nomeJogo]:
                for contadorUsuario in range(1, len(listaUsuarios), 1):
                    pontuacaoJogo = 0
                    listaUsuarios[contadorUsuario], pontuacao1 = resultadoApostadorFaseEliminatoria(listaUsuarios[contadorUsuario],pontuacaoJogo,listaUsuarios[contadorUsuario][124+3*nomeJogo],listaUsuarios[contadorUsuario][125+3*nomeJogo],usuario[124+3*nomeJogo],usuario[125+3*nomeJogo])
                    listaUsuarios[contadorUsuario], pontuacao2 = resultadoApostadorFaseEliminatoriaSelecao(listaUsuarios[contadorUsuario],pontuacaoJogo,listaUsuarios[contadorUsuario][126+3*nomeJogo],usuario[126+3*nomeJogo])
                    st.subheader(f'A pontuação de {listaUsuarios[contadorUsuario][0]} foi: {pontuacao1+pontuacao2} ponto(s)')
                    np.save(str(listaUsuarios[contadorUsuario][0]),listaUsuarios[contadorUsuario])

    return

#-----------------------------------------------------------------------------#

def apostasQuartas(usuario,nomeUsuario,usuarioMestre):

    st.subheader('Quartas de final')
    #-----------------------------
    opcoesQuartas1 = ['Brasil','Croácia']
    opcoesQuartas2 = ['Holanda','Argentina']
    opcoesQuartas3 = ['Inglaterra','França']
    opcoesQuartas4 = ['Marrocos','Portugal']
    opcoesQuartas  = [opcoesQuartas1,
                      opcoesQuartas2,
                      opcoesQuartas3,
                      opcoesQuartas4]
    #-----------------------------
    horarioQuartas1 = horarioJogo(2022,12,9,12,0)
    horarioQuartas2 = horarioJogo(2022,12,9,16,0)
    horarioQuartas3 = horarioJogo(2022,12,10,16,0)
    horarioQuartas4 = horarioJogo(2022,12,10,12,0)
    horarioQuartas  = [horarioQuartas1,
                       horarioQuartas2,
                       horarioQuartas3,
                       horarioQuartas4]
    #-----------------------------
    dataQuartas1 = datetime(2022,12,9,12,0)
    dataQuartas2 = datetime(2022,12,9,16,0)
    dataQuartas3 = datetime(2022,12,10,16,0)
    dataQuartas4 = datetime(2022,12,10,12,0)
    dataQuartas  = [dataQuartas1,
                    dataQuartas2,
                    dataQuartas3,
                    dataQuartas4]
    #-----------------------------
    for nomeJogo in range(4):
        st.subheader(f'Jogo {nomeJogo+1} - {opcoesQuartas[nomeJogo][0]} x {opcoesQuartas[nomeJogo][1]} - {dataQuartas[nomeJogo]}')
        with st.form(key = 'incluirApostaFaseEliminatoriasQuartasJogo'+str(nomeJogo+1)):
            apostaQuartas = st.selectbox('Qual será a seleção classificada?', options = opcoesQuartas[nomeJogo], index = 0)
            apostaQuartasSelecao1 = st.number_input(label = opcoesQuartas[nomeJogo][0], min_value = 0, max_value = 10, step = 1, format = '%d')
            apostaQuartasSelecao2 = st.number_input(label = opcoesQuartas[nomeJogo][1], min_value = 0, max_value = 10, step = 1, format = '%d')
            botaoApostaQuartas = st.form_submit_button(label = 'Apostar')
        if botaoApostaQuartas and horarioQuartas[nomeJogo]:
            if apostaQuartas == opcoesQuartas[nomeJogo][0] and apostaQuartasSelecao1 < apostaQuartasSelecao2 or apostaQuartas == opcoesQuartas[nomeJogo][1] and apostaQuartasSelecao2 < apostaQuartasSelecao1:
                st.subheader('Apostas INVÁLIDAS!')
                st.write(f'Tente realizar as apostas novamente.')
            else:
                usuario[148+3*nomeJogo], usuario[149+3*nomeJogo] = apostaQuartasSelecao1, apostaQuartasSelecao2
                usuario[150+3*nomeJogo] = listaSelecoes().index(apostaQuartas)
                np.save(str(nomeUsuario),usuario)
        elif botaoApostaQuartas and not horarioQuartas[nomeJogo]:
            st.subheader('O jogo já começou!')
            st.write(f'Você NÃO pode realizar as apostas.')
        if usuario[148+3*nomeJogo] != '' and usuario[150+3*nomeJogo] != '':
            st.subheader('Aposta registrada!')
            st.write(f'{opcoesQuartas[nomeJogo][0]} {usuario[148+3*nomeJogo]} X {usuario[149+3*nomeJogo]} {opcoesQuartas[nomeJogo][1]}')
            st.write(f'Aposta classificação: {listaSelecoes()[int(usuario[150+3*nomeJogo])]}')
        if usuarioMestre[148+3*nomeJogo] != '' and usuarioMestre[150+3*nomeJogo] != '':
            st.subheader('Fim de jogo!')
            st.write(f'{opcoesQuartas[nomeJogo][0]} {usuarioMestre[148+3*nomeJogo]} X {usuarioMestre[149+3*nomeJogo]} {opcoesQuartas[nomeJogo][1]}')
            st.write(f'Seleção classificada: {usuarioMestre[150+3*nomeJogo]}')

    return usuario

#-----------------------------------------------------------------------------#

def apostasQuartasApostador(contadorUsuario):

    dataHoraMinutoAtual = datetime.strptime(datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%d/%m/%y %H:%M'), '%d/%m/%y %H:%M')

    #-----------------------------
    st.subheader('Quartas de final')
    #-----------------------------

    opcoesQuartas1 = ['Brasil','Croácia']
    opcoesQuartas2 = ['Holanda','Argentina']
    opcoesQuartas3 = ['Inglaterra','França']
    opcoesQuartas4 = ['Marrocos','Portugal']
    opcoesQuartas  = [opcoesQuartas1,
                      opcoesQuartas2,
                      opcoesQuartas3,
                      opcoesQuartas4]
    #-----------------------------
    horarioQuartas1 = horarioJogo(2022,12,9,12,0)
    horarioQuartas2 = horarioJogo(2022,12,9,16,0)
    horarioQuartas3 = horarioJogo(2022,12,10,16,0)
    horarioQuartas4 = horarioJogo(2022,12,10,12,0)
    horarioQuartas  = [horarioQuartas1,
                       horarioQuartas2,
                       horarioQuartas3,
                       horarioQuartas4]
    #-----------------------------

    for nomeJogo in range(4):
        st.write(f'Jogo {nomeJogo+1} - {np.array(listaUsuarios)[contadorUsuario][0]}')
        if not horarioQuartas[nomeJogo]:
        #if horarioOitavas[nomeJogo]:
            if np.array(listaUsuarios)[contadorUsuario][148+3*nomeJogo] != '':
                st.write(f'{opcoesQuartas[nomeJogo][0]} {np.array(listaUsuarios)[contadorUsuario][148+3*nomeJogo]}x{np.array(listaUsuarios)[contadorUsuario][149+3*nomeJogo]} {opcoesQuartas[nomeJogo][1]}')
                st.write(f'Classificado: {listaSelecoes()[int(listaUsuarios[contadorUsuario][150+3*nomeJogo])]}')
            else:
                st.write(f'Aposta NÃO realizada.')
    
    #-------------------------------------------

    return

#-----------------------------------------------------------------------------#

def lerUsuarios():
    '''
    
    Função para ler os usuários.
    
    '''
    usuarioMestre = np.load('usuarioMestre.npy')
    Paulo  = np.load('Paulo.npy')
    Bola   = np.load('Bola.npy')
    Thiti  = np.load('Thiti.npy')
    Marcos = np.load('Marcos.npy')
    Rafa   = np.load('Rafa.npy')
    Taio   = np.load('Taio.npy')
    #usuario1 = np.load('usuario1.npy')
    #usuario2 = np.load('usuario2.npy')
    #usuario3 = np.load('usuario3.npy')
    #listaUsuarios = [usuarioMestre,usuario1,usuario2,usuario3,Paulo,Bola,Thiti,Marcos,Rafa,Taio]
    listaUsuarios = [usuarioMestre,Paulo,Bola,Thiti,Marcos,Rafa,Taio]

    return listaUsuarios

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#-----------------------------------------------------------------------------#
#=============================================================================#
#-----------------------------------------------------------------------------#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# pegando os usuarios
listaUsuarios = lerUsuarios()

# pegar o usuario mestre
usuarioMestre = np.load('usuarioMestre.npy')

def main():
    
    ''' Simple Login App '''
    menu = ['Home','Cadastro','Login']
    choice = st.sidebar.selectbox('Menu',menu)

    #-----------------------------------------------------------------------------#
    #=============================================================================#
    #-----------------------------------------------------------------------------#

    if choice == 'Home':
        st.subheader('Acesso do administrador')
        nomeUsuario  = st.text_input('Nome de usuário')
        senhaUsuario = st.text_input('Senha', type = 'password')

        if nomeUsuario == listaUsuarios[0][0] and senhaUsuario == listaUsuarios[0][1]:
            task = st.sidebar.selectbox('Task',['Conexão','Reset','Placares','Usuários'])

            if task == 'Conexão':
                st.title('Conectado')
                st.sidebar.success('Você está logado como {}'.format(nomeUsuario))
                
            elif task == 'Reset':
                st.title('Reset de dados')
                st.sidebar.success('Você está logado como {}'.format(nomeUsuario))

            elif task == 'Placares':
                st.title('Placares dos jogos')
                st.sidebar.success('Você está logado como {}'.format(nomeUsuario))
                placarJogos(nomeUsuario)

            elif task == 'Usuários':
                st.title('Usuários')
                st.sidebar.success('Você está logado como {}'.format(nomeUsuario))
                st.header(f'Usuários: {np.array(listaUsuarios)[:,0]}')
                st.subheader(listaUsuarios)

        else:
            st.subheader('Você não tem acesso')

    #-----------------------------------------------------------------------------#
    #=============================================================================#
    #-----------------------------------------------------------------------------#

    elif choice == 'Cadastro':
        st.subheader('Criar nova conta')

    #-----------------------------------------------------------------------------#
    #=============================================================================#
    #-----------------------------------------------------------------------------#

    elif choice == 'Login':
        nomeUsuario  = st.sidebar.text_input('Nome de usuário')
        senhaUsuario = st.sidebar.text_input('Senha', type = 'password')

        if nomeUsuario != '':
            for contadorUsuario in range(len(listaUsuarios)):
                if nomeUsuario == np.array(listaUsuarios)[:,0][contadorUsuario]:
                    login = True
                    break
                elif contadorUsuario == len(listaUsuarios)-1:
                    st.sidebar.error('Usuário inexistente.')
                    login = False

        if st.sidebar.checkbox('Login') and login:
            # pegar o usuario
            indiceUsuario = np.where(np.array(listaUsuarios)[:,0] == nomeUsuario)[0][0]
            usuario = listaUsuarios[indiceUsuario]

            if nomeUsuario == usuario[0] and senhaUsuario == usuario[1]:
                # confirmação do login
                st.sidebar.success('Você está logado como {}'.format(nomeUsuario))
                task = st.sidebar.selectbox(label = 'Selecionar o campeonato', options = ['Copa do Mundo 2022','Outros'], index = 1)

                if task == 'Copa do Mundo 2022':
                    st.title('Bolão da Copa do Mundo 2022')
                    taskInterno = st.sidebar.selectbox(label = 'Opções', options = ['Apostas iniciais','Apostas fase de grupos','Apostas nas fases eliminatórias','Resumo das apostas','Links externos'], index = 0)

                    if taskInterno == 'Apostas iniciais':
                        usuario = apostasIniciais(usuario,nomeUsuario)

                    elif taskInterno == 'Apostas fase de grupos':
                        usuario = apostasFaseGrupos(usuario,nomeUsuario,usuarioMestre)

                    elif taskInterno == 'Apostas nas fases eliminatórias':
                        st.header('Apostas nas fases eliminatórias')
                        usuario = apostasQuartas(usuario,nomeUsuario,usuarioMestre)
                        # Text files
                        text_contents = '''Foo, Bar
                                        123, 456
                                        789, 000
                                        '''
                        # Different ways to use the API
                        st.download_button('Download CSV', text_contents, 'text/csv')
                        st.download_button('Download CSV', text_contents)  # Defaults to 'text/plain'

                        with open('myfile.csv') as f:
                            st.download_button('Download CSV', f)  # Defaults to 'text/plain'
                        # ---
                        
                        # Binary files
                        binary_contents = b'whatever'

                        # Different ways to use the API
                        st.download_button('Download file', binary_contents)  # Defaults to 'application/octet-stream'

                        with open('myfile.zip', 'rb') as f:
                            st.download_button('Download Zip', f, file_name='archive.zip')  # Defaults to 'application/octet-stream'

                        # You can also grab the return value of the button,
                        # just like with any other button.
                        if st.download_button(...):
                            st.write('Thanks for downloading!')

                        usuario = apostasOitavas(usuario,nomeUsuario,usuarioMestre)

                    elif taskInterno == 'Resumo das apostas':
                        st.header('Resumo das apostas')

                        tabs = []
                        for tab in range(len(listaUsuarios)):
                            tabs.append(np.array(listaUsuarios)[tab][0])

                        tabs[0] = 'Classificação do Bolão'
                        tabs = st.tabs(tabs)
                        for contadorUsuario in range(len(listaUsuarios)):
                            if contadorUsuario == 0:
                                with tabs[contadorUsuario]:
                                    st.header(f'Resumo das apostas do Bolão')
                                    classificacaoDoBolao()
                                    classificacaoBolaoGrupos()
                            else:
                                with tabs[contadorUsuario]:
                                    st.header(f'Resumo das apostas - {np.array(listaUsuarios)[contadorUsuario][0]}')                                    
                                    apostasQuartasApostador(contadorUsuario)
                                    apostasOitavasApostador(contadorUsuario)
                                    apostasPrincipaisApostador(contadorUsuario)
                                    apostasGruposApostador(contadorUsuario)
                                    apostasFaseGruposApostador(contadorUsuario)

                    elif taskInterno == 'Links externos':
                        st.header('Em breve ...')

                elif task == 'Outros':
                    st.title('Dá uma seguradinha que estamos começando ainda ... 🎈')

            else:
                # não confirmação do login
                st.sidebar.error('Senha inválida.')

#-----------------------------------------------------------------------------#
#=============================================================================#
#-----------------------------------------------------------------------------#

if __name__ == '__main__':
    main()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#-----------------------------------------------------------------------------#
#=============================================================================#
#-----------------------------------------------------------------------------#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
