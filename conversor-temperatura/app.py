from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        temperatura_c = request.form.get('temperatura')
        if temperatura_c:
            try:
                temperatura_c = float(temperatura_c)
                temperatura_f = (temperatura_c * 9) / 5 + 32
                return render_template('conversor.html', temperatura_f=temperatura_f, temperatura_c=temperatura_c)
            except ValueError:
                return redirect('/')
    return render_template('conversor.html')

if __name__ == '__main__':
    app.run(debug=True)