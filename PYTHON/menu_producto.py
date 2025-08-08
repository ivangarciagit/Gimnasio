from funciones import dataframe, ingreso_verificar_id, val_nombre, delay, val_descripcion, validar_precio
from clases_tablas import Producto


def menu_Producto(conn):
    while True:
        try:
            select = int(input("""
1 - Desea agregar un Producto 
2 - Desea ver lista de Productos
3 - Desea Actualizar   
4 - Desea Regresar al Menu anterior  
Ingrese su opción:   """))
        except ValueError:
            print("Por favor, ingresa un número válido.")
        if select == 1:  # Ingresar Datos y validarlos
            producto = Producto(conn)
            nombre = val_nombre()
            descripcion = val_descripcion()
            precio = validar_precio()
            tabla = 'Provedor'
            mensaje = 'Ingresa el ID de tu Provedor'
            provedor_id = ingreso_verificar_id(
                conn, tabla, mensaje, mostrar_info_extra=True)  # Validar que el provedor existe
            conn.conectar()
            producto.agregar(nombre, descripcion, precio, provedor_id)
            print('Los Datos fueron insertados con exito..')
            conn.cerrar()
        elif select == 2:  # Listar Datos
            producto = Producto(conn)
            conn.conectar()
            tabla = producto.listar()
            conn.cerrar()
            dataframe(tabla)
            delay(3)
        elif select == 3:  # Actualizar Datos
            producto = Producto(conn)
            table = 'Producto'
            mensaje = 'Ingrese el ID del Producto que deseas actualizar'
            producto_id = ingreso_verificar_id(conn, table, mensaje)
            while True:
                try:
                    sel_campo = int(input("""
Selecciona el campo que deseas actualizar
1 - Nombre
2 - Descripcion
3 - Precio
4 - Provedor_id
Ingrese su opción:   """))
                except ValueError:
                    print("Por favor, ingresa un número válido.")
                if sel_campo == 1:
                    campo = 'nombre'
                    nuevo_valor = val_nombre()
                    break

                elif sel_campo == 2:
                    campo = 'descripcion'
                    nuevo_valor = val_descripcion()
                    break

                elif sel_campo == 3:
                    campo = 'precio'
                    nuevo_valor = validar_precio()
                    break
                elif sel_campo == 4:
                    campo = 'provedor_id'
                    tabla = 'Provedor'
                    mensaje = 'Ingresa el ID de tu Provedor'
                    nuevo_valor = ingreso_verificar_id(
                        conn, tabla, mensaje, mostrar_info_extra=True)  # Validar que el provedor existe
                    break
                else:
                    print('Opcion no valida')
            conn.conectar()
            producto.actualizar_campo(producto_id, campo, nuevo_valor)
            conn.cerrar()
        elif select == 4:
            break
        else:
            print("Opción no válida, intenta otra vez.")
