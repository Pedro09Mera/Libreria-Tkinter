#  Proyecto: Reewgistro de estudiante
#  Empresa:  Pedro Mera
# Proceso: Crud correspondiente
# Recursos:Pedro Mera//

from dominio.entidades2 import *
from dao.conexion import *
import mysql.connector as mc

#class Crud:

    #def __init__(self):
        #self.con = Conexion()

    #def getAllProducto(self,base,query):
        #lista = []
        #cone = self.con.conectar(base)
        #cursor1 = cone.cursor()
        #cursor1.execute(query)
        #tupla = cursor1.fetchall()
        #for i in range(len(tupla)):
            #obj = Producto(tupla[i][0],tupla[i][1],tupla[i][2],tupla[i][3])
            #lista.append(obj)
        #cone.close()
        #return  lista


class CrudUsuario:

    def __init__(self):
        self.con = Conexion()


    def insertUser(self,base,datos):
        msg = ""
        try:
            cone= self.con.conectar(base)
            cursor1 = cone.cursor()
            sql ="insert into usuario(id_usuario,numero_matricula,nombre,apellido) "+\
            "values(%s,%s,%s,%s)"
            cursor1.execute(sql,datos)
            cone.commit()
            cone.close()
            msg = str(cursor1.rowcount) + " resgistro(s) afectados."
        except(mc.IntegrityError) as ex:
            msg = str(ex)
        return msg


    def getLogin(self,base,clave):

        obj=None
        sql="select * from usuario where id_usuario=%s and numero_matricula=%s"
        cone = self.con.conectar(base)
        cursor1= cone.cursor()
        cursor1.execute(sql,clave)
        tupla = cursor1.fetchall()
        cone.close()
        if len(tupla)!=0:
            obj=Usuario(tupla[0][0],tupla[0][1],tupla[0][2],tupla[0][3])
        return obj


    def validateUser(self,base,clave):

        obj=None
        sql="select * from usuario where id_usuario=%s"
        cone = self.con.conectar(base)
        cursor1= cone.cursor()
        cursor1.execute(sql,clave)
        tupla = cursor1.fetchall()
        cone.close()
        if len(tupla)!=0:
            obj=Usuario(tupla[0][0],tupla[0][1],tupla[0][2],tupla[0][3])
        return obj


    def getAllUsers(self,base):

        lista=[]
        cone = self.con.conectar(base)
        cursor1= cone.cursor()
        query1= "select * from id_usuario order by nombre"
        cursor1.execute(query1)
        result = cursor1.fetchall()
        for i in range(len(result)):
            obj= Usuario(result[i][0],result[i][1],result[i][2],
                         result[i][3])
            lista.append(obj)
        cone.close()
        return lista


    def updateUser(self,base,datos):
        msg = ""
        try:
            cone = self.con.conectar(base)
            cursor1 = cone.cursor()
            sql = "update id_usuario set numero_matricula =%s,nombre=%s,apellido=%s " + \
                  "where id_usuario=%s"
            cursor1.execute(sql, datos)
            cone.commit()
            cone.close()
            msg = str(cursor1.rowcount) + " resgistro(s) afectados."

        except(mc.IntegrityError) as ex:
            msg = str(ex)

            return msg


    def deleteDatos(self,base,clave):
        msg = ""
        try:
            cone= self.con.conectar(base)
            cursor1 = cone.cursor()
            sql ="delete from usuario where id_usuario=%s"
            cursor1.execute(sql,clave)
            cone.commit()
            cone.close()
            msg = str(cursor1.rowcount) + " resgistro(s) afectados."
        except(mc.IntegrityError) as ex:
            msg = str(ex)
        return msg


    def updateDatos(self,base,datos):
        msg = ""
        try:
            cone= self.con.conectar(base)
            cursor1 = cone.cursor()
            sql ="update datos_estudiantes set celular=%s,tipo_sangre=%s,discapacidad=%s,dirrecion=%s,correo=%s where cedula=%s"
            cursor1.execute(sql,datos)
            cone.commit()
            cone.close()
            msg = str(cursor1.rowcount) + " resgistro(s) afectados."
        except(mc.IntegrityError) as ex:
            msg = str(ex)
        return msg


class CrudPersonal:

    def __init__(self):
        self.con = Conexion()

    def insertDatos(self,base,datos):
        msg = ""
        try:
            cone= self.con.conectar(base)
            cursor1 = cone.cursor()
            sql ="insert into datos_estudiantes(cedula,celular,tipo_sangre,discapacidad,dirrecion,correo,id_usuarioo,estado_matricula) "+\
            "values(%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor1.execute(sql,datos)
            cone.commit()
            cone.close()
            msg = str(cursor1.rowcount) + " resgistro(s) afectados."
        except(mc.IntegrityError) as ex:
            msg = str(ex)
        return msg


    def getDatos(self,base,clave):

        obj=None
        sql="select * from datos_estudiantes where cedula=%s"
        cone = self.con.conectar(base)
        cursor1= cone.cursor()
        cursor1.execute(sql,clave)
        tupla = cursor1.fetchall()
        cone.close()
        if len(tupla)!=0:
            obj= Datos(tupla[0][0],tupla[0][1],tupla[0][2],tupla[0][3],
                         tupla[0][4],tupla[0][5],tupla[0][6],tupla[0][7])
        return obj



    def getAllDatos(self,base):
        lista=[]
        cone = self.con.conectar(base)
        cursor1= cone.cursor()
        query1= "select * from datos_estudiantes where estado_matricula = 'A' order by cedula"
        cursor1.execute(query1)
        result = cursor1.fetchall()
        for i in range(len(result)):
            obj= Datos(result[i][0],result[i][1],result[i][2],
                         result[i][3],result[i][4],result[i][5],
                          result[i][6],result[i][7])
            lista.append(obj)
        cone.close()
        return lista


    def deletePerson(self,base,clave):
        msg = ""
        try:
            cone= self.con.conectar(base)
            cursor1 = cone.cursor()
            sql ="update  datos_estudiantes set estado_matricula='I' where cedula=%s"
            cursor1.execute(sql,clave)
            cone.commit()
            cone.close()
            msg = str(cursor1.rowcount) + " resgistro(s) afectados."
        except(mc.IntegrityError) as ex:
            msg = str(ex)
        return msg





#class CrudEstudiante:

    #def __init__(self):
        #self.conectar = Conexion()

    #def resultProcedure(self,base,nom_proceso,parametros):
        #conectar = self.conectar.conectar(base)
        #cursor = conectar.cursor()
        #resul = cursor.callproc(nom_proceso,parametros)
        #conectar.commit()
        #conectar.close()
        #return resul

#def estudiante():
    #cre = CrudEstudiante()
    #primer_parcial = input("primer parcial: ")
    #segundo_parcial = input("segundo parcial:")
    #examen = input("examen: ")
    #parametros = (primer_parcial, segundo_parcial, examen, None, None, None,"PYTHON")
    #parametros = cre.resultProcedure("sistemaa_academico", "promedio", parametros)
    #print("resultado:"), parametros[6]
    #print("mensaje: "), parametros[7]
    #print("total:"), parametros[8]
    #print("estado"), parametros[9]
