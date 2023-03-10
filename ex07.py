
### EX 07 PYTHON ###
# Faça um programa que leia 5 números e informe o maior número #

def maior_numero(arr):
    maior = 0
    for i in arr:
        if i > maior:
            maior = i
    return maior

lista = [5, 9, 6, 4, 5, 7, 10]
print(maior_numero(lista))