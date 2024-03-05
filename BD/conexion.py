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



    def listarEmpleados(self):
            self.conexion = mysql.connector.connect(
                host = "localhost",
                port = "3306",
                user = "root",
                password = "sandro12352*",
                db = "proyectorqs"
            )
            try:
                cursor = self.conexion.cursor()
                sql = "SELECT * FROM empleados"
                cursor.execute(sql)
                datos = cursor.fetchall()             
                return datos
                
            except Error as ex:
                print("Error es : ",ex)

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

    def agregarUsuario(self,objUsuario,id_empleado):  
        self.conexion = mysql.connector.connect(
                host = "localhost",
                port = "3306",
                user = "root",
                password = "sandro12352*",
                db = "proyectorqs"
            ) 
        if self.conexion.is_connected:
            try:
                cursor = self.conexion.cursor()
                sql = f"INSERT INTO usuarios (username,contraseña,idEmpleadoUsuario) values('{objUsuario.getUsername()}','{objUsuario.getContraseña()}',{id_empleado})"
                cursor.execute(sql)
                self.conexion.commit()
                cursor.close()
                
            except Error as ex:
                print("Error es : ",ex)
    

    

    def agregarEmpleados(self,objEmpleado):
            self.conexion = mysql.connector.connect(
                host = "localhost",
                port = "3306",
                user = "root",
                password = "sandro12352*",
                db = "proyectorqs"
            ) 
            try:
                cursor = self.conexion.cursor()
                sql = f"INSERT INTO empleados (nombres,apellidos,dni,cargo) values('{objEmpleado.getNombresEmpleado()}','{objEmpleado.getApellidosEmpleado()}','{objEmpleado.getDniEmpleado()}','{objEmpleado.getCargoEmpleado()}')"
                cursor.execute(sql)
                id_empleado = cursor.lastrowid
                self.conexion.commit()                
                cursor.close()
                return id_empleado
               
            except Error as ex:
                print("Error es : ",ex)

    def actualizarUsuarios(self,id,nuevaContraseña):
        if self.conexion.is_connected:
            try:
                cursor = self.conexion.cursor()
                sql = f"UPDATE USUARIOS set contraseña={nuevaContraseña} where idUsuario ={id}"
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
        self.conexion = mysql.connector.connect(
                host = "localhost",
                port = "3306",
                user = "root",
                password = "sandro12352*",
                db = "proyectorqs"
            )
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
                sql = f"INSERT INTO alumnos (nombres,apellidos,padre,madre,dni,telefono,direccion,fechaNacimiento,sexo,paisNacimiento,idApoderado) values ('{nombres}','{apellidos}','{nombre_padre}','{nombre_madre}','{dni}','{telefono}','{direccion}')"
                cursor.execute(sql)
                self.conexion.commit()
                cursor.close()

            
            except Error as ex:
                print("Error es : ",ex)

    def buscarAlumno(self,nombres,apellidos):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = f"SELECT * FROM alumnos where nombres like '{nombres}%' and apellidos like '{apellidos}%'"
                alumno = cursor.execute(sql)
                alumno = cursor.fetchall()
                cursor.close()
                return alumno
                

            
            except Error as ex:
                print("Error es : ",ex)

