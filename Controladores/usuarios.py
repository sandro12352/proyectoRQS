class Usuarios:
    def __init__(self,username,contraseña):
        self.__username =username
        self.__contraseña = contraseña

    def getUsername(self):
        return self.__username
    
    def getContraseña(self):
        return self.__contraseña
    

    def setIdUsuario(self,id_usuario):
        self.__id = id_usuario


    def setUsername(self,username):
        self.__username = username
        
    
    def setContraseña(self,contraseña):
        self.__contraseña = contraseña
        
    
   