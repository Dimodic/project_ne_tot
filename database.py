import sqlite3


def get_db_connection():
    conn = sqlite3.connect('matrix_bot.db')
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS profiles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            matrix TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS operations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            operation_type TEXT NOT NULL,
            matrix1 TEXT NOT NULL,
            matrix2 TEXT,
            result TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()
