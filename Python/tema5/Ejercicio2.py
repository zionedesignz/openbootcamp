def validarNumeroPrimo(numero):
    if numero==0 or numero==1 or numero==2 or numero==4:
        return 'El número es primo'
    else:
        for i in range(2,numero):
            esPrimo = True
            if numero%i== 0:
                esPrimo = False
                break
        return 'El número es primo' if esPrimo else 'El número no es primo'

numero = int(input('Introduce un número:'))
print(validarNumeroPrimo(numero))