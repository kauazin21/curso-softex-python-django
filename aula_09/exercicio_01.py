numeros = [1,5,2,8,5,3,5]
numero_procurado = 5
contador = 0

for numero in numeros:
    if numero == 5:
        contador +=1

print(f'O numero procurado: {numero_procurado}, aparece {contador} vezes na lista.')