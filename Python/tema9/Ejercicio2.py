from functools import reduce


def main():
    lista = [1, 2, 3, 4, 5, 6]
    listaImpares = filter(obtenerElementosImpares, lista)
    sumaImpares = reduce(sumarElementos, listaImpares)
    print(sumaImpares)


def obtenerElementosImpares(valor):
    if valor % 2 != 0:
        return valor


def sumarElementos(valorAcumulado, valorActual):
    return valorAcumulado+valorActual


if __name__ == '__main__':
    main()
