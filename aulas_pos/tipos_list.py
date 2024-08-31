l=[] # lista
t=() # tupla
d={} # dicionario
s={} # set obs: diferentemente dos dicionarios não tem dados repetidos


l= list()
t= tuple()
d= dict()
s= set()

l.append('1')
l.append('1') # lsita aceita dados repetidos
l.append(1) # aceita diferentes tipos
# l.sort() # odenar com tipos diferentes (int e srt juntos) da erro
l.append(list()) # lista dentro da lista

# listas sao mutaveis
# tuplas são imutaveis
print(l)
print (len(l)) # tamanho

t=('A','B')
# NAO TEM OPCAO DE INCLUIR MAIS OU ALTERAR

print(t)

s.add('A')
s.add('A')

print(s)# resultado ('A') obs: set so aceita a primeira ocorrencia do dado

s.add('a') # aceita
s.add(1) # aceita tipos diferentes

# s.add(set()) # não aceita outros objetos complexos dentro, somente dados basicox

print(s)

d={'nome':'thiago','escola':'senac'}


