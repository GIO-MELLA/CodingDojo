class CuentaBancaria:
# atributo de clase
    nombre_banco = "Banco Dojo Nacional"
    cuentasBanco = []

    def __init__(self, tasa_int = 0.01 ,balance = 0.0):
        self.tasa_int = tasa_int
        self.balance = balance
        CuentaBancaria.cuentasBanco.append(self)

    def deposito(self, monto):
        print(f"\n < ABONO + $ {monto} > {CuentaBancaria.nombre_banco}")
        print(f" Saldo Actual Balance: $ {self.balance}")
        self.balance += monto
        print(f" Nuevo Saldo Balance: $ {self.balance}")

        return self

    def retiro(self, monto):
        print(f"\n < RETIRO - $ {monto} > {CuentaBancaria.nombre_banco}")
        print(f" Saldo Actual Balance: $ {self.balance}")

        if self.balance >=  monto:
                self.balance -= monto
                print(f" Nuevo Saldo Balance: $ {self.balance}")
        else:
            self.balance -= 5
            print(" Fondos insuficientes: cobrando una tarifa de $ 5")
            print(f" Nuevo Saldo Balance: $ {self.balance}")

        return self
    
    def mostrar_info_cuenta(self):
        print("------------------------------")
        print(f" Balance Final: $ {self.balance}")
        print("------------------------------\n")

        return self

    def generar_interes(self):
        print(f"\n < INTERÉS {self.tasa_int*100} % > {CuentaBancaria.nombre_banco}")
        print(f" Saldo Actual Balance: $ {self.balance}")

        if (self.balance) > 0:
            interes = self.balance * self.tasa_int
            self.balance += interes
            print(f" ...\n Se ha aplicado un interés de $ {interes}")
            print(f" Nuevo Saldo Balance: $ {self.balance}")
        else:
            print("¡No hay fondos suficientes para aplicar tasa de interés!")
        
        return self
    
    @classmethod
    def print_todas_las_cuentas(cls):
        for cuenta in cls.cuentasBanco:
            cuenta.mostrar_info_cuenta()

class Usuario:
    
    def __init__(self, nombre, apellido, tipo_cuenta, cuenta= CuentaBancaria(tasa_int=0.02, balance=0.0)):
        self.nombre = nombre
        self.apellido = apellido
        self.tipo_cuenta = tipo_cuenta
        self.cuenta = cuenta
        
    def hacer_deposito(self, monto):
        self.cuenta.deposito(monto)
        return self
    
    def hacer_retiro(self, monto):
        self.cuenta.retiro(monto)
        return self
        
    def transferir(self, monto, otro_usuario, tipo_cuenta):
        
        print(f" < TRANSFERENCIA + ${monto}>")
        print(f"DESDE: Usuario {self.nombre} {self.apellido} - Tipo de Cuenta: {self.tipo_cuenta} - Saldo: $ {self.cuenta.balance}")
        self.hacer_retiro(monto)
        print(f"\nA: Usuario {otro_usuario} - Tipo de Cuenta: {tipo_cuenta}\n")
    """
    otro_usuario.cuenta.deposito(monto)
    falta como abonar a la otra cuenta
    """

    def mostrar_balance_usuario(self):
        print("------------------------------")
        print(f" Usuario: {self.nombre} {self.apellido}")
        print(f" Tipo de Cuenta: {self.tipo_cuenta}")
        self.cuenta.mostrar_info_cuenta()

guido1 = Usuario("Guido", "Von 1", "CORRIENTE", CuentaBancaria(balance =0.0))
guido2 = Usuario("Guido", "Von 2", "RUT", CuentaBancaria(balance=10000))

guido1.hacer_deposito(500).hacer_deposito(100).hacer_deposito(1000).hacer_retiro(1200).mostrar_balance_usuario()
guido2.hacer_deposito(1000).hacer_deposito(1000).hacer_retiro(2000).mostrar_balance_usuario()

guido2.transferir(5000, "guido1", "CORRIENTE")

guido1.mostrar_balance_usuario()
guido2.mostrar_balance_usuario()

# Giovanna Mella