from flask import Blueprint, render_template
from werkzeug.exceptions import abort


bp = Blueprint('menu', __name__)

@bp.route('/')
def menu():
    return render_template('menu.html')