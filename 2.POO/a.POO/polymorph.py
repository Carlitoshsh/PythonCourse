class Persona:
    def __init__(self, name):
        self.name = name

    def avanza(self):
        print("Ando caminando")

class Ciclista(Persona):
    def __init__(self, name):
        super().__init__(name)

    def avanza(self):
        print("Ando en bici")

def main():
    persona = Persona('David')
    persona.avanza()
    ciclista = Persona('David')
    ciclista.avanza()


if __name__ == "__main__":
    main()