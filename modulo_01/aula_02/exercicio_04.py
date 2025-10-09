#Verificador de senha
senha = 'python123'

senha_user = input("Digite a senha: ")

if senha_user == senha:
    print("Acesso concedido!")
else:
    print("Senha incorreta!")