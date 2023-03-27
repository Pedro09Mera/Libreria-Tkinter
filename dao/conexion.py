#  Proyecto: Reewgistro de estudiante
#  Empresa:  Pedro Mera
# Proceso: conexion a la base de datos
# Recursos:Pedro Mera//
import mysql
import mysql.connector as mc

class Conexion:

    def conectar(self,base):
        credenciales = {
            "host" : "localhost",
            "port" : "3306",
            "user" : "root",
            "password" : "root1234",
            "database" : base,
            "auth_plugin":'mysql_native_password'
        }
        cone = mysql.connector.connect(**credenciales)
        return  cone


obc = Conexion()
print(obc.conectar("sistemaa_academico"))