
### EX 08 PYTHON ###
# Faça um programa que leia 5 números e informe a soma e a média dos números #

def soma(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma

def media(lista):
    return soma(lista)/len(lista)

lista = [5, 9, 6, 4, 5, 7, 10]
print("Soma: {}".format(soma(lista)))
print("Média: {:.2f}".format(media(lista)))