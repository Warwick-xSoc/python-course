from uuid import uuid4

from .game import Game


class GameService:
    def create_gane(self):
        return Game(
            uuid=uuid4(),
            questions=[]
        )
