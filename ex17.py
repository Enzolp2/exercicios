
### EX 17 PYTHON ###
# FATORIAL #

def fatorial(n):
    resultado = 1
    fator = n
    while fator > 1: 
        resultado *= fator
        fator -= 1
    return resultado
print(fatorial(8))