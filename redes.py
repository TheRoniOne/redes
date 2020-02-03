import numpy

class Router:
    def __init__(self, nombre):
        self.nombre = nombre
        self.area = 1
        self.vecinos = []
        self.conocidos = []

    def anunciarVecinos(self):
        pass

def leerCSV():
    matriz = numpy.loadtxt(open("adyacencia.csv", "rb"), delimiter=",")
    matriz = matriz.astype(int)
    return matriz

def crearRouters(numRouters):
    routers = []
    for i in range(numRouters):
        router = Router("Router {}".format(i+1))
        routers.append(router)
    return routers

def main():
    matrizAdyacencia = leerCSV()
    routers = crearRouters(len(matrizAdyacencia))

if __name__ == '__main__':
    main()
