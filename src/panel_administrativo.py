class PanelAdministrativo:
    def __init__(self, gestion_usuarios):
        self.gestion_usuarios = gestion_usuarios
        self.admin_user = {"usuario": "admin", "contrasena": "admin123"}

    def acceder_panel(self, usuario, contrasena):
        return usuario == self.admin_user["usuario"] and contrasena == self.admin_user["contrasena"]

    def eliminar_usuario(self, identificacion):
        return self.gestion_usuarios.eliminar_usuario(identificacion)

    def cambiar_estado_usuario(self, identificacion, nuevo_estado):
        usuario = self.gestion_usuarios.obtener_usuario(identificacion)
        if usuario:
            usuario.estado = nuevo_estado
            return True
        return False
