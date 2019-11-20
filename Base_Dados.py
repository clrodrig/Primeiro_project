#importar sql
import sqlite3

conn = sqlite3.connect('UserData.db') # criando a base de dados em SQL

cursor = conn.cursor()

#Criar a Tabela

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    User TEXT NOT NULL,
    Password TEXT NOT NULL
);
""")
print('Dados conectado')