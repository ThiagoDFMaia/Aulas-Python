import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as snb
import numpy as np
import plotly.graph_objs as go
import plotly.subplots as sp
from datetime import datetime
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

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
  
    df = df.loc[(df['idade'] >= 0) & (df['idade'] <= 110)].copy()

    df.loc[:, 'ESTCIV'] = df['ESTCIV'].replace(r'/a', '(a)', regex=True)

    
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)


    return df

def insere_grafico_pizza (dados,axes,titulo,i,j):
  
    axes[i, j].pie(dados, autopct='%1.1f%%', startangle=90,pctdistance=1.2,textprops={'fontsize': 7})
    axes[i, j].set_title(titulo,loc="left")
    axes[i, j].axis('equal')  # Para garantir que o gráfico seja um círculo
    axes[i, j].legend(dados.index, title="Legenda", loc="lower left", bbox_to_anchor=(-0.1, 0), fontsize='small')
    return axes
def insere_grafico_linha(axes,agrupado,titulo,i,j,xlabel,ylabel,legenda):
    for sexo in agrupado.index:
        axes[0, 1].plot(agrupado.columns, agrupado.loc[sexo], marker='o', label=sexo)
    axes[0, 1].set_title(titulo)
    axes[0, 1].set_xlabel(xlabel)
    axes[0, 1].set_ylabel(ylabel)
    axes[0, 1].legend(title=legenda)
    axes[0, 1].grid(True)
    return axes

def insere_grafico_barras(axes,contagem_racacor,i,j,titulo,xlabel,ylabel,paleta):
 
    snb.barplot(x=contagem_racacor.index, y=contagem_racacor.values, hue=contagem_racacor.index, palette=paleta, ax=axes[i, j], legend=False)
    axes[i, j].set_title(titulo)
    axes[i, j].set_xlabel(xlabel)
    axes[i, j].set_ylabel(ylabel)
    axes[i, j].grid(axis='y')
    return axes



def insere_grafico_histograma(axes, idade, i, j):
    intervalo_bins = range(5, 101, 5)
    n, bins, patches = axes[i, j].hist(idade, bins=intervalo_bins, color='lightblue', edgecolor='black', rwidth=0.6)

    for k in range(len(bins)-1):
        if 10 <= bins[k] < 35:
            patches[k].set_facecolor('crimson')
        else:
            patches[k].set_facecolor('darkblue')

    axes[i, j].set_title('Distribuição das Idades: Destaques e Picos de Incidência', fontsize=14)
    axes[i, j].set_xlabel('Idade', fontsize=12)
    axes[i, j].set_ylabel('Total', fontsize=12)
    axes[i, j].set_ylim(0, 12000)  # Ajuste do limite do eixo y
    axes[i, j].xaxis.set_major_locator(ticker.MultipleLocator(5))
    axes[i, j].yaxis.set_major_locator(ticker.MultipleLocator(1000))

    for rect, label in zip(patches, n):
        height = rect.get_height()
        axes[i, j].text(rect.get_x() + rect.get_width() / 2, height, f'{int(label)}', ha='center', va='bottom', fontsize=7, color='black')

    handles = [plt.Line2D([0], [0], color='crimson', lw=4),
               plt.Line2D([0], [0], color='darkblue', lw=4)]
    labels = ['Faixa 10-35 anos destacada', 'Outras faixas etárias']
    axes[i, j].legend(handles=handles, labels=labels, loc='upper right', fontsize='small', title='Legenda', title_fontsize='small')

    axes[i, j].grid(axis='y', linestyle='--', alpha=0.7)

    return axes


def gera_subplot(df):
    
    # Criar uma figura com subplots 3x2 (3 linhas, 2 colunas)
    fig, axes = plt.subplots(3, 2, figsize=(22, 25))

# Ajustar espaçamento entre os subplots
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, wspace=0.1, hspace=0.5)

    # Gráfico de pizza - Distribuição por Sexo
    axes=insere_grafico_pizza( df['SEXO'].value_counts(),axes,'Distribuição por Sexo',0,0)
    
    # Gráfico de linha - Distribuição por Sexo e Ano
    axes=insere_grafico_linha(axes,df.groupby(['SEXO', 'ano']).size().unstack(),'Distribuição por Sexo e Ano',0,1,'Ano','Total','Sexo')

    # Gráfico de barras - Distribuição de Raça/Cor
    axes=insere_grafico_barras(axes,df['RACACOR'].value_counts(),1,0,'Distribuição de Raça/Cor','Raça/Cor','Total','viridis')
   
    # Gráfico de pizza - Distribuição por Estado Civil
    axes=insere_grafico_pizza(df['ESTCIV'].value_counts(),axes,'Distribuição por Estado Civil',1,1)


    # Histograma - Distribuição das Idades com destaque
    axes=insere_grafico_histograma(axes,df['idade'],2,0)
   
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
    intervalo_bins = range(5, 101, 5)
    n, bins = np.histogram(idade, bins=intervalo_bins)  # Calcular o histograma com numpy
    hist_data = pd.Series(n, index=[f'{bins[i]}-{bins[i+1]}' for i in range(len(bins)-1)])

    # Destacar faixa de 10-35 anos
    colors = ['darkblue'] * len(hist_data)  # Cor inicial padrão para todas as barras
    for i, bin_range in enumerate(hist_data.index):
        start_age = int(bin_range.split('-')[0])
        if 10 <= start_age < 35:
            colors[i] = 'crimson'  # Destaca a faixa de idade entre 10 e 35 anos

    # Adicionar o histograma ao gráfico
    fig.add_trace(go.Bar(
        x=hist_data.index,
        y=hist_data.values,
        marker=dict(color=colors, line=dict(color='black', width=1)),
        text=[f'{int(value)}' for value in hist_data.values],  # Rótulo com os valores
        textposition='auto'
    ), row=3, col=1)

    # Layout e ajustes
    fig.update_layout(height=900, width=1200, title_text="Visualizações dos gráficos iterativos com o Plotly", title_x=0.5, showlegend=False)
    fig.update_xaxes(title_text="Ano", row=1, col=2)
    fig.update_yaxes(title_text="Total", row=1, col=2)
    fig.update_xaxes(title_text="Raça/Cor", row=2, col=1)
    fig.update_yaxes(title_text="Total", row=2, col=1)
    fig.update_xaxes(title_text="Idade", row=3, col=1)
    fig.update_yaxes(title_text="Total", row=3, col=1, range=[0, max(hist_data.values) + 1000])  # Ajuste do limite do eixo y

    # Exibir o gráfico
    fig.show()



def codifica_coluna(dados):
    # codifica dados não numericos em numericos

    for coluna in dados.columns:
        if dados[coluna].dtype == 'object':  # Verifica se a coluna é do tipo object
            le=LabelEncoder()
            dados[coluna]=le.fit_transform(dados[coluna])

    return dados

def separa_dados_treinamento (df,perc_test):
    df_treino, df_teste = train_test_split(df, test_size=perc_test, random_state=42)
    return df_treino,df_teste