"""Exercício 1: Molde de uma Pessoa
Crie uma classe chamada Pessoa. No "registro de nascimento" (__init__), toda pessoa deve
ter um nome e uma idade.

Exercício 2: Criando Pessoas Reais
Usando a classe Pessoa que você criou, crie dois objetos:
1. Uma pessoa chamada "João", com 25 anos.
2. Uma pessoa chamada "Maria", com 30 anos.
Depois de criá-los, imprima o nome e a idade de cada um para confirmar que deu certo.

Exercício 3: Ensinando a se Apresentar
Adicione um método (uma "ação") à sua classe Pessoa chamado apresentar. Esse método
deve imprimir uma frase como: "Olá, meu nome é [nome] e eu tenho [idade] anos." Chame
esse método para os objetos "João" e "Maria"."""

class Pessoa():
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

pessoa1 = Pessoa("João", 20)
pessoa2 = Pessoa("Maria", 30)

print(pessoa1.nome, pessoa1.idade)
print(pessoa2.nome, pessoa2.idade)

print("== Apresentação ==")
pessoa1.apresentar()
pessoa2.apresentar()