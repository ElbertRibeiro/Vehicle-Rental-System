#lendo os dados db.py
import sqlite3

#conetando ao data base
conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

#lendo os dados
cursor.execute("""
SELECT * FROM  clientes;
""")

for linha in cursor.fetchall():
    print(linha)

conn.close()