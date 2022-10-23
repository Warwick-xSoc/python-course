from flask import Blueprint, redirect, render_template, request, url_for, session

from wahoot.game import Player, AnswerType, PlayerState

from .adapters import GameUIAdapter
from .common import game_service
from .session import USERNAME_SESSION_KEY

# All pages under /game/...
bp = Blueprint("game", __name__)

# When the player hits the 'start game' button, redirect to join page
@bp.route("/start", methods=["POST"])
def start():
    diff_selection = int(request.form.get("diff"))
    game = game_service.new_game(num_qs=10, difficulty=diff_selection)

    return redirect(url_for("game.join", game_id=game.game_id))

# Show the username prompt page
@bp.route("/join/<string:game_id>", methods=["GET"])
def join_page(game_id):
    return render_template("join_game.html", game_id=game_id, error=None)

# Attempt to send off the username
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

    return redirect(url_for("game.play", game_id=game_id))

# For sending and recieving questions
@bp.route("/play/<string:game_id>", methods=["GET", "POST"])
def play(game_id):
    # Attempt to get game information
    game = game_service.get_game(game_id)
    if game is None:
        return "Game not found", 404

    # Attempt to get player information
    player_name = session.get(USERNAME_SESSION_KEY)
    player = game.players.get(player_name)
    
    if player is None:
        return redirect(url_for("game.join", game_id=game_id))

    if player.state is PlayerState.FINISHED:
        return redirect(url_for("game.end", game_id=game_id))

    if player.state is PlayerState.WAITING:
        player.start_question_attempt(game.time_per_question)

    # Did not submit an answer
    if player.current_attempt.has_timed_out:
        player.end_question_attempt(AnswerType.TIMEOUT)
        return redirect(url_for("game.answer_outcome", game_id=game_id))

    # Has submitted an answer
    if request.method == "POST":
        choice = GameUIAdapter.get_question_choice_selected(request.form)
        correct_choice = GameUIAdapter.get_correct_answer_index(request.form)

        if choice is None or correct_choice is None:
            # TODO(tomas): display error message
            pass

        game.on_question_answer(player, choice, correct_choice)

        return redirect(url_for("game.answer_outcome", game_id=game_id))

    choices, correct_index = game.questions[player.current_question].get_options()  

    return render_template(
        "in_game.html",
        game=game,
        player=player,
        current_question=game.questions[player.current_question],
        choices=choices,
        correct_index=correct_index
    )

# For displaying the result of a question
@bp.route("/outcome/<string:game_id>", methods=["GET"])
def answer_outcome(game_id):
    game = game_service.get_game(game_id)

    if game is None:
        return "Game not found", 404

    player_name = session.get(USERNAME_SESSION_KEY)
    player = game.players.get(player_name)

    if player is None:
        return redirect(url_for("game.join", game_id=game_id))

    if player.state is PlayerState.ANSWERING and player.current_attempt.has_timed_out:
        player.end_question_attempt(AnswerType.TIMEOUT)

    is_last_question = player.state == PlayerState.FINISHED

    return render_template(
        "answer_outcome.html",
        game=game,
        player=player,
        is_last_question=is_last_question
    )

# For displaying the game's end leaderboard
@bp.route("/end/<string:game_id>", methods=["GET"])
def end(game_id):
    game = game_service.get_game(game_id)

    if game is None:
        return "Game not found", 404
    
    return render_template(
        "end.html",
        game=game
    )