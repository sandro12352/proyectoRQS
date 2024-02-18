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

    def listarUsuarios(self):
            self.conexion = mysql.connector.connect(
                host = "localhost",
                port = "3306",
                user = "root",
                password = "sandro12352*",
                db = "proyectorqs"
            )
            try:
                cursor = self.conexion.cursor()
                sql = "SELECT * FROM USUARIOS"
                cursor.execute(sql)
                datos = cursor.fetchall()               
                return datos
                
            except Error as ex:
                print("Error es : ",ex)

    def agregarUsuario(self,username,contraseña):   
        if self.conexion.is_connected:
            try:
                cursor = self.conexion.cursor()
                sql = f"INSERT INTO usuarios (username,contraseña) values('{username}','{contraseña}')"
                cursor.execute(sql)
                self.conexion.commit()
                cursor.close()
                
            except Error as ex:
                print("Error es : ",ex)

    def actualizarUsuarios(self,id,nuevaContraseña):
        if self.conexion.is_connected:
            try:
                cursor = self.conexion.cursor()
                sql = f"UPDATE USUARIOS set contraseña={nuevaContraseña} where id ={id}"
                cursor.execute(sql)
                self.conexion.commit()
                cursor.close()
            except Error as ex:
                print("Error es : ",ex)

            
    def listarMatricula(self):
        if self.conexion.is_connected:
            try:
                cursor = self.conexion.cursor()
                sql = "SELECT * FROM MATRICULAS"
                cursor.execute(sql)
                datos = cursor.fetchall()
                return datos
            except Error as ex:
                print("Error es : ",ex)

    

    def listarAlumnos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "SELECT * FROM alumnos "
                cursor.execute(sql)
                datos = cursor.fetchall()
                return datos
            
            except Error as ex:
                print("Error es : ",ex)


    def registrarAlumno(self,nombres,apellidos,nombre_padre,nombre_madre,dni,telefono,direccion):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = f"INSERT INTO alumnos (nombres,apellidos,nombre_padre,nombre_madre,dni,telefono,direccion) values ('{nombres}','{apellidos}','{nombre_padre}','{nombre_madre}','{dni}','{telefono}','{direccion}')"
                cursor.execute(sql)
                self.conexion.commit()
                self.listarAlumnos()
                cursor.close()

            
            except Error as ex:
                print("Error es : ",ex)



