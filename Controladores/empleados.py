class Empleados:
    def __init__(self,idEmpleado,nombres,apellidos,dni,cargo):
        self.__id = idEmpleado
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__dni = dni
        self.__cargo = cargo

    def getIdEmpleado(self):
        return self.__id

    def getNombresEmpleado(self):
        return self.__nombres
    
    def getApellidosEmpleado(self):
        return self.__apellidos
    
    def getDniEmpleado(self):
        return self.__dni
    
    def getCargoEmpleado(self):
        return self.__cargo
    
    def setNombresEmpleado(self,nombres):
        self.__nombres = nombres

    def setApellidosEmpleado(self,apellidos):
        self.__apellidos=apellidos

    def setDniEmpleado(self,dni):
        self.__dni = dni

    def setCargoEmpleado(self,cargo):
        self.__cargo = cargo
