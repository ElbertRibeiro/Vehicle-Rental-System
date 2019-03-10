#07 update data.py
import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

#idermos definir o id a ser alterado
id_cliente = 1
#como usamos o fone como parametro
#iremos criara um novo fone

novo_fone = '11-1000-2014'
novo_criado_em = '2014-06-11'

#alterando os dados da tabela
cursor.execute("""
UPDATE clientes
SET fone = ?, criado_em = ?
WHERE id = ?
""", (novo_fone, novo_criado_em, id_cliente))

conn.commit()

print('Dados alterados com sucesso')

conn.close()