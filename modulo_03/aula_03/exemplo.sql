-- Active: 1759940460693@@127.0.0.1@3306
CREATE TABLE professores (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
);

CREATE TABLE alunos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    id_professor INTEGER NOT NULL,
    FOREIGN KEY (id_professor) REFERENCES professores(id)
);

DROP TABLE alunos;

INSERT INTO professores
VALUES
(2, 'Rafael');

INSERT INTO alunos(nome, id_professor)
VALUES
('Gabriel', 2),
('Patrick', 2);

SELECT * FROM professores;
SELECT * FROM alunos;

SELECT 
    id AS identificador, nome,
    id_professor AS registro_professor 
FROM alunos;

SELECT
alunos.nome AS aluno, 
professores.nome AS professor
FROM alunos
INNER JOIN professores ON alunos.id_professor = professores.id;