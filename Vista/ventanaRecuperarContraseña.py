from Controladores.alumnos import*
from Vista.login import *
from PyQt5 import  QtWidgets, uic
from Vista.registrarUsuario import*
from BD.conexion import*






 
class VentanaRecuperarContrasena(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaRecuperarContrasena, self).__init__(parent)
        uic.loadUi("UI/ventanaRecuperarContraseña.ui", self)
        self.data = ConexionMysql()
        self.btnConfirmar.clicked.connect(self.cambiar)






    def cambiar(self):
        username = self.txtUsername.text()
        contraseña = self.txtNuevaCon.text()
        usuarios = self.data.listarUsuarios()
        id = -1
        for user in usuarios:
            if username == user[1]:
                id = user[0]


        if username !="" and contraseña != "":
            if id  !=-1:
                self.data.actualizarUsuarios(id,contraseña)
                QtWidgets.QMessageBox.information(self,"Recuperar contraseña","Contraseña Actualizada",QtWidgets.QMessageBox.Ok)
                self.close()
            else:
                QtWidgets.QMessageBox.information(self,"Recuperar contraseña","Usuario no registrado",QtWidgets.QMessageBox.Ok)

        else:
            QtWidgets.QMessageBox.information(self,"Recuperar contraseña","Espacios vacios",QtWidgets.QMessageBox.Ok)


        


