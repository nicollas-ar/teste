from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')

    from models.usuario_model import cadastrar_usuario
    cadastrar_usuario(nome, email, senha)

    return 'Usuário cadastrado com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)