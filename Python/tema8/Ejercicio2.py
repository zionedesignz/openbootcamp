import pickle


def main():
    pathSplit = __file__.split('\\')
    pathSplit.pop()
    path = '\\'.join(pathSplit)

    coche = Vehiculo('Honda', 'Civic', 'negro', 3)

    f = open(path+'/data.bin', 'wb')
    pickle.dump(coche, f)
    f.close()

    df = open(path+'/data.bin', 'rb')
    dCoche = pickle.load(df)
    df.close()

    print(
        f'El coche es de la marca {dCoche.marca}, modelo {dCoche.modelo}, color {dCoche.color} y tiene {dCoche.puertas} puertas.')


class Vehiculo:
    marca: None
    modelo: None
    color: None
    puertas: None

    def __init__(self, marca, modelo, color, puertas):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.puertas = puertas

    def obtenerMarca(self):
        return self.marca


if __name__ == '__main__':
    main()
