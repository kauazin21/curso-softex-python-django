numeros = []

while True:
    #try e except para tratamento de erro
    try:
        numero = float(input("Digite um número:\n" \
        "Digite -1 para parar."))

        if numero == -1:
            break
        else:
            numeros.append(numero)

    except ValueError:
        print("Você digitou algo diferente de um número.")
        
print(numeros)