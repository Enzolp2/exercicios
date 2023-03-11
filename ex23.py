
### EX 23 PYTHON ###
# ENCONTRAR N PRIMOS #

def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def encontrar_primos(n):
    primos = [2]
    if n < 2:
        return []
    for i in range(3, n+1, 2):
        if isPrime(i):
            primos.append(i)
    return primos
    
        
print("-" * 25)
while True:
    n = int(input("Digite um valor: "))
    resultado = encontrar_primos(n)
    print(resultado)
    
