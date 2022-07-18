
class Usuario:

    nombre_banco = "Interbank"

    def __init__(self,name):
        self.name = name
        self.balance_cuenta = 0

    def hacer_deposito(self, balance_cuenta):
        self.balance_cuenta += balance_cuenta

    def hacer_retiro(self, balance_cuenta):
        self.balance_cuenta -= balance_cuenta

    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.name}, Balance: ${self.balance_cuenta}")

adrien = Usuario("Adrien")
nibbles = Usuario("Mr. Nibbles")
benny_bob = Usuario("Benny Bob")

adrien.hacer_deposito(100)
adrien.hacer_deposito(50)
adrien.hacer_deposito(150)
adrien.hacer_retiro(20)
adrien.mostrar_balance_usuario()

nibbles.hacer_deposito(1000)
nibbles.hacer_deposito(1500)
nibbles.hacer_retiro(200)
nibbles.hacer_retiro(500)
nibbles.mostrar_balance_usuario()

benny_bob.hacer_deposito(1000)
benny_bob.hacer_retiro(250)
benny_bob.hacer_retiro(200)
benny_bob.hacer_retiro(500)
benny_bob.mostrar_balance_usuario()

print(Usuario.nombre_banco)