import sqlite3

connection = sqlite3.connect('filmes.db')
cursor = connection.cursor()
cursor.execute('''
               CREATE TABLE filmes (
    id INTEGER PRIMARY KEY AUTOINCREMENT
    , nome VARCHAR(255) NOT NULL
    , diretor VARCHAR (255) NOT NULL
    , ano_lancamento INTEGER NOT NULL
);
               ''')

connection.commit()
connection.close()