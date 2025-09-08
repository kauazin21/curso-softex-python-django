agenda = {"Mateus": "21123456789",
          "Luana": "21223344556",
          "Fabrício": "22003399554",}
while True:
    opcao = input("1 - Adicionar contato\n"
                  "2 - Buscar contato\n"
                  "3 - Sair\n"
                  "Escolha uma opção: ")
    
    if opcao == '1':
        nome_novo_contato = input("Digite o nome do contato que deseja adicionar: ")

        numero_novo_contato = input("Digite o número do contato que deseja adicionar: ")

        agenda[nome_novo_contato] = numero_novo_contato

        print(f"O contato: {nome_novo_contato} com o número: {numero_novo_contato} foi adicionado.")

    elif opcao == '2':
        nome = input("Digite o nome do contato: ")
        contato = agenda.get(nome, "Contato não encontrado!")
        print(contato)

    elif opcao == '3':
        print("Encerrando...")
        break
    else:
        print("Digite uma opção válida!")