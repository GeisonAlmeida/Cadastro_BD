from flask import Blueprint, render_template

index_route = Blueprint('index', __name__)

@index_route.route('/')
def page_index():
    return render_template('index.html')
