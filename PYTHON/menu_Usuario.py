from funciones import dataframe, ingreso_verificar_id, val_nombre, val_correo, val_auto, delay
from clases_tablas import Usuarios


def menu_Usuarios(conn):
    while True:
        try:
            select = int(input("""
1 - Desea agregar un Usuario 
2 - Desea ver lista de Usuario
3 - Desea Actualizar un dato  
4 - Desea Regresar al Menu anterior  
Ingrese su opción:   """))
        except ValueError:
            print("Por favor, ingresa un número válido.")
        if select == 1:
            usuario = Usuarios(conn)
            nombre = val_nombre()  # Valida el nombre
            correo = val_correo()  # Valida correo
            vehiculo = val_auto()   # Valida auto
            conn.conectar()
            usuario.agregar(nombre, correo, vehiculo)
            print('Los Datos fueron insertados con exito..')
            conn.cerrar()
        elif select == 2:
            usuario = Usuarios(conn)
            conn.conectar()
            tabla = usuario.listar()
            conn.cerrar()
            dataframe(tabla)
            delay(3)
        elif select == 3:
            usuario = Usuarios(conn)
            table = 'Usuarios'
            mensaje = 'Ingrese el ID del Usuario'
            # Ingresa y verifica que la ID exista
            usuario_id = ingreso_verificar_id(conn, table, mensaje)
            while True:
                try:
                    sel_campo = int(input("""
Selecciona el campo que deseas actualizar
1 - Nombre
2 - Correo
3 - Vehiculo
Ingrese su opción:   """))
                except ValueError:
                    print("Por favor, ingresa un número válido.")
                if sel_campo == 1:
                    campo = 'nombre'
                    nuevo_valor = val_nombre()
                    break

                elif sel_campo == 2:
                    campo = 'correo'
                    nuevo_valor = val_correo()
                    break

                elif sel_campo == 3:
                    campo = 'vehiculo'
                    nuevo_valor = val_auto()
                    break

                else:
                    print('Opcion no valida')
            conn.conectar()
            usuario.actualizar_campo(usuario_id, campo, nuevo_valor)
            conn.cerrar()
        elif select == 4:
            break
        else:
            print("Opción no válida, intenta otra vez.")
