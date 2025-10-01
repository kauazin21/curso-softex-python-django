from pessoa import Pessoa

materias:dict[str, list[float]] = {}

class Estudante(Pessoa):
    def __init__(self, nome: str, idade: int, matricula: str):
        super().__init__(nome, idade)
        self.matricula = matricula

    def add_nota_materia(self, materia: str, nota:float):
        self.materia = materia
        self.nota = nota
        aula = materias.get(self.materia)
        print(f"aula atual: {aula}")
        if aula:
            aula.append(self.nota)
        else:
            materias[self.materia] = [self.nota]
        
        print(f"dicionario de materias: {materias}")

