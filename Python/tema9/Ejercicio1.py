def main():
    paises = input(
        'Indica países a los que desearías viajar (separados por comas)')

    if not ',' in paises:
        print('Debes indicar más de un país y separarlos por comas')
    else:
        listaPaisesSinEspacios = paises.replace(' ', '')
        listaPaises = listaPaisesSinEspacios.split(',')
        setListaPaises = set(listaPaises)
        for pais in setListaPaises:
            print(pais)


if __name__ == '__main__':
    main()
