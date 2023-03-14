
### EX 31 PYTHON ###
# REGISTRADORA RUDIMENTAR #

def total(lista_produtos):
    return sum(lista_produtos)

def exibir(lista_produtos, valor):
    print("Lojas Tabajara")
    for i in range(len(lista_produtos)):
        print("Produto {}: R$ {}".format(i+1, lista_produtos[i]))
    print("Total: {:.2f}".format(total(lista_produtos)))
    print("Dinheiro: {}".format(valor))
    print("Troco: {:.2f}".format(valor-total(lista_produtos)))
    print("-"*35)



def main():
    while True:
        count = 0
        lista_produtos = []
        while True:
            count += 1
            produto = float(input("Produto {}: R$ ".format(count)))
            if produto == 0:
                break
            else:        
                lista_produtos.append(produto)
        print("Total: {:.2f}".format(total(lista_produtos)))
        dinheiro = float(input("Pagamento: R$ "))
        print("-"*35)
        exibir(lista_produtos, dinheiro)

main()

