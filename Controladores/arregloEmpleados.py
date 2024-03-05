from Controladores.empleados import*
from BD.conexion import*
conn = ConexionMysql()
class ArregloEmpleados:

    def __init__(self):
        self.dataEmpleados = conn.listarEmpleados()

    def tamañoEmpleados(self):
        return len(self.dataEmpleados)
    
    # def obteneridEmpleado(self,):
    #     for empleado in self.dataEmpleados:
            

    def devolverEmpleado(self,pos):
        return self.dataEmpleados[pos]    
    
    def buscarEmpleado(self,dni):
        self.dataEmpleados = conn.listarEmpleados()
        for empleado in self.dataEmpleados:
            if dni == empleado[3]: 
                return empleado[0]
        return -1    
