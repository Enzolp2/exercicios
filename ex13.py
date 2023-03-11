
### EX 13 PYTHON ###

def calcula_potencia(base, expoente):
    value = 1
    for i in range(expoente):
        value *= base
    return value

print(calcula_potencia(2, 10))