from flask import Blueprint
from werkzeug.exceptions import abort


bp = Blueprint('menu', __name__)

@bp.route('/')
def menu():
    return render_template('home.html')