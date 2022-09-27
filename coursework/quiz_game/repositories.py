from .game import Game, Question
from random import sample
from typing import Optional

class QuestionBank:
    def __init__(self, csv_filename: str):
        # Each csv line should be in the format: 
        # difficulty, question, correct, wrong_1, wrong_2, wrong_3
        # difficulty ranges from 0-2: Easy, Medium, Hard

        with open(csv_filename) as file:
            text = file.read()
        str_data = [line.split(",") for line in text.split("\n")]

        self.questions = []
        for q in str_data:
            q_diff = int(q[0])
            q_text = q[1]
            q_answers = q[2:]
            self.questions.append(Question(q_diff, q_text, q_answers))

    # Get a question from the repository. Can specify a difficulty.
    def get_questions(self, num, difficulty = -1) -> list[Question]:

        if difficulty <= -1 or difficulty > 2:
            # Pick a random question if no difficulty specified
            return sample(self.questions, num)
        
        # Otherwise, pick a question that has the specified difficulty
        diff_questions = [q for q in self.questions if q.difficulty == difficulty]
        return sample(diff_questions, num)
                

class GameRepository:
    def __init__(self) -> None:
        self.games = dict()

    def get_game_by_id(self, game_id: str) -> Optional[Game]:
        return self.games.get(game_id)

    def add_game(self, game: Game):
        self.games[game.game_id] = game