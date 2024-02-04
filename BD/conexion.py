import mysql.connector
from mysql.connector import Error


class ConexionMysql:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host = "localhost",
                port = "3306",
                user = "root",
                password = "sandro12352*",
                db = "proyectorqs"
            )
            print("Conexion correcta...")
        except Error as ex:
            print("Fallo la conexion ",ex)


    def traerDatos(self):
        if self.conexion.is_connected:
            try:
                cursor = self.conexion.cursor()
                sql = "SELECT * FROM USUARIOS "
                cursor.execute(sql)
                datos = cursor.fetchall()
                for dato in datos:
                    print(dato)
                return datos
            except Error as ex:
                print("Error es : ",ex)


    def listarMatricula(self):
        if self.conexion.is_connected:
            try:
                cursor = self.conexion.cursor()
                sql = "SELECT * FROM MATRICULAS ORDER BY codigo DESC"
                cursor.execute(sql)
                datos = cursor.fetchall()
                return datos
            except Error as ex:
                print("Error es : ",ex)

    def agregarUsuario(self,usuario):   
        if self.conexion.is_connected:
            try:
                cursor = self.conexion.cursor()
                sql = f"INSERT INTO usuarios (username,contraseña) values('{usuario[0]}','{usuario[1]}')"
                cursor.execute(sql)
                self.conexion.commit()
            except Error as ex:
                print("Error es : ",ex)

    def listarAlumnos(self):
        if self.conexion.is_connected:
            try:
                cursor = self.conexion.cursor()
                sql = "SELECT * FROM alumnos "
                cursor.execute(sql)
                datos = cursor.fetchall()
                return datos
            
            except Error as ex:
                print("Error es : ",ex)





        

