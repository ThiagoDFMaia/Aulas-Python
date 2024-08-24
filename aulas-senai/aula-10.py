import os
import time

lista_cpf=["1234567",'4567899','789456','03208477139']
lista_usuarios= ['gomes','silvester','lucas','thiago']

op=''

while op!='5':

    print(30*'-','Bem vindo ao sistema de cadastro de usuários',30*'-')
    print(30*'-','MENU DE OPÇÕES','-'*30)
    print('1- Cadastrar usuário')
    print('2- Consultar usuários')
    print('3- Acessar sistema')
    print('4- Remover usuário')
    print("5- Sair")

    print(60*'-')

    op=input('Qual sua opção: ')

    os.system("cls")

    if op=='1':
        print("-"*20,'Cadastrando usuário',20*'-')
        novo_usuario = input("Digite o novo usuario: ")
        novo_cpf = input(f"Digite o CPF do usuário {novo_usuario}: ")
        if (novo_cpf in lista_cpf):
            print('Cpf ja cadastrado!')
        else:  
            lista_cpf.append(novo_cpf)
            lista_usuarios.append(novo_usuario)
            print('Usuário cadastrado com sucesso')
         
    elif op=='2':
        print("-"*20,'Usuário cadastrados',20*'-')
        for i in range (len(lista_usuarios)):
            print(f'Usuario : {lista_usuarios[i]} CPF: {lista_cpf[i]}')
    elif op=='3':
        print("-"*20,'LOGIN DE USUÁRIO',20*'-')
        cpf_login= input('Digite o cpf para login: ')

        if cpf_login in lista_cpf:
            print('Login realizado com sucesso!!')
        
        else:
            print('CPF NÃO CADASTRADO! Digite 1 para cadastrar!!')
    elif op=='4':
        #for i in range (len(lista_usuarios)):
        #    print(f'{i} Usuário: {lista_usuarios[1]} ')
        print("-"*20,'Removendo usuário',20*'-')
        cpf_remover = input("Digite o CPF do usuário que deseja excluir: ")

        if cpf_remover in lista_cpf:
            indice = lista_cpf.index(cpf_remover)
            nome= lista_usuarios.pop(indice)

            lista_cpf.pop(indice)

            print(f'Usuário removido com sucesso! Usuario:{nome} cpf:{cpf_remover}')

        else:
            print("CPF não encontrado!")

    elif op=='5':
        print("Volte sempre! obrigado!")
    else:
        print("Opção invalida! Tente novamente!")
    #time.sleep(2)
    os.system('pause')
    os.system("cls")
print("Voce saiu do sistema!")