from flask import Flask
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

@app.route('/')
def hello():
    init_db()
    return "Halo dari Flask + Docker + Jenkins + Database!"

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
