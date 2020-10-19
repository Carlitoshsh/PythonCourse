# Divide and conquere
import random


def mergesort(lista):
    if(len(lista) > 1):
        medio = len(lista)//2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print(izquierda, '**', derecha)

        # Ordenamiento
        mergesort(izquierda)
        mergesort(derecha)

        # iteradores
        i = 0
        j = 0
        # iteradorListaPrincipal
        k = 0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

        print(f'izquierda {izquierda} *** derecha {derecha}')
        print(lista)
        print('-'*20)

    return lista


if __name__ == "__main__":
    size_list = int(input('Size? '))
    lista = [random.randint(0, 100) for i in range(size_list)]
    print(lista)
    print('-'*2)

    list_ordered = mergesort(lista)
    print(list_ordered)
