from funciones import dataframe, existe_id, val_nombre, val_correo, val_auto, delay
from conexion import ConexionDB
from clases_tablas import Usuarios

conn = ConexionDB()


def menu_Usuarios():
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
            conn.conectar()
            tabla = 'Usuarios'
            while True:  # Ingresar el id
                entrada = input("Ingresa el ID : ")
                if entrada.isdigit() and int(entrada) >= 1:
                    usuario_id = int(entrada)
                    if existe_id(conn.conn, tabla, usuario_id):  # Validar el ID
                        print(
                            f"El usuario con ID {usuario_id} existe.")
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
            usuario.actualizar_campo(usuario_id, campo, nuevo_valor)
            conn.cerrar()
        elif select == 4:
            break
        else:
            print("Opción no válida, intenta otra vez.")
