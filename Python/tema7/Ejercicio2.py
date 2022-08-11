import time

t = time.localtime()
horaActual = t.tm_hour


def calcularTiempoRestanteTrabajo():
    año, mes, dia, _, _, _, dS, dA, hV = t
    tLimite = (año, mes, dia, 19, 0, 0, dS, dA, hV)
    tLimiteSeg = time.mktime(tLimite)
    tSeg = time.time()

    tRestSeg = int(tLimiteSeg) - int(tSeg)
    minutostRest = tRestSeg//60
    segundosRest = tRestSeg % 60
    horasRest = minutostRest//60
    minutosRest = minutostRest % 60

    horas = str(horasRest) + ' horas' if horasRest > 0 else ''
    minutos = str(minutosRest) + ' minutos' if minutosRest > 0 else ''
    segundos = str(segundosRest) + ' segundos' if segundosRest > 0 else ''

    print('Te quedan', horas, minutos, segundos, 'de trabajo')


if horaActual > 19:
    print('Es la hora de ir a casa')
else:
    calcularTiempoRestanteTrabajo()
