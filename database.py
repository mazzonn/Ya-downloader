import sqlite3

DB_NAME = 'app_data.db'

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS token_data (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        token TEXT NOT NULL
                    )''')
    conn.commit()
    conn.close()

def save_token(token):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('DELETE FROM token_data')
    
    cursor.execute('INSERT INTO token_data (token) VALUES (?)', (token,))
    
    conn.commit()
    conn.close()

def load_token():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('SELECT token FROM token_data ORDER BY id DESC LIMIT 1')
    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]
    else:
        return ''