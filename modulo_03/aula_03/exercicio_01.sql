CREATE TABLE autores (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    nacionalidade TEXT NOT NULL
);

CREATE TABLE livros (
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    ano_publi INTEGER NOT NULL,
    id_autor INTEGER NOT NULL,
    FOREIGN KEY (id_autor) REFERENCES autores(id)
);

DROP TABLE livros;

INSERT INTO autores(nome, nacionalidade)
VALUES
('Collen', 'Americano'),
('Ziraldo', 'Brasileiro');

INSERT INTO livros(titulo, ano_publi, id_autor)
VALUES
('Assim que acaba', 2021, 1),
('Menino maluquinho', 2005, 2),
('Verão', 2023, 1);

SELECT * FROM autores;
SELECT titulo, ano_publi FROM livros;

SELECT
    L.titulo AS Livros,
    A.nome AS Autores
FROM
    livros AS L
INNER JOIN autores AS A ON L.id_autor = A.id;