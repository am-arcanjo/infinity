import sqlite3

def adicionar_filme(nome: str, diretor: str, ano_de_lancamento: int, arquivo_banco: str):
    connection = sqlite3.connect(arquivo_banco)
    cursor = connection.cursor()
    cursor.execute(f'''
                INSERT INTO filmes (nome, diretor, ano_lancamento) VALUES 
                ('{nome}', '{diretor}', {ano_de_lancamento})
            ''')
    connection.commit()
    connection.close()
    

while True:
    nome = input("Digite o nome de um filme: ")
    diretor = input("Digite o nome do seu diretor: ")
    ano_de_lancamento = int(input("Digite o ano de lançamento do filme: "))
    adicionar_filme(nome, diretor, ano_de_lancamento, 'filmes.db')
    print("\n Filme adicionado com sucesso!")
    continuar = input("Deseja continuar? (S/N) ")
    if continuar == 'N':
        break





# Versão sem ser em método 
# connection = sqlite3.connect('filmes.db')
# cursor = connection.cursor()
# cursor.execute('''
#               INSERT INTO filmes (nome, diretor, ano_lancamento) VALUES 
# ('Toy Story', 'John Lasseter', 1995)
#               ''')

# connection.commit()
# connection.close()