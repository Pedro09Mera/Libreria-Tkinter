from tkinter import*
from tkinter import  ttk
from procesos.procesosGui import *
from procesos.procesososD import *
from dao.crud import *
from vistas.registroEstude2 import *
from vistas.registroDatos import *
#from vistas.menuD import *
from archivos.archivosD import *


class Gestion:

    clk = 0
    nfila = [-1,-11]

    def __init__(self,obj=None):
        if obj!=None:
            self.objU= obj
        self.cont=0
        self.pos=-1
        self.cade = Cadenas()
        self.obC = ProcesosGui()
        self.crud = CrudPersonal()
        self.lista = self.crud.getAllDatos("sistemaa_academico")
        self.getWindow()
        self.getFrame()
        self.setLabel()
        self.setEntry()
        self.getButtons()
        #self.imagen()
        self.showTable(self.lista)
        self.windowAc.mainloop()



    def getWindow(self):
        self.windowAc = Tk()
        self.windowAc.title("Registro de Estudiantes")
        self.obC.getCenter(self.windowAc,400,1280)
        self.windowAc.resizable(0,0)
        self.windowAc.iconbitmap(r"C:/Users/Lenovo/PycharmProjects/pythonProject1/pythonProject/Examen/descarga-_4_.ico")
        self.windowAc.config(bg="Light sky blue")
        #c = Canvas(self.windowAc, height=350, width=1200, bg="SteelBlue4").place(x=10, y=10)

    #def imagen(self):
        #self.userphoto = PhotoImage(file="C:/Users/Lenovo/Downloads/superior.png")
        # self.etiqueta5 = Label(self.windowAc, image=self.userphoto, bg="white").place(x=900, y=10)

    def getFrame(self):
        self.marco = Frame(self.windowAc, bd=1500,bg="Navyblue")
        self.marco.pack(fill="both",expand=1)
        self.marco.config(cursor="pirate")
        self.marco.config(bd=500)
        self.marco.config(relief="sunken")

    def setLabel(self):
        self.lbl_titulo = Label (self.windowAc,
                                 fg="black",
                                 text="Datos de los Estudiantes:",
                                 bg="white",
                                 font=(12)).place(x=430, y=40)
        self.lbl_busqueda = Label(self.windowAc,
                                  fg="black",
                                  text="Ingrese la cedula:",
                                  bg="white",
                                  font=(12)).place(x=230, y=77)

    def setEntry(self):
        self.validadate1 = self.windowAc.register(self.validarCedula)
        self.cedula= Entry(self.windowAc,font=("Arial",12),bg="lightgray",validate="key",
                           validatecommand=(self.validadate1,"%d","%S","%s"))
        self.cedula.place(x=450, y=80,)

        self.user1 = Entry(self.windowAc, font=("Arial", 12))
        self.user1.place(x=450, y=80, )


    def getButtons(self):
        self.Registro = Button(self.windowAc,
                              relief="flat",
                              text="Registros",
                              bg="white",
                              font=("Arial", 16),
                              fg="black",
                              cursor="hand1",
                              command= lambda: self.registro()
                              ).place(x=450, y=330,
                                      width=110, height=40)
        self.cancelar = Button(self.windowAc,
                               relief="flat",
                               text="Cancelar",
                               bg="white",
                               font=("Arial", 16),
                               fg="black",
                               cursor="hand1",
                               command=self.windowAc.destroy
                               ).place(x=600, y=330,
                                       width=110,height=40)

        self.boton_Busqueda = Button(self.windowAc,
                                      relief="flat",
                                      text="Buscar",
                                      bg="white",
                                      fg="black",
                                      cursor="hand1",
                                      command=lambda: self.busque()
                                      )
        self.boton_Busqueda.place(x=680, y=80, width=90)


    def showTable(self, lista1=None):

        self.tabla = ttk.Treeview(self.windowAc, columns=(1, 2, 3, 4, 5, 6),
                                  show="headings", height=8)
        self.tabla.bind("<1>", self.onClick)
        vsb = ttk.Scrollbar(self.windowAc, orient="vertical",
                            command=self.tabla.yview)
        vsb.place(x=1245, y=147, height=160)
        self.tabla.configure(yscrollcommand=vsb.set)

        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure("Treeview.Heading", bg="light blue")

        self.tabla.heading(1, text="CEDULA")
        self.tabla.heading(2, text="CELULAR")
        self.tabla.heading(3, text="TIPO_SANGRE")
        self.tabla.heading(4, text="DISCAPACIDAD")
        self.tabla.heading(5, text="DIRRECION")
        self.tabla.heading(6, text="CORREO")


        self.tabla.column(1, anchor=CENTER)
        self.tabla.column(2, anchor=CENTER)
        self.tabla.column(3, anchor=CENTER)
        self.tabla.column(4, anchor=CENTER)
        self.tabla.column(5, anchor=CENTER)
        self.tabla.column(6, anchor=CENTER)

        for i in range(len(lista1)):
            self.tabla.insert("", "end", values=(lista1[i].cedula,
                                                 lista1[i].celular,
                                                 lista1[i].tipo_sangre,
                                                 lista1[i].discapacidad,
                                                 lista1[i].dirrecion,
                                                 lista1[i].correo
                                                 ))
        self.tabla.place(x=55, y=120)


    def onClick(self,event):

        item = event.widget.identify("item", event.x,event.y)
        text = self.cade.getCadena(item)

        if text!='':
            Gestion.clk +=1
            self.pos = int(text)
            print(self.pos)
            if Gestion.clk == 1:
                Gestion.nfila[0] = self.pos
            if Gestion.clk ==2:
                Gestion.nfila[1] = self.pos
                Gestion.clk = 0
            if Gestion.clk ==0 and Gestion.nfila[1] ==Gestion.nfila[0]:
                #print("the text is" + text,self.pos, self.lista[pos-1].cedula)
                fr = Edicion(self.lista[self.pos -1])
                #print("ventana cargada")

        else:
            Gestion.clk = 0


    def validarCedula(self,accion,car,texto):
        if accion!="1":
            return True
        return car in "1234567890" and len(texto)<10


    def busque(self):
        datos=(self.user1.get(),)
        #print(self.pos, "tabla 2")
        obj = self.crud.getDatos("sistemaa_academico",datos)
        #print(obj.getData())
        self.lista1=[]
        #lista1=[]
        if obj!=None:
            self.cont+=1
            self.lista1.append(obj)
            self.lista=self.lista1
            self.showTable(self.lista1)
            self.user1.delete(0,END)
        else:
            self.lista1= self.crud.getAllDatos("sistemaa_academico")
            self.showTable(self.lista1)


    def registro(self):
        fres = NewDatos(self.objU)



#bg= Gestion()