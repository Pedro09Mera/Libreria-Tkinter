#  Proyecto: Registro de sistema estudiantil
#  Empresa:  Pedro Mera
# Proceso: registro
# Recursos:Pedro Mera//
from tkinter import *
from procesos.procesosGui import *
from vistas.dialogo import *
from dao.crud import *


class NewDatos:

    def __init__(self,obj = None):
        titulo=""
        if obj!=None:
            self.objU = obj
            titulo="id_usuario"+obj.nombre
            #self.activate("normal",NORMAL)
            #self.cargarDatos(obj)
        self.crud = CrudPersonal()
        self.dlg = Dialogo()
        self.ovC = ProcesosGui()
        self.getWindow(titulo)
        self.getFrame()
        self.getLabels()
        self.getInpunts()
        self.getButtons()
        #self.ven.mainloop()


    def getWindow(self,titulo = None):
        self.ven = Toplevel()
        self.ven.title(titulo)
        self.ovC.getCenter(self.ven,570,720)
        self.ven.iconbitmap(r"C:/Users/Lenovo/PycharmProjects/pythonProject1/pythonProject/Examen/descarga-_4_.ico")
        self.ven.resizable(0,0)
        #self.ven.geometry("870x450")


    def getFrame(self):
        self.marco = Frame(self.ven, bd=15, bg="#8DA6CE")
        self.marco.pack(fill="both", expand=1)
        self.marco.config(cursor="pirate")
        self.marco.config(bd=50)
        self.marco.config(relief="groove")


    def getLabels(self):
        posX = 120
        tam = 15
        eti1 = Label(self.marco, fg="black",
                     bg="white", text="Registro de Estudiantes",
                     font=("Tahoma", 18)).place(x=170, y=30)
        eti2 = Label(self.marco, fg="black",
                     bg="white", text="Cedula:",
                     font=("Tahoma", tam)).place(x=70, y=100)

        eti3 = Label(self.marco, fg="black",
                     bg="white", text="Celular:",
                     font=("Tahoma", tam)).place(x=70, y=150)

        eti4 = Label(self.marco, fg="black",
                     bg="white", text="Tipo de Sangre:",
                     font=("Tahoma", tam)).place(x=70, y=200)

        eti5 = Label(self.marco, fg="black",
                     bg="white", text="Discapacidad:",
                     font=("Tahoma", tam)).place(x=70, y=250)

        eti5 = Label(self.marco, fg="black",
                     bg="white", text="Direccion:",
                     font=("Tahoma", tam)).place(x=70, y=300)

        eti6 = Label(self.marco, fg="black",
                     bg="white", text="Correo:",
                     font=("Tahoma", tam)).place(x=70, y=350)


    def getInpunts(self):
        posX = 350

        self.validadate1 = self.marco.register(self.validarCedula)
        self.cedula = Entry(self.marco, font=("Arial", 12),bg="lightgray", validate="key",
                            validatecommand=(self.validadate1, "%d", "%S", "%s"))
        self.cedula.place(x=280, y=100, width=180, height=25 )

        self.celular = Entry(self.marco, font=("Tahoma", 16),bg="lightgray")
        self.celular.place(x=280, y=150, width=180, height=25)

        self.tipo_sangre = Entry(self.marco, font=("Tahoma", 16),bg="lightgray")
        self.tipo_sangre.place(x=280, y=200, width=180, height=25)

        self.discapacidad = Entry(self.marco, font=("Tahoma", 16),bg="lightgray")
        self.discapacidad.place(x=280, y=250, width=180, height=25)

        self.dirrecion = Entry(self.marco, font=("Tahoma", 16),bg="lightgray")
        self.dirrecion.place(x=280, y=300, width=180, height=25)

        self.correo = Entry(self.marco, font=("Tahoma", 16),bg="lightgray")
        self.correo.place(x=280, y=350, width=180, height=25)


    def getButtons(self):
        self.boton = Button(self.marco,
                            relief="flat",
                            text="Eliminar",
                            bg="white",
                            fg="black",
                            cursor="hand1",
                            command=self.vaciarDatos
                            ).place(x=490, y=30, width=90)

        self.aceptar = Button(self.marco, relief="flat",
                              text="Registrar", bg="white",
                              font=("Arial", 16), fg="black",
                              cursor="hand1",
                              command=self.grabar
                              )
        self.aceptar.place(x=150, y=410,
                           width=130)

        self.cancelar = Button(self.marco, relief="flat",
                               text="Cancelar", bg="white",
                               font=("Arial", 16), fg="black",
                               cursor="hand1",
                               command=self.ven.destroy).place(x=300, y=410,
                                                               width=130)

        self.buscar = Button(self.marco, relief="flat",
                             text="buscar", bg="white",
                             font=("Arial",16), fg="black",
                             cursor="hand1",
                             command=self.getID
                             )
        self.buscar.place(x=490, y=95, width=90,height=30)


    def grabar(self):
        msg= ""
        datos = (self.cedula.get(),
                 self.celular.get(),
                 self.tipo_sangre.get(),
                 self.discapacidad.get(),
                 self.dirrecion.get(),
                 self.correo.get(),self.objU.id_usuario
                 ,'A')
        #print(datos)
        msg = self.crud.insertDatos("sistemaa_academico",datos)

        self.dlg.setValues("Mensaje", 150,320)
        self.dlg.setMensaje(msg)
        self.dlg.getDialogo()
        self.vaciarDatos()


    def vaciarDatos(self):
        self.cedula.delete(0, END)
        self.celular.delete(0,END)
        self.tipo_sangre.delete(0, END)
        self.discapacidad.delete(0, END)
        self.dirrecion.delete(0, END)
        self.correo.delete(0, END)


    def validarCedula(self,accion,car,texto):
        if accion!="1":
            return True
        return car in "01234567890" and len(texto)<10


    def getID(self):
        datos =(self.cedula.get(),)
        obj = self.crud.getDatos("sistemaa_academico",datos)
        if obj!= None:
            self.dlg.setValues("Mensaje", 150,320)
            self.dlg.setMensaje("Cedula ya existe! ")
            self.dlg.getDialogo()
        else:
            self.dlg.setValues("Mensaje", 150, 320)
            self.dlg.setMensaje("Cedula Disponible! ")
            self.dlg.getDialogo()