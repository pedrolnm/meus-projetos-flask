from flask import Flask, request, render_template
import string
import secrets

app = Flask(__name__)

def gerar_senha_segura(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    return senha


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        tamanho = int(request.form.get('tamanho'))
        try:
            if 4 <= tamanho <=40:
                senha = gerar_senha_segura(tamanho=tamanho)
                return render_template('gerador.html', senha=senha, tamanho=tamanho)
            else:
                erro = 'Escolha um número de 4 até 40.'
                return render_template('gerador.html', erro=erro)
        except:
            erro = 'Escolha um número de 4 até 40.'
            return render_template('gerador.html', erro=erro)

    else:
        return render_template('gerador.html')


if __name__ == '__main__':
    app.run(debug=True)