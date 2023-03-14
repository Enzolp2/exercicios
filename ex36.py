
### EX 36 PYTHON ###
# CONSTRUTOR DE TABUADA #

def tabuada(valor, inicio, fim):
    print("\nConstruindo a tabuada de {} começando em {} e terminando em {}:\n".format(valor, inicio, fim))
    for i in range(inicio, fim+1):
        print("{} x {} = {}".format(valor, i, valor*i))

def verificar_valores(inicio, fim):
    if inicio > fim: return False

def main():
    print("Construtor de Tabuadas\n" + "-" * 30)
    while True:
        valor = int(input('Construir a tabuada de: '))
        inicio = int(input('Começar por: '))
        fim = int(input('Terminar em: '))
        if verificar_valores(inicio, fim) == False:
            print("\nValores inválidos!\n")
        else:
            tabuada(valor, inicio, fim)
            print('\n')

main()

