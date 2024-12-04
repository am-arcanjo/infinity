import sqlite3

def apagar_filme(nid: int, arquivo_banco: str):
    connection = sqlite3.connect(arquivo_banco)
    cursor = connection.cursor()
    cursor.execute(f'''
                DELETE FROM filmes
                WHERE id == {id} 
            ''')
    connection.commit()
    connection.close()
    

while True:
    id = int(input('Qual o id do filme que deseja deletar?: '))
    apagar_filme(id, 'filmes.db')
    print("\n Filme deletado com sucesso!")
    continuar = input("Deseja continuar? (S/N) ")
    if continuar == 'N':
        break
