from uuid import uuid4
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from quiz_game.repositories import QuestionRepository


bp = Blueprint('game', __name__)

@bp.route('/start')
def start():
    return redirect(url_for('game.play', id=uuid4()))

@bp.route('/play/<string:id>')
def play(id):

    question_bank = QuestionRepository("test.csv")
    question = question_bank.get_question()

    return render_template(
        'in_game.html', 
        game_id = id,
        question_no = 1,
        question_text = question.question,
        options = question.choices
    )