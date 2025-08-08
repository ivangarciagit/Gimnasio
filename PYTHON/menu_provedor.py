from funciones import dataframe, ingreso_verificar_id, val_nombre, val_correo, delay
from clases_tablas import Provedor


def menu_Provedor(conn):
    while True:
        try:
            select = int(input("""
1 - Desea agregar un Provedor 
2 - Desea ver lista de Provedores
3 - Desea Actualizar un dato  
4 - Desea Regresar al Menu anterior  
Ingrese su opción:   """))
        except ValueError:
            print("Por favor, ingresa un número válido.")
        if select == 1:  # Ingresar Datos
            provedor = Provedor(conn)
            nombre = val_nombre()
            correo = val_correo()
            conn.conectar()
            provedor.agregar(nombre, correo)
            print('Los Datos fueron insertados con exito..')
            conn.cerrar()
        elif select == 2:  # Listar Datos
            provedor = Provedor(conn)
            conn.conectar()
            tabla = provedor.listar()
            conn.cerrar()
            dataframe(tabla)
            delay(3)
        elif select == 3:  # Actualizar Datos
            provedor = Provedor(conn)
            table = 'Provedor'
            mensaje = 'Ingrese el ID del Provedor'
            provedor_id = ingreso_verificar_id(conn, table, mensaje)
            while True:
                try:
                    sel_campo = int(input("""
Selecciona el campo que deseas actualizar
1 - Nombre
2 - Correo
Ingrese su opción:   """))
                except ValueError:
                    print("Por favor, ingresa un número válido.")
                if sel_campo == 1:
                    campo = 'nombre'
                    nuevo_valor = val_nombre()
                    break

                elif sel_campo == 2:
                    campo = 'contacto'
                    nuevo_valor = val_correo()
                    break
                else:
                    print('Opcion no valida')
            conn.conectar()
            provedor.actualizar_campo(provedor_id, campo, nuevo_valor)
            conn.cerrar()
        elif select == 4:
            break
        else:
            print("Opción no válida, intenta otra vez.")
