#  Proyecto: Registro de sistema estudiantil
#  Empresa:  Pedro Mera
# Proceso: Login de inicio de seccion con tkinder
# Recursos:Pedro Mera//

import tkinter
from tkinter import *
from vistas.dialogo import *
from vistas.registroEstudiante1 import *
from vistas.registroEstude2 import *
from procesos.procesosGui import*
from vistas.meduD import *
from dao.crud import *


class Login:

    def __init__(self,nombre=None):
        self.crud= CrudUsuario()
        self.ovC = ProcesosGui()
        self.cont =0
        self.msg = ""
        self.getWindow(nombre)
        self.getFrame()
        self.getButtons()
        self.getLabels()
        self.getInputs()
        self.imagen()
        self.ventana.mainloop()

    def getWindow(self, nombre):
        self.ventana = Tk()
        self.ovC.getCenter(self.ventana,480,600)
        self.ventana.config(bg="Navy blue")
        self.ventana.title("INSTITUTO SUPERIOR TECNOLOGICO GUAYAQUIL")
        self.ventana.geometry("600x540")
        self.ventana.iconbitmap("C:/Users/Lenovo/PycharmProjects/pythonProject1/pythonProject/Examen/descarga-_4_.ico")
        self.ventana.resizable(0,0)


    def imagen(self):
        self.userphoto=PhotoImage(file="C:/Users/Lenovo/PycharmProjects/pythonProject1/pythonProject/Examen/istg.png")
        self.etiqueta5 = Label(self.ventana, image=self.userphoto, bg="white").place(x=170, y=30)


    def getFrame(self):
        self.marco = Frame(self.ventana, bd=1500,bg="Navy blue")
        self.marco.pack(fill="both",expand=1)
        self.marco.config(cursor="pirate")
        self.marco.config(bd=500)
        self.marco.config(relief="groove")

#fgvbdfh
    def getLabels(self):
        eti1 = Label(self.ventana,fg="black",bg="white",text="ID_USUARIO",
                     font=("Arial",18)).place(x=40,y=300)
        eti2 = Label(self.ventana,fg="black",bg="white",text="N°MATRICULA",
                     font=("Arial",18)).place(x=40,y=350)
        self.eti3 = Label(self.ventana,fg="black",bg="blue",text="",
                     font=("Arial",18))
        self.eti3.place(x=150,y=280)


    def getInputs(self):
        self.id_usuario = Entry(self.ventana,font=("Arial",18),bg="lightgray")
        self.id_usuario.place(x=250,y=300)
        self.numero_matricula = Entry(self.ventana,font =("Arial",18),bg="lightgray")
        self.numero_matricula.place(x=250,y=350)
        self.numero_matricula.config(show="")


    def getButtons(self):

        self.acceder = Button(self.ventana,
                              relief="flat",
                              text="ACCEDER",
                              bg="white",
                              font=("Arial", 16),
                              fg="black",
                              cursor="circle",
                              command=self.accion1
                              ).place(x=100, y=400,
                                      width=130, height=40)
        self.cancelar = Button(self.ventana,
                               relief="flat",
                               text="CANCELAR",
                               bg="white",
                               font=("Arial", 16),
                               fg="black",
                               cursor="hand1",
                               command=self.ventana.destroy
                               ).place(x=350, y=400,
                                       width=130, height=40)

        self.registrar = Button(self.ventana,
                                relief="flat",
                                text="Registrar a Estudiantes",
                                bg="white",
                                font=("Arial", 18),
                                fg="black",
                                cursor="hand1",
                                command=self.accion2
                                ).place(x=170, y=470,
                                        width=255, height=50)


    def accion1(self):
        self.dlg1 = Dialogo()
        self.dlg1.setValues("Logueo", 150, 250)
        clave2 = (self.id_usuario.get(), self.numero_matricula.get())
        obj1 = self.crud.getLogin("sistemaa_academico", clave2)
        if obj1 != None:
            self.ventana.destroy()
            obj = MenuApp(obj1)
        else:
            self.msg = "Usuario incorrecto!"
            self.eti3['text'] = self.msg
            self.dlg1.setValues("Logueo", 150, 300)
            self.dlg1.setMensaje("Usuario incorrecto")
            self.dlg1.getDialogo()

    def accion2(self):
        ven1 =Registro ("Registro de usuarios.")
        #arc = Dialogo("Registro de usuario")
        # self.ventana.destroy()



obj=Login()

#Hola a todoss putos xd

