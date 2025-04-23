

class CatalogoRecursos:
    def __init__(self):
        self.catalogo = []

    def agregar_recurso(self, titulo, autor, categoria, anio):
        recurso = {
            "titulo": titulo,
            "autor": autor,
            "categoria": categoria,
            "anio": anio
        }
        self.catalogo.append(recurso)
        print(f"Recurso '{titulo}' agregado exitosamente.")

    def buscar_por_titulo(self, titulo):
        resultados = [r for r in self.catalogo if r["titulo"].lower() == titulo.lower()]
        if resultados:
            print("Resultado(s) encontrado(s):")
            for r in resultados:
                print(r)
        else:
            print("No se encontraron recursos con ese título.")
            return resultados

    def buscar_por_categoria(self, categoria):
        resultados = [r for r in self.catalogo if r["categoria"].lower() == categoria.lower()]
        if resultados:
            print("Resultado(s) en la categoría:")
            for r in resultados:
                print(r)
        else:
            print("No se encontraron recursos en esa categoría.")
            return resultados 

    def listar_catalogo(self):
        if self.catalogo:
            print("Catálogo de recursos:")
            for r in self.catalogo:
                print(r)
        else:
            print("El catálogo está vacío.")
