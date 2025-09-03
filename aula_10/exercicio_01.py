vendas = [("Teclado", 50, 2), ("Mouse", 25.50, 4),("Monitor", 300, 1),("Fone", 45, 1), ("Webcam", 75.20, 2)]
vendas_filtradas = []
produtos_unicos = set()

for venda in vendas:
    if (venda[1] * venda[2]) >= 100:
        vendas_filtradas.append(venda)

    if venda[2] == 1:
        produtos_unicos.add(venda[0])
        
print("Vendas filtradas(valor total >= 100):\n"
      f"{vendas_filtradas}\n"
      "Produtos unicos:\n"
      f"{produtos_unicos}")