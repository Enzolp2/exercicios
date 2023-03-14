
### EX 32 PYTHON ###
# CÁLCULO FATORIAL #

def fatorial(n):
    if n == 2:
        return 2
    else:
        return n * fatorial(n-1)

def saida(n):
    saida = "".join(str(i) + " . " for i in range(n, 0, -1))
    return saida[:len(saida)-2]

while True:
    valor = int(input("Digite um número inteiro: "))
    print("{}! = {}= {}".format(valor, saida(valor), fatorial(valor)))
