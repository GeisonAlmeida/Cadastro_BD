from flask import Flask, url_for, render_template #importando a biblioteca


# Iniciando a aplicação
app = Flask(__name__) 

# Criando a rota
@app.route('/')
def page_index():
    return render_template('index.html')

@app.route('/cadastro')
def page_cadastro():
    return render_template('cadastro.html')

@app.route('/admin')
def page_admin():
    return "Rota para Cadastro"

# Iniciando a execução.
app.run(debug=True) 
