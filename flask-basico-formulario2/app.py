from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/saudacao', methods=['POST'])
def saudacao():
    nome = request.form.get('nome')
    idade = request.form.get('idade')

    return render_template('saudacao.html', nome=nome, idade=idade)



if __name__ == '__main__':
    app.run(debug=True)