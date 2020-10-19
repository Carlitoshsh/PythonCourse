class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, coordenada):
        return coordenada

if __name__ == "__main__":
    a = Coordinates(4,5)
    b = 2
    print(isinstance(b, Coordinates))
