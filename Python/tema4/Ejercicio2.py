valorInicial = int(input('Introduce valor inicial: '))
valorFinal = int(input('Introduce valor final: '))
listaValores = []

if valorInicial < valorFinal:
    for numero in range(valorInicial, valorFinal+1):
        if numero%2 != 0:
            listaValores.append(numero)
    print(listaValores)
else:
    print('El valor inicial debe ser inferior al valor final')