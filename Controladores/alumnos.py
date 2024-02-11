class Alumnos:

    def __init__(self,codigoAlumno,nombresAlumno,apellidosAlumno,padreAlumno,madreAlumno,dniAlumno,telefonoAlumno,direccionAlumno):
        self.__codigo = codigoAlumno
        self.__nombres  = nombresAlumno
        self.__apellidos  = apellidosAlumno
        self.__padre = padreAlumno
        self.__madre = madreAlumno
        self.__dni  = dniAlumno
        self.__telefono  = telefonoAlumno
        self.__direccion  = direccionAlumno

        
    def getCodigoAlumno(self):
        return self.__codigo

    def getNombresAlumno(self):
        return self.__nombres
    
    def getApellidosAlumno(self):
        return self.__apellidos
    
    def getPadreAlumno(self):
        return self.__padre
    
    def getMadreAlumno(self):
        return self.__madre


    def getDniAlumno(self):
        return self.__dni
    
    def getTelefonoAlumno(self):
        return self.__telefono
    

    def getDireccionAlumno(self):
        return self.__direccion
   
    
    def setNombresAlmuno(self,nombre):
        self.__nombres = nombre

    
    def setApellidosAlumno(self,nombre):
        self.__nombres = nombre

    def setPadreAlumno(self,padre):
        self.__padre = padre 
    
    def setMadreAlumno(self,madre):
        self.__madr = madre

    def setSeccionAlumno(self,seccion):
        self.__seccion = seccion


    def setDniAlumno(self,nombre):
        self.__nombres = nombre


    def setTelefonoAlumno(self,nombre):
        self.__nombres = nombre

    def setDireccionAlumno(self,nombre):
        self.__nombres = nombre


    
        




        