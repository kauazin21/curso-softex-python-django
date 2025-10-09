#Avaliador de notas
nota = float(input("Digite a nota do aluno: "))

if nota < 5:
    print("Conceito D")

elif nota < 6.9:
    print("Conceito C")

elif nota < 8.9:
    print("Conceito B")
    
else:
    print("Conceito A")
