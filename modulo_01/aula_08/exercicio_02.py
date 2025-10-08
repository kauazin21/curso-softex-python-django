num_telefone = input("Digite um número de telefone com 11 dígitos: ")
for num in num_telefone:
    contador_repetidos = 0
    
    if num not in "0123456789":
        print("Número de telefone inválido!")
        break
    
    for c in num_telefone:
        if num==c:
            contador_repetidos += 1
        if contador_repetidos >= 3:
            print("O número não é válido")
            break

print(f"O número: ({num_telefone[:2]}){num_telefone[2:7]}-{num_telefone[7:12]} é válido")



    