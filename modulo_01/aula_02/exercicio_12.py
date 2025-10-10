#acumulador de soma
soma = 0
contador = 0

while contador < 5:
    num = int(input("Digite um número: "))
    soma += num
    
    contador += 1

print(f"A soma dos 5 números digitados: {soma}")