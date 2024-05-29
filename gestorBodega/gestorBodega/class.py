"""import pymongo
from pymongo.gridfs import gridfs
 esto se supone que es para gestionar imagenes  """
class Personal:

    def __init__(self, id_personal, nombrePersonal, rol, telefono):
        self.id_personal = id_personal
        self.nombrePersonal = nombrePersonal
        self.rol = rol
        self.telefono = telefono

    def get_id_personal(self):
        return self.id_personal

    def set_id_personal(self, nuevo_id_personal):
         self.id_personal = nuevo_id_personal

    def get_nombrePersonal(self):
         return self.nombrePersonal

    def set_nombrePersonal(self, nuevo_nombrePersonal):
         self.nombrePersonal = nuevo_nombrePersonal

    def get_rol(self):
        return self.rol

    def set_rol(self, nuevo_rol):
         self.rol = nuevo_rol

    def get_telefono(self):
        return self.telefono

    def set_telefono(self, nuevo_telefono):
        self.telefono = nuevo_telefono

    def __str__(self):
        return f"Personal: {self.nombrePersonal} ({self.rol.nombreRol}) - Teléfono: {self.telefono}"

class Rol:


    def __init__(self, id_rol, nombreRol):
        self.id_rol = id_rol
        self.nombreRol = nombreRol

    def get_id_rol(self):
         return self.id_rol

    def get_nombreRol(self):
         return self.nombreRol

    def __str__(self):
         return f"Rol: {self.nombreRol}"
    
class Juego:

    def __init__(self, codigoDeBarra, nombreJuego, consola, distribucion, imagen_id, estado, stock):
        self.codigoDeBarra = codigoDeBarra
        self.nombreJuego = nombreJuego
        self.consola = consola
        self.distribucion = distribucion
        """self.imagen_id = imagen_id"""
        self.estado = estado
        self.stock = stock 
    
        """     def get_imagen(self, db):
        fs = gridfs.GridFS(db)
        return fs.get(self.imagen_id).read() """

    def __str__(self):

        return f"Juego: {self.nombreJuego} ({self.consola.nombreConsola}) - Estado: {self.estado.nombreEstado}"

class Ubicacion:

     def __init__(self, idUbicacion, nombreUbicacion):
        self.idUbicacion = idUbicacion
        self.nombreUbicacion = nombreUbicacion

     def __str__(self):
        return f"Ubicación: {self.nombreUbicacion}"

class Stock:
    def __init__(self, ubicacion, cantidad):
        self.ubicacion = ubicacion
        self.cantidad = cantidad

    def __str__(self):
        return f"Stock: {self.cantidad} unidades en {self.ubicacion.nombreUbicacion}"

    def restar_cantidad(self, unidades_a_restar):
        self.cantidad -= unidades_a_restar

    def aumentar_cantidad(self, unidades_a_agregar):
        self.cantidad += unidades_a_agregar

class Estado:
     def __init__(self, idEstado, nombre):
        self.idEstado = idEstado
        self.nombre = nombre

     def __str__(self):
        return f"Estado: {self.nombre}"
