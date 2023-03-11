
### EX 11 PYTHON ###

def gerar_tabuada(n):
    if (n < 1) or (n > 10):
        print("-" * 30, "\nValor inválido! Somente valores de 1 a 10\n", "-" * 30)
        return True
    else:
        print("-" * 30, "\nTabuada de {}:".format(n))
        for i in range(1, 11):
            print("5 X {} = {}".format(i, i*n))

def main():
    run = True
    while run:
        run = gerar_tabuada(int(input("Digite um valor de 1 a 10: ")))

main()