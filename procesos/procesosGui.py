from tkinter import *


class ProcesosGui:

    def getCenter(self,obv,altura,ancho):
        window_height = altura
        window_width = ancho
        screen_width = obv.winfo_screenwidth()
        screen_height = obv.winfo_screenheight()
        x_cordinate = int((screen_width/2)-(window_width/2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        obv.geometry("{}x{}+{}+{}".format(window_width,window_height,
                                                x_cordinate,y_cordinate))