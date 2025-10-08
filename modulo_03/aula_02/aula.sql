-- Active: 1759768115865@@127.0.0.1@3306
CREATE TABLE alunos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER
);

INSERT INTO alunos(nome, idade) VALUES ('João', 20);

INSERT INTO alunos(nome, idade) VALUES ('Maria', 22);

INSERT INTO alunos(nome, idade) VALUES ('Kauã', 25);

SELECT * FROM alunos;

SELECT nome FROM alunos;

SELECT * FROM alunos WHERE idade = 20;

SELECT * FROM alunos WHERE nome = 'Maria' AND idade = 22;

UPDATE alunos SET idade = 21 WHERE nome = 'João';

DELETE FROM alunos WHERE id = 3;