from tkinter import *

from procesos.procesosGui import *


class Dialogo:

    def __init__(self,nombre=None):
        self.dlC = ProcesosGui()
        #self.getWindow(nombre)
        self.titulo=""
        self.altura=0
        self.ancho=0
        self.__mensaje =""
        #self.imagen()
        #self.dialogo.mainloop()

    #def getWindow(self,nombre):
        #self.ventana = Tk()
        #self.ventana.iconbitmap(r"C:/Users/Lenovo/PycharmProjects/pythonProject1/pythonProject/Examen/descarga-_4_.ico")


    def setValues(self,titulo,altura,ancho):
        self.titulo=titulo
        self.altura=altura
        self.ancho=ancho

    def setMensaje(self,msg):
        self.__mensaje=msg

    def getMensaje(self):
        return self.__mensaje

    def getDialogo(self):
        self.dialogo = Toplevel()
        self.dlC.getCenter(self.dialogo,self.altura,self.ancho)
        self.dialogo.title(self.titulo)
        self.dialogo.resizable(0,0)
        self.dialogo.config(bg ="purple")
        lb1 = Label(self.dialogo,text=self.__mensaje,font=("Arial",18),fg="black",
                    bg="purple").place(x=50,y=30)
        self.btn1 = Button(self.dialogo,relief="flat",
                           text="Aceptar",
                           bg="purple ",
                           fg="black",
                           cursor="circle",
                           command=self.dialogo.destroy).place(x=100,y=100,width=90)
