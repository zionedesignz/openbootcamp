edad = int(input('Por favor introduce tu edad:'))

if edad >= 18:
    print('Eres mayor de edad')
elif edad <= 0:
    print('La edad introducida no es válida')
else:
    print('Eres menor de edad')