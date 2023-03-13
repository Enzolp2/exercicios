
### EX 26 PYTHON ###
# CONTAR VOTOS #

class Candidatos:
    def __init__(self, codigo, nome, qnt_votos=0):
        self.codigo = codigo
        self.nome = nome
        self.qnt_votos = qnt_votos

    def contar_voto(self):
        self.qnt_votos += 1


def menu(candidatos):
    print("-------- MENU --------")
    for i in candidatos:
        print(i.codigo, "-", i.nome)
    print("-"*22)

def resultado(candidatos):
    print("------- RESULTADO -------")
    for i in candidatos:
        print(i.nome, "-", i.qnt_votos)

def vencedor(candidatos):
    nome = ""
    votos = 0
    for i in candidatos:
        if i.qnt_votos > votos:
            nome = i.nome
            votos = i.qnt_votos
    print("O vencedor foi {} com {} votos.".format(nome, votos))

cadidato_1 = Candidatos(1, "Luis Henrique")
cadidato_2 = Candidatos(2, "Felipe Patarra")
cadidato_3 = Candidatos(3, "José Campos")

lista_candidatos = [
    cadidato_1,
    cadidato_2,
    cadidato_3,
]

while True:
    eleitores = int(input('Digite o número de eleitores: '))
    menu(lista_candidatos)
    for i in range(1, eleitores + 1):
        print("Eleitor nº {}".format(i))
        voto = input("Voto: ")
        for i in range(1, 4):
            if voto == str(i):
                lista_candidatos[i-1].qnt_votos += 1
                break

    resultado(lista_candidatos)
    vencedor(lista_candidatos)
    print("Votação Encerrada!")
    break