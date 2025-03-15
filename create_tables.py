import sqlite3

def createTables():

    sql_statements = [ 
    """CREATE TABLE IF NOT EXISTS Machine (
            id INTEGER PRIMARY KEY, 
            ip TEXT NOT NULL, 
            user TEXT NOT NULL, 
            senha TEXT NOT NULL, 
            porta INTEGER NOT NULL,
            cadastro DATE NOT NULL
        );""",

    """CREATE TABLE IF NOT EXISTS User (
            id INTEGER PRIMARY KEY, 
            email TEXT NOT NULL, 
            name TEXT,
            cadastro DATE NOT NULL,
            profile INTEGER NOT NULL
        );""",

    """CREATE TABLE IF NOT EXISTS nodes (
            id INTEGER PRIMARY KEY, 
            name TEXT NOT NULL,
            id_machine INTEGER NOT NULL,
            id_user INTEGER NOT NULL,
            cpu_cores INTEGER NOT NULL,
            ram INTEGER NOT NULL,
            device INTEGER NOT NULL,
            network INTEGER NOT NULL,
            cadastro DATE NOT NULL,
            FOREIGN KEY (id_machine) REFERENCES Machine (id),
            FOREIGN KEY (id_user) REFERENCES User (id)
        );"""
    ]

    # create a database connection
    try:
        with sqlite3.connect('sysDB.db') as conn:
            # create a cursor
            cursor = conn.cursor()

            # execute statements
            for statement in sql_statements:
                print(statement)
                cursor.execute(statement)
                print("Executou create")

            # commit the changes
            conn.commit()

            print("Tables created successfully.")
    except sqlite3.OperationalError as e:
        print("Failed to create tables:", e)