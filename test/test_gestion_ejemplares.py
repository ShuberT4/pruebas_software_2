import unittest
from src.gestion_ejemplares import GestionEjemplares  

class TestGestionEjemplares(unittest.TestCase):

    def setUp(self):
        # Crea una instancia de GestionEjemplares antes de cada prueba
        self.gestion = GestionEjemplares()

    def test_agregar_ejemplar(self):
        # Prueba para agregar un ejemplar
        self.gestion.agregar_ejemplar("001", "Libro A", "Autor X", 2020, "Ficción")
        ejemplares = self.gestion.ejemplares
        self.assertEqual(len(ejemplares), 1)
        self.assertEqual(ejemplares["001"]["titulo"], "Libro A")

    def test_editar_ejemplar(self):
        # Prueba para editar un ejemplar existente
        self.gestion.agregar_ejemplar("001", "Libro A", "Autor X", 2020, "Ficción")
        self.gestion.editar_ejemplar("001", nuevo_titulo="Libro A Editado")
        ejemplares = self.gestion.ejemplares
        self.assertEqual(ejemplares["001"]["titulo"], "Libro A Editado")

    def test_eliminar_ejemplar(self):
        # Prueba para eliminar un ejemplar
        self.gestion.agregar_ejemplar("001", "Libro A", "Autor X", 2020, "Ficción")
        self.gestion.eliminar_ejemplar("001")
        ejemplares = self.gestion.ejemplares
        self.assertEqual(len(ejemplares), 0)

if __name__ == "__main__":
    unittest.main()
