"""
class <name>(<super_class>):
    def __init__(self, <params>):
        self.<init_params>

    def <method>(self, <params>):
        <implementation>
"""


class Hotel:
    def __init__(self, numero_maximo_de_huespedes, lugares_de_estacionamiento):
        self.numero_maximo_de_huespedes = numero_maximo_de_huespedes
        self.lugares_de_estacionamiento = lugares_de_estacionamiento
        self.huespedes = 0

    def anadir_huespedes(self, cantidad_de_huespedes):
        self.huespedes += cantidad_de_huespedes

    def checkout(self, cantidad_de_huespedes):
        self.huespedes -= cantidad_de_huespedes

    def ocupacion_total(self):
        return self.huespedes

hotel = Hotel(50, 20)
hotel.anadir_huespedes(3)
hotel.checkout(1)
a = hotel.ocupacion_total() # 2
print(a)
