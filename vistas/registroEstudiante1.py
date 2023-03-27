from  tkinter import *
from procesos.procesosGui import *
from vistas.dialogo import *
from dao.crud import *
from archivos.archivosD import *
from dominio.entidades2 import *
class Registro:

    def __init__(self,titulo = None):
        self.crud = CrudUsuario()
        self.dlg= Dialogo()
        self.ovC = ProcesosGui()
        self.getWindow(titulo)
        self.getFrame()
        self.getLabels()
        self.getInputs()
        self.getButtons()


    def getWindow(self,titulo = None):
        self.ven = Toplevel()
        self.ven.title(titulo)
        self.ven.config(bg="navyblue")
        self.ovC.getCenter(self.ven,400,570)
        self.ven.iconbitmap(r"C:/Users/Lenovo/PycharmProjects/pythonProject1/pythonProject/Examen/descarga-_4_.ico")
        self.ven.resizable(0,0)
        #self.ven.mainloop()


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
                     bg="white", text="Registro de Estudiantes",
                     font=("Tahoma", 18)).place(x=200, y=30)
        eti2 = Label(self.marco, fg="black",
                     bg="white", text="Id_Usuario:",
                     font=("Tahoma", tam)).place(x=70, y=100)

        eti3 = Label(self.marco, fg="black",
                     bg="white", text="Numero de Matricula:",
                     font=("Tahoma", tam)).place(x=70, y=150)

        eti4 = Label(self.marco, fg="black",
                     bg="white", text="Nombre:",
                     font=("Tahoma", tam)).place(x=70, y=200)

        eti5 = Label(self.marco, fg="black",
                     bg="white", text="Apellido:",
                     font=("Tahoma", tam)).place(x=70, y=250)


    def getInputs(self):
        posX = 350
        self.id_usuarioo = Entry(self.marco, font=("Tahoma", 16),bg="lightgray")
        self.id_usuarioo.place(x=280, y=100, width=180, height=25)

        self.numero_matricula = Entry(self.marco, font=("Tahoma", 16),bg="lightgray")
        self.numero_matricula.place(x=280, y=150, width=180, height=25)
        #self.numero_matricula.config(show="")

        self.nombre = Entry(self.marco, font=("Tahoma", 16),bg="lightgray")
        self.nombre.place(x=280, y=200, width=180, height=25)

        self.apellido = Entry(self.marco, font=("Tahoma", 16),bg="lightgray")
        self.apellido.place(x=280, y=250, width=180, height=25)


    def getButtons(self):
        self.btn0 = Button(self.marco,
                           relief="flat",
                           text="Vaciar campos",
                           bg="white",
                           fg="black",
                           cursor="hand1",
                           command=self.vaciar
                           ).place(x=80, y=30, width=90)

        self.aceptar = Button(self.marco, relief="flat",
                              text="Aceptar", bg="white",
                              font=("Arial", 16), fg="black",
                              cursor="hand1",
                              command=self.grabar
                              ).place(x=150, y=290,
                                      width=110)
        self.cancelar = Button(self.marco, relief="flat",
                               text="Cancelar", bg="white",
                               font=("Arial", 16), fg="black",
                               cursor="hand1",
                               command=self.ven.destroy).place(x=300, y=290,
                                                                width=110, height=40)

    def grabar(self):
        datos=(self.id_usuarioo.get(),
               self.numero_matricula.get(),
               self.nombre.get(),
               self.apellido.get())
        msg = self.crud.insertUser("sistemaa_academico",datos)

        self.dlg.setValues("Mensaje",150,320)
        self.dlg.setMensaje(msg)
        self.dlg.getDialogo()
        self.vaciar()


    def vaciar(self):
        self.id_usuarioo.delete(0, END)
        self.numero_matricula.delete(0, END)
        self.nombre.delete(0, END)
        self.apellido.delete(0, END)