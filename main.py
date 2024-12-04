from flask import Flask #importando a biblioteca
from routes.index import index_route


# Iniciando a aplicação
app = Flask(__name__) 

#Registrando as rotas da pasta "routes"
app.register_blueprint(index_route)

# Iniciando a execução.
app.run(debug=True) 
