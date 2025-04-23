import unittest

from src.gestor_usuario import GestionUsuarios


class TestGestionUsuarios(unittest.TestCase):

    def setUp(self):
        self.gestion = GestionUsuarios()

    def test_registro_usuario_exitoso(self):
        resultado = self.gestion.crear_usuario(
            "1001", "Juan", "Pérez", "juan@correo.com", "1234"
        )
        self.assertTrue(resultado)
        self.assertIn("1001", self.gestion.usuarios)

    def test_registro_usuario_existente(self):
        self.gestion.crear_usuario("1001", "Juan", "Pérez", "juan@correo.com", "1234")
        resultado = self.gestion.crear_usuario("1001", "Juan", "Pérez", "juan@correo.com", "1234")
        self.assertFalse(resultado)

    def test_eliminar_usuario_existente(self):
        self.gestion.crear_usuario("1002", "Ana", "Lopez", "ana@correo.com", "abcd")
        resultado = self.gestion.eliminar_usuario("1002")
        self.assertTrue(resultado)
        self.assertNotIn("1002", self.gestion.usuarios)

    def test_eliminar_usuario_inexistente(self):
        resultado = self.gestion.eliminar_usuario("9999")
        self.assertFalse(resultado)

if __name__ == '__main__':
    unittest.main()
