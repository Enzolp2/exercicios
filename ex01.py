
### EX01 PYTHON ###
def validar_nota(nota):
    try:
        if (int(nota) < 0) or (int(nota) > 10):
            return "Nota precisa estar entre 0 e 10!"
    except:
        return "Nota precisa ser um número!"

    return True

while True:
    nota = input("Digite sua nota: ")
    resposta = validar_nota(nota)
    if resposta == True:
        print("Nota cadastrada!")
        break
    else:
        print(resposta)