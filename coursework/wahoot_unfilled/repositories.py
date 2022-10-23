from csv import DictReader
from random import sample
from typing import Optional

from .game import Game, Question


class QuestionBank:
    def __init__(self, csv_filename: str):
        """
        Each csv line should be in the format:
        difficulty, question, correct, wrong_1, wrong_2, wrong_3
        difficulty ranges from 0-2: Easy, Medium, Hard
        """

        self.questions = [Question(0, "What's 1+1?", "2", ["1", "3", "4"])]

    def get_questions(self, num: int, difficulty: int = -1) -> list[Question]:
        """
        Get specified number of questions with the given difficulty.

        :param num: number of questions
        :param difficulty: difficulty of the questions
        """

        return [self.questions[0]] * num


class GameHistory:
    def __init__(self) -> None:
        self.games = dict()

    def get_game_by_id(self, game_id: str) -> Optional[Game]:
        return self.games.get(game_id)

    def add_game(self, game: Game):
        self.games[game.game_id] = game
