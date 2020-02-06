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
            routers[self.vecinos[i]].recibir(self.id, raiz, 1, routers)

    def recibir(self, proxSalto, raiz, numSaltos, routers):
        if (raiz not in self.paquetes): #si no conoces la raiz guarda la ruta y reenviala
            self.paquetes.append(raiz)
            ruta = Ruta(raiz, proxSalto, numSaltos)
            self.rutas.append(ruta)
            self.reenviar(proxSalto, raiz, numSaltos + 1, routers)
        elif (numSaltos < self.buscarRuta(raiz).numSaltos):
            self.paquetes.append(raiz)
            ruta = Ruta(raiz, proxSalto, numSaltos)
            self.rutas[self.rutas.index(self.buscarRuta(raiz))] = ruta
            self.reenviar(proxSalto, raiz, numSaltos + 1, routers)

    def reenviar(self, proxSalto, raiz, numSaltos, routers):
        for i in range(len(self.vecinos)):
            if (self.vecinos[i] != proxSalto) and (self.vecinos[i] != raiz): #no reenvies el msj por donde te llego
                routers[self.vecinos[i]].recibir(self.id, raiz, numSaltos, routers)

    def buscarRuta(self, raiz):
        for ruta in self.rutas:
            if (ruta.raiz == raiz):
                return ruta

    def mostrarRutas(self):
        print("\nMostrando rutas del {}".format(self.nombre))
        print("Hacia:", "\t    Proximo salto:", "  Numero de saltos:")
        for ruta in self.rutas:
            print("Router", ruta.raiz + 1, "     Router", ruta.proxSalto + 1, "           ", ruta.numSaltos)

class Ruta:
    def __init__(self, raiz, proxSalto, numSaltos):
        self.raiz = raiz
        self.proxSalto = proxSalto
        self.numSaltos = numSaltos

def crearRouters():
    routers = []
    numRouters = int(input("Ingrese el numero de routers en la topologia: "))
    for i in range(numRouters):
        print("\nConfigurando Router ", i + 1)
        router = Router("Router {}".format(i + 1), i)
        for j in range(numRouters):
            if (i != j):
                valor = input("Si Router {} es vecino de Router {}, ingrese 1, caso contrario ingrese 0: ".format(i + 1,
                                                                                                                j + 1))
                if (int(valor) == 1):
                    router.vecinos.append(j)
        routers.append(router)
    return routers

def main():
    routers = crearRouters()
    for router in routers:
        router.enviar(routers)

    for router in routers:
        router.mostrarRutas()

if __name__ == '__main__':
    main()
