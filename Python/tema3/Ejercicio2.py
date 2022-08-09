peso = float(input('Por favor introduce tu peso (kg):'))
estatura = float(input('Por favor introduce tu estatura (m):'))

indiceMasaCorporal = peso/(estatura**2)
indiceMasaCorporalRounded = round(indiceMasaCorporal, 2)

print('Tu índice de masa corporal es: ', str(indiceMasaCorporalRounded))