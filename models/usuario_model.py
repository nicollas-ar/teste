import psycopg2
from dotenv import load_dotenv
import os


load_dotenv()

# Fetch variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Connect to the database
connection = psycopg2.connect(DATABASE_URL)

def cadastrar_usuario(nome, email, senha):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)", (nome, email, senha))
    connection.commit()
    cursor.close()
