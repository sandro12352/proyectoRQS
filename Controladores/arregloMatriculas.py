from Controladores.matriculas import*
from BD.conexion import*

conn = ConexionMysql()

class ArregloMatriculas:

    def __init__(self):
        self.dataMatriculas=[]
        self.cargar()


    def cargar(self):
        datosMatriculas = conn.listarMatricula()
        for dato in datosMatriculas:
            codigo  = dato[0]
            total = dato

        pass


   