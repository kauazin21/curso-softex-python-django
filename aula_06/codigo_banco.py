conta_corrente = "123456-7"
senha_user = "9999"
saldo_atual = 0
limite_saldo_negativo = 500.00
nome_user = "José"

while True:
    for i in range(3):
        conta = input("Entre com a sua conta corrente: ")
        senha = input("Entre com a sua senha: ")

        if conta == conta_corrente and senha == senha_user:
            print(f"Bem vindo, {nome_user}!")
            acesso_permitido = True
            break

        else:
            print("Conta ou senha inválida!")
            acesso_permitido = False

    if not acesso_permitido:
        break
    
    while True:
        opcao = input("Escolha uma opção:\n" \
        "1- Ver saldo.\n" \
        "2- Sacar valor.\n" \
        "3- Depositar.\n" \
        "4- Pagar Boleto.\n" \
        "5- Alterar senha. \n" \
        "6- Sair")

        if opcao == "1":
            print(f"Seu saldo atual é de {saldo_atual}.")
        elif opcao == "2":
            valor_a_sacar = float(input("Entre com o valor a ser sacado: "))
            if valor_a_sacar <= (saldo_atual + limite_saldo_negativo):
                saldo -= valor_a_sacar
                print("Saldo liberado, retire seu valor!")
        elif opcao == "3":
            depositar = float(input("Insira o valor a ser depositado: "))
            if depositar > 0:
                saldo += depositar
            else:
                print("Valor inválido!")
        elif opcao == "4":
            pass
        elif opcao == "5":
            pass
        elif opcao == "6":
            print("Atendimento finalizado")
            break
        else:
            print("Opção Inválida")