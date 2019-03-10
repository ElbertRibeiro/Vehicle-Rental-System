#09 alter table.py
import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

#adiciionando uma nova coluna na tabela clientes
cursor.execute("""
ALTER TABLE clientes
ADD COLUM bloqueado BOOLEAN;
""")

conn.commit()

print('Novo campo adicionado com sucesso.')


conn.close()