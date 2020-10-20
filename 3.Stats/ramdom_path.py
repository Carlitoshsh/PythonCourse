from borr import BorrachoTradicional
from field import Field
from coord import Coord

from bokeh.plotting import figure, show


def caminata(field, borr, steps):
    start = field.get_coords(borr)
    for _ in range(steps):
        field.move_borr(borr)

    return start.distance(field.get_coords(borr))


def test_walked(steps, repetitions, type_borr):
    borr = type_borr(name='David')
    origin = Coord(0, 0)
    distances = []

    for _ in range(repetitions):
        field = Field()
        field.add_borr(borr, origin)
        test_walked = caminata(field, borr, steps)
        distances.append(round(test_walked, 1))

    return distances


def draw(axis_x, axis_y):
    graf = figure(title='Camino aleatorio', x_axis_label='pasos',
                  y_axis_label='distancia')
    arrx = axis_x
    arry = axis_y
    print(arrx)
    print(arry)
    graf.line(x=arrx, y=arry)
    # graf..
    show(graf)


def main(distances_walked, repetitions, tipo):
    distances_per_walk = []

    for distance in distances_walked:
        distances = test_walked(distance, repetitions, tipo)
        media = round(sum(distances) / len(distances), 4)
        distances_max = max(distances)
        distances_min = min(distances)
        distances_per_walk.append(int(media))
        print(f'{tipo.__name__} caminara aleatoria de {distance} pasos')
        print(f'Media = {media}')
        print(f'Max = {distances_max}')
        print(f'Min = {distances_min}')

    draw(distances_walked, distances_per_walk)


if __name__ == "__main__":
    distances_walked = [10, 100, 1000, 10000]
    repetitions = 100

    main(distances_walked, repetitions, BorrachoTradicional)
