from flask import render_template, request, redirect, url_for, session, flash
from . import app
import bcrypt

usuarios = {}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
        if request.method == 'POST':
            usuario_cadastro = request.form.get('usuario_cadastro')
            senha_cadastro = request.form.get('senha_cadastro')
            if usuario_cadastro not in usuarios:
                senha_cadastro_hash = bcrypt.hashpw(senha_cadastro.encode(), bcrypt.gensalt())
                usuarios[usuario_cadastro] = senha_cadastro_hash
                flash('Usuário cadastrado com sucesso!')
                return redirect(url_for('login'))
            else:
                flash("Este nome de usuário já está em uso. Tente outro!")
                return redirect(url_for('cadastro'))
        else:
            return render_template('cadastro.html')


@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    senha_hash = usuarios.get(usuario)

    if senha_hash and  bcrypt.checkpw(senha.encode(), senha_hash):
        session['usuario'] = usuario
        return redirect(url_for('home'))
    else:
        return render_template('erro.html')


@app.route('/home')
def home():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('home.html', usuario=session['usuario'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))
