
from src.prestamos_reservas import PrestamosReservas
from src.gestor_usuario import GestionUsuarios
from src.catalogo_recursos import CatalogoRecursos
from src.gestion_ejemplares import GestionEjemplares
from src.panel_administrativo import PanelAdministrativo

def menu_usuarios(gestor):
    while True:
        print("\n--- Menú de Gestión de Usuarios ---")
        print("1. Crear usuario")
        print("2. Eliminar usuario")
        print("3. Listar usuarios")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombres = input("Nombres: ")
            apellidos = input("Apellidos: ")
            identificacion = input("Identificación: ")
            correo = input("Correo institucional: ")
            contrasena = input("Contraseña: ")
            gestor.crear_usuario(nombres, apellidos, identificacion, correo, contrasena)
        elif opcion == "2":
            identificacion = input("Ingrese la identificación del usuario a eliminar: ")
            gestor.eliminar_usuario(identificacion)
        elif opcion == "3":
            gestor.listar_usuarios()
        elif opcion == "4":
            break
        else:
            print("Opción no válida")

def menu_catalogo(catalogo):
    while True:
        print("\n--- Menú del Catálogo de Recursos ---")
        print("1. Agregar recurso")
        print("2. Buscar por título")
        print("3. Buscar por categoría")
        print("4. Listar todos los recursos")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            anio = input("Año de publicación: ")
            catalogo.agregar_recurso(titulo, autor, categoria, anio)
        elif opcion == "2":
            titulo = input("Ingrese el título a buscar: ")
            catalogo.buscar_por_titulo(titulo)
        elif opcion == "3":
            categoria = input("Ingrese la categoría a buscar: ")
            catalogo.buscar_por_categoria(categoria)
        elif opcion == "4":
            catalogo.listar_catalogo()
        elif opcion == "5":
            break
        else:
            print("Opción no válida")

def menu_principal():
    gestor_usuarios = GestionUsuarios()
    catalogo = CatalogoRecursos()
    prestamos = PrestamosReservas()
    gestion_ejemplares = GestionEjemplares()
    panel_admin = PanelAdministrativo(gestor_usuarios)

    while True:
        print("\n===== Sistema de Gestión de Biblioteca Digital =====")
        print("1. Gestión de Usuarios")
        print("2. Catálogo de Recursos")
        print("3. Préstamos y Reservas")
        print("4. Gestión de Ejemplares")
        print("5. Panel Administrativo")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_usuarios(gestor_usuarios)
        elif opcion == "2":
            menu_catalogo(catalogo)
        elif opcion == "3":
            menu_prestamos(prestamos)
        elif opcion == "4":
            menu_ejemplares(gestion_ejemplares)
        elif opcion == "5":
            menu_panel_administrativo(panel_admin)
        elif opcion == "6":
            print("Saliendo del sistema")
            break     

if __name__ == "__main__":
    menu_principal()

def menu_prestamos(prestamos):
    while True:
        print("\n--- Menú de Préstamos y Reservas ---")
        print("1. Registrar recurso disponible")
        print("2. Registrar préstamo")
        print("3. Listar préstamos")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo = input("Código del recurso: ")
            cantidad = int(input("Cantidad disponible: "))
            prestamos.registrar_recurso(codigo, cantidad)
        elif opcion == "2":
            usuario_id = input("ID del usuario: ")
            recurso_codigo = input("Código del recurso: ")
            cantidad = int(input("Cantidad a prestar: "))
            fecha_inicio = input("Fecha de inicio (dd/mm/aaaa): ")
            fecha_fin = input("Fecha de fin (dd/mm/aaaa): ")
            prestamos.registrar_prestamo(usuario_id, recurso_codigo, cantidad, fecha_inicio, fecha_fin)
        elif opcion == "3":
            prestamos.listar_prestamos()
        elif opcion == "4":
            break
        else:
            print("Opción no válida")

def menu_ejemplares(gestion):
    while True:
        print("\n--- Menú de Gestión de Ejemplares ---")
        print("1. Agregar ejemplar")
        print("2. Editar ejemplar")
        print("3. Eliminar ejemplar")
        print("4. Listar ejemplares")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo = input("Código del ejemplar: ")
            titulo = input("Título del ejemplar: ")
            autor = input("Autor del ejemplar: ")
            ano = input("Año de publicación: ")
            categoria = input("Categoría del ejemplar: ")
            gestion.agregar_ejemplar(codigo, titulo, autor, ano, categoria)
        elif opcion == "2":
            codigo = input("Código del ejemplar a editar: ")
            nuevo_titulo = input("Nuevo título (deja vacío para no cambiar): ")
            nuevo_autor = input("Nuevo autor (deja vacío para no cambiar): ")
            nuevo_ano = input("Nuevo año (deja vacío para no cambiar): ")
            nueva_categoria = input("Nueva categoría (deja vacío para no cambiar): ")
            gestion.editar_ejemplar(codigo, nuevo_titulo, nuevo_autor, nuevo_ano, nueva_categoria)
        elif opcion == "3":
            codigo = input("Código del ejemplar a eliminar: ")
            gestion.eliminar_ejemplar(codigo)
        elif opcion == "4":
            gestion.listar_ejemplares()
        elif opcion == "5":
            break
        else:
            print("Opción no válida")

def menu_panel_administrativo(panel):
    while True:
        print("\n--- Panel Administrativo ---")
        print("1. Cambiar estado de usuario")
        print("2. Eliminar usuario")
        print("3. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            identificacion = input("ID del usuario: ")
            nuevo_estado = input("Nuevo estado (activo, bloqueado, desactivado): ").lower()
            panel.cambiar_estado_usuario(identificacion, nuevo_estado)
        elif opcion == "2":
            identificacion = input("ID del usuario a eliminar: ")
            panel.eliminar_usuario(identificacion)
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")
