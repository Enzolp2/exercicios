
### EX 19 PYTHON ###
# MENOR, MAIOR e SOMA (0 a 1000) #

def validacao(n):
    if (n >= 1000) or (n <= 0):
        return False
    else:
        return True

def main(arr):
    arr.sort()
    print("Maior valor: {} \nMenor valor: {} \nSoma dos valores: {}".format(arr[-1], arr[0], sum(arr)))


dados = []
while True:
    print("-" * 30, "\nPara cadastrar um valor - Digite um número \nPara ver o resultado - Digite uma letra\n", "-" * 30)
    value = input("-> ")
    try:
        if validacao(int(value)):
            dados.append(int(value))
            print(dados)
        else:
            print("Dado inválido! Apenas número entre 0 e 1000\n")
    except:
        main(dados)
        break
