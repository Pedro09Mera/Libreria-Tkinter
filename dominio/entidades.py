class Pais:

    def __init__(self,p1,p2,p3,p4):
        self.cod_pais= p1
        self.nombre_pais = p2
        self.ciudad= p3
        self.n_habitantes= p4

    def getData(self):
        return  str(self.cod_pais)+" "+ self.nombre_pais+" "+self.ciudad+" "+str(self.n_habitantes)

    def getFields(self):
        return  "Codigo Postal:"+str(self.cod_pais)+"\nNombre del Pis:"+ self.nombre_pais+"\n"+\
                "Ciudad:"+self.ciudad+"\nNumero de habitantes:"+str(self.n_habitantes)+"\n"

    def setNombre(self,nombre):
        self.nombre_pais= nombre

    def getNombre(self):
        return self.nombre_pais