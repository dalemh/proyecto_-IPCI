class cliente:

    def __init__(self,id, nombre,apellido, usuario,password,admin):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.password = password
        self.admin = admin

    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getUsuario(self):
        return self.usuario

    def getPassword(self):
        return self.password
    
    def getAdmin(self):
        return self.admin

    def setId(self, id):
        self.id = id
 
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellido(self, apellido):
        self.apellido = apellido
    
    def setUsuario(self, usuario):
        self.usuario = usuario

    def setPassword(self, password):
        self.password = password
    
    def setAdmin(self, admin):
        self.admin = admin