from Controladores.alumnos import*
from Vista.login import *
from PyQt5 import  QtWidgets, uic
from Vista.registrarUsuario import*
from BD.conexion import*






 
class VentanaRecuperarContrasena(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaRecuperarContrasena, self).__init__(parent)
        uic.loadUi("UI/ventanaRecuperarContraseña.ui", self)

        self.btnConfirmar.clicked.connect(self.cambiar)






    def cambiar(self):
        username = self.txtUsername.text()
        contraseña = self.txtNuevaCon.text()
        
        if username !="" and contraseña != "":
            pos = aUsuario.buscarUsuario(username)
            id = aUsuario.devolverUsuario(pos).getIdUsuario()
            conn.actualizarUsuarios(id,contraseña)
            QtWidgets.QMessageBox.information(self,"Recuperar contraseña","Contraseña Actualizada",QtWidgets.QMessageBox.Ok)
            self.close()

        else:
            QtWidgets.QMessageBox.information(self,"Recuperar contraseña","Espacios vacios",QtWidgets.QMessageBox.Ok)


        


