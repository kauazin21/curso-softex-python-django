from estudante import Estudante

class Escola:
    def __init__(self, nome: str):
        self.nome = nome
        self.estudantes: list[Estudante] = []
    
    def add_estudante(self, estudante: Estudante):
        self.estudantes.append(estudante)

    def mostrar_relatorio(self):
        print(f"=== Relatório da Escola {self.nome} ===")
        for estudante in self.estudantes:
            estudante.mostrar_informacoes()
            print("-" * 40)