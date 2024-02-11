from PyQt5 import  QtWidgets, uic
from PyQt5 import  QtCore
from Vista.login import *
from PyQt5.QtWidgets import QFrame, QPushButton, QTableWidgetItem, QHBoxLayout
from Controladores.arregloAlumnos import*
from Controladores.alumnos import*



aAlum = ArregloAlumnos()


class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaPrincipal, self).__init__(parent)
        uic.loadUi("UI/ventanaPrincipal.ui", self)        
        self.btnAtras.setVisible(False)
        self.show()
        
        
        

        self.cboCuenta.currentIndexChanged.connect(self.cerrarSession)
        self.btnMenu.clicked.connect(self.mover_menu)
        self.ventanAlumnos()
        self.btnAtras.clicked.connect(self.mover_menu)

        self.btnLogut.clicked.connect(lambda:self.cboCuenta.showPopup())
        self.btnHome.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pageHome))
        self.btnPagos.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagePagos))
        self.btnMatricula.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pageMatricula))
        
        

        

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
            self.tblAlumnos.setItem(i,0,QtWidgets.QTableWidgetItem(str(aAlum.devolverAlumno(i).getCodigoAlumno())))
            self.tblAlumnos.setItem(i,1,QtWidgets.QTableWidgetItem(aAlum.devolverAlumno(i).getNombresAlumno()))
            self.tblAlumnos.setItem(i,2,QtWidgets.QTableWidgetItem(aAlum.devolverAlumno(i).getApellidosAlumno()))
            self.tblAlumnos.setItem(i,3,QtWidgets.QTableWidgetItem(aAlum.devolverAlumno(i).getPadreAlumno()))
            self.tblAlumnos.setItem(i,4,QtWidgets.QTableWidgetItem(aAlum.devolverAlumno(i).getMadreAlumno()))
            self.tblAlumnos.setItem(i,5,QtWidgets.QTableWidgetItem(aAlum.devolverAlumno(i).getDniAlumno()))
            self.tblAlumnos.setItem(i,6,QtWidgets.QTableWidgetItem(aAlum.devolverAlumno(i).getTelefonoAlumno()))
            self.tblAlumnos.setItem(i,7,QtWidgets.QTableWidgetItem(aAlum.devolverAlumno(i).getDireccionAlumno()))
            
            
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
        self.btnAlumnos.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pageAlumnos))   


    
        
    
       
    def ventaMatriculas(self):
        pass












