import unittest
from src.panel_administrativo import PanelAdministrativo
from src.gestor_usuario import GestionUsuarios

class TestPanelAdministrativo(unittest.TestCase):

    def setUp(self):
        self.gestion_usuarios = GestionUsuarios()
        self.panel = PanelAdministrativo(self.gestion_usuarios)
        self.gestion_usuarios.crear_usuario("Pedro", "Gómez", "001", "pedro@correo.com", "clave123")

    def test_acceso_panel_admin(self):
        self.assertTrue(self.panel.acceder_panel("admin", "admin123"))
        self.assertFalse(self.panel.acceder_panel("usuario", "user123"))

    def test_eliminar_usuario(self):
        self.assertTrue(self.panel.eliminar_usuario("001"))
        self.assertIsNone(self.gestion_usuarios.obtener_usuario("001"))

    def test_cambiar_estado_usuario(self):
        self.panel.cambiar_estado_usuario("001", "inactivo")
        usuario = self.gestion_usuarios.obtener_usuario("001")
        self.assertEqual(usuario.estado, "inactivo")

if __name__ == "__main__":
    unittest.main()
