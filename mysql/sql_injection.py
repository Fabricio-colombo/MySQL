
# Problema do SQL Injection corrigido.

import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='021196',
    database='bdfabrin',
)

cursor = conexao.cursor()

nome_produto = "chocolate"
valor = 15

comando = 'INSERT INTO vendas (nome_produto, valor) VALUES (%s, %s)'
valores = (nome_produto, valor)

cursor.execute(comando, valores)

conexao.commit()

cursor.close()
conexao.close()
