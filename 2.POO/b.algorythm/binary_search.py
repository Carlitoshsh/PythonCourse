# Divide and conquere
import random

def binary_search(lista, start, end, number_to_find):
    print(f'Buscando entre {lista[start]} y {lista[end-1]}')
    if start > end:
        return False
    
    middle = (start+end)// 2

    if lista[middle] == number_to_find:
        return True
    elif lista[middle] < number_to_find:
        return binary_search(lista, middle + 1, end, number_to_find)
    else:
        return binary_search(lista, start, middle-1, number_to_find)


if __name__ == "__main__":
    size_list = int(input('Size? '))
    number_to_find = int(input('What number? '))

    lista = sorted([random.randint(0, 100) for i in range(size_list)])
    
    isFind = binary_search(lista, 0, len(lista), number_to_find)
    print(lista)
    print(
        f'El elemento {number_to_find} {"esta" if isFind else "no está"} en la lista')
