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
from funcoes import *

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#-----------------------------------------------------------------------------#
#=============================================================================#
#-----------------------------------------------------------------------------#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def lerUsuarios():
    '''
    Função para ler os usuários.
    '''
    usuarioMestre = np.load('usuarioMestre.npy')
    usuario1 = np.load('usuario1.npy')
    usuario2 = np.load('usuario2.npy')
    listaUsuarios = [usuarioMestre,usuario1,usuario2]

    return listaUsuarios

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#-----------------------------------------------------------------------------#
#=============================================================================#
#-----------------------------------------------------------------------------#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# criando o usuario mestre
listaUsuarios = lerUsuarios()

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

        if st.sidebar.checkbox('Login'):
            # pegar o usuario mestre
            usuarioMestre = np.load('usuarioMestre.npy')
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
                        st.header('Apostas Campeão, Final da Copa do Mundo, Terceiro Colocado e Classificados nos Grupos')
                        #st.header('Não consegui fazer')
                        #apostasIniciais()

                    elif taskInterno == 'Apostas fase de grupos':
                        st.header('Fase de Grupos')

                    elif taskInterno == 'Apostas nas fases eliminatórias':
                        st.header('Apostas nas fases eliminatórias')

                    elif taskInterno == 'Resumo das apostas':
                        st.header('Resumo das apostas')

                    elif taskInterno == 'Links externos':
                        st.header('Em breve ...')

                elif task == 'Outros':
                    st.title('Dá uma seguradinha que estamos começando ainda ... 🎈')

            else:
                # não confirmação do login
                st.sidebar.error('Usuário/senha inválidos')

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
