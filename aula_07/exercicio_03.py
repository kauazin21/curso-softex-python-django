posicao = 0

print("Escolha uma opção:\n"
      "1- Avançar\n"
      "2- Recuar\n"
      "3- Status\n"
      "4- Desligar")

while True:
    opcao_escolhida = int(input("Escolha a opção desejada: "))

    if opcao_escolhida == 1:
        posicao += 1

    elif opcao_escolhida == 2:
        posicao -= 1

    elif opcao_escolhida == 3:
        print(f"O robô está na posição {posicao}")

    elif opcao_escolhida == 4:
        print("Programa encerrado!")
        break

    else:
        print("Digite uma opção válida!")
