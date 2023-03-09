
### EX03 PYTHON ###

def validar_informacoes(nome, idade, salario, sexo, estado_civil):
    if len(nome) < 3:
        return "Nome com caracteres insuficientes!"

    try:
        if (int(idade) < 0) or (int(idade) > 150):
            return "Idade inválida!"
    except:
        return "Idade precisa ser um número!"
    
    try:
        if int(salario) <= 0:
            return "Salário Inválido!"
    except:
        return "Salário precisa ser um número!"
    
    if sexo.lower() not in ('f', 'm'):
        return "Sexo inválido!"

    if estado_civil.lower() not in ('s', 'c', 'v', 'd'):
        return "Estado Civil inválido!"
    
    return True

while True:
    nome = input("Nome: ")
    idade = input("Idade: ")
    salario = input("Salário: ")
    sexo = input("Sexo (m/f): ")
    estado_civil = input("Estado Civil (s/c/v/d): ")

    resposta = validar_informacoes(nome, idade, salario, sexo, estado_civil)

    if resposta == True:
        print("Cadastro realizado com sucesso!")
        break
    else:
        print(resposta)