from Controladores.alumnos import*
from BD.conexion import*
conn = ConexionMysql()
class ArregloAlumnos:

        def __init__(self):
            self.dataAlumnos = []
            self.cargar()

        def cargar(self):
            datos = conn.listarAlumnos()
            for dato in datos:
                codigo = dato[0] 
                nombres = dato[1]
                apellidos = dato[2]
                padre = dato[3]
                madre=dato[4]
                dni = dato[5]
                telefono =dato[6]
                direccion = dato[7]
                objAlum = Alumnos(codigo,nombres,apellidos,padre,madre,dni,telefono,direccion)  
                self.registrarAlumno(objAlum)
      
             
        
        
        def registrarAlumno(self,objAlum):
           self.dataAlumnos.append(objAlum)

        def devolverAlumno(self,pos):
            return self.dataAlumnos[pos]

        def tamañoArregloAlumnos(self):
             return len(self.dataAlumnos)
        
        def buscarCliente(self,dni):
            for i in range(len(self.tamañoArregloAlumnos())):
                 if dni == self.dataAlumnos[i].getdniAlumno():
                       return i
            return -1
        def eliminarAlumno(self,indice):
            del (self.dataAlumnos[indice])


