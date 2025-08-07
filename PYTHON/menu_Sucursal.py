from funciones import dataframe, existe_id, val_nombre, val_direccion
from conexion import ConexionDB
from clases_tablas import Sucursal
from funciones import delay
conn = ConexionDB()


def menu_Sucursal():
    while True:
        try:
            select = int(input("""
1 - Desea agregar una Sucursal
2 - Desea ver lista de Sucursales
3 - Desea Actualizar un dato  
4 - Desea Regresar al Menu anterior  
Ingrese su opción:   """))
        except ValueError:
            print("Por favor, ingresa un número válido.")
        if select == 1:
            sucursal = Sucursal(conn)
            nombre_suc = val_nombre()
            direccion = val_direccion()
            conn.conectar()
            sucursal.agregar(nombre_suc, direccion)
            print('Los Datos fueron insertados con exito..')
            conn.cerrar()
        elif select == 2:
            sucursal = Sucursal(conn)
            conn.conectar()
            tabla = sucursal.listar()
            conn.cerrar()
            dataframe(tabla)
            delay(3)
        elif select == 3:
            sucursal = Sucursal(conn)
            conn.conectar()
            tabla = 'Sucursal'
            while True:  # Ingresar el id
                entrada = input("Ingresa el ID : ")
                if entrada.isdigit() and int(entrada) >= 1:
                    sucursal_id = int(entrada)
                    if existe_id(conn.conn, tabla, sucursal_id):  # Validar el ID
                        print(
                            f"El usuario con ID {sucursal_id} existe.")
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
1 - Nombre de la Sucursal
2 - Direccion
Ingrese su opción:   """))
                except ValueError:
                    print("Por favor, ingresa un número válido.")
                if sel_campo == 1:
                    campo = 'nombre'
                    nuevo_valor = val_nombre()
                    break
                elif sel_campo == 2:
                    campo = 'direccion'
                    nuevo_valor = val_direccion()
                    break
                else:
                    print('Opcion no valida')
            sucursal.actualizar_campo(sucursal_id, campo, nuevo_valor)
            conn.cerrar()
        elif select == 4:
            break
