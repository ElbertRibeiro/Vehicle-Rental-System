#10 view table info.py

import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()
#inserir o nome da tabela
nome_tabela = 'clientes'

#obtendo informações da tabela
#USAMOS O COMANDO 'PRAGMA' PARA LER AS INF DA TABELA
cursor.execute('PRAGMA table_info({})'.format(nome_tabela))

colunas = [tupla[1] for tupla in cursor.fetchall()]
print('Colunas: ', colunas)
#ou
#for coluna in colunas
#      print(coluna)

#listando as tablas do db
cursor.execute("""
SELECT name FROM sqlite_master WHERE type='table' ORDER BY name
""")

print('Tabelas: ')
for tabela in cursor.fetchall():
    print("%s" % (tabela))

#obtendo o schema da tabela
cursor.execute("""
SELECT sql FROM sqlite_master WHERE type='table' AND name=?
""", (nome_tabela,))

print('Schema: ')
for schema in cursor.fetchall():
    print("%s" % (schema))

conn.close()