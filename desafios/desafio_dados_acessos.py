registro_acessos = []
usuarios_acesso_bem_sucedidos = set()
total_minutos_sessao = 0

while True:
    usuario = input('Digite o nome de usuário (ou "parar" para sair): ')
    if usuario == "parar":
        print("RESULTADOS:")
        break
    while True:
        status = input("Selecione o status:\n"
                    "1 - Sucesso\n"
                    "2 - Falha\n"
                    "Opção: ")
        if status == "1" or status == "2":
            break
        else:
            print("Escolha apenas as opções 1 ou 2!")
    
    try:
        duracao_minutos = int(input("Digite a duração da sessão em minutos: "))
    except ValueError:
        print("A duração da sessão deve ser escrita em minutos (numero inteiro)")

    if status == "1":
        status = "sucesso"
    elif status == "2":
        status = "falha" 

    acesso_valido = (usuario, status, duracao_minutos)

    if acesso_valido[1] == "sucesso":
        registro_acessos.append(acesso_valido)
        total_minutos_sessao += acesso_valido[2]
    
    for acesso in registro_acessos:
        if acesso_valido[1] == "sucesso":
            usuarios_acesso_bem_sucedidos.add(acesso[0])

print(f"Registro de acessos:\n{registro_acessos}")
print()
print(f"Usuários com acesso bem-sucedido:\n{usuarios_acesso_bem_sucedidos}")
print()
print(f"Tempo total das sessões bem-sucedidas: {total_minutos_sessao} minutos")