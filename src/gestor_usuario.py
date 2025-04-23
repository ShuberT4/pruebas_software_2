class Usuario:
    def __init__(self, nombres, apellidos, identificacion, correo, contrasena, estado='activo'):
        self.nombres = nombres
        self.apellidos = apellidos
        self.identificacion = identificacion
        self.correo = correo
        self.contrasena = contrasena
        self.estado = estado

class GestionUsuarios:
    def __init__(self):
        self.usuarios = []

    def crear_usuario(self, nombres, apellidos, identificacion, correo, contrasena):
        if not all([nombres, apellidos, identificacion, correo, contrasena]):
            return "Faltan datos, el usuario no fue creado."

        nuevo_usuario = Usuario(nombres, apellidos, identificacion, correo, contrasena)
        self.usuarios.append(nuevo_usuario)
        return "creado"

    def eliminar_usuario(self, identificacion):
        for usuario in self.usuarios:
            if usuario.identificacion == identificacion:
                self.usuarios.remove(usuario)
                return True
        return False

    def obtener_usuario(self, identificacion):
        for usuario in self.usuarios:
            if usuario.identificacion == identificacion:
                return usuario
        return None

    def listar_usuarios(self):
        return self.usuarios
