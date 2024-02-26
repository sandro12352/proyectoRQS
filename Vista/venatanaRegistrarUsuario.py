from Controladores.alumnos import*
from Vista.login import *
from PyQt5 import  QtWidgets, uic
from BD.conexion import*





class RegistrarUsuario(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(RegistrarUsuario, self).__init__(parent)
        uic.loadUi("UI/registrarUsuario.ui", self)
        
        #Instanciando un objeto de la clase conexion 
        self.datosTotales = ConexionMysql()
        
        self.btnRegistrar.clicked.connect(self.registrarNewUsuario)

    def validar(self):
        if self.txtUsuario.text() == "":
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
    
    

    def registrarEmpleado(self):
        nombres = self.txtNombres.text()
        apellidos = self.txtApellidos.text()
        cargo = self.cboCargo.currentText()

        self.datosTotales.agregarEmpleados(nombres,apellidos,cargo)    






    def registrarNewUsuario(self):
        self.registrarEmpleado()
        username = self.txtUsuario.text()
        password= self.txtPassword.text()
        confimarPassowrd = self.txtConfirmarCon.text()
        #Lista todos los usuarios de la BD
        usuarios = self.datosTotales.listarUsuarios()
        #Hacemos un recorrido a la lista usuarios y comparamos el username con la posicion 1 para verificar si ya existe
        for user in usuarios:
            if username == user[1]:
               return QtWidgets.QMessageBox.information(self,"Registro de Usuario","Usuario ya registrado",QtWidgets.QMessageBox.Ok)
        

        if self.validar() == "" :
            if confimarPassowrd == password:                          
                    self.datosTotales.agregarUsuario(username,password)
                    self.txtUsuario.clear()
                    self.txtPassword.clear()
                    self.txtConfirmarCon.clear()
            else:
                QtWidgets.QMessageBox.information(self,"Registro usuario","Contraseña no coinciden",QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self,"Registro usuario","Faltan llenar" + self.validar(),QtWidgets.QMessageBox.Ok)
        

        
