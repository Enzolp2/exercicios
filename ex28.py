
### EX 28 PYTHON ###
# TOTAL E MÉDIA CD's #

def main():
    preco_cd = [

    ]
    while True:
        quantidade_cd = int(input("Digite a quantidade de DVD's -> "))
        for i in range(quantidade_cd):
            preco_cd.append(int(input("Digite o preço (R$) do CD nº {}: ".format(i+1))))
        print("-" * 30)
        print("Total: R$ {}\nMédia: R$ {:.2f}".format(sum(preco_cd), sum(preco_cd)/len(preco_cd)))
        break
main()