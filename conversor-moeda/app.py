from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        valor = float(request.form.get('valor'))
        moeda = request.form.get('moeda')
        taxas = {'dolar': 5.60, 'euro': 6.40, 'iene': 0.04}

        if moeda in taxas:
            valor_convertido = valor / taxas[moeda]
            return render_template('conversor_moeda.html', valor=valor_convertido, moeda=moeda)

        else:
            return redirect('/')
    else:
        return render_template('conversor_moeda.html', valor=None, moeda=None)

if __name__ == '__main__':
    app.run(debug=True)