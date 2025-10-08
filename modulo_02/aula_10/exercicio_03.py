acessos = [("Pedro", "sucesso"), ("Ana","falha"), ("Maria","sucesso"),("Pedro","falha"), ("Ana","falha")]
usuarios_sucesso = set()
usuarios_falha = set()

for usuario, status_login in acessos:
    if status_login == "sucesso":
        usuarios_sucesso.add(usuario)
    else:
        usuarios_falha.add(usuario)

    somente_falha = usuarios_falha.difference(usuarios_sucesso)
    
    
print("Usuários com pelo menos um login bem-sucedido:\n"
      f"{usuarios_sucesso}\n"
      "\nUsuários que tiveram somente logins com falha:\n"
      f"{somente_falha}")
