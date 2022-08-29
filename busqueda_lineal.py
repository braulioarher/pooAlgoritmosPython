import random
from pickletools import markobject

contador = 0

def busqueda_lineal(lista, objetivo):   #O(n)
    match = False
    global contador
    for elemento in lista:
        contador += 1
        if elemento == objetivo:
            match = True
            break

    print(contador)
    return match


if __name__ == "__main__":
    tamano_de_lista = int(input("De que tamano quieres tu lista? "))
    objetivo = int(input("Que numero quieres encontrar? "))

    lista = list(range(0,10001))

    encontrado = busqueda_lineal(lista, objetivo)

    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')