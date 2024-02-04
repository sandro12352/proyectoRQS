class Matricula:
    def __init__(self,codigoMatricula,totalPagar,fechaMatricula):
        self.__codigo = codigoMatricula
        self.__total = totalPagar
        self.__fecha = fechaMatricula


    def getCodigoMatricula(self):
        return self.__codigo
    
    def getTotalPagar(self):
        return self.__total
    
    def getFechaMatricula(self):
        return self.__fecha
    

    def setCodigoMatricula(self,codigo):
        self.__codigo = codigo

    def setTotalPagar(self,total):
        self.__total = total

    def setFechaMatricula(self,fechaMatricula):
        self.__fecha = fechaMatricula
    

    