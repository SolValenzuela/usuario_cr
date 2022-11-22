# importar la función que devolverá una instancia de una conexión
from mysqlconnection import connectToMySQL
# modelar la clase después de la tabla usuarios de nuestra base de datos

class Usuario:

    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']


# ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('usuarios').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de usuarios
        usuarios = []
        # Iterar sobre los resultados de la base de datos y crear instancias de usuarios con cls
        for usuario in results:
            usuarios.append( cls(usuario) )
        return usuarios
    

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO usuarios ( first_name , last_name , email  ) VALUES ( %(first_name)s , %(last_name)s , %(email)s  );"
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL('usuarios').query_db( query, data )