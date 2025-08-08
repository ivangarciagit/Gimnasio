
from funciones import dataframe, val_nombre, delay, ingreso_verificar_id
from clases_tablas import Tienda


def menu_Tienda(conn):
    while True:
        try:
            select = int(input("""
1 - Desea agregar una Tienda 
2 - Desea ver lista de Tiendas
3 - Desea Actualizar un dato  
4 - Desea Regresar al Menu anterior  
Ingrese su opción:   """))
        except ValueError:
            print("Por favor, ingresa un número válido.")
        if select == 1:
            nombre = val_nombre()  # Valida el nombre
            tienda = Tienda(conn)

            table = 'Sucursal'
            mensaje = 'Ingrese el ID de la sucursal que pertenece'
            sucursal_id = ingreso_verificar_id(
                conn, table, mensaje, mostrar_info_extra=True)
            conn.conectar()
            tienda.agregar(nombre, sucursal_id)
            print('Los Datos fueron insertados con exito..')
            conn.cerrar()
        elif select == 2:
            tienda = Tienda(conn)
            conn.conectar()
            tabla = tienda.listar()
            conn.cerrar()
            dataframe(tabla)
            delay(3)
        elif select == 3:
            tienda = Tienda(conn)
            table = 'Tienda'
            mensaje = 'Ingresa el ID de la tienda que deseas actualizar : '
            tienda_id = ingreso_verificar_id(conn, table, mensaje)
            while True:
                try:
                    sel_campo = int(input("""
Selecciona el campo que deseas actualizar
1 - Nombre
2 - Sucursal id
Ingrese su opción:   """))
                except ValueError:
                    print("Por favor, ingresa un número válido.")
                if sel_campo == 1:
                    campo = 'nombre'
                    nuevo_valor = val_nombre()
                    break

                elif sel_campo == 2:
                    campo = 'sucursal_id'
                    tienda = Tienda(conn)
                    table = 'Sucursal'
                    mensaje = 'Ingresa el ID de la sucursal que deseas asignar esta tienda '
                    nuevo_valor = ingreso_verificar_id(
                        conn, table, mensaje, mostrar_info_extra=True)
                    break
            conn.conectar()
            tienda.actualizar_campo(tienda_id, campo, nuevo_valor)
            conn.cerrar()

        elif select == 4:
            break
        else:
            print("Opción no válida, intenta otra vez.")
