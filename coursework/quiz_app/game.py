from flask import Blueprint, flash, redirect, render_template, request, url_for, session

from quiz_game.repositories import GameRepository
from quiz_game.services import GameService
from quiz_game.repositories import QuestionBank
from quiz_game.game import Player, AnswerType

from .adapters import GameUIAdapter
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
        return render_template(
            "join_game.html", game_id=game_id, error="Invalid username."
        )

    game = game_service.get_game(game_id)

    if game is None:
        return "Game not found", 404

    player = Player(username)

    session[USERNAME_SESSION_KEY] = username
    game.players[username] = player

    player.start_question_attempt(game.time_per_question)

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

    if not game.player_has_next_question(player):
        pass

    if request.method == "POST":
        choice = GameUIAdapter.get_question_choice_selected(request.form)

        if choice is None:
            # TODO(tomas): display error message
            pass

        game.on_question_answer(player, choice)

        return redirect(url_for("game.answer_outcome", game_id=game_id))
    else:
        if player.current_attempt.has_timed_out:
            player.end_question_attempt(AnswerType.TIMEOUT)
            player.current_question += 1

        if player.current_attempt.is_resolved:
            player.current_question += 1

        player.start_question_attempt(game.time_per_question)

        return render_template(
            "in_game.html",
            game=game,
            player=player,
            current_question=game.get_player_current_question(player)
        )


# Join -> Question -> Show outcome -> Question -> ... -> Leaderboard and summary
# Post /play -> answer question -> redirect to outcome
# Get /outcome -> show result and question number
# Get /play -> if !has attempted current, start attempt
@bp.route("/outcome/<string:game_id>", methods=["GET"])
def answer_outcome(game_id):
    game = game_service.get_game(game_id)

    if game is None:
        return "Game not found", 404

    player_name = session.get(USERNAME_SESSION_KEY)
    player = game.get_player(player_name)

    if player is None:
        return redirect(url_for("game.join", game_id=game_id))

    if not player.current_attempt.is_resolved and player.current_attempt.has_timed_out:
        player.end_question_attempt(AnswerType.TIMEOUT)

    return render_template(
        "answer_outcome.html",
        game=game,
        player=player
    )