class Teclado:
    def ligar(self):
        print("O teclado foi ativado.")

class Mouse:
    def ligar(self):
        print("Mouse operando.")

class Monitor:
    def ligar(self):
        print("Monitor funcionando.")

class Computador:
    def __init__(self):
        self.teclado = Teclado()
        self.mouse = Mouse()
        self.monitor = Monitor()

    def ligar_computador(self):
        print("O computador está ligando.")
        self.teclado.ligar()
        self.mouse.ligar()
        self.monitor.ligar()

rodar = Computador()
rodar.ligar_computador()