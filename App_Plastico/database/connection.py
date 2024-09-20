import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            port='3306',
            database='app_plastico',
            user='root',
        )
        if connection.is_connected():
            print("Conexión a la base de datos MariaDB exitosa")
            return connection
    except mysql.connector.Error as e:
        print(f"Error al conectar a MariaDB: {e}")
    return None
