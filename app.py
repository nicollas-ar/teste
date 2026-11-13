from flask import Flask, render_template, request
from psycopg2 import IntegrityError
from models.usuario_model import cadastrar_usuario

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form.get('nome', '').strip()
    email = request.form.get('email', '').strip()
    senha = request.form.get('senha', '')
    confirmar_senha = request.form.get('confirmar_senha', '')

    if not nome or not email or not senha:
        return 'Preencha todos os campos.', 400
    if senha != confirmar_senha:
        return 'As senhas não coincidem.', 400

    try:
        cadastrar_usuario(nome, email, senha)
    except IntegrityError:
        return 'Este e-mail já está cadastrado.', 409

    return 'Usuário cadastrado com sucesso!'


if __name__ == '__main__':
    app.run(debug=True)
