'''
1.
Tendocomodadodeentradaaaltura(h)deumapessoa,construaumalgoritmoquecalculeseupesoideal,utilizandoasseguintesfórmulas:
1.
Parahomens:(72.7*h)-58
2.
Paramulheres:(62.1*h)-44.7
Obs:Construirfunçõesindependes:umaparahomenseoutraparamulheres.Oretornodecimaldecadafunçãodeveserformatadoem2casadecimais.

'''

def peso_ideal_homens(h):
    return (72.7*h)-58
def peso_ideal_mulheres(h):
    return (62.1*h)-44.7


h=float(input('Por favor digite sua altura: '))

sexo=input('Digite H para HOMEM ou M Para mulher: ').lower()

if sexo=='h':
    print(f'Seu peso ideal é: {peso_ideal_homens(h):.2f}')
elif sexo=='m':
    print(f'Seu peso ideal é: {peso_ideal_mulheres(h):.2f}')
else: 
    print('Opção invalida')
    


