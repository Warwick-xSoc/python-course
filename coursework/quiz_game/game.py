from typing import Optional


class Question:
    def __init__(self, difficulty, question, choices):
        """
        Represents a Quiz question

        :param difficulty:
        :param question: the actual question
        :param choices: list containing possible answers. The correct answer is always at index 0.
        """
        self.difficulty = difficulty
        self.question = question
        self.choices = choices

    @staticmethod
    def from_dict(dictionary: dict) -> 'Question': 
        return Question(
            difficulty=dictionary["difficulty"],
            question=dictionary["question"],
            choices=[
                dictionary[f"wrong_{i}"]
                for i in range(1, 4)
            ]
        )


    def __repr__(self):
        return f'Question({self.difficulty}, "{self.question}", {self.choices})'


class Player:
    def __init__(self, name: str):
        """
        Represents a Quiz player, and keeps track of their info

        :param name:
        """
        self.name = name
        self.score = 0
        self.this_streak = 0
        self.max_streak = 0
        self.n_correct = 0
        self.n_answered = 0

    def apply_scoring(self, status: str, time_left: float):
        # status: Correct, Incorrect, Timeout
        # time_left: float between 0 to 20
        match status:
            case "Correct":
                self.n_answered += 1
                self.n_correct += 1
                self.score += (time_left * 100) // 2 + self.this_streak * 100

                self.this_streak += 1
                if self.this_streak > self.max_streak:
                    self.max_streak = self.this_streak

            case "Incorrect":
                self.this_streak = 0
                self.n_answered += 1
                pass


class Game:
    def __init__(self, game_id, questions, current_question=0):
        """
        Represents the state of a game

        :param game_id: the unique id of the game
        :param questions: questions to be asked in order
        """
        self.game_id = game_id
        self.questions = questions
        self.players = {}

    def get_player(self, player_name: str) -> Optional[Player]:
        return self.players[player_name]

    @property
    def has_finished(self):
        return self.current_question == len(self.questions)
