def validarAñoBisiesto(año):
    if año%100==0 and año%400==0:
        return 'El año '+str(año)+' es bisiesto'
    elif año%4==0:
        return 'El año '+str(año)+' es bisiesto'
    else:
        return 'El año '+str(año)+' no es bisiesto'

numero = int(input('Introduce un año:'))
print(validarAñoBisiesto(numero))