import csv, numpy

class router:
    def __init__(self, nombre, ip):
        self.nombre = nombre
        self.ip = ip
        self.area = 1
        self.conocidos = []

    def anunciarVecinos(self):
        pass

def leerCSV():
    matriz = numpy.loadtxt(open("adyacencia.csv", "rb"), delimiter=",", skiprows=1)
    matriz = matriz.astype(int)
    print(matriz)

def main():
    leerCSV()

if __name__ == '__main__':
    main()
