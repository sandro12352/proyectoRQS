from Controladores.empleados import*
from BD.conexion import*
conn = ConexionMysql()
class ArregloEmpleados:

    def __init__(self):
        self.dataEmpleados = conn.listarEmpleados()

    
    def asignarEmpleados(self):
        for empleado in self.dataEmpleados:
            id = empleado[0]
            nombres = empleado[1]
            apellidos = empleado[2]
            dni = empleado[3]
            cargo = empleado[4]
            objEmpleado = Empleados(id,nombres,apellidos,dni,cargo)
            print(objEmpleado)
    
    
    def tamañoEmpleados(self):
        return len(self.dataEmpleados)

    def devolverEmpleado(self,pos):
            return self.dataEmpleados[pos]    
    
    def buscarEmpleado(self,id):
        for i in range(self.tamañoEmpleados):
            if id == self.dataEmpleados[i].getIdEmpleado():   
                return i
        return -1    
