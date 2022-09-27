from typing import Optional
from random import choices

from .repositories import GameRepository, QuestionBank
from .game import Game


class GameService:
    def __init__(self, game_repo: GameRepository, question_bank: QuestionBank) -> None:
        self.game_repo = game_repo
        self.question_bank = question_bank
    
    def new_game(self, num_qs: int = 10) -> Game:
        game = Game(self._generate_id(), self.question_bank.get_questions(num_qs))
        self.game_repo.add_game(game)
        return game
    
    def get_game(self, game_id: str) -> Optional[Game]:
        return self.game_repo.get_game_by_id(game_id)


    # Generate random hexadecimal string for a game id (5 characters)
    def _generate_id(self) -> int:
        return "".join(choices("0123456789ABCDEF", k=5))
