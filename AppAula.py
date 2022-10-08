#O código só roda se tiver salvo (Ctrl + s)
import streamlit as st
import pandas as pd
"### Salve"

# ou coloca dentro do write

st.write("**Alo** alo")

# vale a mesma notação do jupyter pra várias linhas

''' Salve

             ou

                salve'''
"Mostrando uma tabela de dados `pandas`"

df = pd.read_csv(r"C:\Users\guico\OneDrive\Documentos\UFPR\Matérias\Mineração de Dados\Datasets\iris.csv", sep = ";") 
#sep é o separador, se imprimir sem fica tudo em uma coluna com os elementos separados por ;
st.write(df)

'## Gerando um histograma de valores aleatórios'

numero = int(st.text_input('Número de intervalos do histograma',0))
st.write('O tamanho de intervalos é', numero)




# Widgets
separador = st.selectbox(
    'Selecione o separador utilizado na tabela',
    (';', ',', ' '))

st.write('You selected:', separador)

#Upload de arquivos

obj = st.file_uploader("Faça o upload de um banco de dados",['csv'])
df = pd.read_csv(obj, sep = separador )
st.write(df)

#Slider
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

#Botão
if "lista" not in st.session_state:
    st.session_state["lista"] = []

numero_digitado = st.number_input("Digite um número")
if st.button('Adiciona número'):
# É a mesma coisa que if st.button('Say hello') == True:
    st.write('Cliquei no botão')      
    st.session_state["lista"].append(numero_digitado)
    
st.line_chart( st.session_state["lista"] )
st.session_state


# Fazer uma tree
#df = pd.read_csv(r"C:\Users\guico\OneDrive\Documentos\UFPR\Matérias\Mineração de Dados\Datasets\producao_grega.csv")

#Requisições na internet

import requests as rq

respostas = rq.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
