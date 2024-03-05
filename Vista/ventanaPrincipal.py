from PyQt5 import  QtWidgets, uic
from PyQt5 import  QtCore
from Vista.login import *
from Controladores.style import*
from Vista.ventanaMatricula import VentanaMatricula
from Controladores.arregloAlumnos import*
from Controladores.alumnos import*






class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaPrincipal, self).__init__(parent)
        uic.loadUi("UI/ventanaPrincipal.ui", self)       

        self.btnAtras.setVisible(False)
        self.show()
        
        self.btnRegistrarMatricula.clicked.connect(self.abrirMatricula)
        
        self.btnLogut.clicked.connect(lambda:self.cboCuenta.showPopup())
        self.cboCuenta.currentIndexChanged.connect(self.cerrarSession)

        #BARRA DE MENU DESPEGABLE
        self.btnMenu.clicked.connect(self.mover_menu)
        self.btnAtras.clicked.connect(self.mover_menu)

        # pageAlumnos 
        self.btnAlumnos.clicked.connect(self.ventanAlumnos)
        #BOTONES DEL pageAlumnos 
        self.btnActualizar.clicked.connect(self.actualziarTablaAlumnos)
        self.txtBuscar.returnPressed.connect(self.buscarAlmuno)

        #pagePrincipal
        self.btnHome.clicked.connect(self.ventanaPrincipal)

        #pagePagos
        self.btnPagos.clicked.connect(self.ventanaPagos)

        #pageMatriculas
        self.btnMatricula.clicked.connect(self.ventaMatriculas)

        #pageDocentes
        self.btnDocentes.clicked.connect(self.ventanaDocentes)
         
        
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
        aAlum = ArregloAlumnos()
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

            # Establecer el contenedor como widget de la celda
            container_widget = botenesAcciones()      
            self.tblAlumnos.setCellWidget(i, 8, container_widget)
            
      
       #
        self.lblTexto.setText("REGISTRA UN ALUMNO")
        self.stackedWidget.setCurrentWidget(self.pageAlumnos)

    def abrirMatricula(self):
        self.ventaMatricula =  VentanaMatricula() 
        self.ventaMatricula.show()

    def actualziarTablaAlumnos(self):
        self.limpiarTablaAlumnos()
        self.ventanAlumnos()

    def limpiarTablaAlumnos(self):
        self.tblAlumnos.clearContents()
        self.tblAlumnos.setRowCount(0)


    def buscarAlmuno(self):     
        consulta = self.txtBuscar.text().strip()  # Obtener el texto del QLineEdit y eliminar espacios en blanco al principio y al final   
        
        if consulta:
            nombre, *apellido = consulta.split(maxsplit=1)  # Dividir la cadena en dos partes, máximo 1 split
            apellido = apellido[0] if apellido else ""
            alumno = conn.buscarAlumno(nombre,apellido)
            self.limpiarTablaAlumnos()
            self.tblAlumnos.setRowCount(len(alumno))
            self.tblAlumnos.verticalHeader().setVisible(False)
            for i in range(0,len(alumno)):
                self.tblAlumnos.setItem(i,0,QtWidgets.QTableWidgetItem(str(alumno[i][0])))
                self.tblAlumnos.setItem(i,1,QtWidgets.QTableWidgetItem(alumno[i][1]))
                self.tblAlumnos.setItem(i,2,QtWidgets.QTableWidgetItem(alumno[i][2]))
                self.tblAlumnos.setItem(i,3,QtWidgets.QTableWidgetItem(alumno[i][3]))
                self.tblAlumnos.setItem(i,4,QtWidgets.QTableWidgetItem(alumno[i][4]))
                self.tblAlumnos.setItem(i,5,QtWidgets.QTableWidgetItem(alumno[i][5]))
                self.tblAlumnos.setItem(i,6,QtWidgets.QTableWidgetItem(alumno[i][6]))
                self.tblAlumnos.setItem(i,7,QtWidgets.QTableWidgetItem(alumno[i][7]))
                container_widget = botenesAcciones()
                self.tblAlumnos.setCellWidget(i, 8, container_widget)
        
            
        else:
            QtWidgets.QMessageBox.information(self,"Buscar alumno","Usuario no encontrado",QtWidgets.QMessageBox.Ok)    

    

    def ventanaPrincipal(self):
        self.lblTexto.setText("INICIO")
        self.stackedWidget.setCurrentWidget(self.pageHome)
        
    
       
    def ventaMatriculas(self):
        self.lblTexto.setText("MATRICULAS DE ALUMNOS")
        self.stackedWidget.setCurrentWidget(self.pageMatricula)




    def ventanaPagos(self):
        self.lblTexto.setText("PAGOS")
        self.stackedWidget.setCurrentWidget(self.pagePagos)


    def ventanaDocentes(self):
        self.lblTexto.setText("DOCENTES")
        self.stackedWidget.setCurrentWidget(self.pageDocentes)




