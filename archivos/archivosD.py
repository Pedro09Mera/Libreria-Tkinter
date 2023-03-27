    #  Proyecto: Reewgistro de estudiante
     #  Empresa:  Pedro Mera
      # Proceso: archivos
      # Recursos://



from dominio.entidades import *
from vistas.registroEstudiante1 import *
from dominio.entidades2 import *
class ArchivoD:

    def create(self,ruta,registro,modo):
        archivo = open(ruta,modo)
        archivo.write(registro)
        archivo.close()

    def getAllPaises(self,ruta):
        lista=[]
        try:
            archivo = open(ruta,"r")
            for linea in archivo.readlines():
                tupla = linea.split(";")
                obj = Pais(int(tupla[0]),tupla[1],tupla[2],float(tupla[3]))
                lista.append(obj)
            archivo.close()
        except:
            print("Error de lectura...")
        return

    def getAllRegistro(self,ruta):
        lista=[]
        try:
            archivo = open (ruta,"r")
            for linea in archivo.readlines():
                tupla = linea.split(";")
                obj = Usuario(tupla[0],tupla[1],tupla[2],(tupla[3]))
                lista.append(obj)
            archivo.close()
        except:
            print("Error")

    def getAllDatos(self,ruta):
        lista = []
        try:
            archivo = open(ruta, "r")
            for linea in archivo.readlines():
                tupla = linea.split(";")
                obj = Datos(tupla[0], tupla[1], tupla[2], (tupla[3]),tupla[4],tupla[5],tupla[6],tupla[7])
                lista.append(obj)
            archivo.close()
        except:
            print("Error")