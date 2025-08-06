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

    try:
        cursor.execute(query, (usuario_id,))
        resultado = cursor.fetchone()
    except Exception as e:
        cursor.close()
        print(f"Error en la consulta: {e}")
        return False

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
