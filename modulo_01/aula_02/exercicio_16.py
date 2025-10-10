#Jogo de Advinhação com dicas
num_secreto = 4

tentativas = 3

while tentativas > 0:
    num = int(input("Digite um número: "))
    if num > num_secreto:
        print("Errou!!!")
        print("Dica: O número secreto é menor")
        tentativas -= 1
        print(f"Tentativas: {tentativas}")

    elif num < num_secreto:
        print("Errou!!!")
        print("Dica: O número secreto é maior")
        tentativas -= 1
        print(f"Tentativas: {tentativas}")
    else:
        print("Parabéns! Você acertou o número secreto.")
        break