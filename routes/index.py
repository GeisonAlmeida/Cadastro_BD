from flask import Blueprint, render_template

index_route = Blueprint('index', __name__)

"""
    Rota /index/  (GET) - Pegar informação do bando de dados para logar

"""

@index_route.route('/')
def page_index():
    return render_template('index.html')


