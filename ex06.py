
### EX 06 PYTHON ###

def imprimir_coluna():
    for i in range(1, 21):
        print(i)

def imprimir_linha():
    print([i for i in range(1,21)])

imprimir_coluna()
print("-"*10)
imprimir_linha()