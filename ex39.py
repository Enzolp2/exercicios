
### EX 39 PYTHON ###
# MAIOR e MENOR DICT #

textos = [
    'Primeiro',
    'Segundo',
    'Terceiro',
    'Quarto',
    'Quinto',
    'Sexto',
    'Sétimo',
    'Oitavo',
    'Nono',
    'Décimo',
]

def maior(arr: dict):
    numero = ''
    altura = 0
    for i in arr:
        if arr[i] > altura:
            altura = arr[i]
            numero = i
    return numero, altura

def menor(arr: dict):
    numero = ''
    altura = 99999
    for i in arr:
        if arr[i] < altura:
            altura = arr[i]
            numero = i
    return numero, altura

def main():
    alunos = {

    }
    for i in range(10):
        num_aluno = input('Digtie o número do {} aluno: '.format(textos[i]))
        altura_aluno = float(input('Digite a altura do {} aluno: '.format(textos[i])))
        alunos[num_aluno] = altura_aluno
    n_maior_aluno, alt_maior_aluno = maior(alunos)
    n_menor_aluno, alt_menor_aluno = menor(alunos)
    print("- - - Maior Aluno - - -\nNúmero: {}\nAltura: {}".format(n_maior_aluno, alt_maior_aluno))
    print("- - - Menor Aluno - - -\nNúmero: {}\nAltura: {}".format(n_menor_aluno, alt_menor_aluno))

main()