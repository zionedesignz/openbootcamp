import math

def calculaAreaTriangulo(altura, base):
    return round((base*altura)/2)

def calculaAreaCirculo(radio):
    return round(math.pi*(radio**2),2)

altura = float(input('Indica la altura del triángulo (cm):'))
base = float(input('Indica la base del triángulo (cm):'))
areaTriangulo = calculaAreaTriangulo(altura,base)
print('El area del triángulo es de '+str(areaTriangulo)+'cm²')

radio = float(input('Indica el radio del círculo (cm):'))
areaCirculo = calculaAreaCirculo(radio)
print('El area del círculo es de '+str(areaCirculo)+'cm²')