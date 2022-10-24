import os

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
    )

    from . import routes
    from . import menu

    app.register_blueprint(menu.bp)
    app.register_blueprint(routes.bp, url_prefix="/game")

    return app
