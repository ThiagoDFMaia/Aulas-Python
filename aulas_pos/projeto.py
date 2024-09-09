import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as snb
import numpy as np
import plotly.graph_objs as go
import plotly.subplots as sp
from datetime import datetime


def calcular_media_escolaridade(x):
    try:
        # Tentamos dividir os valores numéricos
        return (int(x.split()[0]) + int(x.split()[2])) / 2
    except (ValueError, IndexError):
        # Se houver erro (como no caso de 'Nenhuma'), retornamos np.nan
        return np.nan

def calcular_idade(data_nascimento, data_obito):
    if pd.isnull(data_obito):  # Se a data de óbito for NaN, usar a data atual
        data_obito = datetime.now()
    idade = data_obito.year - data_nascimento.year - ((data_obito.month, data_obito.day) < (data_nascimento.month, data_nascimento.day))
    return idade

def tratamento_dados(df):
    df.drop(columns=['ESCMAE','CIRURGIA'], inplace=True)
    df['ASSISTMED']=df['ASSISTMED'].fillna('nao informado')
    df['OCUP']=df['OCUP'].fillna('nao informado')

    
    df['ESC'] = df['ESC'].apply(lambda x: calcular_media_escolaridade(x) if pd.notnull(x) else np.nan)
    moda_esc=df['ESC'].mode()[0]
    df['ESC']=df['ESC'].fillna(moda_esc)

    df['DTNASC'] = pd.to_datetime(df['DTNASC'], format='%Y-%m-%d', errors='coerce')
    df['DTOBITO'] = pd.to_datetime(df['DTOBITO'], format='%Y-%m-%d', errors='coerce')
    df['idade'] = df.apply(lambda row: calcular_idade(row['DTNASC'], row['DTOBITO']), axis=1)
    df.drop(columns=['DTNASC'], inplace=True)
    df = df.loc[(df['idade'] >= 0) & (df['idade'] <= 110)]

    df['ESTCIV'] = df['ESTCIV'].replace(r'/a', '(a)',regex=True)

    df.drop_duplicates()
    df.dropna(inplace=True)


    return df


def gera_subplot(df):
    
    # Criar uma figura com subplots 3x2 (3 linhas, 2 colunas)
    fig, axes = plt.subplots(3, 2, figsize=(15, 18))

    # Ajustar espaçamento entre os subplots
    plt.subplots_adjust(hspace=0.4, wspace=0.4)

    # Gráfico de pizza - Distribuição por Sexo
    sexo = df['SEXO'].value_counts()
    axes[0, 0].pie(sexo, labels=sexo.index, autopct='%1.1f%%', startangle=90)
    axes[0, 0].set_title('Distribuição por Sexo')
    axes[0, 0].axis('equal')  # Para garantir que o gráfico seja um círculo

    # Gráfico de linha - Distribuição por Sexo e Ano
    agrupado = df.groupby(['SEXO', 'ano']).size().unstack()
    for sexo in agrupado.index:
        axes[0, 1].plot(agrupado.columns, agrupado.loc[sexo], marker='o', label=sexo)
    axes[0, 1].set_title('Distribuição por Sexo e Ano')
    axes[0, 1].set_xlabel('Ano')
    axes[0, 1].set_ylabel('Total')
    axes[0, 1].legend(title='Sexo')
    axes[0, 1].grid(True)

    # Gráfico de barras - Distribuição de Raça/Cor
    contagem_racacor = df['RACACOR'].value_counts()
    snb.barplot(x=contagem_racacor.index, y=contagem_racacor.values, palette='viridis', ax=axes[1, 0])
    axes[1, 0].set_title('Distribuição de Raça/Cor')
    axes[1, 0].set_xlabel('Raça/Cor')
    axes[1, 0].set_ylabel('Total')
    axes[1, 0].grid(axis='y')

    # Gráfico de pizza - Distribuição por Estado Civil
    estado_civil = df['ESTCIV'].value_counts()
    axes[1, 1].pie(estado_civil, labels=estado_civil.index, autopct='%1.1f%%', startangle=90)
    axes[1, 1].set_title('Distribuição por Estado Civil')
    axes[1, 1].axis('equal')  # Para garantir que o gráfico seja um círculo

    # Histograma - Distribuição das Idades com destaque
    idade = df['idade']
    intervalo_bins = range(5, 101, 5)
    n, bins, patches = axes[2, 0].hist(idade, bins=intervalo_bins, color='lightgray', edgecolor='black')

    # Realçar a faixa etária de 15 a 30 anos
    for i in range(len(bins)-1):
        if 15 <= bins[i] < 30:
            patches[i].set_facecolor('crimson')

    # Identificar as idades com maior incidência (top 3 picos)
    max_indices = np.argsort(n)[-3:]
    for i in max_indices:
        patches[i].set_facecolor('orange')

    axes[2, 0].set_title('Distribuição das Idades: 15-30 Anos e Picos de Incidência')
    axes[2, 0].set_xlabel('Idade')
    axes[2, 0].set_ylabel('Total')
    axes[2, 0].xaxis.set_major_locator(ticker.MultipleLocator(5))
    axes[2, 0].yaxis.set_major_locator(ticker.MultipleLocator(500))

    # Adicionar anotações e legenda
    axes[2, 0].annotate('Faixa crítica: 15-30 anos', xy=(20, max(n) * 0.9), xytext=(35, max(n) * 0.8),
                        arrowprops=dict(facecolor='crimson', shrink=0.05), fontsize=12, color='black')

    for i in max_indices:
        axes[2, 0].annotate(f'Pico: {int(bins[i])}-{int(bins[i+1])}', xy=(bins[i], n[i]), xytext=(bins[i]+5, n[i] + 300),
                            arrowprops=dict(facecolor='orange', shrink=0.05), fontsize=10, color='black')

    axes[2, 0].legend(['Faixa 15-30 anos destacada', 'Maiores incidências'], loc='upper right')
    axes[2, 0].grid(axis='y')

    # Remover o último subplot (vazio)
    axes[2, 1].remove()

    # Exibir todos os gráficos em uma única figura
    plt.show()



def gera_grafico_iterativo(df):
# Criando a figura de subplots (3x2) para compatibilidade com gráficos de pizza
    fig = sp.make_subplots(
        rows=3, cols=2,
        subplot_titles=("Distribuição por Sexo", "Distribuição por Sexo e Ano",
                        "Distribuição de Raça/Cor", "Distribuição por Estado Civil",
                        "Distribuição de Idades"),
        specs=[[{'type': 'pie'}, {'type': 'xy'}],
            [{'type': 'bar'}, {'type': 'pie'}],
            [{'type': 'bar'}, {'type': 'xy'}]]
    )

    # Gráfico de pizza - Distribuição por Sexo
    sexo_counts = df['SEXO'].value_counts()
    fig.add_trace(go.Pie(labels=sexo_counts.index, values=sexo_counts.values, hole=.3), row=1, col=1)

    # Gráfico de linha - Distribuição por Sexo e Ano
    agrupado = df.groupby(['SEXO', 'ano']).size().unstack()
    for sexo in agrupado.index:
        fig.add_trace(go.Scatter(x=agrupado.columns, y=agrupado.loc[sexo], mode='lines+markers', name=sexo), row=1, col=2)

    # Gráfico de barras - Distribuição de Raça/Cor
    racacor_counts = df['RACACOR'].value_counts()
    fig.add_trace(go.Bar(x=racacor_counts.index, y=racacor_counts.values, marker=dict(color=racacor_counts.values, colorscale='Viridis')), row=2, col=1)

    # Gráfico de pizza - Distribuição por Estado Civil
    estciv_counts = df['ESTCIV'].value_counts()
    fig.add_trace(go.Pie(labels=estciv_counts.index, values=estciv_counts.values, hole=.3), row=2, col=2)

    # Histograma - Distribuição de Idades com destaque
    idade = df['idade']
    n, bins = np.histogram(idade, bins=range(5, 101, 5))  # Calcular o histograma com numpy
    hist_data = pd.Series(n, index=[f'{bins[i]}-{bins[i+1]}' for i in range(len(bins)-1)])

    # Realçar faixa de 15-30 anos e picos
    colors = ['lightgray'] * len(hist_data)  # Inicialmente todas as barras são cinza
    for i, bin_range in enumerate(hist_data.index):
        start_age = int(bin_range.split('-')[0])
        if 15 <= start_age < 30:
            colors[i] = 'crimson'
    for i in hist_data.nlargest(3).index:
        idx = list(hist_data.index).index(i)
        colors[idx] = 'orange'

    fig.add_trace(go.Bar(x=hist_data.index, 
                        y=hist_data.values, 
                        marker=dict(color=colors)), row=3, col=1)

    # Layout e ajustes
    fig.update_layout(height=900, width=1200, title_text="Visualizações dos graficos iterativos com o plotly",title_x=0.5,  showlegend=False)
    fig.update_xaxes(title_text="Ano", row=1, col=2)
    fig.update_yaxes(title_text="Total", row=1, col=2)
    fig.update_xaxes(title_text="Raça/Cor", row=2, col=1)
    fig.update_yaxes(title_text="Total", row=2, col=1)
    fig.update_xaxes(title_text="Idade", row=3, col=1)
    fig.update_yaxes(title_text="Total", row=3, col=1)

    # Exibir o gráfico
    fig.show()






df=pd.read_csv('aulas_pos\\dataset\\suicidios_2010_a_2019.csv')

df.info()


df=tratamento_dados(df)
df.info()

print(df.head())


gera_subplot(df)
gera_grafico_iterativo(df)
