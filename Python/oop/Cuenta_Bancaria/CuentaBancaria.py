class CuentaBancaria:
# atributo de clase
    nombre_banco = "Banco Dojo Nacional"
    
    def __init__(self, tasa_int = 0.01 ,balance = 0.0):
        self.tasa_int = tasa_int
        self.balance = balance

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
        print("\n----------------------------------------")
        print(f" Balance Final: $ {self.balance}")
        print("----------------------------------------")

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

# Ejemplos
guidoCB = CuentaBancaria(0.01, 0.0)
guidoCB.deposito(500).deposito(500).deposito(1000).retiro(1200).generar_interes().mostrar_info_cuenta()

alejCB = CuentaBancaria(0.01, 0.0)
alejCB.deposito(1000).deposito(1000).retiro(200).retiro(300).retiro(250).retiro(250).generar_interes().mostrar_info_cuenta()

# Giovanna Mella

