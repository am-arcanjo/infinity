import sqlite3

connection = sqlite3.connect('filmes.db')
cursor = connection.cursor()
cursor.execute('''
               INSERT INTO filmes (nome, diretor, ano_lancamento) VALUES 
('Toy Story', 'John Lasseter', 1995)
               ''')

connection.commit()
connection.close()