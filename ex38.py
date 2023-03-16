
### EX 38 PYTHON ###
# INCREMENTO PERCENTUAL #


def calculo_salarial(salario, ano):
    salario_inicial = salario
    porcentagem = 0.015
    salario = salario + (salario*porcentagem)
    ano += 1
    while ano < 2000:
        ano += 1
        porcentagem = porcentagem * 2
        salario = salario + (salario_inicial * porcentagem)
        print("Ano: {}\nPorcentagem: {:.2f}\nSalário: {:.2f}".format(ano, porcentagem, salario))

calculo_salarial(1000, 1995)