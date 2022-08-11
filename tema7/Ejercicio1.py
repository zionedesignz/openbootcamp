import calculadora as calc

valorA = 15
valorB = 6

resultadoSuma = calc.sumar(valorA, valorB)
resultadoResta = calc.restar(valorA, valorB)
resultadoMultiplicacion = calc.multiplicar(valorA, valorB)
resultadoDivision = calc.dividir(valorA, valorB)

print('La suma de '+str(valorA)+' más '+str(valorB)+' es '+ str(resultadoSuma))
print('La resta de '+str(valorA)+' menos '+str(valorB)+' es '+ str(resultadoResta))
print('La multiplicación de '+str(valorA)+' por '+str(valorB)+' es '+ str(resultadoMultiplicacion))
print('La división de '+str(valorA)+' entre '+str(valorB)+' es '+ str(resultadoDivision))