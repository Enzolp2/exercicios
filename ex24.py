
### EX 24 PYTHON ###
# MÉDIA ARITMÉTICA #

def media_aritmetica(notas):
    return sum(notas)/len(notas)

def menu():
    print("-" * 20)
    print(" "*8 + "MENU")
    print("-" * 20)
    print("r - Resetar Notas\nq - Sair\nc - Calcular Média")
    print("-"*10)
    

menu()
notas = []
while True:
    value = input("\nDigite uma Nota: ").lower()

    try:
        value = float(value)
        notas.append(value)
        print(notas)
    except:
        if value == 'q':
            print("Encerrando...")
            break
        elif value == 'r':
            notas.clear()
            print("Notas resetadas!")
        elif value == 'c':
            print("Média: {:.2f}".format(media_aritmetica(notas)))
            break
        else:
            print("Valor inválido!")
