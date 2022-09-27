from quiz_game.repositories import GameRepository
from quiz_game.services import GameService
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from quiz_game.repositories import QuestionBank


bp = Blueprint('game', __name__)

game_repository = GameRepository()
question_bank = QuestionBank("test.csv")
game_service = GameService(game_repository, question_bank)


@bp.route('/start')
def start():
    game = game_service.new_game()
    return redirect(url_for('game.play', game_id=game.game_id))

@bp.route('/play/<string:game_id>', methods = ['GET', 'POST'])
def play(game_id):

    if game := game_service.get_game(game_id) is None:
        return "404"

    match request.method:
        case "GET":
            # return template asking for username which when submitted, 
            # posts to same URL with player_id=username, q_num=1
            return "404"
        case "POST":
            # Player ID (name) should be stored in the post request
            # Request should store player_id and question
            data : dict = request.form
            if player_id := data.get("player_id") is None:
                return "404"
            if question := data.get("q_num") is None:
                return "404"
            
            player = game.get_player(player_id)

            return render_template(
                'in_game.html', 
                game_id = game_id,
                question_no = 1,
                question_text = question.question,
                options = question.choices,
                player = player
            )
        case _:
            return "404"