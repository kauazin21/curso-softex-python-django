#validação de E-mail
while True:
    email = input("Digite seu email: ")
    if "@gmail.com" in email:
        print("Email válido!")
        break
    else:
        print("Email inválido! Digite novamente")