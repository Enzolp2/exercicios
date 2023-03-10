
### EX 10 PYTHON ###
# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles #

def gerar_inteiros(n1, n2):
    return [i for i in range(n1+1, n2)]

print(gerar_inteiros(18, 77))
