
### EX 18 PYTHON ###
# ENCONTRAR PRIMOS #

def e_primo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print("-" * 25, "\nBem vindo!\nTente encontrar algum número primo...\n", "-" * 25)
while True:
    n = int(input("Digite um valor: "))
    if e_primo(n) == True:
        print("Número primo encontrado!")
        break
    else:
        print("Continue procurando...")