class Comodo:
    def __init__(self, nome):
        self.nome = nome

class Casa:
    def __init__(self, comodos: list[Comodo]):
        self.comodos = comodos

    def adicionar_comodo(self, comodo: Comodo):
        self.comodos.append(comodo)
        

    def listar_comodos(self):
        for comodo in self.comodos:
            print(f"comodo: {comodo.nome}")


rodar = Casa([Comodo("Quarto")])
rodar.adicionar_comodo(Comodo("Quarto"))
rodar.adicionar_comodo(Comodo("Sala"))
rodar.adicionar_comodo(Comodo("Banheiro"))
rodar.adicionar_comodo(Comodo("Quintal"))
rodar.listar_comodos()