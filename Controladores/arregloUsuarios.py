from Controladores import usuarios
from BD.conexion import*
from Controladores.arregloEmpleados import*
conn = ConexionMysql()

class ArregloUsuarios:
    def __init__(self) :
        self.dataUsuarios = conn.listarUsuarios()



    def tamañoUsuarios(self):
        return len(self.dataUsuarios) 
    
    def devolverUsuario(self,pos):
        return self.dataUsuarios[pos]
    
    def buscarUsuario(self,id):
        for i in range(self.tamañoUsuarios()):
            if id == self.dataUsuarios[i].getIdUsuario():
                return i
        return -1
    