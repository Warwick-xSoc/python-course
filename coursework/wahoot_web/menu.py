from flask import Blueprint, render_template

from .common import game_history


bp = Blueprint("menu", __name__)


@bp.route("/")
def menu():
    return render_template("menu.html")

@bp.route("/history")
def history():
    return render_template(
        "game_history.html",
        games=game_history.games.values()
    )