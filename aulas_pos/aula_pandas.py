# importar as bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
# sklearn biblioteca de aprendizado de maquina, mas tem algubs recursos para processamento de dados


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

    dataFrame.drop_duplicates()
    dataFrame.drop(columns=['Cabin','PassengerId','Name','Ticket'],inplace=True)
    dataFrame.dropna(inplace=True)
    '''
    converte tipo da coluna
    dataFrame['Age']= dataFrame['Age'].astype(int)
    '''

    '''
    print(dataFrame.info())
    print(dataFrame.tail())
    print(dataFrame.describe())
    '''
   
    '''
    fit_transform
        padroniza toda coluna enviada para int . obs: no processamento de aprendizado de maquin só é possível enviar int.
        No caso ele pega o padrao e insere numeros de identificação. exemplo o=homem e 1=mulher
    
    '''
    # codifica dados não numericos em numericos
    le=LabelEncoder()
    dataFrame['Sex']=le.fit_transform(dataFrame['Sex'])
    dataFrame['Embarked']=le.fit_transform(dataFrame['Embarked'])
    print(dataFrame.info())
    print(dataFrame)
    return dataFrame

def exemploGrafico():
    plt.plot([1,2],[3,4],'r--')
    plt.show()

def visualizacaoGrafica(dataFrame):
    idade=dataFrame['Age']
    sex=dataFrame['Sex']
    plt.plot(sex,idade,'g^')
    plt.show()
    #plt.plot([1,2],[3,4],'r--')
    # plt.show()

def visualizacaoGraficaBarras(dataFrame):
    dadosGrupo=dataFrame.groupby('Sex').groups
    print(dadosGrupo)
    
    lb=[]
    vl=[]

    for grp in dadosGrupo:
        print(grp)
        lb.append(grp)
        print(len(dadosGrupo[grp]))
        vl.append(len(dadosGrupo[grp]))
    
    cores=['tab:red','tab:blue']
    plt.bar(lb,vl,color=cores)
    plt.show()

def visualizacaoGraficaBarras2(dataFrame):
    dadosGrupo=dataFrame.groupby('Embarked').groups
    print(dadosGrupo)
    
    lb=[]
    vl=[]

    
    for grp in dadosGrupo:
        print(grp)
        lb.append(str(grp))
        print(len(dadosGrupo[grp]))
        vl.append(len(dadosGrupo[grp]))
    
    cores=['tab:red','tab:blue','tab:green']
    plt.bar(lb,vl,color=cores)
    plt.show()

def barras (df):
    temp=df[['Sex','Survived']]
    temp=temp.groupby('Sex').sum()
    print(temp)
    plt.bar(temp['Sex'],temp[1])
    plt.show()

url='C:\\Users\\aluno\\Desktop\\Thiago\\Aulas-Python\\aulas_pos\\dataset\\titanic.csv'
# carrega o arquivo
df=carregarDados(url)
# prepara o arquivo
df=prepararDados(df)

print( df.head())

# print(exemploGrafico())
# print(visualizacaoGrafica(df))
# visualizacaoGraficaBarras(df)
visualizacaoGraficaBarras2(df)
#print(barras(df))
#print(df['Sex','Survived'].plot(kind='bar'))

