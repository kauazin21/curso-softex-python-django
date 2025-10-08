numeros = [1,2,3,4,5,6,7,8,9,10]
num_primos = []

for num in numeros:
    eh_primo = True
    if num < 2:
        eh_primo = False
    else:
        for i in range(2,num):
            if num % i == 0:
                eh_primo = False
                break
    
    if eh_primo:
        num_primos.append(num)

print(f"Os números primos da lista {numeros} são: {num_primos}")