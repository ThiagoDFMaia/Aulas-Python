def soma(n1,n2):
  return n1+n2

def subtracao(n1,n2):
  return n1-n2

def multiplicacao(n1,n2):
  return n1*n2

def divisao(n1,n2):
  return n1/n2

def resto(n1,n2):
  return n1%n2

def potencia(n1,n2):
  return n1**n2

def raiz(n1,n2):
  return n1**(1/n2)

def calcular(opcao,n1,n2):
  if(opcao==1):
    print("Valor da soma : "+str(soma(n1,n2)))

  if(opcao==2):
    print("Valor da subtracao : "+str(subtracao(n1,n2)))

  if(opcao==3):
    print("Valor da multiplicacao : "+str(multiplicacao(n1,n2)))

  if(opcao==4):
    print("Valor da divisao : "+str(divisao(n1,n2)))
  if(opcao==5):
    print("Valor do resto : "+str(resto(n1,n2)))

  if(menu()==6):
    print("Valor da potencia : "+str(potencia(n1,n2)))

  if(menu()==7):
    print("Valor da raiz : "+str(raiz(n1,n2)))




def menu():
  print("1 - Soma")
  print("2 - Subtracao")
  print("3 - Multiplicacao")
  print("4 - Divisao")
  print("5 - Resto")
  print("6 - Potencia")
  print("7 - Raiz")
  print("0 - Sair")
  return int(input("Digite a opcao :"))



numeros={}
test=1
while(test != 0):
    test=menu()
    if (test != 0):
      n1=float(input("Digite n1 :"))
      ##numeros.append(n1)
      n2=float(input("Digite n2 :"))
      
      calcular(test,n1,n2)

    





