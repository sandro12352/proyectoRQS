from PyQt5 import  QtWidgets, uic
from PyQt5 import  QtCore
from Vista.login import *
from PyQt5.QtWidgets import QFrame, QPushButton, QTableWidgetItem, QHBoxLayout
from Vista.ventanaMatricula import VentanaMatricula
from Controladores.arregloAlumnos import*
from Controladores.alumnos import*



aAlum = ArregloAlumnos()


class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaPrincipal, self).__init__(parent)
        uic.loadUi("UI/ventanaPrincipal.ui", self)        
        self.btnAtras.setVisible(False)
        self.show()
        
        self.btnRegistrarAlumno.clicked.connect(self.abrirMatricula)
        
        self.btnLogut.clicked.connect(lambda:self.cboCuenta.showPopup())
        self.cboCuenta.currentIndexChanged.connect(self.cerrarSession)
        self.btnMenu.clicked.connect(self.mover_menu)
        
        self.btnAtras.clicked.connect(self.mover_menu)
        self.btnAlumnos.clicked.connect(self.ventanAlumnos) 
        self.btnHome.clicked.connect(self.ventanaPrincipal)
        self.btnPagos.clicked.connect(self.ventanaPagos)
        self.btnMatricula.clicked.connect(self.ventaMatriculas)
        self.ventanAlumnos()   
        
    def asignarCuenta(self,usuario):
        self.btnLogut.setText(usuario + "\t\t" )
        self.btnLogut.setStyleSheet("""QPushButton{ background:#fff; border:none;border-radius:5px; padding:3px 10px;font-size: 20px;font-family: "Georgia";}"""
        "QPushButton:hover{background-color:#f2f2f2}")


    def mover_menu(self):
        width = self.frame_lateral.width()
        normal = 0

        if width == 0:
            extender = 300
        else:
            extender = normal

        self.mostrarMenu() 
        if extender!=0:
            self.mostrarAtras()
        self.animacion = QtCore.QPropertyAnimation(self.frame_lateral, b'minimumWidth')
        self.animacion.setDuration(300)
        self.animacion.setStartValue(width)
        self.animacion.setEndValue(extender)
        self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animacion.start() 

    def mostrarAtras(self):
        self.btnMenu.setVisible(False)
        self.btnAtras.setVisible(True)

    def mostrarMenu(self):
        self.btnAtras.setVisible(False)
        self.btnMenu.setVisible(True)

    def cerrarSession(self):
        elegir = self.cboCuenta.currentText()
        if elegir == "Cerrar":
            self.close()          
            self.ventalogin()
            
            
        if elegir == "Salir":
            self.close()
                
    def ventalogin(self):
        from Vista.login import Login
        self.ventana_login= Login()
        self.ventana_login.show()
        
        
        
       
    def ventanAlumnos(self):
        #asignar filas y columna  
        self.tblAlumnos.setRowCount(aAlum.tamañoArregloAlumnos())
        self.tblAlumnos.setColumnCount(9)
        self.tblAlumnos.verticalHeader().setVisible(False)
        for i in range(0,aAlum.tamañoArregloAlumnos()):
            self.tblAlumnos.setItem(i,0,QtWidgets.QTableWidgetItem(str(aAlum.devolverAlumno(i)[0])))
            self.tblAlumnos.setItem(i,1,QtWidgets.QTableWidgetItem(aAlum.devolverAlumno(i)[1]))
            self.tblAlumnos.setItem(i,2,QtWidgets.QTableWidgetItem(aAlum.devolverAlumno(i)[2]))
            self.tblAlumnos.setItem(i,3,QtWidgets.QTableWidgetItem(aAlum.devolverAlumno(i)[3]))
            self.tblAlumnos.setItem(i,4,QtWidgets.QTableWidgetItem(aAlum.devolverAlumno(i)[4]))
            self.tblAlumnos.setItem(i,5,QtWidgets.QTableWidgetItem(aAlum.devolverAlumno(i)[5]))
            self.tblAlumnos.setItem(i,6,QtWidgets.QTableWidgetItem(aAlum.devolverAlumno(i)[6]))
            self.tblAlumnos.setItem(i,7,QtWidgets.QTableWidgetItem(aAlum.devolverAlumno(i)[7]))
            
            
            
             #crear un cotenedor para el boton dentro del item
            container_widget = QFrame()
            container_layout = QHBoxLayout(container_widget)

            #crear botones
            botonVer = QPushButton("VER", container_widget)
            botonActualizar = QPushButton("EDITAR", container_widget)
            botonEliminar = QPushButton("ELIMINAR", container_widget)
        
            botonVer.setCursor(QtCore.Qt.PointingHandCursor)
            botonActualizar.setCursor(QtCore.Qt.PointingHandCursor)
            botonEliminar.setCursor(QtCore.Qt.PointingHandCursor)

            botonVer.setFixedSize(120, 40)
            botonActualizar.setFixedSize(120, 40)
            botonEliminar.setFixedSize(120, 40)

            botonActualizar.setStyleSheet("QPushButton{ background-color:#1877f2; margin-bottom:2px;border-radius:10px;font-size:15px;color:#fff}"
                                "QPushButton:hover{background-color:#4267b2}")
            botonVer.setStyleSheet("QPushButton{ background-color:#B49C09; margin-bottom:2px;border-radius:10px;font-size:15px;color:#fff}"
                                "QPushButton:hover{background-color:#4267b2;}")
            botonEliminar.setStyleSheet("QPushButton{ background-color:#d34; margin-bottom:2px;border-radius:10px ;font-size:15px;color:#fff}"
                                "QPushButton:hover{background-color:#4267b2;}")
 
            container_layout.addWidget(botonVer)
            container_layout.addWidget(botonActualizar)
            container_layout.addWidget(botonEliminar)
            
            self.tblAlumnos.setCellWidget(i, 8, container_widget)
            
      
        # Establecer el contenedor como widget de la celda
        self.lblTexto.setText("REGISTRA UN ALUMNO")
        self.stackedWidget.setCurrentWidget(self.pageAlumnos)

    def abrirMatricula(self):
        self.ventaMatricula =  VentanaMatricula() 
        self.ventaMatricula.show()

    def limpiarTablaAlumnos(self):
        self.tblAlumnos.clearContents()
        self.tblAlumnos.setRowCount(0)

    def ventanaPrincipal(self):
        self.lblTexto.setText("INICIO")
        self.stackedWidget.setCurrentWidget(self.pageHome)
        
    
       
    def ventaMatriculas(self):
        self.lblTexto.setText("MATRICULAS DE ALUMNOS")
        self.stackedWidget.setCurrentWidget(self.pageMatricula)




    def ventanaPagos(self):
        self.lblTexto.setText("PAGOS")
        self.stackedWidget.setCurrentWidget(self.pagePagos)







