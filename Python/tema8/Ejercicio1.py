def main():
    dato = 'Texto línea 1'
    dato2 = [
        'Texto línea 2',
        'Texto línea 3',
        'Texto línea 4'
    ]

    escribeFichero(dato)
    escribeFichero(dato2)


def escribeFichero(data):
    pathSplit = __file__.split('\\')
    pathSplit.pop()
    path = '\\'.join(pathSplit)

    f = open(path+'\datos.txt', 'a', encoding='utf-8')
    tipoDato = type(data).__name__

    match(tipoDato):
        case 'str':
            if not data.endswith('\n'):
                data += '\n'
            f.write(data)
        case 'list':
            for linea in data:
                if not linea.endswith('\n'):
                    linea += '\n'
                f.write(linea)

    f.close()


if __name__ == '__main__':
    main()
