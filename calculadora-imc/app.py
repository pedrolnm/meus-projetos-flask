from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/imc', methods=['POST'])
def imc():
    peso = float(request.form.get('peso'))
    altura = float(request.form.get('altura'))
    imc = (peso / (altura ** 2))
    imc = round(imc, 2)
    if imc <= 18.5:
        mensagem = 'Abaixo do peso'
    elif imc <= 24.9:
        mensagem = 'Peso normal'
    elif imc <= 29.9:
        mensagem = 'Sobrepeso'
    else:
        mensagem = 'Obesidade'

    return render_template('imc.html', peso=peso, altura=altura, imc=imc, mensagem=mensagem)


if __name__ == '__main__':
    app.run(debug=True)