from flask import Flask #importando a biblioteca
from routes.index import index_route
from routes.users import user_route


# Iniciando a aplicação
app = Flask(__name__) 

#Registrando as rotas da pasta "routes"
app.register_blueprint(index_route)
app.register_blueprint(user_route, url_prefix='/cadastro')

# Iniciando a execução.
app.run(debug=True) 
