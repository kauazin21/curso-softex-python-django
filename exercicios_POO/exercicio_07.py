"""Crie duas classes: Motor e Carro.
1. A classe Motor terá um atributo potencial.
2. A classe Carro terá modelo. Ao criar um Carro, ele deve também criar um objeto Motor e
guardá-lo como um de seus atributos (ex: self.motor = Motor(100)).
Crie um método no Carro chamado exibir_potencia que imprime a potência do seu motor."""

class Motor:
    def __init__(self, potencia: int) -> None:
        self.potencia = potencia


class Carro:
    def __init__(self, modelo: str, potencia_motor: int) -> None:
        self.modelo = modelo
        self.motor = Motor(potencia_motor)  # cria o motor dentro do carro

    def exibir_potencia(self) -> None:
        print(f"O carro {self.modelo} tem {self.motor.potencia} cavalos de potência.")


meu_carro = Carro("Fusca Turbo", 150)

meu_carro.exibir_potencia()
