import numpy

class Router:
    def __init__(self, nombre, ID):
        self.id = ID
        self.nombre = nombre
        self.area = 1
        self.vecinos = []
        self.conocidos = []
        self.rutas = []
        self.paquetesLSP = []

    def enviarLSP(self, routers):
        miLSP = [(self.id, self.vecinos)]
        self.paquetesLSP.append(miLSP)
        for i in range(len(self.vecinos)):
            #print(self.vecinos[i][0])
            routers[self.vecinos[i][0]].recibirLSP(self.id, miLSP, routers)

    def recibirLSP(self, origen, msjLSP, routers):
        if (msjLSP not in self.paquetesLSP): #no reevies ni guardes el msjLSP si ya lo tenias
            self.paquetesLSP.append(msjLSP)
            self.reenviarLSP(origen, msjLSP, routers)

    def reenviarLSP(self, origen, msjLSP, routers):
        for i in range(len(self.vecinos)):
            #print(self.vecinos[i][0])
            if (self.vecinos[i][0] != origen): #no reenvies el msjLSP por donde te llego
                routers[self.vecinos[i][0]].recibirLSP(self.id, msjLSP, routers)

    def calcularRutas(self): #todo
        while (True):
            ruta = Ruta(self, )

class Ruta:
    def __init__(self, raiz, destino):
        self.raiz = raiz
        self.destino = destino
        self.recorrido = [(self.raiz, self.destino)]
        self.distancias = []

    def calcDist(self, indice, matrizAdy): #todo
        pass

def leerCSV():
    matriz = numpy.loadtxt(open("adyacencia.csv", "rb"), delimiter=",")
    matriz = matriz.astype(int)
    return matriz

def crearRouters(matriz):
    routers = []
    for i in range(len(matriz)):
        router = Router("Router {}".format(i+1), i)
        for j in range(len(matriz)):
            if (matriz[i][j] != -1):
                router.vecinos.append((j, matriz[i][j]))
        routers.append(router)
    return routers

def main():
    matrizAdyacencia = leerCSV()
    routers = crearRouters(matrizAdyacencia)
    #print(routers[0].vecinos)
    #routers[0].enviarLSP(routers)
    """for router in routers:
        router.enviarLSP()"""

if __name__ == '__main__':
    main()
