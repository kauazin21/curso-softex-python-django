"""Crie uma nova classe chamada Produto. Todo produto deve ter nome e preço. Depois, crie
duas instâncias:
1. Um "Caderno" que custa 15.50.
2. Uma "Caneta" que custa 3.00.
Imprima o nome e o preço de cada produto"""

class Produto():
    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome
        self.preco = preco

produto_1 = Produto("Caderno", 15.50)
produto_2 = Produto("Caneta", 3.0)

print("Nome e preço dos produtos:")
print(f"{produto_1.nome}: R${produto_1.preco:.2f}")
print(f"{produto_2.nome}: R${produto_2.preco:.2f}")