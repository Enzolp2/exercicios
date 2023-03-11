
### EX 22 PYTHON ###
# ENCONTRAR PRIMOS 2 #

def e_primo(n):
    if n <= 0:
        return False
    divisores = [1]
    for i in range(2, n):
        if n % i == 0:
            divisores.append(i)
    if len(divisores) > 1:
        divisores.append(n)
        return divisores
    else:
        return True

print("-" * 25, "\nBem vindo!\nTente encontrar algum número primo...\n", "-" * 25)
while True:
    n = int(input("Digite um valor: "))
    resultado = e_primo(n)
    if resultado == True:
        print("Número primo encontrado!")
    elif resultado == False:
        print("Número inválido!")
    else:
        print("Esse número não é primo!\n Divisores: {}".format(resultado))