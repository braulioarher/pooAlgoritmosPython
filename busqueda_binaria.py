import random

contador = 0


def busqueda_binaria(lista, comienzo, final, objetivo):

    global contador
    contador += 1
    if comienzo > final:
        return False

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)  
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)


if __name__ == "__main__":
    tamano_de_lista = int(input("De que tamano quieres tu lista? "))
    objetivo = int(input("Que numero quieres encontrar? "))

    lista = list(range(0,10001))

    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)

    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print(contador)