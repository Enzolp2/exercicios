
### EX 14 PYTHON ###

def verificar_pares(numeros):
    return len([i for i in numeros if i % 2 == 0])

def main():
    numeros = []
    for i in range(1, 11):
        numeros.append(int(input("Número {}: ".format(i))))
    numeros_pares = verificar_pares(numeros)
    numeros_impares = len(numeros) - numeros_pares
    print("Números Pares: {} \nNúmeros Impares: {}".format(numeros_pares, numeros_impares))

main()