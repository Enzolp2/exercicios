
### EX 27 PYTHON ###
# MÉDIA ALUNOS #

class Escola():
    def __init__(self):
        self.turmas = []

    def cadastrar(self, turma):
        self.turmas.append(turma)
    
    def media_alunos(self):
        return sum([i.alunos for i in self.turmas])/len(self.turmas)


class Turma():
    def __init__(self, codigo, alunos, escola=None):
        self.codigo = codigo
        self.alunos = alunos
        if escola != None:
            escola.cadastrar(self)

escola1 = Escola()

def main(escola):
    while True:
        quantidade_turmas = int(input("Digite a quantidade de turmas -> "))
        for i in range(quantidade_turmas):
            while True:
                n_alunos = int(input("Digite o número de alunos da turma nº {} -> ".format(i + 1)))
                if n_alunos > 40:
                    print("Quantidade máxima de alunos: 40")
                else:
                    turma = Turma(i, n_alunos, escola)
                    break

        print("A média da soma de todos os alunos é: {:.2f}".format(escola.media_alunos()))
main(escola1)