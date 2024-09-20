def create_tables(cursor):
    create_users_table_query = '''
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL
    )
    '''
    create_consumo_table_query = '''
    CREATE TABLE IF NOT EXISTS consumo (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        fecha DATE,
        cantidad DECIMAL(10, 2),
        descripcion TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    '''
    create_sugerencias_table_query = '''
    CREATE TABLE IF NOT EXISTS sugerencias (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        recomendacion TEXT,
        fecha DATE,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    '''
    create_metas_table_query = '''
    CREATE TABLE IF NOT EXISTS metas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        meta TEXT,
        fecha_inicio DATE,
        fecha_fin DATE,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    '''
    create_historial_table_query = '''
    CREATE TABLE IF NOT EXISTS historial (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        accion TEXT,
        fecha DATE,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    '''
    try:
        cursor.execute(create_users_table_query)
        cursor.execute(create_consumo_table_query)
        cursor.execute(create_sugerencias_table_query)
        cursor.execute(create_metas_table_query)
        cursor.execute(create_historial_table_query)
    except mysql.connector.Error as e:
        print(f"Error al crear las tablas: {e}")
