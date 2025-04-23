
class PrestamosReservas:
    def __init__(self):
        self.prestamos = []
        self.recursos_disponibles = {}

    def registrar_recurso(self, codigo, cantidad):
        self.recursos_disponibles[codigo] = self.recursos_disponibles.get(codigo, 0) + cantidad

    def registrar_prestamo(self, usuario_id, recurso_codigo, cantidad, fecha_inicio, fecha_fin):
        disponibles = self.recursos_disponibles.get(recurso_codigo, 0)

        if disponibles >= cantidad:
            self.prestamos.append({
                "usuario_id": usuario_id,
                "recurso_codigo": recurso_codigo,
                "cantidad": cantidad,
                "fecha_inicio": fecha_inicio,
                "fecha_fin": fecha_fin
            })
            self.recursos_disponibles[recurso_codigo] -= cantidad
            print("Préstamo registrado exitosamente.")
        else:
            print(" El recurso no está disponible en la cantidad solicitada.")

    def listar_prestamos(self):
        if not self.prestamos:
            print("No hay préstamos registrados.")
            return
        for p in self.prestamos:
            print(f"Usuario: {p['usuario_id']} | Recurso: {p['recurso_codigo']} | "
                  f"Cantidad: {p['cantidad']} | Desde: {p['fecha_inicio']} hasta: {p['fecha_fin']}")
