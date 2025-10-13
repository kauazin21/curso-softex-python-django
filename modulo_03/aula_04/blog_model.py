"""
Crie a class BlogModel seguindo o exemplo da UserModel;
BlogModel deve ter os atributos:
 - conn do tipo DatabaseConnection
 - criar a tabela quando instanciado

tabela blogs:
 - id;
 - titulo;
 - conteudo;
 - data_criacao;
 - data_atualizacao;
 - id_user (chave estrangeira referente a tabela usuarios);

Faça um CRUD para:
- criar postagem
- ler todas as postagens
- ler postagens pelo id
- ler postagens pelo id_user
- atualizar postam (pelo id da postagem)
- deletar postagem (pedo id da postagem)

**Consulte o UserModel para se guiar
"""

import sqlite3
from datetime import datetime
from database import DatabaseConnection

class BlogModel:
    def __init__(self):
        self.db_conn = DatabaseConnection()
        self._create_table()

    def _create_table(self):
        self.db_conn.connect()
        self.db_conn.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS blogs(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                conteudo TEXT NOT NULL,
                data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
                data_atualizacao DATETIME DEFAULT CURRENT_TIMESTAMP,
                id_user INTEGER NOT NULL
                FOREIGN KEY (id_user) REFERENCES usuarios(id)
            );

"""
    )
        self.db_conn.close()

    def create_post(self, titulo, conteudo):
        self.db_conn.connect()
        self.db_conn.cursor.execute(
            """
            INSERT INTO blogs(titulo, conteudo)
            VALUES
            (?, ?);
    """,
        (titulo, conteudo),
        )
        print("Postagem feita com sucesso!")

        self.db_conn.close()

    def read_all(self):
        self.db_conn.connect
        self.db_conn.cursor.execute(

            
        )