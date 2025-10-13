-- Active: 1760370889518@@127.0.0.1@3306
CREATE TABLE alunos(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
);

CREATE TABLE cursos(
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL
);

CREATE TABLE alunos_cursos (
    id_aluno INTEGER,
    id_curso INTEGER,
    FOREIGN KEY (id_aluno) REFERENCES alunos(id),
    FOREIGN KEY (id_curso) REFERENCES cursos(id)
);

INSERT INTO alunos(nome)
VALUES
('Paulo'),
('Maria'),
('João'),
('Carla');

INSERT INTO cursos(titulo)
VALUES
('backend'),
('frontend');

INSERT INTO alunos_cursos(id_aluno, id_curso)
VALUES
(1,2),
(1,1),
(2,1),
(3,2),
(4,1),
(4,2);

SELECT * FROM alunos;
SELECT * FROM cursos;
SELECT * FROM alunos_cursos;

SELECT
    A.nome AS Aluno,
    C.titulo AS Curso
FROM 
    alunos AS A
INNER JOIN alunos_cursos AS AC ON AC.id_aluno = A.id
INNER JOIN cursos AS C ON AC.id_curso = C.id;

SELECT COUNT(*) AS 'Quantidade de alunos' FROM alunos;

SELECT COUNT(*) AS 'Num de Alunos de back' FROM alunos_cursos
WHERE id_curso = 1;

SELECT
    COUNT(A.nome) AS num_alunos,
    C.titulo AS Curso
FROM 
    alunos AS A
INNER JOIN alunos_cursos AS AC ON AC.id_aluno = A.id
INNER JOIN cursos AS C ON AC.id_curso = C.id
GROUP BY C.titulo;