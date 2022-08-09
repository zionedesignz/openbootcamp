# OPCIÓN A
from cgi import print_arguments


valorInicial = 100
valorFinal = 1

while valorInicial >= valorFinal:
    if valorInicial == 1:
        print(str(valorInicial))
    else:
        print(str(valorInicial), end=', ')
    valorInicial -= 1

print('--------------------------------------------------')
# OPCIÓN B
valorInicial = 1
valorFinal = 100
lista = []

for i in range(valorInicial, valorFinal+1):
    lista.append(i)
print(sorted(lista, reverse=True))
