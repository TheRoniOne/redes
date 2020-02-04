import numpy

class Router:
    def __init__(self, nombre, ID):
        self.id = ID
        self.nombre = nombre
        self.area = 1
        self.vecinos = []
        self.recorridos = []
        self.conocidos = []
        self.rutas = []
        self.paquetesLSP = []

    def enviarLSP(self, routers):
        miLSP = (self.id, self.vecinos)
        print("Mensaje LSP creado", miLSP)
        self.paquetesLSP.append(miLSP)
        for i in range(len(self.vecinos)):
            print("Enviando mensaje LSP a Router {}".format(self.vecinos[i][0] + 1))
            routers[self.vecinos[i][0]].recibirLSP(self.id, miLSP, routers)

    def recibirLSP(self, origen, msjLSP, routers):
        if (msjLSP not in self.paquetesLSP): #no reevies ni guardes el msjLSP si ya lo tenias
            self.paquetesLSP.append(msjLSP)
            print("Mensaje LSP recibido y guardado", msjLSP)
            self.reenviarLSP(origen, msjLSP, routers)

    def reenviarLSP(self, origen, msjLSP, routers):
        for i in range(len(self.vecinos)):
            #print(self.vecinos[i][0])
            if (self.vecinos[i][0] != origen): #no reenvies el msjLSP por donde te llego
                routers[self.vecinos[i][0]].recibirLSP(self.id, msjLSP, routers)
                print("Mensaje LSP reenviado a Router {}".format(self.vecinos[i][0] + 1))

    def buscarLSP(self, id):
        for paquete in self.paquetesLSP:
            if (paquete[0] == id):
                return paquete

    def buscarRuta(self, destino):
        for ruta in self.rutas:
            if (ruta.destino == destino)
                return ruta

    def calcularRutas(self): #todo
        for i in range(len(self.paquetesLSP)):
            if (i == 0):
                for vecino in self.vecinos:
                    ruta = Ruta(self.id, vecino[0])
                    ruta.distancias.append(vecino[1])
                    self.rutas.append(ruta)
                    self.conocidos.append(vecino[0])
                self.recorridos.append(self.id)
            else:
                for ruta in self.rutas:
                    if (ruta.destino not in self.recorridos):
                        msjLSP = self.buscarLSP(ruta.destino)
                        for vecino in msjLSP[1]:
                            if (vecino[0] != self.id):
                                rutaNueva = ruta
                                rutaNueva.destino = vecino[0]
                                rutaNueva.recorrido.append(ruta.destino, rutaNueva.destino)
                                rutaNueva.distancias.append(ruta.distancias[-1] + vecino[1])
                                if (vecino[0] not in self.conocidos):
                                    self.rutas.append(rutaNueva)
                                    self.conocidos.append(vecino[0])
                                elif (rutaNueva.distancias[-1] < self.buscarRuta(vecino[0]).distancias[-1]):
                                    self.rutas[self.rutas.index(self.buscarRuta(vecino[0]))] = rutaNueva
                        self.recorridos.append(ruta.destino)

class Ruta:
    def __init__(self, raiz, destino):
        self.raiz = raiz
        self.destino = destino
        self.recorrido = [(self.raiz, self.destino)]
        self.distancias = []

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
    #routers[0].enviarLSP(routers)
    for router in routers:
        router.enviarLSP(routers)

if __name__ == '__main__':
    main()
