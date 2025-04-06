import sqlite3

def createTables():

    sql_statements = [ 
    """CREATE TABLE IF NOT EXISTS MAQUINA (
            id_maquina INTEGER PRIMARY KEY AUTOINCREMENT, 
            ip TEXT NOT NULL, 
            nome TEXT,
            usuario TEXT NOT NULL, 
            senha TEXT NOT NULL, 
            porta INTEGER NOT NULL,
            data_cadastro timestamp NOT NULL
        );""",

    """CREATE TABLE IF NOT EXISTS USUARIO (
            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT, 
            login TEXT, 
            nome TEXT, 
            email TEXT NOT NULL, 
            senha TEXT,
            perfil TEXT NOT NULL,
            data_cadastro timestamp NOT NULL
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
            data_cadastro timestamp NOT NULL,
            FOREIGN KEY (id_maquina) REFERENCES Maquina (id_maquina),
            FOREIGN KEY (id_usuario) REFERENCES Usuario (id_usuario)
        );""",

        """INSERT INTO USUARIO VALUES (
            1,
            'thiago.freire',
            'Thiago Paiva Freire',
            'thiago.freire@nca.ufma.br',
            'scrypt:32768:8:1$mzoHFBlwjVod1Vqg$b907fad9c0a9452d195cd991c49f389870244ea16d8b523ba0c80f96e8f8ccfb0bf62387071f3957bdd213850a21f1793b6602736de91cf08291614a47046f0a',
            'A',
            '2025-03-23 17:13:19'
        );""",

        """INSERT INTO MAQUINA VALUES (
            1,
            '192.168.200.169',
            'SRV-VIPLAB1',
            'viplab',
            'viplab321',
            22,
            '2025-03-21 02:33:06'
        );""",

        """INSERT INTO MAQUINA VALUES (
            2,
            '192.168.200.116',
            'SRV-VIPLAB2',
            'viplab',
            'viplab321',
            22,
            '2025-03-21 02:31:38'
        );""",

        """INSERT INTO MAQUINA VALUES (
            3,
            '192.168.200.140',
            'SRV-VIPLAB3',
            'viplab',
            'viplab321',
            22,
            '2025-03-21 02:33:59'
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