usuarios = []

def consultar_usuario(usuario):
    for usuario in usuarios:
        if usuario['usuario'] == usuario:
            return usuario
    return False


def agregar_usuario(usuario,nombre,clave):

    if consultar_usuario(usuario):
        return False
    nuevo_usuario = {
        'usuario': usuario,
        'nombre': nombre,
        'clave': clave
    }
    usuarios.append(nuevo_usuario)
    return True

def modificar_usuario(usuario,clave,nuevo_usuario,nueva_clave):
    for usuario in usuarios:
        if usuario['usuario'] == usuario:
            usuario['usuario'] = nuevo_usuario
            clave['clave'] = nueva_clave
            return True
    return False

def eliminar_usuario(usuario):
    for usuario in usuarios:
        if usuario['usuario'] == usuario:
            usuarios.remove(usuario)
            return True
    return False