"""Crie uma classe Retangulo que é inicializada com base e altura. Crie dois métodos:
1. calcular_area(): deve retornar o cálculo base * altura.
2. calcular_perimetro(): deve retornar o cálculo 2 * (base + altura).
Crie um retângulo, chame os dois métodos e imprima os resultados que eles retornam."""

class Retangulo:
    def __init__(self, base: float, altura: float) -> None:
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return self.base * self.altura

    def calcular_perimetro(self) -> float:
        return 2 * (self.base + self.altura)


# Criando um retângulo de exemplo
retangulo = Retangulo(5, 3)

# Chamando os métodos e imprimindo os resultados
print(f"Área do retângulo: {retangulo.calcular_area():.2f}")
print(f"Perímetro do retângulo: {retangulo.calcular_perimetro():.2f}")
