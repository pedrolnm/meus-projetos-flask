# Estudos Flask 

Este repositório reúne meus estudos e pequenos projetos utilizando o microframework [Flask](https://flask.palletsprojects.com/), com foco em aprendizado prático e progressivo.

Cada exercício está em uma pasta separada com seu próprio código e templates, facilitando a organização e consulta.

---


## Exercícios disponíveis

- **Exercício 1** – Site de boas-vindas com Flask  
- **Exercício 2** – Formulário de Saudação com Flask  
- **Exercício 3** – Formulário com Nome e Idade  
- **Exercício 4** – Calculadora de IMC com Flask  
- **Exercício 5** – Conversor de Temperatura (Celsius para Fahrenheit)  
- **Exercício 6** – Lista de Tarefas simples com Flask  
- **Exercício 7** – Projeto de Login Simples com Flask  
- **Exercício 8** – Gerador de Senhas Seguras com Flask

---

### Exercício 1: Site de Boas-Vindas
- **Objetivo:** Criar uma página simples de boas-vindas com Flask.
- **Arquivos criados:** `app.py`, `templates/boasvindas.html`.

### Exercício 2: Formulário de Saudação
- **Objetivo:** Criar um formulário onde o usuário digita seu nome e a aplicação exibe uma saudação personalizada.
- **Arquivos criados:** `app.py`, `templates/form.html`, `templates/saudacao.html`.

### Exercício 3: Formulário com Nome e Idade
- **Objetivo:** Estender o formulário anterior para incluir o campo de idade, exibindo uma saudação com nome e idade do usuário.
- **Arquivos criados:** `app.py`, `templates/form.html`, `templates/saudacao.html`.

### Exercício 4: Calculadora de IMC com Flask
- **Objetivo:** Criar um formulário que recebe o peso e altura do usuário, calcula o IMC e mostra a classificação (ex: peso normal, sobrepeso, etc.).
- **Arquivos criados:** `app.py`, `templates/form.html`, `templates/imc.html`.

### Exercício 5: Conversor de Temperatura (Celsius para Fahrenheit)
- **Objetivo:** Criar um formulário que recebe uma temperatura em Celsius e converte para Fahrenheit, exibindo o resultado.
- **Arquivos criados:** `conversor-temperatura/app.py`, `conversor-temperatura/templates/conversor.html`.

### Exercício 6: Lista de Tarefas simples com Flask
- **Objetivo:** Criar uma aplicação web simples para adicionar, listar e remover tarefas.
- **Arquivos criados:** `lista-tarefas/app.py`, `lista-tarefas/templates/index.html`.

### Exercício 7: Projeto de Login Simples com Flask
- **Objetivo:** Criar um sistema de login com cadastro e autenticação de usuários, usando Flask, session e mensagens flash.
- **Arquivos criados:** `app/__init__.py`, `app/routes.py`, `app/templates/cadastro.html`, `app/templates/erro.html`, `app/templates/home.html`, `app/templates/login.html`, `app/templates/mensagens_flash.html`, `run.py`.

### Exercício 8: Gerador de Senhas Seguras com Flask
- **Objetivo:** Criar um gerador de senhas seguras aleatórias com Flask, permitindo que o usuário defina o tamanho da senha (de 4 a 40 caracteres).
- **Arquivos criados:** `app.py`, `templates/gerador.html`.

---


##  Como executar um exercício

1. Navegue até a pasta do exercício desejado:
   ```bash
   cd exercicio-1-boas-vindas
   ```

2. Ative seu ambiente virtual (se estiver usando um):
   ```bash
   source ../.venv/bin/activate  # Linux/Mac
   .\..\venv\Scripts\activate     # Windows
   ```

3. Instale as dependências (se necessário):
   ```bash
   pip install flask
   ```

4. Execute a aplicação:
   ```bash
   python app.py
   ```

5. Acesse no navegador:
   [http://localhost:5000](http://localhost:5000)

---

##  Objetivo

O objetivo deste repositório é aprender e praticar os conceitos fundamentais do Flask, como:

- **Roteamento básico**: Entender como o Flask manipula rotas para exibir diferentes páginas.
- **Templates HTML**: Como utilizar o mecanismo de templates do Flask para gerar páginas dinâmicas.
- **Formulários e requisições POST**: Como criar formulários simples e tratar as requisições POST para interagir com o usuário.
- **Estruturação de projetos**: Organizar o código e os arquivos de maneira escalável, com o uso de templates e rotas.

---
