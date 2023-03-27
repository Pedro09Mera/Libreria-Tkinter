from tkinter import *
from procesos.procesosGui import *
from vistas.dialogo import *
from dao.crud import *
from PIL import Image

class Software:

    def __init__(self,obj = None):
        self.crud = CrudPersonal()
        self.dlg = Dialogo()
        self.ovC = ProcesosGui()
        self.getWindow()
        self.getFrame()
        self.imagen()
        self.ven.mainloop()

    def getWindow(self,titulo = None):
        self.ven =Toplevel()
        self.ven.title("TECNOLOGIA EN DESARROLLO DE SOWTWARE")
        self.ovC.getCenter(self.ven,480,600)
        self.ven.iconbitmap(r"C:/Users/Lenovo/PycharmProjects/pythonProject1/pythonProject/Examen/descarga-_4_.ico")
        self.ven.config(bg="navy blue")
        #self.ven.resizable(0,0)
        self.ven.geometry("700x700")

    def imagen(self):
        self.userphoto=PhotoImage(file=r"C:/Users/Lenovo/OneDrive/Documentos/OneDrive/Escritorio/Desarrollo (1).png")
        self.etiqueta5 = Label(self.ven, image=self.userphoto, bg="white").place(x=50, y=60,width=1335, height=700)


    def getFrame(self):
        self.marco = Frame(self.ven, bd=1500, bg="Navyblue")
        self.marco.pack(fill="both", expand=1)
        self.marco.config(cursor="pirate")
        self.marco.config(bd=500)
        self.marco.config(relief="sunken")

