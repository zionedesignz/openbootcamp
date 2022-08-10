class Alumno:
    nombre: str = None
    nota: float = None

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

        print('El alumno '+self.nombre+' con nota ' +
              str(self.nota)+' ha '+self.validarAprobado())

    def validarAprobado(self):
        if self.nota >= 5:
            return 'aprobado'
        else:
            return 'suspendido'


alumno = Alumno('Javier', 4.9)
