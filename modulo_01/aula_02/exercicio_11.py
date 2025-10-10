#tabuada simples
num = int(input("Digite um número: "))

tabuada = [1,2,3,4,5,6,7,8,9,10]

for i in tabuada:
    resultado = num * i
    print(f"{num} x {i} = {resultado}")