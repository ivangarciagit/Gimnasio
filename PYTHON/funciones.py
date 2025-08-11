import pandas as pd
import re
import time
from datetime import datetime, date


def existe_id(conexion, tabla, usuario_id):  # Valida si el ID existe en la base de datos
    tablas_permitidas = ['Usuarios', 'Estacionamiento',
                         'Sucursal', 'Tienda', 'Producto', 'Venta', 'Provedor', 'Detalle_venta']

    if tabla not in tablas_permitidas:
        raise ValueError(
            f"La tabla '{tabla}' no está permitida para esta consulta.")

    cursor = conexion.cursor()
    query = f"SELECT 1 FROM {tabla} WHERE id = %s LIMIT 1"
    cursor.execute(query, (usuario_id,))
    resultado = cursor.fetchone()
    cursor.close()
    return resultado is not None


def dataframe(lista):  # Crea Data Frame
    df = pd.DataFrame(lista)
    print(df)


def val_nombre():  # Valida que no este vacio el nombre
    while True:
        nombre = input("Agrega tu nombre: ").strip()
        if nombre:
            return nombre
        else:
            print("El nombre no puede estar vacío. Intenta de nuevo.")


def val_descripcion():  # Valida que no este vacio
    while True:
        nombre = input("Agrega la descripcion: ").strip()
        if nombre:
            return nombre
        else:
            print("El nombre no puede estar vacío. Intenta de nuevo.")


def val_direccion():  # Valida que no este vacio el nombre
    while True:
        nombre = input("Agrega la Direccion:  ").strip()
        if nombre:
            return nombre
        else:
            print("El nombre no puede estar vacío. Intenta de nuevo.")


def val_correo():  # Valida si tiene correo
    patron_email = r'[^@]+@[^@]+\.[^@]+'
    while True:
        correo = input('Ingresa tu correo: ').strip()
        if re.match(patron_email, correo):
            return correo
        print("Correo inválido. Intenta con un formato ejemplo@dominio.com")


def val_auto():   # Valida si tiene carro
    while True:
        entrada = ''
        entrada = input('Si tiene carro ingresa 1 si no ingresa 0 :  ')
        if entrada == '1' or entrada == '0':
            vehiculo = int(entrada)
            return vehiculo
        else:
            print("Por favor, ingresa solo 1 o 0.")


def delay(tiempo):
    time.sleep(tiempo)


def mostrar_sucursales(conn, table):
    if table == 'Sucursal':
        from clases_tablas import Sucursal
        sucursal = Sucursal(conn)
        tabla = sucursal.listar()
        dataframe(tabla)
        delay(2)
    elif table == 'Provedor':
        from clases_tablas import Provedor
        provedor = Provedor(conn)
        tabla = provedor.listar()
        dataframe(tabla)
        delay(2)
    elif table == 'Tienda':
        from clases_tablas import Tienda
        tienda = Tienda(conn)
        tabla = tienda.listar()
        dataframe(tabla)
        delay(2)
    elif table == 'Usuarios':
        from clases_tablas import Usuarios
        usuarios = Usuarios(conn)
        tabla = usuarios.listar()
        dataframe(tabla)
        delay(2)
    elif table == 'Producto':
        from clases_tablas import Producto
        producto = Producto(conn)
        tabla = producto.listar()
        dataframe(tabla)
        delay(2)

    else:
        pass


def ingreso_verificar_id(conn, tabla, mensaje, mostrar_info_extra=False):
    conn.conectar()
    try:
        while True:
            entrada = input(mensaje + ": ")
            if entrada.isdigit() and int(entrada) >= 1:
                id_verificada = int(entrada)
                if existe_id(conn.conn, tabla, id_verificada):
                    print(f"La ID {id_verificada} existe.")
                    return id_verificada
                else:
                    print(
                        "ID errónea, no existe en la base de datos. Intenta de nuevo.")
                    if mostrar_info_extra:
                        mostrar_sucursales(conn, tabla)
                        print('Estas son las ID, corrobore el ID de la suya')
                        delay(2)
            else:
                print("Ingresa una ID valida")
    finally:
        conn.cerrar()


def validar_precio(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            precio = float(entrada)
            if precio < 0:
                print("El precio debe ser un número positivo.")
                continue
            return round(precio, 2)
        except ValueError:
            print("Por favor, ingresa un número válido.")


def validar_fecha():
    while True:
        fecha_in = input("Ingrese una fecha en formato dd/mm/yyyy: ")
        try:
            fecha = datetime.strptime(fecha_in, "%d/%m/%Y")
            return fecha
        except ValueError:
            print("Fecha inválida. Por favor, inténtelo de nuevo.")


def asignar_fecha():
    return date.today()


def cantidad_producto():
    while True:
        entrada = input('Ingrese la cantidad de productos vendidos: ')
        try:
            numero = int(entrada)
            if numero <= 0:
                print("El número debe ser mayor a 0 y entero")
                continue
            return numero
        except ValueError:
            print("Por favor, ingresa un número entero válido.")
