from funciones import dataframe, ingreso_verificar_id, delay, validar_fecha, validar_precio
from clases_tablas import Venta


def menu_Venta(conn):
    while True:
        try:
            select = int(input("""
1 - Desea agregar un Venta 
2 - Desea ver lista de Ventas
3 - Desea Actualizar un dato de la Venta 
4 - Desea Regresar al Menu anterior  
Ingrese su opción:   """))
        except ValueError:
            print("Por favor, ingresa un número válido.")
        if select == 1:  # Ingresar Datos
            venta = Venta(conn)
            table = 'Tienda'  # Verificar que el ID del usuario existe
            mensaje = 'Ingrese el ID de la Tienda asociada a la venta'
            tienda_id = ingreso_verificar_id(
                conn, table, mensaje, mostrar_info_extra=True)
            table = 'Usuarios'
            mensaje = 'Ingrese el ID  del Usuario que hizo la compra'
            usuario_id = ingreso_verificar_id(
                conn, table, mensaje, mostrar_info_extra=True)
            fecha = validar_fecha()
            mensaje = 'Cual fue el total de la venta :'
            total = validar_precio(mensaje)
            conn.conectar()
            venta.agregar(tienda_id, usuario_id, fecha, total)
            print('Los Datos fueron insertados con exito..')
            conn.cerrar()
        elif select == 2:  # Listar Datos
            venta = Venta(conn)
            conn.conectar()
            tabla = venta.listar()
            conn.cerrar()
            dataframe(tabla)
            delay(3)
        elif select == 3:  # Actualizar Datos
            venta = Venta(conn)
            table = 'Venta'
            mensaje = 'Ingrese el ID de la Venta'
            venta_id = ingreso_verificar_id(conn, table, mensaje)
            while True:
                try:
                    sel_campo = int(input("""
Selecciona el campo que deseas actualizar
1 - tienda_id
2 - usuario_id
3 - fecha
4 - total
Ingrese su opción:   """))
                except ValueError:
                    print("Por favor, ingresa un número válido.")
                if sel_campo == 1:
                    campo = 'tienda_id'
                    table = 'Tienda'
                    mensaje = 'Ingresa el ID de la tienda que quiere asignar la Venta'
                    nuevo_valor = ingreso_verificar_id(
                        conn, table, mensaje, mostrar_info_extra=True)
                    break

                elif sel_campo == 2:
                    campo = 'usuario_id'
                    table = 'Usuarios'
                    mensaje = 'Ingresa el ID del Usuario que quiere asignar la Venta'
                    nuevo_valor = ingreso_verificar_id(
                        conn, table, mensaje, mostrar_info_extra=True)
                    break

                elif sel_campo == 3:
                    campo = 'fecha'
                    nuevo_valor = validar_fecha()
                    break
                elif sel_campo == 4:
                    campo = 'total'
                    mensaje = 'Ingrese el Total de la Venta :'
                    nuevo_valor = validar_precio(mensaje)
                    break

                else:
                    print('Opcion no valida')
            conn.conectar()
            venta.actualizar_campo(venta_id, campo, nuevo_valor)
            conn.cerrar()
        elif select == 4:
            break
        else:
            print("Opción no válida, intenta otra vez.")
