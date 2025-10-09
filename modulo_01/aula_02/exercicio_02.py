#Calculadora de desconto
preco_produto = float(input("Digite o valor do produto: "))

desconto = preco_produto * 0.1

if preco_produto > 100:
    preco_produto = preco_produto - desconto
    print("O produto ganhou um desconto de 10%!")
    print(f"VALOR DO PRODUTO: R${preco_produto:.2f}") 