'''
3.	Faça um programa que leia e valide as seguintes informações:
1.	Nome: maior que 3 caracteres;
2.	Idade: entre 0 e 150;
3.	Salário: maior que zero;
4.	Sexo: 'f' ou 'm';
5.	Estado Civil: 's', 'c', 'v', 'd’;

Obs: Deve ser criado uma função para cada item a ser verificado.
 
'''


def valida_nome(nome):
    if str.__len__(nome)>3:
       return f'Nome: {nome}'
    else:
       return 'Nome invalido! Favor digite pelo menos 4 caracteres'
def valida_idade(idade):
    if idade >=0 and idade <=150:
       return f'Idade : {idade}'
    else:
       return 'Idade invalida!'
def valida_salario (salario):
    if salario>0:
       return f'Salario: {salario : .2f}'
    else:
       return 'Salario invalido! Favor digite um salario maior que 0'
def valida_sexo (sexo):
    if sexo=='h' or sexo=='m':
        if sexo=='h':
            return f'Sexo: MASCULINO'
        else :
            return f'Sexo: FEMININO'
    else:
       return 'Sexo invalido'
def valida_estado_civil (estado_civil):
    if estado_civil=='s':
        return 'Estado civil solteiro!' 
    elif estado_civil=='c':
        return 'Estado civil casado!'
    elif estado_civil=='v':
        return 'Estado civil viuvo'
    elif estado_civil=='d':
        return 'Estado civil divorciado'
    else:
        return 'Opção invalida'

   



nome=input('Digite o nome: ')
print(valida_nome(nome))

idade=int( input('Digite o idade: '))
print(valida_idade(idade))

salario=float( input('Digite o salario: '))
print(valida_salario(salario))

sexo= input('Digite o Sexo: H (PARA HOMEM) OU M (PARA MULHER) ').lower()
print(valida_sexo(sexo))

estado_civil= input('Digite o estado civil: s (solteiro), c (casado), v (viuvo), d (divorciado) ').lower()
print(valida_estado_civil(estado_civil))