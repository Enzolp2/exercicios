
### EX 20 PYTHON ###
# FATORIAL 2 #

def fatorial(n):
    resultado = 1
    fator = n
    while fator > 1: 
        resultado *= fator
        fator -= 1
    return resultado

def validacao(n):
    if n > 16 or n < 1:
        return False
    else:
        return True

while True:
    valor = int(input('Digite um valor para calcular o fatorial: '))
    if validacao(valor):
        print("O fatorial de {} é: {}".format(valor, fatorial(valor)))
    else:
        print("Valor inválido! Apenas inteiro positivos menores que 16")
