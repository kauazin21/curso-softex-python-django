"""Crie uma classe Carro com os atributos modelo e nivel_combustivel (começando com 0).
1. Crie um método para abastecer(litros) que aumenta o nível de combustível.
2. Crie um método dirigir(distância) que consome combustível (ex: 1 litro a cada 10 km). O
método deve verificar se há combustível suficiente para a viagem. Se houver, diminua o
combustível e avise que o carro andou. Se não, avise que não há combustível."""

class Carro:
    def __init__(self, modelo: str) -> None:
        self.modelo = modelo
        self.nivel_combustivel = 0  # começa vazio

    def abastecer(self, litros: float) -> None:
        self.nivel_combustivel += litros
        print(f"O carro {self.modelo} foi abastecido com {litros}L.")
        print(f"Nível atual de combustível: {self.nivel_combustivel:.2f}L")

    def dirigir(self, distancia: float) -> None:
        consumo_necessario = distancia / 10  # 1 litro a cada 10 km
        if consumo_necessario <= self.nivel_combustivel:
            self.nivel_combustivel -= consumo_necessario
            print(f"O carro {self.modelo} andou {distancia} km.")
            print(f"Combustível restante: {self.nivel_combustivel:.2f}L")
        else:
            print(f"Combustível insuficiente para andar {distancia} km.")
            print(f"Nível atual de combustível: {self.nivel_combustivel:.2f}L")



meu_carro = Carro("Fusca")

meu_carro.abastecer(20)   
meu_carro.dirigir(50)     
meu_carro.dirigir(300)    