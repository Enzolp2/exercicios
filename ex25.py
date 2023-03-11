
### EX 24 PYTHON ###
# MÉDIA ARITMÉTICA CONDICIONAL #

def media(nums):
    return sum(nums)/len(nums)

def verficar_media(media):
    if media > 60:
        return "Idosa"
    elif media > 25:
        return "Adulta"
    else:
        return "Jovem"

def main():
    idades = []
    while True:
        idade = input("Digite a idade ou 'c' para calcular a média: ").lower()
        try:
            idade = int(idade)
            idades.append(idade)
            print(idades)
        except:
            if idade == 'c':
                med = media(idades)
                print("A média das idade é {:.2f} e está da categoria {}".format(med, verficar_media(med)))
                break
            else:
                print("Valor inválido!")

main()