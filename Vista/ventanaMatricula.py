from PyQt5 import  QtWidgets, uic
from Vista.ventanaPrincipal import*
from BD.conexion import*


conn = ConexionMysql()



 
class VentanaMatricula(QtWidgets.QMainWindow):
    alumnoRegistrado = QtCore.pyqtSignal()
    def __init__(self, parent = None):
        super(VentanaMatricula, self).__init__(parent)
        uic.loadUi("UI/ventanaMatricula.ui", self)

        
        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnLimpiar.clicked.connect(self.limpiarDatos)

    
    


    def registrar(self):
        nombres =self.txtNombres.text()
        apellidos=self.txtApellidos.text()
        nombre_padre=self.txtPadre.text()
        nombre_madre=self.txtMadre.text()
        dni=self.txtDni.text()
        telefono=self.txtTelefono.text()
        direccion=self.txtDireccion.text()



        conn.registrarAlumno(nombres,apellidos,nombre_padre,nombre_madre,dni,telefono,direccion)
        QtWidgets.QMessageBox.information(self,"Mensaje","REGISTRADO",QtWidgets.QMessageBox.Ok)
        self.limpiarDatos()
        self.alumnoRegistrado.emit()

    
    def limpiarDatos(self):
        self.txtNombres.clear()
        self.txtApellidos.clear()
        self.txtPadre.clear()
        self.txtMadre.clear()
        self.txtDni.clear()
        self.txtEdad.clear()
        self.txtTelefono.clear()
        self.txtDireccion.clear()
    
    