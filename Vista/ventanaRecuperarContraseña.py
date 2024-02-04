from Contraladores.alumnos import*
from Vista.login import *
from PyQt5 import  QtWidgets, uic





 
class VentanaRecuperarContrasena(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaRecuperarContrasena, self).__init__(parent)
        uic.loadUi("UI/ventanaRecuperarContraseña.ui", self)







    
