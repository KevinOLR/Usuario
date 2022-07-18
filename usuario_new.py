
class Usuario:

    nombre_banco = "New Bank"

    def __init__(self,name):
        self.name = name
        self.balance_cuenta = 0

    def hacer_deposito(self, balance_cuenta):
        self.balance_cuenta += balance_cuenta
        return self

    def hacer_retiro(self, balance_cuenta):
        self.balance_cuenta -= balance_cuenta
        return self

    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.name}, Balance: ${self.balance_cuenta}")
        return self

adrien = Usuario("Adrien")
nibbles = Usuario("Mr. Nibbles")
benny_bob = Usuario("Benny Bob")

adrien.hacer_deposito(100).hacer_deposito(50).hacer_deposito(150).hacer_retiro(20).mostrar_balance_usuario()

nibbles.hacer_deposito(1000).hacer_deposito(1500).hacer_retiro(200).hacer_retiro(500).mostrar_balance_usuario()

benny_bob.hacer_deposito(1000).hacer_retiro(250).hacer_retiro(200).hacer_retiro(500).mostrar_balance_usuario()

print(Usuario.nombre_banco)