notas = [("Ana", 9.5),("João", 8.0),("Maria",10.00),
         ("Pedro", 7.5),("Ana",10.0),("Calos", 6.5)]


abaixo_nota = set()
maior_nota = 0

for nome, nota in notas:
    if nota > maior_nota:
        maior_nota = nota
    
    if nota < 7:
        abaixo_nota.add(nome)

alunos_maior_nota = []
for nome, nota in notas:
    if nota == maior_nota:
        alunos_maior_nota.append(nome)
alunos_maior_nota = tuple(alunos_maior_nota)
    
print(f"A maior nota alcançada é: {maior_nota}\n"
      f"\nAlunos que tiraram a maior nota:{alunos_maior_nota}\n"
      f"\nAlunos que tiraram nota menor que 7.0: {abaixo_nota}")