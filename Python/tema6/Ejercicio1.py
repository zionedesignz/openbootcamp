class Vehiculo:
    color = None
    ruedas = None
    puertas = None

    def asignarColor(self, color):
        self.color = color

    def asignarRuedas(self, ruedas):
        self.ruedas = ruedas

    def asignarPuertas(self, puertas):
        self.puertas = puertas


class Coche(Vehiculo):
    velocidad = None
    cilindrada = None

    def asignarVelocidad(self, velocidad):
        self.velocidad = velocidad

    def asignarCilindrada(self, cilindrada):
        self.cilindrada = cilindrada


superCoche = Coche()
superCoche.asignarColor('rojo')
superCoche.asignarRuedas(5)
superCoche.asignarPuertas(3)
superCoche.asignarVelocidad(220)
superCoche.asignarCilindrada(3000)

print('El superCoche es de color '+superCoche.color+', tiene '+str(superCoche.ruedas)+' ruedas, tiene '+str(superCoche.puertas) +
      ' puertas, alcanza una velocidad punta de '+str(superCoche.velocidad)+'Km/h y tiene una cilindrada de '+str(superCoche.cilindrada)+'cm³.')
