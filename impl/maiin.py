from menu.menuD import *
from dominio.entidades import *
from procesos.procesososD import *
from archivos.archivosD import *

class Main:

    def __init__(self):
        self.ruta="C:/Users/Lenovo/PycharmProjects/pythonProject1/pythonProject/Examen/Pais.csv"
        self.arc=ArchivoD()
        self.obMn = MenuD()
        self.obI = Ingreso()
        self.busque = Busqueda()
        self.lista_paises= self.arc.getAllPaises(self.ruta)

    def getRun(self):
        print("\t\t♥Registro de Habitantes de paises de una ciudad♥")
        tupla=("REGISTRE SU PAIS","CONSULTA","ACTUALIZAR DATOS","ELIMINAR DATOS","LISTAR","SALIR")
        pais = self.obMn.getMenu(tupla)
        if pais == 1:
            self.registro()
            input("TECLA ENTER CONTINUAR.")
            self.getRun()
        if pais == 2:
            self.Consulta()
            input("TECLA ENTER CONTINUAR.")
            self.getRun()
        if pais == 3:
            self.editar()
            input("TECLA ENTER CONTINUAR.")
            self.getRun()
        if pais == 4:
            self.eliminar()
            input("TECLA ENTER CONTINUAR.")
            self.getRun()
        if pais == 5:
            self.listar()
            input("TECLA ENTER CONTINUAR")
            self.getRun()
        if pais == 6:
            print("Salio del registro con exito")

    def registro(self):
        print("\t\tRegistro de paises.")
        codigo = self.obI.inInt("Ingrese  codigo  del pais a registrar:")
        self.lista_paises = self.arc.getAllPaises(self.ruta)
        nombre = input("Nombre del Pais a registar:")
        ciudad = input("Ciudad del Pais: ")
        n_habitantes= self.obI.inFloat("Numero de Habitantes: ")
        obj= Pais(codigo,nombre,ciudad,n_habitantes)
        registro1 = str(obj.cod_pais) + ";" + obj.getNombre() + ";" + obj.ciudad + ";" + str(obj.n_habitantes) + ";\n"
        self.arc.create("Pais.csv", registro1, "a")
        #self.lista_paises.append(obj)

    def Consulta(self):
        print("\t\tConsulta de Pais.")
        codigo = self.obI.inInt("Codigo del pais :")
        self.lista_paises = self.arc.getAllPaises(self.ruta)
        obj = self.busque.getObject(codigo,self.lista_paises)
        if obj!= None:
            print(obj.getFields())
        else:
            print("El codigo del ingresado no esta registrado!")

    def editar(self):
        print("\t\tActualizar Nuevos Datos de un Nuevo Pais.")
        codigo = self.obI.inInt("Codigo del pais:")
        self.lista_paises = self.arc.getAllPaises(self.ruta)
        posi = self.busque.getPosition(codigo,self.lista_paises)
        print("Posicion: ",posi)
        if posi!=-1:
            print(self.lista_paises[posi].getFields())
            nombre_pais = input("Nombre de pais: ")
            ciudad = input("ciudad: ")
            n_habitantes = self.obI.inFloat("Numero de habitantes: ")
            self.lista_paises[posi].nombre_pais=nombre_pais
            self.lista_paises[posi].ciudad=ciudad
            self.lista_paises[posi].n_habitantes= n_habitantes
            registros=""
            for i in range(len(self.lista_paises)):
                registros = registros + str(self.lista_paises[i].cod_pais) + ";" + \
                            self.lista_paises[i].getNombre() + ";" + self.lista_paises[i].ciudad + ";" + str(self.lista_paises[i].n_habitantes) + ";\n"
            self.arc.create(self.ruta,registros, "w")
            print("Datos de la ciudad actualizado!!")
        else:
            print("Codigo Pais no existe!!")
    def eliminar(self):
        print("\t\tElimanar  datos de los paises")
        codigo=self.obI.inInt("Codigo del pais: ")
        self.lista_paises = self.arc.getAllPaises(self.ruta)
        pos = self.busque.getPosition(codigo,self.lista_paises)
        if pos!=-1:
            print(self.lista_paises[pos].getFields())
            self.lista_paises.pop(pos)
            registros = "w"
            for i in range(len(self.lista_paises)):
                registros = registros + str(self.lista_paises[i].cod_pais) + ";" + self.lista_paises[i].getNombre() + ";" + self.lista_paises[i].ciudad + ";" + str(self.lista_paises[i].n_habitantes) + ";\n"
            self.arc.create(self.ruta, registros, "w")
            print("Los datos fueron eliminados")
        else:
            print("El codigo  ingresado no es el correcto")

    def listar(self):
        print("\t\tPaises Ingresados.")
        self.lista_paises = self.arc.getAllPaises(self.ruta)
        for i in range(len(self.lista_paises)):
            print(self.lista_paises[i].getData())