"""Crie uma classe ContaBancaria. Toda conta deve começar com um titular e um saldo inicial.
Crie um método depositar(valor) que some um valor ao saldo da conta. Crie um objeto,
deposite um valor e imprima o novo saldo
Na mesma classe ContaBancaria, adicione um método para sacar(valor). Este método deve
verificar se há saldo suficiente na conta.
● Se houver, ele deve subtrair o valor do saldo e imprimir "Saque realizado com sucesso.".
● Se não houver, ele deve imprimir "Saldo insuficiente." e não alterar o saldo.
Teste os dois cenários: um saque bem-sucedido e uma tentativa de sacar mais do que
tem."""

class ContaBancaria():
    def __init__(self, titular: str, saldo_inicial: float) -> None:
        self.titular = titular
        self.saldo_inicial = saldo_inicial
    
    def depositar(self, valor: float):
        self.saldo_inicial += valor
        print(f"O valor de R${valor:.2f} foi adicionado a sua conta.")
        print(f"Novo saldo: R${self.saldo_inicial:.2f}")

    def sacar(self, valor: float):
        if valor <= self.saldo_inicial:
            self.saldo_inicial -= valor
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

cliente = ContaBancaria("Kauã", 0)

cliente.depositar(100)
print()
cliente.sacar(50)
print()
cliente.depositar(30)
print()
cliente.sacar(300)