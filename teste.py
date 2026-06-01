import sqlite3

conn = sqlite3.connect("banco.db")
cursor = conn.cursor()

try:
    cursor.execute("""
    ALTER TABLE livros ADD COLUMN genero_id INTEGER
    """)

    print("Coluna genero_id adicionada com sucesso!")

except sqlite3.OperationalError as erro:
    print("Aviso:", erro)

conn.commit()
conn.close()