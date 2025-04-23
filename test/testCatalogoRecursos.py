import unittest
from src.catalogo_recursos import CatalogoRecursos

class TestCatalogoRecursos(unittest.TestCase):

    def setUp(self):
        # Crea una instancia de CatalogoRecursos antes de cada prueba
        self.catalogo = CatalogoRecursos()

    def test_buscar_categoria(self):
        # Prueba de búsqueda por categoría
        self.catalogo.agregar_recurso(1, "Libro A", "Autor X", "Categoría 1")
        self.catalogo.agregar_recurso(2, "Libro B", "Autor Y", "Categoría 2")

        resultado = self.catalogo.buscar_por_categoria("Categoría 1")
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0]['titulo'], "Libro A")

    def test_buscar_libro_por_titulo(self):
        # Prueba de búsqueda por título
        self.catalogo.agregar_recurso(1, "Libro A", "Autor X", "Categoría 1")
        self.catalogo.agregar_recurso(2, "Libro B", "Autor Y", "Categoría 2")

        resultado = self.catalogo.buscar_por_titulo("Libro A")
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0]['titulo'], "Libro A")

    def test_buscar_recurso_inexistente(self):
        # Prueba de búsqueda de recurso que no existe
        resultado = self.catalogo.buscar_por_titulo("Libro Inexistente")
        self.assertEqual(len(resultado), 0)

if __name__ == "__main__":
    unittest.main()
