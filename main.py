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

def apostaPodio(usuario,apostaCampeao,apostaViceCampeao,apostaTerceiroColocado):
    
    # apostas podio
    usuario[9] = listaSelecoes().index(apostaCampeao) #apostaCampeao
    usuario[10] = listaSelecoes().index(apostaViceCampeao) #apostaViceCampeao
    usuario[11] = listaSelecoes().index(apostaTerceiroColocado) #apostaTerceiroColocado

    return

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

# DB Management
dados = sqlite3.connect('dados.db')
d = dados.cursor()

#-----------------------------------------------------------------------------#

def cria_tabela_usuarios():
    d.execute("CREATE TABLE IF NOT EXISTS tabela(login TEXT, senha TEXT)")

#-----------------------------------------------------------------------------#

def adicionar_dados_usuarios(login, senha):
    d.execute("INSERT INTO tabela(login, senha) VALUES(?, ?)", (login, senha))
    dados.commit()

#-----------------------------------------------------------------------------#

def login_usuario(username,password):
    d.execute('SELECT * FROM tabela WHERE login = ? AND senha = ?',(username,password))
    dado = d.fetchall()
    return dado

#-----------------------------------------------------------------------------#

def todos_os_usuarios():
    d.execute('SELECT * FROM tabela')
    dado = d.fetchall()
    return dado

#-----------------------------------------------------------------------------#

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

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#-----------------------------------------------------------------------------#
#=============================================================================#
#-----------------------------------------------------------------------------#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# criando o usuario mestre
usuariosLista = usuarioMestre()

def main():
    
    ''' Simple Login App '''
    menu = ['Home','Cadastro','Login']
    choice = st.sidebar.selectbox('Menu',menu)

    #-----------------------------------------------------------------------------#
    #=============================================================================#
    #-----------------------------------------------------------------------------#

    if choice == 'Home':
        st.subheader('Acesso do administrador')
        username = st.text_input('Nome de usuário')
        password = st.text_input('Senha', type = 'password')

        if username == 'usuarioMestre' and password == 'appBolao':
            task = st.sidebar.selectbox('Task',['Conexão','Reset','Placares','Usuários'])

            if task == 'Conexão':
                st.subheader('Conectado')
                
            elif task == 'Testes':
                st.subheader('Testes')

            elif task == 'Placares':
                st.title('Placares')


            elif task == 'Usuários':
                st.subheader('Usuários')

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
        username = st.sidebar.text_input('Nome de usuário')
        password = st.sidebar.text_input('Senha', type = 'password')

        if st.sidebar.checkbox('Login'):
            # pegar o índice do usuario
            indiceUsuario = np.where(np.array(todos_os_usuarios())[:,0] == username)[0][0]
            usuario = usuariosLista[indiceUsuario]
            usuarioMestre = np.load('usuarioMestre.npy')

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
