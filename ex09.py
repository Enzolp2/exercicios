
### EX 09 PYTHON ###
# Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50 #

def verificar_primo(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def imprimir_primos(n):
    return [i for i in range(2, n+1) if verificar_primo(i)]
    
print(imprimir_primos(50))