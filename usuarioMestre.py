#-----------------------------------------------------------------------------#
#=============================================================================#
#-----------------------------------------------------------------------------#

# Projeto - Bolão da Copa do Mundo
# Novembro 2022

#-----------------------------------------------------------------------------#
#=============================================================================#
#-----------------------------------------------------------------------------#

# importanto bibliotecas
#import streamlit as st
import sqlite3
import pandas as pd
import webbrowser
from datetime import date, datetime, time, timedelta
from time import strftime
import time
import pytz
import numpy as np # biblioteca Python usada para trabalhar com arrays
import pandas as pd

#-----------------------------------------------------------------------------#
#=============================================================================#
#-----------------------------------------------------------------------------#

# Funções

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
                       ['Brasil','Sérvia','Suiça','Camarões','G'],
                       ['Portugal','Gana','Uruguai','Coreia do Sul','H']]) # grupos da copa do mundo 2022
    
    return grupos

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

def apostaPodio(usuario,apostaCampeao,apostaViceCampeao,apostaTerceiroColocado):
    
    # apostas podio
    usuario[9] = listaSelecoes().index(apostaCampeao) #apostaCampeao
    usuario[10] = listaSelecoes().index(apostaViceCampeao) #apostaViceCampeao
    usuario[11] = listaSelecoes().index(apostaTerceiroColocado) #apostaTerceiroColocado

    return

#-----------------------------------------------------------------------------#
#=============================================================================#
#-----------------------------------------------------------------------------#

# caminho do usuário do app

nome = 'Paulo'
senha = 'P2043=pc)'
# 1. realizar o cadastro
usuario = cadastroApostador(nome,senha)
print(usuario)
print('')

# 2. Apostas

# Bolão
opcoesBolao = ['Campeão do mundo','Vice de nada','cara que não sabe de futebol, mas não vai ser o pior do bolão','Pangaré do futebol']
usuario[8] = 0

# Campeao, final e terceiro
apostaCampeao = 'Argentina'
apostaViceCampeao = 'França'
apostaTerceiroColocado = 'Espanha'
apostaPodio(usuario,apostaCampeao,apostaViceCampeao,apostaTerceiroColocado)

# Selecoes grupos
grupoA1 = 'Holanda'
grupoA2 = 'Equador'
grupoB1 = 'Inglaterra'
grupoB2 = 'Estados Unidos'
grupoC1 = 'Argentina'
grupoC2 = 'México'
grupoD1 = 'França'
grupoD2 = 'Dinamarca'
grupoE1 = 'Espanha'
grupoE2 = 'Alemanha'
grupoF1 = 'Bélgica'
grupoF2 = 'Croácia'
grupoG1 = 'Brasil'
grupoG2 = 'Suíça'
grupoH1 = 'Uruguai'
grupoH2 = 'Portugal'
apostaGrupos(usuario,0,grupoA1,grupoA2)
apostaGrupos(usuario,1,grupoB1,grupoB2)
apostaGrupos(usuario,2,grupoC1,grupoC2)
apostaGrupos(usuario,3,grupoD1,grupoD2)
apostaGrupos(usuario,4,grupoE1,grupoE2)
apostaGrupos(usuario,5,grupoF1,grupoF2)
apostaGrupos(usuario,6,grupoG1,grupoG2)
apostaGrupos(usuario,7,grupoH1,grupoH2)

# Fase grupos
for grupo in range(8):
    for jogo in range(6):
        #fazerAposta(usuario,j,i,i+1,i+2)
        golMandante  = grupo+1
        golVisitante = jogo+1
        fazerApostaPrimeiraFase(usuario, grupo, jogo, golMandante, golVisitante)

# Fase eliminatória
apostaOitavasSelecao1 = 2
apostaOitavasSelecao2 = 1
apostaOitavas         = 15
for nomeJogo in range(8):
    usuario[124+3*nomeJogo], usuario[125+3*nomeJogo] = apostaOitavasSelecao1, apostaOitavasSelecao2
    usuario[126+3*nomeJogo] = apostaOitavas

print('')
np.save(nome,usuario)
usuario = np.load(str(nome)+'.npy')
print(usuario)
print('')

#-----------------------------------------------------------------------------#
#=============================================================================#
#-----------------------------------------------------------------------------#