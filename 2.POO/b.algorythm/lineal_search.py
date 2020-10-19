import random


def lineal_search(lista, objetivo):
    match = False

    for elemento in lista: # O(n)
        if elemento == objetivo:
            match = True
            break

    return match


if __name__ == "__main__":
    size_list = int(input('Size? '))
    number_to_find = int(input('What number? '))

    lista = [random.randint(0, 100) for i in range(size_list)]
    isFind = lineal_search(lista, number_to_find)
    print(lista)
    print(
        f'El elemento {number_to_find} {"esta" if isFind else "no está"} en la lista')
