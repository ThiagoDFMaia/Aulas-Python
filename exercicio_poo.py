# Definindo a classe Casa
class Casa:
    def __init__(self, bairro, valor, iptu):
        self.bairro = bairro
        self.valor = valor
        self.iptu = iptu

    

# Definindo a classe Aluguel
class Aluguel:
    def __init__(self):
        self.casas = []

    def adicionar_casa(self, casa):
        self.casas.append(casa)



# Criando objetos da classe Casa
casa1 = Casa("Taguatinga", 10000.00, 1000.27)
casa2 = Casa("Gama", 20000.00, 2000.50)
casa3 = Casa("W3 SUL", 100000.00, 5000.55)

# Criando uma instância da classe Aluguel
aluguel = Aluguel()

# Adicionando casas usando o método adicionar_casa
aluguel.adicionar_casa(casa1)
aluguel.adicionar_casa(casa2)
aluguel.adicionar_casa(casa3)


# listando as casas
for casa in aluguel.casas:
    print(casa.bairro,casa.valor,casa.iptu)