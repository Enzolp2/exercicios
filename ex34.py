
### EX 34 PYTHON ###
# É PRIMO? #

def isPrime(n):
    if n == 2 or n == 3: return True
    if n%2 == 0 or n < 2: return False

    for i in range(3, int(n**0.5) + 1, 2):  # SOMENTE NÚMEROS ÍMPAR
        if n % i == 0:
            return False
    return True

def main():
    while True:
        numero = int(input("Digite um número: "))
        if isPrime(numero):
            print("\n{} é primo\n".format(numero))
        else:
            print("\n{} não é primo\n".format(numero))

main()