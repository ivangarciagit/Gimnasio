from funciones import dataframe, ingreso_verificar_id, val_nombre, val_direccion
from clases_tablas import Sucursal
from funciones import delay


def menu_Sucursal(conn):
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
        if select == 1:  # Insertar Dato
            sucursal = Sucursal(conn)
            nombre_suc = val_nombre()
            direccion = val_direccion()
            conn.conectar()
            sucursal.agregar(nombre_suc, direccion)
            print('Los Datos fueron insertados con exito..')
            conn.cerrar()
        elif select == 2:  # Listar Datos
            sucursal = Sucursal(conn)
            conn.conectar()
            tabla = sucursal.listar()
            conn.cerrar()
            dataframe(tabla)
            delay(3)
        elif select == 3:  # Actualizar Datos
            sucursal = Sucursal(conn)
            table = 'Sucursal'
            mensaje = 'Ingrese el ID de la Sucursal'
            sucursal_id = ingreso_verificar_id(
                conn, table, mensaje)  # Inrgeso y verifica la ID
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
            conn.conectar()
            sucursal.actualizar_campo(sucursal_id, campo, nuevo_valor)
            conn.cerrar()
        elif select == 4:
            break
