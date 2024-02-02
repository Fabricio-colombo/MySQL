

# ele tem um problema de segurança conhecido como "SQL Injection" devido à concatenação de strings para formar a consulta SQL. 


import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='021196',
    database='bdfabrin',
)

cursor = conexao.cursor()

#CRUD - Create, Read, Update, Delete

nome_produto = "toddynho"
valor = 4

comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'

cursor.execute(comando)
conexao.commit()




cursor.close()
conexao.close()