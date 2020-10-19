class Car:
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._anio = 0
        self._estado = 'En reposo'
        self._motor = Motor(cilindros=4)

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def _anio(self, nuevo_anio):
        self._anio = nuevo_anio

    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(5)
        else: 
            self._motor.inyecta_gasolina(6)
        self._estado = 'En movimiento'
        self.__test()

    def __test(self):
        print("Test private called!")


class Motor:
    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
        """
        Inyecta gasolina al motor
        """
        print(f'Cantidad inyectada: {cantidad}')

if __name__ == "__main__":
    car = Car('Mazda','Mazda 2', 'Red')
    # car.acelerar()
    # print(car.anio)
    # Using normal call (Atributte error)
    # car.__test()
    # Using name mangling
    # car._Car__test()
