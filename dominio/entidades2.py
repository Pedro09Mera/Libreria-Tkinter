class Producto:


    def __init__(self,*args):
        self.pro_codigo = args[0]
        self.pro_nombre= args[1]
        self.pro_familia= args[2]
        self.pro_precio= args[3]

    def getData(self):
        return str(self.pro_codigo)+" "+self.pro_nombre+" "+self.pro_familia+" "+str(self.pro_precio)

class Usuario:

    def __init__(self, *param):
        self.id_usuario = param[0]
        self.numero_matricula = param[1]
        self.nombre = param[2]
        self.apellido = param[3]

    def getData(self):
        return self.id_usuario + " " + self.numero_matricula + " " +self.nombre + " " + self.apellido

    def getFields(self):
        return  "id_usuario:"+self.id_usuario+"\nNumero_matricula:"+ self.numero_matricula+"\n"+\
                "Nombre:"+self.nombre+"\nApellido:"+self.apellido+"\n"





class Datos:

    def __init__(self,*param):
        self.cedula = param [0]
        self.celular = param[1]
        self.tipo_sangre = param [2]
        self.discapacidad = param [3]
        self.dirrecion = param [4]
        self.correo = param [5]
        self.id_usuarioo = param[6]
        self.estado_matricula = param[7]

    def getData(self):
        return  self.cedula+" "+self.celular+" "+self.tipo_sangre+" "+self.discapacidad+" "+self.dirrecion+" "+self.correo+" "+self.id_usuarioo+" "+self.estado_matricula