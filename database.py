import sqlite3

DB_NAME = "consultas.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS consultas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT,
            pregunta TEXT,
            respuesta TEXT,
            con_imagen INTEGER,
            fecha TEXT
        )
    """)
    conn.commit()
    conn.close()

def guardar_consulta(usuario, pregunta, respuesta, con_imagen, fecha):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO consultas (usuario, pregunta, respuesta, con_imagen, fecha) VALUES (?, ?, ?, ?, ?)",
              (usuario, pregunta, respuesta, int(con_imagen), fecha))
    conn.commit()
    conn.close()