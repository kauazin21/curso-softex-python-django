numero_secreto = 7

print("Bem vindo ao jogo de adivinhar o número secreto!")
print(30 * "=")

for tentativas in range(5):
    numero_user = int(input("Digite um número inteiro de 1 a 10: "))
    if numero_user == numero_secreto:
        print("Parabéns! Você acertou o número secreto")
        break

    elif numero_user > numero_secreto:
        print("O número que você digitou é maior que o número secreto\n"
              f"Número de tentativas: {tentativas} (Número máximo de tentativas: 5)")
    
    elif numero_user < numero_secreto:
        print("O número que você digitou é menor que o número secreto\n"
              f"Número de tentativas: {tentativas} (Número máximo de tentativas: 5)")