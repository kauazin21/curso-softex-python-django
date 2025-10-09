idade = int(input("Digite sua idade: "))

if idade >= 0:
    if idade < 13:
        print("Criança")

    elif idade < 18:
        print("Adolescente")

    elif idade < 60:
        print("Adulto")

    else:
        print("Idoso")

else:
    print("Digite uma idade válida!")