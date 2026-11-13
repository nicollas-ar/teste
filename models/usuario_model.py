import os
import psycopg2
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash

load_dotenv()


def cadastrar_usuario(nome, email, senha):
    url = os.getenv("DATABASE_URL")
    if not url:
        raise RuntimeError("Configure a variável DATABASE_URL no arquivo .env")

    with psycopg2.connect(url, sslmode="require", connect_timeout=10) as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id BIGSERIAL PRIMARY KEY,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    senha TEXT NOT NULL
                )
            """)
            cursor.execute(
                "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)",
                (nome, email, generate_password_hash(senha)),
            )
