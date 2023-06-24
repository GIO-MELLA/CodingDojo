class Usuario:
    nombre_banco = "< Primer Dojo Nacional >"

    def __init__(self , name, email, saldo_cuenta):
        self.name = name
        self.email = email
        self.saldo_cuenta = saldo_cuenta

    def hacer_deposito(self, monto):
        print("\nBuenas tardes <", self.name, ">  Bienvenido(a) al", Usuario.nombre_banco)
        print(" Saldo Actual: $", self.saldo_cuenta, " |   Abono: $", monto)
        self.saldo_cuenta += monto
        return self

    def hacer_retiro(self, monto):
        print("\nBuenas tardes <", self.name, ">  Bienvenido(a) al", Usuario.nombre_banco)
        print(" Saldo Actual: $", self.saldo_cuenta, " |   Retiro: $", monto)
        self.saldo_cuenta -= monto
        return self

    def transferir_dinero(self, monto, destino):
        print("\nBuenas tardes <", self.name, ">  Bienvenido(a) al", Usuario.nombre_banco)
        print(" Saldo Actual: $", self.saldo_cuenta, "  Monto a Transferir: $", monto)

        if(monto <= self.saldo_cuenta):
            self.saldo_cuenta -= monto
            destino.hacer_deposito(monto)
            print("\n", self.name, "¡Tranferencia realizada con exito! Saldo Actual en la cuenta: $", self.saldo_cuenta)
        else:
            print("\n", self.name, ", No se puede realizar la tranferencia <Saldo insuficiente>")

        return self

    def mostrar_balance(self):
        print("\n----------------------------------------")
        print(" Nombre del titular: ", self.name)
        print(" Balance: $", self.saldo_cuenta)
        print("----------------------------------------")

guido = Usuario("Guido Van Rossum", "guido@python.com", 0)
monty = Usuario("Monty Black", "monty@python.com", 0)
alej = Usuario("Alej Pillow", "alej@python.com", 0)

guido.hacer_deposito(100).hacer_deposito(200).hacer_deposito(500).hacer_retiro(100).mostrar_balance()

monty.hacer_deposito(1000).hacer_deposito(500).hacer_retiro(300).hacer_retiro(200).mostrar_balance()

alej.hacer_deposito(500).hacer_retiro(100).hacer_retiro(200).hacer_retiro(200).mostrar_balance()

monty.transferir_dinero(1000, alej).mostrar_balance()
alej.mostrar_balance()

# Giovanna Mella