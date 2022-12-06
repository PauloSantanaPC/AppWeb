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

def apostasIniciais():

	st.header('Apostas Campeão, Final da Copa do Mundo, Terceiro Colocado e Classificados nos Grupos')

    #-----------------------------------------------------------------------------#

    inicioCopa = horarioJogo(2022,11,22,10,0)
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

    st.subheader('Apostas Campeão, Final da Copa do Mundo e Terceiro Colocado ')
    with st.form(key = 'include_campeao'):
        apostaCampeao = st.selectbox('Quem será o campeão da Copa do Mundo 2022?', options = listaSelecoes(), index = 0)
        apostaViceCampeao = st.selectbox('Quem será o vice campeão da Copa do Mundo 2022?', options = listaSelecoes(), index = 0)
        apostaTerceiroColocado = st.selectbox('Quem será o terceiro colocado da Copa do Mundo 2022?', options = listaSelecoes(), index = 0)
        botaoApostaCampeao = st.form_submit_button(label = 'Apostar')
    if botaoApostaCampeao and inicioCopa:
    #if botaoApostaCampeao and not inicioCopa:
        apostaPodio(usuario,apostaCampeao,apostaViceCampeao,apostaTerceiroColocado)
        np.save(str(username),usuario)
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
            np.save(str(username),usuario)
        if usuario[2*nomeGrupo+12] != '':
            st.subheader('Apostas registradas!')
            st.write(f'Aposta primeiro colocado: {listaSelecoes()[int(usuario[2*nomeGrupo+12])]}')
            st.write(f'Aposta primeiro colocado: {listaSelecoes()[int(usuario[2*nomeGrupo+13])]}')

    #-----------------------------------------------------------------------------#


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#-----------------------------------------------------------------------------#
#=============================================================================#
#-----------------------------------------------------------------------------#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
