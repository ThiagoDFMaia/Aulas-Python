import lib_projeto as lib

import pandas as pd

import os 





os.system('cls')

df=pd.read_csv('dataset\\suicidios_2010_a_2019.csv')
print(80*'#')
print(30*'#','Informações do DataFrame\n\n')
df.info()

print(80*'#')
print(30*'#','Iniciando o tratamento\n\n')
df=lib.tratamento_dados(df)
print(30*'#','DataFrame após o tratamento!\n\n')
df.info()

print(df.head())

print(80*'#')
print(30*'#','Gerando os graficos\n\n')

lib.gera_subplot(df)
lib.gera_grafico_iterativo(df)

print(80*'#')
print (30*'#', 'Ajustando DataFrame para o treinamento\n\n')


for coluna in df.columns:
    if df[coluna].dtype == 'object':  # Verifica se a coluna é do tipo object
        df[coluna] = lib.codifica_coluna(df[coluna])
print(df.head())
print(df.info())
print(80*'#')
print(30*'#','Separando os dados para treinamento e teste\n\n')

df_treino,df_teste= lib.separa_dados_treinamento(df,0.3)
print(10*'#','Dados para treinamento\n')
print(df_treino.info())
print('\n\n')
print(10*'#','Dados para teste\n')
print(df_teste.info())