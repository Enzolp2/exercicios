
### EX 29 PYTHON ###
# TABELA PREÇOS LOJA 1,99 #

def tabela_precos(preco, nome_loja):
    print("{} - Tabela de Preços\n".format(nome_loja) + "-"*35)
    for i in range(1, 51):
        print("{} - R$ {:.2f}".format(i, preco*i))

tabela_precos(1.99, "Loja Quase Dois")
