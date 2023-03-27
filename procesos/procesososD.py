class Ingreso:

    def inInt(self,cadena):
        x = -1
        while x < 0:
            try:
                x = int(input(cadena))
            except:
                x = -1
                print("Error de valor!")
        return x

    def inFloat(self,cadena):
        x = -1
        while x < 0:
            try:
                x = float(input(cadena))
            except:
                x = -1
                print("Error de valor!")
        return x

class Busqueda:

    def getObject(self, codigo,lista):
        obj = None
        for i in range(len(lista)):
            if codigo== lista[i].cod_pais:
               obj = lista[i]
               break
        return obj

    def getPosition(self,codigo,lista):
        pos = -1
        for i in range(len(lista)):
            if codigo== lista[i].cod_pais:
                pos = i
                break
        return pos

class Cadenas:

    def getCadena(self,cadena):
        msg = ""
        for i in range(1, len(cadena)):
            msg = msg + cadena[i]
        return msg