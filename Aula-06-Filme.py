import os

nome= input('Favor digite seu nome: ')
idade=int (input('Qua sua idade: '))



while True:
    print(10*'-',"Bem vindo ao CINEMA!",10*'-')
    print(50*'-')
    print('sala 1 - Vingadores - Censura 16 anos')
    print('Sala 2 - Ataque das aranhas - Censura 18 anos')
    print('Sala 3 - Frozen - Censura Livre')
    print('Sala 4 - Toy story - Censura 12 anos')
    print('Sala 5 - As branquelas - Censura 14 anos')
    print("Digite 6 para sair!")
    print(50*'-')
    op= int (input (f'Sr {nome} digite o número da sala que deseja? '))

    if op==1:
        if idade>=16:
            os.system("cls")
            print(f'Sr {nome} está liberado para assistir "Vingadores"! Bom file!')
            break
        else:
            os.system("cls")
            print(f'Sr {nome} não tem idade para assistir esse filme! Favor escolher outro.')
            
    elif op==2:
        if idade>=18:
            os.system("cls")
            print(f'Sr {nome} está liberado para assistir "O Ataque das aranhas"! Bom filme!')
            break
        else:
            os.system("cls")
            print(f'Sr {nome} não tem idade para assistir esse filme! Favor escolher outro.')
    elif op==3:
        if idade>=0:
            os.system("cls")
            print(f'Sr {nome} está liberado para assistir Frozen! Bom filme!')
            break
        else:
            os.system("cls")
            print(f'Sr {nome} não tem idade para assistir esse filme! Favor escolher outro.')
    elif op==4:
        if idade>=12:
            os.system("cls")
            print(f'Sr {nome} está liberado para assistir Toy Story! Bom filme!')
            break
        else:
            os.system("cls")
            print(f'Sr {nome} não tem idade para assistir esse filme! Favor escolher outro.')
    elif op==5:
        if idade>=14:
            os.system("cls")
            print(f'Sr {nome} está liberado para assistir As branquelas! Bom filme!')
            break
        else:
            os.system("cls")
            print(f'Sr {nome} não tem idade para assistir esse filme! Favor escolher outro.')

    else:
        os.system("cls")
        print("Volte sempre!")
        break


