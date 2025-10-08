class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

    def apresentar(self):
        print(f"Meu nome é {self.nome}, tenho {self.idade} anos e curso {self.curso}")

pessoa = Pessoa("João", 20)
estudante = Estudante("Kauã", 20, "Engenharia")

lista:list[Pessoa] = [pessoa, estudante]

for item in lista:
    item.apresentar()