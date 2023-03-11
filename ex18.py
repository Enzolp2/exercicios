
### EX 18 PYTHON ###
# MENOR, MAIOR e SOMA #

def main(arr):
    arr.sort()
    print("Maior valor: {} \nMenor valor: {} \nSoma dos valores: {}".format(arr[-1], arr[0], sum(arr)))


dados = []
while True:
    print("Para cadastrar um valor - Digite um número \nPara ver o resultado - Digite uma letra")
    value = input("-> ")
    try:
        dados.append(int(value))
    except:
        main(dados)
        break
