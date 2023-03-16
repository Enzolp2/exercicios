
### EX 37 PYTHON ###
# CLASSES #

class Academia:
    def __init__(self):
        self.clientes = [

        ]

    def maior_altura(self):
        maior = 0 
        for i in self.clientes:
            if i.altura > maior:
                maior = i.altura
        return maior
    
    def menor_altura(self):
        menor = self.clientes[0].altura
        for i in range(1, len(self.clientes)):
            if self.clientes[i].altura < menor:
                menor = self.clientes[i].altura
        return menor

    def maior_peso(self):
        maior = 0
        for i in range(len(self.clientes)):
            if self.clientes[i].peso > maior:
                maior = self.clientes[i].peso
        return maior

    def menor_peso(self):
        menor = self.clientes[0].peso
        for i in range(1, len(self.clientes)):
            if self.clientes[i].peso < menor:
                menor = self.clientes[i].peso
        return menor

    def exibir_estatisticas(self):
        print("\n")
        print(f"Maior Altura: {self.maior_altura()}")
        print(f"Menor Altura: {self.menor_altura()}")
        print('-'*20)
        print(f"Maior Peso: {self.maior_peso()}")
        print(f"Menor Peso: {self.menor_peso()}")
        print("\n")

class Clientes:
    def __init__(self, codigo, altura, peso, academia: Academia):
        self.codigo = codigo
        self.altura = altura
        self.peso = peso
        if academia is not None:
            self.academia = academia

    
    def cadastrar(self):
        self.academia.clientes.append(self)


def main():
    academia = Academia()
    count = 0
    while True:
        count += 1
        print("\n---- Cadastro do Cliente mº {} ----".format(count))
        print("0 - Mostrar Estatísticas\n")
        codigo = input("Código: ")
        if codigo == '0':
            academia.exibir_estatisticas()
            break
        altura = float(input("Altura: "))
        peso = float(input("Peso: "))
        cliente = Clientes(codigo, altura, peso, academia)
        cliente.cadastrar()
    print("Programa finalizado com sucesso!")

main()