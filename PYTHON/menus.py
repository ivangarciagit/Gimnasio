

def menu_princial():
    try:
        opcion = int(input("""
Hola, bienvenido a la aplicación del Gimnasio. ¿Qué desea hacer?
Presione el número de la opción:

1 - Entrar a Usuarios
2 - Entrar a Sucursal
3 - Entrar a Estacionamiento
4 - Entrar a Tienda
5 - Entrar a Proveedor
6 - Entrar a Producto
7 - Entrar a Venta
8 - Entrar a DetalleVenta
9 - Salir
Ingrese su opción:   """))
        return opcion
    except ValueError:
        print("Por favor, ingresa un número válido.")
