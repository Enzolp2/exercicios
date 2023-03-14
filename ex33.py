
### EX 33 PYTHON ###
# MAIOR, MENOR e MÉDIA #

def calcular_estatistica(lista):
    return max(lista), min(lista), sum(lista)/len(lista)

def exibir_estatistica(maior, menor, media):
    print("-" * 30)
    print("Maior Temperatura: {:.2f} ºC".format(maior))
    print("Menor Temperatura: {:.2f} ºC".format(menor))
    print("Temperatura Média: {:.2f} ºC".format(media))
    print("-" * 30)

def main():
    lista_temperaturas = []
    print("DEPARTAMENTO ESTADUAL DE METEOROLOGIA\n" + "-" * 30)
    print("x - Mostrar estatísticas\n")
    while True:
        temperatura = input("Temperatura (ºC): ")
        try:
            temperatura = float(temperatura)
            lista_temperaturas.append(temperatura)
        except:
            if temperatura.lower() == "x":
                maior, menor, media = calcular_estatistica(lista_temperaturas)
                exibir_estatistica(maior, menor, media)
                break
            else:
                print("Valor inválido!")

while True:
    main()
