-- Active: 1759768115865@@127.0.0.1@3306
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY,
    primeiro_nome TEXT NOT NULL,
    sobrenome TEXT,
    email TEXT NOT NULL,
    senha TEXT NOT NULL
);

CREATE TABLE postagens (
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    postagem TEXT,
    id_autor INT
);

INSERT INTO usuarios(primeiro_nome, sobrenome, email, senha)
VALUES
('Kauã', 'Mendes', 'kaua123@gmail.com', '1100'),
('Ju', 'Miiller', 'jumiiller@gmail.com', '2200'),
('João', 'Victor', 'joaovt21@gmail.com', '3300'),
('Ana', 'Clara', 'aninha22@gamil.com', '4400'),
('Caio', 'Marques', 'caiomar44@gmail.com', '5500');

SELECT * FROM usuarios;

INSERT INTO postagens (titulo, postagem, id_autor)
VALUES
('Casa', 'Casa alugada', 3),
('Praia', 'Praia top', 4),
('Familia', 'familia q amo', 1),
('Festa', 'Festa maneira', 2),
('Facul', 'aula top', 5);

SELECT * FROM postagens;