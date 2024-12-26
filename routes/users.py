from flask import Blueprint, render_template
from DB_fake.account import USERS

user_route = Blueprint('cadastro', __name__)

"""
    Rota /cadastro/ (POST) - Formulário de cadastro
    Rota /cadastrar/ (POST) - Mandar as informações para serem inseridas no BD

"""
@user_route.route('/')
def page_cadastro():
    return render_template('cadastro.html')


@user_route.route('/cadastrados')
def funcao_cadastrados():
    return render_template('cadastrados.html', users=USERS)
