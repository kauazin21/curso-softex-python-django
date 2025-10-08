lista1 = ["abacaxi", "uva", "pera", "morango"]
lista2 = ["laranja", "morango", "uva", "maçã"]
lista3 = []

for fruta1 in lista1:
    for fruta2 in lista2:
        if fruta1 == fruta2:
            lista3.append(fruta2)

print(lista3)