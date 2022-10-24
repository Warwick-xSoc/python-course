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
        # Unfilled version:
        # self.question = Question(0, "", "Yes", ["a"])

        self.questions = []

        with open(csv_filename) as file:
            reader = DictReader(file)

            for question in reader:
                self.questions.append(Question.from_dict(question))

    def get_questions(self, num, difficulty=-1) -> list[Question]:
        """
        Get specified number of questions with the given difficulty.

        :param num: number of questions
        :param difficulty: difficulty of the questions
        """
        # Unfilled version
        # return [self.questions[0]] * num

        # If specified, pick questions that have this difficulty
        if 0 <= difficulty <= 2:
            diff_questions = [q for q in self.questions if q.difficulty == difficulty]
            return sample(diff_questions, num)
            
        # Pick a random question if no difficulty specified
        return sample(self.questions, num)


class GameHistory:
    def __init__(self) -> None:
        self.games = dict()

    def get_game_by_id(self, game_id: str) -> Optional[Game]:
        return self.games.get(game_id)

    def add_game(self, game: Game):
        self.games[game.game_id] = game
