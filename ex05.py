
### EX 05 PYTHON ###

def validar_entrada(pop_a, pop_b, cresc_a, cresc_b):
    try:
        pop_a, pop_b, cresc_a, cresc_b = float(pop_a), float(pop_b), float(cresc_a), float(cresc_b)
        if cresc_a > cresc_b:
            return True
        else:
            return "A população A nunca ultrapassará a população B."
    except:
        return "As informações precisam ser números! \nNúmeros decimais separar por ponto (.)"

def calcular_pop(pop_a, pop_b, cresc_a, cresc_b):
    ano = 0
    pop_a, pop_b, cresc_a, cresc_b = float(pop_a), float(pop_b), float(cresc_a), float(cresc_b)
    while pop_a < pop_b:
        pop_a += (pop_a * cresc_a)
        pop_b += (pop_b * cresc_b)
        ano += 1
    return ano, pop_a, pop_b

while True:

    pop_a = input("Digite a quantidade da população A: ")
    cresc_a = input("Digite o valor do crescimento anual de A: ")
    pop_b = input("Digite a quantidade da população B: ")
    cresc_b = input("Digite o valor do crescimento anual de B: ")

    validacao = validar_entrada(pop_a, pop_b, cresc_a, cresc_b)
    if validacao == True:
        ano, pop_a, pop_b = calcular_pop(pop_a, pop_b, cresc_a, cresc_b)
        print("Cálculo finalizado!")
        break
    else:
        print(validacao)

print("-"*10)
print("Ano: {}".format(ano))
print("População A: {}".format(pop_a))
print("População B: {}".format(pop_b))
