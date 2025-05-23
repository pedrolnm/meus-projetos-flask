from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tarefas = []

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        tarefa = request.form.get('tarefa')
        if tarefa:
            tarefas.append(tarefa)
        return redirect('/')
    else:
        return render_template('index.html', tarefas=tarefas)

@app.route('/excluir/<int:index>', methods=['POST'])
def excluir_tarefa(index):
    if 0 <= index < len(tarefas):
        tarefas.pop(index)
        return redirect('/')
    else:
        return 'Não foi possível encontrar a tarefa desejada'


if __name__ == '__main__':
    app.run(debug=True)