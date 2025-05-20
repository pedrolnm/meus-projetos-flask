from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/saudacao', methods=['POST'])
def saudacao():
    nome = request.form.get('nome')
    return render_template('form.html', nome=nome)


if __name__ == '__main__':
    app.run(debug=True)