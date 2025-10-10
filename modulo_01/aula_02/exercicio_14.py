#somador de números positivos
print("="*30)
print("Somador de números posivos")
print("***Digite um número negativo para parar e somar os números***")
print("="*30)


soma = 0

while True:
    num = int(input("Digite um número: "))
    if num >= 0:
        soma = soma + num
    else:
        break

print(f"Soma de todos os números positivos: {soma}")