from datetime import datetime
from funciones import delay


class Usuarios:
    def __init__(self, conexion):
        self.conexion = conexion

    def agregar(self, nombre, correo, vehiculo):
        query = "INSERT INTO Usuarios(nombre,correo,vehiculo) Values (%s,%s,%s)"
        self.conexion.ejecutar(query, (nombre, correo, vehiculo))
        print('Los datos se insertaron con exito...')
        delay(3)

    def listar(self):
        return self.conexion.consultar("SELECT * FROM Usuarios")

    def actualizar_campo(self, usuario_id, campo, nuevo_valor):

        query = f"UPDATE Usuarios SET {campo} = %s WHERE id = %s"
        self.conexion.ejecutar(query, (nuevo_valor, usuario_id))
        print('Los datos se actualizaron con exito...')
        delay(2)


class Sucursal:
    def __init__(self, conexion):
        self.conexion = conexion

    def agregar(self, nombre, direccion):
        query = "INSERT INTO Sucursal(nombre,direccion) Values (%s,%s)"
        self.conexion.ejecutar(query, (nombre, direccion))

    def listar(self):
        return self.conexion.consultar("SELECT * FROM Sucursal")

    def actualizar_campo(self, sucursal_id, campo, nuevo_valor):

        query = f"UPDATE Sucursal SET {campo} = %s WHERE id = %s"
        self.conexion.ejecutar(query, (nuevo_valor, sucursal_id))
        print('Los datos se actualizaron con exito...')
        delay(2)


class Estacionamiento:
    def __init__(self, conexion):
        self.conexion = conexion

    def agregar(self, usuario_id, estacionamiento_id, fecha_asignacion=None):
        if fecha_asignacion is None:
            fecha_asignacion = datetime.now().date()
        query = "INSERT INTO Permiso_estacionamiento(usuario_id,estacionamiento_id,fecha_asignacion) Values (%s,%s,%s)"
        self.conexion.ejecutar(
            query, (usuario_id, estacionamiento_id, fecha_asignacion))

    def listar(self):
        return self.conexion.consultar(
            """SELECT s.nombre AS sucursal,
        COUNT(e.id) AS total_lugares,
        SUM(CASE WHEN e.disponible = TRUE THEN 1 ELSE 0 END) AS lugares_disponibles
        FROM Estacionamiento e
        JOIN Sucursal s ON e.sucursal_id = s.id
        GROUP BY s.id, s.nombre;""")


class Tienda:
    def __init__(self, conexion):
        self.conexion = conexion

    def agregar(self, nombre, sucursal_id):
        query = "INSERT INTO Tienda(nombre,sucursal_id) Values (%s,%s)"
        self.conexion.ejecutar(
            query, (nombre, sucursal_id))

    def listar(self):
        return self.conexion.consultar(
            """SELECT 
        Tienda.id AS ID,
        Tienda.nombre AS nombre_tienda,
        Sucursal.nombre AS nombre_sucursal
        FROM Tienda
        JOIN Sucursal ON Tienda.sucursal_id = Sucursal.id;""")

    def actualizar_campo(self, tienda_id, campo, nuevo_valor):

        query = f"UPDATE Tienda SET {campo} = %s WHERE id = %s"
        self.conexion.ejecutar(query, (nuevo_valor, tienda_id))
        print('Los datos se actualizaron con exito...')
        delay(2)


class Provedor:
    def __init__(self, conexion):
        self.conexion = conexion

    def agregar(self, nombre, contacto):
        query = "INSERT INTO Provedor(nombre,contacto) Values (%s,%s)"
        self.conexion.ejecutar(
            query, (nombre, contacto))

    def listar(self):
        return self.conexion.consultar('SELECT * FROM Provedor')

    def actualizar_campo(self, provedor_id, campo, nuevo_valor):

        query = f"UPDATE Provedor SET {campo} = %s WHERE id = %s"
        self.conexion.ejecutar(query, (nuevo_valor, provedor_id))
        print('Los datos se actualizaron con exito...')
        delay(2)


class Producto:
    def __init__(self, conexion):
        self.conexion = conexion

    def agregar(self, nombre, descripcion, precio, provedor_id):
        query = "INSERT INTO Producto(nombre,descripcion,precio,provedor_id) Values (%s,%s,%s,%s)"
        self.conexion.ejecutar(
            query, (nombre, descripcion, precio, provedor_id))

    def listar(self):
        return self.conexion.consultar(
            """SELECT 
    Producto.id,
    Producto.nombre AS nombre_producto,
    Producto.descripcion,
    Producto.precio,
    Provedor.nombre AS provedor
    FROM Producto
    JOIN Provedor ON Producto.provedor_id = Provedor.id;""")

    def actualizar_campo(self, producto_id, campo, nuevo_valor):

        query = f"UPDATE Producto SET {campo} = %s WHERE id = %s"
        self.conexion.ejecutar(query, (nuevo_valor, producto_id))
        print('Los datos se actualizaron con exito...')
        delay(2)


class Venta:
    def __init__(self, conexion):
        self.conexion = conexion

    def agregar(self, tienda_id, usuario_id, fecha, total):
        query = "INSERT INTO Venta(tienda_id,usuario_id,fecha,total) Values (%s,%s,%s,%s)"
        self.conexion.ejecutar(query, (tienda_id, usuario_id, fecha, total))

    def listar(self):
        return self.conexion.consultar(
            """SELECT 
    Venta.id,
    Tienda.nombre AS tienda,
    Usuarios.nombre AS usuario,
    Venta.fecha,
    Venta.total
    FROM Venta
    JOIN Tienda ON Venta.tienda_id = Tienda.id
    JOIN Usuarios ON Venta.usuario_id = Usuarios.id;""")


class Detalle_venta:
    def __init__(self, conexion):
        self.conexion = conexion

    def agregar(self, tienda_id, usuario_id, fecha, total):
        query = "INSERT INTO Detalle_venta(tienda_id,usuario_id,fecha,total) Values (%s,%s,%s,%s)"
        self.conexion.ejecutar(query, (tienda_id, usuario_id, fecha, total))

    def listar(self):
        return self.conexion.consultar(
            """SELECT 
	detalle_venta.id,
    detalle_venta.venta_id,
    producto.nombre,
    detalle_venta.cantidad,
    detalle_venta.subtotal
	FROM detalle_venta
    JOIN producto ON detalle_venta.producto_id = producto.id""")
