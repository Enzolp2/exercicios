
### EX 35 PYTHON ###
# LISTA PRIMOS #

def isPrime(n):
    if n == 2 or n == 3: return True
    if n%2 == 0 or n < 2: return False

    for i in range(3, int(n**0.5) + 1, 2):  # SOMENTE NÚMEROS ÍMPAR
        if n % i == 0:
            return False
    return True

def lista_primos(n):
    primos = [2]
    for i in range(3, n + 1, 2):
        if isPrime(i):
            primos.append(i)
    return primos

while True:
    print('CALCULADORA DE NÚMEROS PRIMOS\n' + '-' * 35)
    numero = int(input('\nDigite um número inteiro: '))
    primos = lista_primos(numero)
    print("\nTodos números primos até {}:\n{}\n".format(numero, primos))
