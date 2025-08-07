
from funciones import dataframe, existe_id, val_nombre, delay
from conexion import ConexionDB
from clases_tablas import Tienda, Sucursal
conn = ConexionDB()


def mostrar_sucursales():
    sucursal = Sucursal(conn)
    conn.conectar()
    tabla = sucursal.listar()
    conn.cerrar()
    dataframe(tabla)
    delay(3)


def menu_Tienda():
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

            tabla = 'Sucursal'
            while True:  # Ingresar el id
                entrada = input(
                    "Ingresa el ID de la sucursal a la que pertences: ")
                if entrada.isdigit() and int(entrada) >= 1:
                    sucursal_id = int(entrada)
                    conn.conectar()
                    if existe_id(conn.conn, tabla, sucursal_id):  # Validar el ID
                        print(
                            f"La sucursal con ID {sucursal_id} existe.")
                        conn.cerrar()
                        break
                    else:
                        print(
                            "ID errónea, no existe en la base de datos. Intenta de nuevo.")
                        mostrar_sucursales()
                        print('Estas son las sucursales corrobore el ID de la suya')
                        delay(2)
                else:
                    print("Ingresa una ID valida")
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
            conn.conectar()
            tabla = 'Tienda'
            while True:  # Ingresar el id
                entrada = input(
                    "Ingresa el ID de la tienda que deseas actualizar : ")
                if entrada.isdigit() and int(entrada) >= 1:
                    tienda_id = int(entrada)
                    if existe_id(conn.conn, tabla, tienda_id):  # Validar el ID
                        print(
                            f"La tienda con ID {tienda_id} existe.")
                        break
                    else:
                        print(
                            "ID errónea, no existe en la base de datos. Intenta de nuevo.")
                else:
                    print("Ingresa una ID valida")
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
                    # Nuevo valor de id
                    tienda = Tienda(conn)

                    tabla = 'Sucursal'
                    while True:  # Ingresar el id
                        entrada = input(
                            "Ingresa el ID de la sucursal que deseas asignar esta tienda: ")
                        if entrada.isdigit() and int(entrada) >= 1:
                            nuevo_valor = int(entrada)
                            conn.conectar()
                            if existe_id(conn.conn, tabla, nuevo_valor):  # Validar el ID
                                print(
                                    f"La Sucursal con ID {nuevo_valor} existe.")
                                conn.cerrar()
                                break
                            else:
                                print(
                                    "ID errónea, no existe en la base de datos. Intenta de nuevo.")
                                mostrar_sucursales()
                                print(
                                    'Estas son las sucursales corrobore el ID de la suya')
                                delay(2)
                        else:
                            print("Ingresa una ID valida")
                else:
                    print('Opcion no valida')
                conn.conectar()
                tienda.actualizar_campo(tienda_id, campo, nuevo_valor)
                conn.cerrar()
                break
        elif select == 4:
            break
        else:
            print("Opción no válida, intenta otra vez.")
