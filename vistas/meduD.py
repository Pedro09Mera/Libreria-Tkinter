#  Proyecto: Registro de sistema estudiantil
#  Empresa:  Pedro Mera
# Proceso: menu
# Recursos:Pedro Mera//

import tkinter
from tkinter import *
from procesos.procesosGui import *
from vistas.registroDatos import *
from vistas.gestionDEestudiante import *
from vistas.diseño_grafico import *
from vistas.carr_sotware import *
from vistas.marketing import *


class MenuApp:

    def __init__(self,obj= None ):
        titulo=""
        if obj !=None :
            self.objU = obj
            titulo = "id_Usuario: "+obj.nombre+"."
        self.obc = ProcesosGui()
        self.getWindow(titulo)
        self.getFrame()
        self.getMenu()
        self.imagen()
        self.ventana.mainloop()


    def getWindow(self,titulo=None):
        self.ventana = Tk()
        self.obc.getCenter(self.ventana,360,900)
        self.ventana.title(titulo)
        self.ventana.resizable(0,0)
        self.ventana.config(bg="navy blue")
        self.ventana.iconbitmap(r"C:/Users/Lenovo/PycharmProjects/pythonProject1/pythonProject/Examen/descarga-_4_.ico")


    def imagen(self):
        self.userphoto = PhotoImage(file="C:/Users/Lenovo/Downloads/logo.png")
        self.etiqueta5 = Label(self.ventana, image=self.userphoto, bg="white").place(x=10, y=10)


    def getFrame(self):
        self.marco = Frame(self.ventana, bd=1500,bg="Navy blue")
        self.marco.pack(fill="both",expand=1)
        self.marco.config(cursor="pirate")
        self.marco.config(bd=500)
        self.marco.config(relief="groove")


    def getMenu(self):
        self.menuP = Menu(self.ventana)
        self.ventana.config(menu=self.menuP)
        self.item1 = Menu(self.menuP)
        self.menuP.add_cascade(label="ARCHIVO", menu=self.item1)
        self.item1.add_command(label="REGISTRAR DATOS", command=self.registroE)
        self.item1.add_command(label="GESTION DE ESTUDINATE", command=self.gestionE)
        self.item1.add_separator()
        #self.item1.add_command(label="Factura", command=self.factura)
        self.item1.add_command(label="SALIR", command=self.ventana.destroy)
        # 2da cascada
        self.item2 = Menu(self.menuP)
        self.menuP.add_cascade(label="OFERTA ACADEMICA", menu=self.item2)
        self.item2.add_command(label="TECNOLOGIA EN DESARROLLO DE SOFWARE", command=self.sofware)
        self.item2.add_command(label="TEGNOLOGIA EN DISEÑO GRAFICO", command=self.grafico)
        self.item2.add_command(label="TEGNOLOGIA SUPERIOR EN MARKETING", command=self.marketing)
        #self.item2.add_command(label="REGISTAR CARRERA", command=self.registro)

        # 3da cascada

        #self.item3 = Menu(self.menuP)
        #self.menuP.add_cascade(label="Editar",menu=self.item3)
        #self.item3.add_command(label="copiar", command=self.copiar)

    def registroE(self):
        reg = NewDatos(self.objU)

    def gestionE(self):
        reg = Gestion(self.objU)

    def sofware(self):
        cs = Software()

    def grafico(self):
        ofa = Grafico()

    def marketing(self):
        carr = Marketing()
        #carr = Marketing()



    #def registro(self):
      #  pass

#obr = MenuApp()