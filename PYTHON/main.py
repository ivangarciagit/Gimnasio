
from menu_Usuario import menu_Usuarios
from menu_Sucursal import menu_Sucursal
from menu_Tienda import menu_Tienda
from menu_provedor import menu_Provedor
from menu_producto import menu_Producto
from menu_Venta import menu_Venta
from menu_detalle_venta import menu_venta_detalle


from conexion import ConexionDB

conn = ConexionDB()


def main():
    while True:
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
8 - Entrar a detalle_venta
9 - Salir
Ingrese su opción:   """))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
        if opcion == 1:  # Opciones de Usuarios
            menu_Usuarios(conn)
        elif opcion == 2:  # Opciones de Sucursal
            menu_Sucursal(conn)
        elif opcion == 3:  # Opciones de Estacionamiento
            pass
        elif opcion == 4:  # Opciones de Tienda
            menu_Tienda(conn)
        elif opcion == 5:  # Opciones de provedor
            menu_Provedor(conn)
        elif opcion == 6:  # Opciones de producto
            menu_Producto(conn)
        elif opcion == 7:  # Opciones de Venta
            menu_Venta(conn)
        elif opcion == 8:  # Opciones de Venta
            menu_venta_detalle(conn)
        elif opcion == 9:
            print('Saliendo del menu....')
            break


main()
