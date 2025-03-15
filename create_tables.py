import sqlite3

def createTables():

    sql_statements = [ 
    """CREATE TABLE IF NOT EXISTS MAQUINA (
            id_maquina INTEGER PRIMARY KEY AUTOINCREMENT, 
            ip TEXT NOT NULL, 
            nome TEXT,
            usuario TEXT NOT NULL, 
            senha TEXT NOT NULL, 
            porta INTEGER NOT NULL
        );""",

    """CREATE TABLE IF NOT EXISTS USUARIO (
            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT, 
            email TEXT NOT NULL, 
            nome TEXT,
            perfil TEXT NOT NULL
        );""",

    """CREATE TABLE IF NOT EXISTS NODOCKER (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nome TEXT NOT NULL,
            id_maquina INTEGER NOT NULL,
            id_usuario INTEGER NOT NULL,
            cpu_cores INTEGER NOT NULL,
            ram INTEGER NOT NULL,
            device INTEGER NOT NULL,
            network INTEGER NOT NULL,
            FOREIGN KEY (id_maquina) REFERENCES Maquina (id_maquina),
            FOREIGN KEY (id_usuario) REFERENCES Usuario (id_usuario)
        );"""
    ]

    # create a database connection
    try:
        with sqlite3.connect('sysDB.db') as conn:
            # create a cursor
            cursor = conn.cursor()

            # execute statements
            for statement in sql_statements:
                cursor.execute(statement)

            # commit the changes
            conn.commit()

            print("Tables created successfully.")
    except sqlite3.OperationalError as e:
        print("Failed to create tables:", e)

if __name__ == "__main__":

    createTables()