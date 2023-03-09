
### EX02 PYTHON ###

def validar_usuario(usuario, senha):
    if usuario.lower() != senha.lower():
        return True
    else:
        return "Usuário e Senha devem ser diferentes!"

while True:
    usuario = input('Usuário: ')
    senha = input('Senha: ')

    resposta = validar_usuario(usuario, senha)
    if resposta == True:
        print('Usuário Cadastrado!')
        break
    else:
        print(resposta)