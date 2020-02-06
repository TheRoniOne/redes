import numpy

class Router:
    def __init__(self, nombre, ID):
        self.id = ID
        self.nombre = nombre
        self.vecinos = []
        self.rutas = []
        self.paquetes = []

    def enviar(self, routers):
        raiz = self.id
        print("Mensaje creado", raiz)
        for i in range(len(self.vecinos)):
            print("Enviando mensaje a Router {}".format(self.vecinos[i][0] + 1))
            routers[self.vecinos[i][0]].recibir(self.id, raiz, 1, routers)

    def recibir(self, proxSalto, raiz, numSaltos, routers):
        if (raiz not in self.paquetes): #si no conoces la raiz guarda la ruta y reenviala
            self.paquetes.append(raiz)
            ruta = Ruta(raiz, proxSalto, numSaltos)
            self.rutas.append(ruta)
            print("Ruta apredida hacia ", raiz + 1)
            self.reenviar(proxSalto, raiz, numSaltos + 1, routers)
        elif (numSaltos < self.buscarRuta(raiz).numSaltos):
            self.paquetes.append(raiz)
            ruta = Ruta(raiz, proxSalto, numSaltos)
            self.rutas[self.rutas.index(self.buscarRuta(raiz))] = ruta
            print("Ruta apredida hacia ", raiz)
            self.reenviar(proxSalto, raiz, numSaltos + 1, routers)

    def reenviar(self, proxSalto, raiz, numSaltos, routers):
        for i in range(len(self.vecinos)):
            #print(self.vecinos[i][0])
            if (self.vecinos[i][0] != proxSalto) and (self.vecinos[i][0] != raiz): #no reenvies el msj por donde te llego
                routers[self.vecinos[i][0]].recibir(self.id, raiz, numSaltos, routers)
                print("Mensaje reenviado a Router {}".format(self.vecinos[i][0] + 1))

    def buscarRuta(self, raiz):
        for ruta in self.rutas:
            if (ruta.raiz == raiz):
                return ruta

    def mostrarRutas(self):
        print("\nMostrando rutas del {}".format(self.nombre))
        for ruta in self.rutas:
            print("Hacia Router {}".format(ruta.raiz + 1), "\tProximo salto: Router {} ".format(ruta.proxSalto + 1),
                  "\tNumero de saltos: {}".format(ruta.numSaltos))

class Ruta:
    def __init__(self, raiz, proxSalto, numSaltos):
        self.raiz = raiz
        self.proxSalto = proxSalto
        self.numSaltos = numSaltos

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
    for router in routers:
        router.enviar(routers)

    for router in routers:
        router.mostrarRutas()

if __name__ == '__main__':
    main()
