from flask import Blueprint, flash, redirect, render_template, request, url_for, session

from quiz_game.repositories import GameRepository
from quiz_game.services import GameService
from quiz_game.repositories import QuestionBank
from quiz_game.game import Player

from .session import USERNAME_SESSION_KEY


bp = Blueprint("game", __name__)

game_repository = GameRepository()
question_bank = QuestionBank("test.csv")
game_service = GameService(game_repository, question_bank)


@bp.route("/start")
def start():
    game = game_service.new_game()
    return redirect(url_for("game.join", game_id=game.game_id))


@bp.route("/join/<string:game_id>", methods=["GET"])
def join_page(game_id):
    return render_template("join_game.html", game_id=game_id, error=None)


@bp.route("/join/<string:game_id>", methods=["POST"])
def join(game_id):
    username = request.form.get("username")

    if username is None or username == "" or username.isspace():
        return render_template("join_game.html", game_id=game_id, error="Invalid username.")
    
    game = game_service.get_game(game_id)

    if game is None:
        return "Game not found", 404

    session[USERNAME_SESSION_KEY] = username
    game.players[username] = Player(username)

    return redirect(url_for("game.play", game_id=game_id))


@bp.route("/play/<string:game_id>", methods=["GET", "POST"])
def play(game_id):
    game = game_service.get_game(game_id)

    if game is None:
        return "Game not found", 404

    player_name = session.get(USERNAME_SESSION_KEY)
    player = game.get_player(player_name)

    if player is None:
        return redirect(url_for("game.join", game_id=game_id))

    match request.method:
        case "GET":
            return render_template(
                "in_game.html",
                game=game,
                player=player,
                current_question=game.questions[player.current_question]
            )
        case "POST":        
            return render_template(
                "in_game.html",
                game=game,
                player=player,
                current_question=game.questions[player.current_question]
            )
