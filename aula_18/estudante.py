from pessoa import Pessoa

class Estudante(Pessoa):
    def __init__(self, nome: str, idade: int, matricula: str):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.materias:dict[str, list[float]] = {}

    def add_nota_materia(self, materia: str, nota:float):
        self.materia = materia
        self.nota = nota
        aula = self.materias.get(self.materia)
        print(f"aula atual: {aula}")
        if aula:
            aula.append(self.nota)
        else:
            self.materias[self.materia] = [self.nota]
        
        print(f"dicionario de materias: {self.materias}")

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome} | Idade: {self.idade} | Matrícula: {self.matricula}")
        for materia, notas in self.materias.items():
            media = sum(notas) / len(notas)
            print(f"  Matéria: {materia} | Notas: {notas} | Média: {media:.2f}")