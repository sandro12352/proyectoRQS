from Controladores.alumnos import*
from Controladores.usuarios import*
from Vista.login import *
from PyQt5 import  QtWidgets, uic
from BD.conexion import*
from Controladores.arregloUsuarios import*


aEmpleado = ArregloEmpleados()
aUsuarios = ArregloUsuarios()

class RegistrarUsuario(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(RegistrarUsuario, self).__init__(parent)
        uic.loadUi("UI/registrarUsuario.ui", self)
        
        #Instanciando un objeto de la clase conexion 
        
        
        self.btnRegistrar.clicked.connect(self.registrarNewUsuario)

    def validar(self):
        if self.txtNombres.text() == "":
            self.txtNombres.setFocus()
            return "Nombres ..."
        elif self.txtApellidos.text() == "":
            self.txtApellidos.setFocus()
            return "Apellidos ..."
        elif self.txtDni.text() == "":
            self.txtDni.text()
            return "Dni ..."
        elif self.txtUsuario.text() == "":
            self.txtUsuario.setFocus()
            return "Usuario...!!1"
        elif self.txtPassword.text() == "":
            self.txtPassword.setFocus()
            return "Contraseña...!!!"
        elif self.txtConfirmarCon.text() == "":
            self.txtConfirmarCon.setFocus()
            return "Confirmar Contraseña ...!!!"
        else:
            return ""
    
    def limpiarDatos(self):
        self.txtNombres.clear()
        self.txtApellidos.clear()
        self.txtDni.clear()
        self.cboCargo.setCurrentIndex(0)
        self.txtUsuario.clear()
        self.txtPassword.clear()
        self.txtConfirmarCon.clear()

    def registrarEmpleado(self):
        nombres = self.txtNombres.text()
        apellidos = self.txtApellidos.text().strip()
        cargo = self.cboCargo.currentText()
        dni = self.txtDni.text()
        pos = aEmpleado.buscarEmpleado(dni) 

        if self.validar() == "" :
            if pos == -1:
                objEmpleado = Empleados(nombres,apellidos,dni,cargo)
                idEmpleado = conn.agregarEmpleados(objEmpleado) 
                return idEmpleado
                    
            else:
                QtWidgets.QMessageBox.information(self,"Registro de Empleado","Empleado ya ah sido registrado",QtWidgets.QMessageBox.Ok)
                return -1
        else:
            QtWidgets.QMessageBox.information(self,"Registro usuario","Faltan llenar" + self.validar(),QtWidgets.QMessageBox.Ok)
            return -1

    def registrarNewUsuario(self):
        id_empleado  =self.registrarEmpleado()
        if id_empleado == -1:  # Si no se pudo registrar el empleado, detener el flujo
            return
        username = self.txtUsuario.text()
        password= self.txtPassword.text()
        confimarPassowrd = self.txtConfirmarCon.text()
        #Lista todos los usuarios de la BD
        usuarios = conn.listarUsuarios()
        #Hacemos un recorrido a la lista usuarios y comparamos el username con la posicion 1 para verificar si ya existe
        for user in usuarios:
            if username == user[1]:
               return QtWidgets.QMessageBox.information(self,"Registro de Usuario","Usuario ya registrado",QtWidgets.QMessageBox.Ok)

        
    
        if confimarPassowrd == password:  
                objUsuario = Usuarios(username,password)                      
                conn.agregarUsuario(objUsuario,id_empleado)
                self.limpiarDatos()
                
        else:
            QtWidgets.QMessageBox.information(self,"Registro usuario","Contraseña no coinciden",QtWidgets.QMessageBox.Ok)
        
        

        
