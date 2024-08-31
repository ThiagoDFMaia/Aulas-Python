# importar as bibliotecas
import pandas as pd
import numpy as np


# Carregar o dataset ou arquivos

def carregarDados(arquivo):
    # Carregar um arquivo csv via pandas
    df=pd.read_csv(arquivo,sep=',', encoding='utf-8')
    return df

def prepararDados(dataFrame):
    print(dataFrame.info())
    print(dataFrame.tail())
    print(dataFrame.describe())
    # std (desvio padrao)
    '''
    Desvio padrao:
    Quanto mais destante da media estiver o dado maior vai ser o desvio padrao
        Ideal é que o desvio(os dados)  esteja o mais proximo possivel da media
    '''
    return dataFrame


url='C:\\Users\\aluno\\Desktop\\Thiago\\Aulas-Python\\aulas_pos\\dataset\\titanic.csv'
# carrega o arquivo
df=carregarDados(url)
# prepara o arquivo
df=prepararDados(df)

print( df.head())

