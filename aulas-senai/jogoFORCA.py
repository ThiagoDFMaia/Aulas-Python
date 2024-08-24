
import random

def desenhar_cabeca():
    return "  O"

def desenhar_braco_esquerdo():
    return " /"

def desenhar_corpo():
    return "|"

def desenhar_braco_direito():
    return "\\"

def desenhar_perna_esquerda():
    return " /"

def desenhar_perna_direita():
    return " \\"
    

def desenhar_boneco(n):
    if n==0:
        cabeca = desenhar_cabeca()
        braco_esquerdo = desenhar_braco_esquerdo()
        corpo = desenhar_corpo()
        braco_direito = desenhar_braco_direito()
        perna_esquerda = desenhar_perna_esquerda()
        perna_direita = desenhar_perna_direita()

        boneco = f"{cabeca}\n{braco_esquerdo}{corpo}{braco_direito}\n{perna_esquerda} {perna_direita}"
        print(boneco)
    elif n==1:
        cabeca = desenhar_cabeca()
        braco_esquerdo = desenhar_braco_esquerdo()
        corpo = desenhar_corpo()
        braco_direito = desenhar_braco_direito()
        perna_esquerda = desenhar_perna_esquerda()
        
        boneco = f"{cabeca}\n{braco_esquerdo}{corpo}{braco_direito}\n{perna_esquerda}"
        print(boneco)
    elif n==2:
        cabeca = desenhar_cabeca()
        braco_esquerdo = desenhar_braco_esquerdo()
        corpo = desenhar_corpo()
        braco_direito = desenhar_braco_direito()
        boneco = f"{cabeca}\n{braco_esquerdo}{corpo}{braco_direito}"
        print(boneco)
    elif n==3:
        cabeca = desenhar_cabeca()
        braco_esquerdo = desenhar_braco_esquerdo()
        corpo = desenhar_corpo()
        boneco = f"{cabeca}\n{braco_esquerdo}{corpo}"
        print(boneco)
    elif n==4:
        cabeca = desenhar_cabeca()
        corpo = desenhar_corpo()
        boneco = f"{cabeca}\n{corpo}"
        print(boneco)
    elif n==5:
        cabeca = desenhar_cabeca()
        boneco = f"{cabeca}"
        print(boneco)
  

lista_palavras=['python', 'programação','computador','notebook','software']

palavra=random.choice(lista_palavras)

letras_corretas=[]
letras_erradas=[]
tentativas=6

while True:
    palavra_escondida=''
    for letra in palavra_escondida:
        if letra in letras_corretas:
            palavra_escondida+=letra
        else:
            palavra_escondida +='_'

    print('Palavra: ', palavra_escondida)
    print(f'Letras erradas: ', letras_erradas)
    print('Tentativas restantes: ',tentativas)
    desenhar_boneco(tentativas)
    if palavra_escondida==palavra:
        print('Parabens! Voce acertou a palavra! ')
        break
    elif tentativas==0:
        print(f'Você perdeu! A palavra correta era: {palavra} Mais sorte na proxima vez!')
        break
    letra_usuario = input ('Digite uma letra: ').lower()
    
    if letra_usuario in palavra:
        print('Letra correta!')
        letras_corretas.append(letra_usuario)
    else:
        print('Letra incorretas!')
        letras_erradas.append(letra_usuario)
        tentativas -=1


