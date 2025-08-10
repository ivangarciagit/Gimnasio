from funciones import ingreso_verificar_id, cantidad_producto
from clases_tablas import Detalle_venta


def subtotal_detalle(conn):
    detalles = []
    detalle = Detalle_venta(conn)
    tabla = 'Producto'
    mensaje = 'Ingrese el ID del producto vendido: '
    id_producto = ingreso_verificar_id(
        conn, tabla, mensaje, mostrar_info_extra=True)
    cantidad = cantidad_producto()
    precio = detalle.obtener_precio_producto(id_producto, conn)
    subtotal = precio * cantidad
    detalles.append({
        'id_producto': id_producto,
        'cantidad': cantidad,
        'subtotal': subtotal})
    while True:
        opcion = input(
            "Presione 1 para agregar producto a la venta, 0 para salir: ").strip()

        if opcion == '1':
            tabla = 'Producto'
            mensaje = 'Ingrese el ID del producto vendido: '
            id_producto = ingreso_verificar_id(conn, tabla, mensaje)
            cantidad = cantidad_producto()
            conn.conectar()
            precio = detalle.obtener_precio_producto(id_producto, conn)
            conn.cerrar()
            subtotal = precio * cantidad
            detalles.append({
                'id_producto': id_producto,
                'cantidad': cantidad,
                'subtotal': subtotal
            })

        elif opcion == '0':
            total = sum(item['subtotal'] for item in detalles)
            return total, detalles

        else:
            print("Error: opción inválida. Por favor, presione 1 o 0.")


def menu_venta_detalle():
    pass
