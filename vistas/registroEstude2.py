from tkinter import *
from procesos.procesosGui import *
from vistas.dialogo import *
from dao.crud import *
from archivos.archivosD import *




class Edicion:

    def __init__(self,obj = None):
        titulo=""
        self.crud = CrudUsuario()
        self.dlg = Dialogo()
        self.ovC = ProcesosGui()
        self.getWindow()
        self.getFrame()
        self.getLabels()
        self.getInpunts()
        self.getButtons()
        if obj!=None:
            self.objU = obj
            self.cedula.insert(0, obj.cedula)
            self.cedula['state'] = "disabled"
            titulo = "id_Usuarioo:" + obj.celular + " " + obj.tipo_sangre + "."
            self.cargarDatos(obj)


    def getWindow(self,titulo = None):
        self.ven = Toplevel()
        self.ven.title(titulo)
        self.ovC.getCenter(self.ven,350,350)
        self.ven.resizable(0,0)
        self.ven.iconbitmap(r"C:/Users/Lenovo/PycharmProjects/pythonProject1/pythonProject/Examen/descarga-_4_.ico")
        self.ven.geometry("820x490")


    def getFrame(self):
        self.marco = Frame(self.ven, bd=10, bg="#8DA6CE")
        self.marco.pack(fill="both", expand=1)
        self.marco.config(cursor="pirate")
        self.marco.config(bd=40)
        self.marco.config(relief="sunken")


    def getLabels(self):
        posX = 120
        tam = 15
        eti1 = Label(self.marco, fg="black",
                     bg="white", text="Registro de Estudiante.",
                     font=("Tahoma", 18)).place(x=220, y=30)
        eti2 = Label(self.marco, fg="black",
                     bg="white", text="Cedula:",
                     font=("Tahoma", tam)).place(x=posX, y=100)

        eti3 = Label(self.marco, fg="black",
                     bg="white", text="Celular:",
                     font=("Tahoma", tam)).place(x=posX, y=150)

        eti4 = Label(self.marco, fg="black",
                     bg="white", text="Tipo de Sangre:",
                     font=("Tahoma", tam)).place(x=posX, y=200)

        eti5 = Label(self.marco, fg="black",
                     bg="white", text="Discapacidad:",
                     font=("Tahoma", tam)).place(x=posX, y=250)

        eti5 = Label(self.marco, fg="black",
                     bg="white", text="Direccion:",
                     font=("Tahoma", tam)).place(x=posX, y=300)

        eti6 = Label(self.marco, fg="black",
                     bg="white", text="Correo:",
                     font=("Tahoma", tam)).place(x=posX, y=350)


    def getInpunts(self):
        posX = 350

        self.cedula = Entry(self.marco, font=("Arial", 12),bg="lightgray")
        self.cedula.place(x=posX, y=100, width=180, height=25)

        self.celular = Entry(self.marco, font=("Tahoma", 16),bg="lightgray")
        self.celular.place(x=posX, y=150, width=180, height=25)

        self.tipo_sangre = Entry(self.marco, font=("Tahoma", 16),bg="lightgray")
        self.tipo_sangre.place(x=posX, y=200, width=180, height=25)

        self.discapacidad = Entry(self.marco, font=("Tahoma", 16),bg="lightgray")
        self.discapacidad.place(x=posX, y=250, width=180, height=25)

        self.dirrecion = Entry(self.marco, font=("Tahoma", 16),bg="lightgray")
        self.dirrecion.place(x=posX, y=300, width=180, height=25)

        self.correo = Entry(self.marco, font=("Tahoma", 16),bg="lightgray")
        self.correo.place(x=posX, y=350, width=180, height=25)


    def getButtons(self):
        self.buscar = Button(self.marco, relief="flat",
                             text="Eliminar", bg="white",
                             font=("Arial", 16), fg="black",
                             cursor="hand1"
                             , command=self.eliminar
                             )
        self.buscar.place(x=550, y=95, width=90, height=30)

        self.aceptar = Button(self.marco, relief="flat",
                              text="Actualizar", bg="white",
                              font=("Arial", 16), fg="black",
                              cursor="hand1",
                              command=self.grabar
                              )
        self.aceptar.place(x=250, y=380,
                           width=110,height=40)
        self.cancelar = Button(self.marco, relief="flat",
                               text="Cancelar", bg="white",
                               font=("Arial", 16), fg="black",
                               cursor="hand1",
                               command=self.ven.destroy).place(x=400, y=380,
                                                               width=110, height=40)

    def grabar(self):
        msg = ""
        datos = (
            #self.cedula.get(),
            self.celular.get(),
            self.tipo_sangre.get(),
            self.discapacidad.get(),
            self.dirrecion.get(),
            self.correo.get(), self.cedula.get())
        msg = self.crud.updateDatos("sistemaa_academico", datos)
        self.dlg.setValues("Mensaje", 150, 320)
        self.dlg.setMensaje(msg)
        self.dlg.getDialogo()


    def eliminar(self):
        datos=(self.cedula.get(),)
        msg = self.crud.deleteDatos("sistemaa_academico",datos)
        self.activate("disabled",DISABLED)
        self.dlg.setValues("Mensaje", 150, 250)
        self.dlg.setMensaje("Registro existoso")
        self.dlg.getDialogo()


    def cargarDatos(self, obj):
        # self.vaciar()
        # self.cedula.insert(0, obj.cedula)
        self.cedula.insert(0, obj.cedula)
        self.celular.insert(0, obj.celular)
        self.tipo_sangre.insert(0, obj.tipo_sangre)
        self.discapacidad.insert(0, obj.discapacidad)
        self.dirrecion.insert(0, obj.dirrecion)
        self.correo.insert(0, obj.correo)


    def activate(self, estado, estadoB):
        self.cedula['state'] = estado
        self.celular['state'] = estado
        self.tipo_sangre['state'] = estado
        self.discapacidad['state'] = estado
        self.dirrecion['state'] = estado
        self.correo['state'] = estado
        self.aceptar.config(state=estadoB)