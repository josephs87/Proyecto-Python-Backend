import mysql.connector

class Usuarios:
    usuarios = []

def consultar_usuario(self, usuario):
    for usuario in self.usuarios:
        if usuario['usuario'] == usuario:
            return usuario
    return False

def agregar_usuario(self,usuario, nombre, clave):
    if self.consultar_usuario(usuario):
        return False
    
    nuevo_usuario = {
        'usuario': usuario,
        'nombre': nombre,
        'clave': clave
    }

    self.usuarios.append(nuevo_usuario)
    return True

def modificar_usuario(self, usuario, nuevo_usuario, clave, nueva_clave):
    for usuario in self.usuarios:
        if usuario['usuario'] == usuario:
            usuario['usuario'] = nuevo_usuario
            clave['clave'] = nueva_clave
            return True
    return False

def eliminar_usuario(self, usuario):
    for usuario in self.usuarios:
        if usuario['usuario'] == usuario:
            self.usuarios.remove(usuario)
            return True
    return False

class Usuarios:

    def __init__(self, host, user, password, database):

        database = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )

        self.cursor = self.database.cursor(dictionary=True)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios(usuario VARCHAR(255) NOT NULL, nombre VARCHAR(255) NOT NULL, clave INT(0, 10) VARCHAR(255)''')
        self.database.commit()

def agregar_usuario(self, usuario, clave):

    sql = "INSERT INTO usuarios (usuario, clave) VALUES (%s, %s)"
    valores = (usuario, clave)

    self.cursor.execute(sql, valores)
    self.database.commit()
    return self.cursor.lastrowid


usuario = Usuarios(host='localhost',  user='root', password='', database='python_bd')

usuario.agregar_usuario('josejoel', 'Jose Videla', 'jobaev')