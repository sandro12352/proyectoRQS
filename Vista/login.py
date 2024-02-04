from PyQt5 import  QtWidgets, uic
from PyQt5 import QtWidgets,QtGui
from Vista.ventanaPrincipal import VentanaPrincipal
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from Vista.ventanaRecuperarContraseña import VentanaRecuperarContrasena
from Vista.registrarUsuario import *
from BD.conexion import*





qtCreatorFile = "UI/login.ui" # nombre del archivo
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)






class Login(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(Login,self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon("imagenes/logo.png"))
        uic.loadUi("UI/login.ui",self)
        
        self.btnIniciar.clicked.connect(self.iniciarSesion)
        self.btnFacebook.clicked.connect(self.facebook)
        self.btnInstagram.clicked.connect(self.Instagram)
        self.btnTwiter.clicked.connect(self.Twiter)
        self.btnTelegram.clicked.connect(self.Telgram)
        self.txtUsuario.setFocus()
        self.btnOlvidar.clicked.connect(self.olvidarContrasena)
        self.btnRegistrar.clicked.connect(self.registrar)

        self.show()
        
    # Aquí van las nuevas funciones
    def iniciarSesion(self):
        usuario = self.txtUsuario.text().lower()
        contraseña = self.txtPassword.text()
        self.validarDatos(usuario,contraseña)


    def validarDatos(self,usuario,contraseña):
        usuarios = conn.traerDatos()
        print(usuarios[0])
        for user in usuarios:
            if usuario == user[1] and contraseña == user[2]:
                self.close()
                self.vprincipal = VentanaPrincipal()
                self.vprincipal.show()
            else:
                self.datoscontra.setText("¡Contraseña incorrecta!")
                self.datosusuario.setText("¡Usuario incorrecto!")
                self.datosusuario.setStyleSheet("color: red;")
                self.datoscontra.setStyleSheet("color: red;")
            if usuario ==user[1] and  contraseña != user[2]:
                self.datoscontra.setText("¡Contraseña incorrecta!")
                self.datosusuario.setText("")
                return
            else:
                self.datosusuario.setText("¡Usuario incorrecto!")
                self.datoscontra.setText("")  
            
                
            if self.txtUsuario.text() == "":
                self.datosusuario.setText("¡Campo obligatorio!")
                self.datosusuario.setStyleSheet("color: red;")
                
            if self.txtPassword.text() == "":
                self.datoscontra.setText("¡Campo obligatorio!")
                self.datoscontra.setStyleSheet("color: red;")
                return
            
    def facebook(self):    
        url = QUrl("https://www.facebook.com/sandro12352/")
        QDesktopServices.openUrl(url)
    

    def Instagram(self):    
        url = QUrl("https://www.instagram.com/sandro023163/")
        QDesktopServices.openUrl(url)

    def Twiter(self):    
        url = QUrl("https://twitter.com/SandroPachas")
        QDesktopServices.openUrl(url)

    def Telgram(self):    
        url = QUrl("https://web.telegram.org/a/")
        QDesktopServices.openUrl(url)
            
            


    

    def olvidarContrasena(self):
        self.ventaRecuperar = VentanaRecuperarContrasena()
        self.ventaRecuperar.show()   



    def registrar(self):
        self.ventaRegisrar = RegistrarUsuario()
        self.ventaRegisrar.show()