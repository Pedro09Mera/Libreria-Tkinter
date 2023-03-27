from procesos.procesosD import *
class MenuD:

    def __init__(self):
        self.obI = Ingreso()

    def getMenu(self,tupla):
        for x in range(len(tupla)):
            print(str(x+1)+"♥"+tupla[x]+".")
        op = 0
        while op<1 or op>len(tupla):
            op= self.obI.inInt("Ingrese un Numero [1__"+str(len(tupla))+"]:")
        return op