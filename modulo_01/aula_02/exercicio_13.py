#Login com tentativas
senha = "python123"

tentativas = 3

while tentativas > 0:
    senha_user = input("Digite a senha: ")
    if senha_user == senha:
        print("Login bem-sucedido!")
        break
    else:
        print("Senha inválida!")
        tentativas -= 1
        print(f"Tentativas restantes: {tentativas}")