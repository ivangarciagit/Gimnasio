import pandas as pd
import re
import time


def existe_id(conexion, tabla, usuario_id):  # Valida si el ID existe en la base de datos
    tablas_permitidas = ['Usuarios', 'Estacionamiento',
                         'Sucursal', 'Tienda', 'Producto', 'Venta']

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


def mostrar_sucursales(conn):
    from clases_tablas import Sucursal
    sucursal = Sucursal(conn)
    conn.conectar()
    tabla = sucursal.listar()
    conn.cerrar()
    dataframe(tabla)
    delay(3)


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
                        mostrar_sucursales(conn)
                        print('Estas son las sucursales, corrobore el ID de la suya')
                        delay(2)
            else:
                print("Ingresa una ID valida")
    finally:
        conn.cerrar()
