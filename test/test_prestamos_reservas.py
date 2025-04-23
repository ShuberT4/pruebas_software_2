import unittest
from src.prestamos_reservas import PrestamosReservas  
class TestPrestamosReservas(unittest.TestCase):

    def setUp(self):
        # Crea una instancia de PrestamosReservas antes de cada prueba
        self.prestamos_reservas = PrestamosReservas()
        self.prestamos_reservas.registrar_recurso("1", 5)  # Agregar recursos al inicio

    def test_registrar_prestamo(self):
        # Prueba de préstamo de un recurso
        self.prestamos_reservas.registrar_prestamo("usuario1", "1", 2, "2025-04-25", "2025-04-30")
        prestamos = self.prestamos_reservas.prestamos
        self.assertEqual(len(prestamos), 1)
        self.assertEqual(prestamos[0]["usuario_id"], "usuario1")
        self.assertEqual(prestamos[0]["recurso_codigo"], "1")
        self.assertEqual(prestamos[0]["cantidad"], 2)

    def test_prestamo_no_disponible(self):
        # Prueba de préstamo cuando el recurso no está disponible
        self.prestamos_reservas.registrar_prestamo("usuario1", "1", 10, "2025-04-25", "2025-04-30")
        # Debería decir que el recurso no está disponible
        prestamos = self.prestamos_reservas.prestamos
        self.assertEqual(len(prestamos), 0)  # No debe haber préstamo registrado

if __name__ == "__main__":
    unittest.main()
