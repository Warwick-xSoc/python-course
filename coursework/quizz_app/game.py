from uuid import uuid4
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


bp = Blueprint('game', __name__)

@bp.route('/')
def index():
    return render_template('home.html')

@bp.route('/game/start')
def start():
    return redirect(url_for('game.play', id=uuid4()))

@bp.route('/game/<string:id>/play')
def play(id):
    return f'Playing game {id}...'