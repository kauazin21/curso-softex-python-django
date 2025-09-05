'''Desafio de Programação: Validação de Triângulo
Seu objetivo: Escrever um algoritmo em Python que determine se três valores, fornecidos pelo usuário, podem formar um triângulo.

As Regras do Jogo
1- Teste se a entrada de dados é um número.
2- Se for um número teste se é positivo
3- Para que três lados (lA,lB,lC) formem um triângulo, eles devem obedecer a duas condições importantes:

A soma: A soma de quaisquer dois lados deve ser maior que o terceiro lado.

lA<lB+lC

lB<lA+lC

lC<lA+lB

A diferença: O valor absoluto da diferença entre dois lados deve ser menor que o terceiro lado.

lA>∣lB−lC∣

lB>∣lA−lC∣

lC>∣lA−lB∣

Dica: use o método abs() para ter o valor absoluto de um número.'''

#valor lado A
while True:
    lado_A = input("Digite o valor do lado A: ")
    if lado_A.isdigit():
        lado_A = int(lado_A)
        if lado_A > 0:
            break
        else:
            print("O lado deve ser maior que 0")
    else:
        print("Use somente números inteiros positivos")

#valor lado B
while True:
    lado_B = input("Digite o valor do lado B: ")
    if lado_B.isdigit():
        lado_B = int(lado_B)
        if lado_B > 0:
            break
        else:
            print("O lado deve ser maior que 0")
    else:
        print("Use somente números inteiros positivos")

#valor lado C
while True:
    lado_C = input("Digite o valor do lado C: ")
    if lado_C.isdigit():
        lado_C = int(lado_C)
        if lado_C > 0:
            break
        else:
            print("O lado deve ser maior que 0")
    else:
        print("Use somente números inteiros positivos")

# a + b > c e a - b < c
soma = (lado_A + lado_B > lado_C) and (lado_B + lado_C > lado_A) and (lado_C + lado_A > lado_B)

diferença = abs(lado_A - lado_B < lado_C) and abs(lado_A - lado_C < lado_B) and abs(lado_B - lado_C < lado_A)

if soma and diferença:
    print("Os valores formam um triângulo")

else:
    print("Os valores não formam um triângulo")