CREATE TABLE filmes (
    id INTEGER PRIMARY KEY AUTOINCREMENT
    , nome VARCHAR(255) NOT NULL
    , diretor VARCHAR (255) NOT NULL
    , ano_lancamento INTEGER NOT NULL
);

INSERT INTO filmes (nome, diretor, ano_lancamento) VALUES 
('Toy Story', 'John Lasseter', 1995)
