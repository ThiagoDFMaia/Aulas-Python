'''
4.	Faça um programa que, determine o maior valor e a soma dos valores.

Obs: pode-se utiliza a lista = [1,2,3,4,5,6,7,8, 10]

'''

def maior (lista):
    maior=lista[0]
    for i in range(len(lista)):
        if lista[i]>maior:
            maior=lista[i]
    return maior

def soma(lista):
    soma=0
    for n in lista:
        soma=soma+n
    return soma

lista = [10,2,3,4,5,6,7,8, 1]

print (f'Maior :{maior(lista)}')
print (f'Soma :{soma(lista)}')
