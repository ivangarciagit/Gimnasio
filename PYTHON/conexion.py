import mysql.connector


class ConexionDB:
    def __init__(self, host='localhost', user='root', password='', database='sistemagym'):
        self.config = {
            'host': host,
            "user": user,
            'password': password,
            'database': database
        }

        self.conn = None
        self.cursor = None

    def conectar(self):
        self.conn = mysql.connector.connect(**self.config)
        self.cursor = self.conn.cursor(dictionary=True)

    def cerrar(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def ejecutar(self, query, params=None):
        self.cursor.execute(query, params or ())
        self.conn.commit()

    def ejecutar_con_retorno(self, query, params=None):
        self.cursor.execute(query, params or ())
        self.conn.commit()
        return self.cursor

    def consultar(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()
