#Categoria de CNH
idade = int(input("Digite sua idade: "))
cnh = input("Possuí CNH?[S|N]: ")

if idade >= 18 and cnh == 'S':
    print("Pode dirigir")
elif idade >= 18 and cnh == 'N':
    print("Precisa tirar a CNH")
else:
    print("Não pode dirigir!")