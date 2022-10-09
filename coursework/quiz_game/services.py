from typing import Optional
from random import choices
from datetime import timedelta


from .repositories import GameHistory, QuestionBank
from .game import Game


class GameService:

    def __init__(self, games: GameHistory, question_bank: QuestionBank) -> None:

        self.games = games
        self.question_bank = question_bank

    def new_game(self, num_qs: int = 10) -> Game:
        game = Game(
            self._generate_id(),
            self.question_bank.get_questions(num_qs),
            timedelta(seconds=20)
        )

        self.games.add_game(game)
        return game

    def get_game(self, game_id: str) -> Optional[Game]:
        return self.games.get_game_by_id(game_id)

    def _generate_id(self) -> int:
        """
        Generate random hexadecimal string for a game id (5 characters)
        """
        return "".join(choices("0123456789ABCDEF", k=5))
