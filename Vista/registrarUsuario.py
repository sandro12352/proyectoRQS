from Contraladores.alumnos import*
from Vista.login import *
from PyQt5 import  QtWidgets, uic
from BD.conexion import*


conn = ConexionMysql()
 
class RegistrarUsuario(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(RegistrarUsuario, self).__init__(parent)
        uic.loadUi("UI/registrarUsuario.ui", self)
        
    

        self.btnRegistrar.clicked.connect(self.registrarNewUsuario)



    def registrarNewUsuario(self):
     
        username = self.txtUsuario.text()
        password= self.txtPassword.text()
        confimarPassowrd = self.txtConfirmarCon.text()
        usuario = (username,password)
        
        if confimarPassowrd == password:
            try:
                self.close()
                conn.agregarUsuario(usuario)
            except Exception as ex:
                print("Error al registrar usuario:", ex)
        else:
             print("Contraseña no coinciden")
        

        
