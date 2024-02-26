from Controladores.alumnos import*
from BD.conexion import*
conn = ConexionMysql()

class ArregloAlumnos:

        def __init__(self):
            self.dataAlumnos = conn.listarAlumnos()
        
        def registrarAlumno(self,objAlum):
           self.dataAlumnos.append(objAlum)

        def devolverAlumno(self,pos):
            return self.dataAlumnos[pos]

        def tamañoArregloAlumnos(self):
             return len(self.dataAlumnos)
        
        def buscarAlumno(self,dni):
            for i in range(len(self.tamañoArregloAlumnos())):
                 if dni == self.dataAlumnos[i].getdniAlumno():
                       return i
            return -1
        def eliminarAlumno(self,indice):
            del (self.dataAlumnos[indice])


