'''
2.	Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).

Obs: Deve-se realiza um tratamento, onde o valor em Fahrenheit não
deve ser negativo

'''

def converte_fahrenheit_celsius(f):
    return 5 * ((f-32) / 9)


f=float(input('Digite a temperatura em Fahrenheit: '))

if f<0:
    print('A temperatura em Fahrenheit não pode ser negativa, por favor digite novamente')
else:
    print(f'Temperatura em Celsius é: {converte_fahrenheit_celsius(f): .3f}')