class GestionEjemplares:
    def __init__(self):
        self.ejemplares = {}

    def agregar_ejemplar(self, codigo, titulo, autor, ano, categoria):
        if codigo not in self.ejemplares:
            self.ejemplares[codigo] = {
                "titulo": titulo,
                "autor": autor,
                "ano": ano,
                "categoria": categoria
            }
            print(f" Ejemplar '{titulo}' agregado exitosamente.")
        else:
            print(" El código del ejemplar ya existe.")

    def editar_ejemplar(self, codigo, nuevo_titulo=None, nuevo_autor=None, nuevo_ano=None, nueva_categoria=None):
        ejemplar = self.ejemplares.get(codigo)
        if ejemplar:
            if nuevo_titulo:
                ejemplar["titulo"] = nuevo_titulo
            if nuevo_autor:
                ejemplar["autor"] = nuevo_autor
            if nuevo_ano:
                ejemplar["ano"] = nuevo_ano
            if nueva_categoria:
                ejemplar["categoria"] = nueva_categoria
            print(f" Ejemplar '{codigo}' editado exitosamente.")
        else:
            print(" Ejemplar no encontrado.")

    def eliminar_ejemplar(self, codigo):
        if codigo in self.ejemplares:
            del self.ejemplares[codigo]
            print(f" Ejemplar '{codigo}' eliminado exitosamente.")
        else:
            print(" El ejemplar no existe.")

    def listar_ejemplares(self):
        if not self.ejemplares:
            print("No hay ejemplares registrados.")
            return
        for codigo, datos in self.ejemplares.items():
            print(f"Código: {codigo} | Título: {datos['titulo']} | Autor: {datos['autor']} | "
                  f"Año: {datos['ano']} | Categoría: {datos['categoria']}")
