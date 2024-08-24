import lib_aula as lib


print('ola')

# criação de variaveis
i =10
print(type(i))
i=10.5
print(type(i))
j=10+i
print(type(j))
i='teste'
print(type(i))
i+" senac"
print(type(i))
i=True
print(type(i))
i=[]
print(type(i))# lista
i=()
print(type(i))# tupla
i={}
print(type(i))# dicionario


# operadores logicos: or, and, not,== nao tem xor e nao tem ===
if 10<2 or 1>5:
    print('teste1')
    print('senac')
    # if alinhado
    if 5>2:# não é uma boa pratica, gera complexidade no codigo. recomendavel maximo 3 ir alinhados
        print('teste3')
elif 10>2: # ==
    print('teste2')
else: # ou elif
    print('falso')

# estruturas de repetição

i=0
while (i<5):
    print(i)
    i+=1

i=5
while (i>0):
    print(i)
    i-=1

# funções e procedimentos
# obs: python aceita funções com mesmo nome. vai chamar a mais abaixo
def calcula(): # procedimento não retorna valor, função retorna valor. obs: retorna implicitamente none
    print('teste - procedimento')

def funcao_calcula(): # função retorna valor
    return ('teste - função')
def calcula2(valor,valor2):
    print(valor)
    print('senac - final')
def calcula2(valor):
    print(valor)
    print('senac - final')
# cuidado, na programaçao estruturada , na chamada de funções com mesmo nome vai prevalecer a função mais abaixo
'''
def calcula2(valor,valor2):
    print(valor)
    print('senac - final')
'''




calcula()


funcao_calcula()
calcula2(10)



valor=10
cotacao=5.60
print (f'valor em dolar {lib.converte_real_dolar(valor,cotacao)}' )


dado =float( input ('Digite o valor em real: '))
# importante fazer a conversao depois de receber
print (f'Valor de {dado} em dolar é: {lib.converte_real_dolar(dado,cotacao)}')

