'''
Realiza a carga do dataset: https://www.kaggle.com/datasets/saurabh00007/iriscsv

Construir um gráfico de linhas utilizando a biblioteca matplotlib com as seguintes informações: SepalLengthCm no eixo X e SepalWidthCm no eixo y

obs: importante realizar a instalação da biblioteca matplotlib com o comando pip install matplotlib

'''

import matplotlib.pyplot as plt
import pandas as pd



url='dataset\\Iris.csv'

df=pd.read_csv(url)

print(df.info())

print(df.head())

temp = df[['SepalLengthCm', 'SepalWidthCm']].sort_values(by=['SepalLengthCm'])

print (temp.head())

plt.plot(temp['SepalLengthCm'],temp['SepalWidthCm'])
plt.xlabel('SepalLengthCm')
plt.ylabel('SepalWidthCm')
plt.grid()

plt.show()

