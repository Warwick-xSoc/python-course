from typing import Optional, Callable
from enum import IntEnum
from datetime import datetime, timedelta, timezone


class AnswerType(IntEnum):
    CORRECT = 1
    INCORRECT = 2
    TIMEOUT = 3


class Question:
    def __init__(self, difficulty, question, correct_answer_index, choices):
        """
        Represents a Quiz question

        :param difficulty:
        :param question: the actual question
        :param correct_answer_index: the index of the correct answer
        :param choices: list containing possible answers. The correct answer is always at index 0.
        """
        self.difficulty = difficulty
        self.question = question
        self.correct_answer_index = correct_answer_index
        self.choices = choices

    def get_answer_type(self, choice: int) -> AnswerType:
        if choice == self.correct_answer_index:
            return AnswerType.CORRECT
        else:
            return AnswerType.INCORRECT

    @staticmethod
    def from_dict(dictionary: dict) -> "Question":
        return Question(
            difficulty=dictionary["difficulty"],
            question=dictionary["question"],
            correct_answer_index=dictionary["correct_index"],
            choices=[dictionary[f"answer_{i}"] for i in range(1, 4 + 1)],
        )

    def __repr__(self):
        return f'Question({self.difficulty}, "{self.question}", {self.choices})'


class QuestionAttempt:
    def __init__(self, start, end, attempt_end=None, outcome=None):
        self.start = start
        self.end = end
        self.attempt_end = attempt_end
        self.outcome = outcome

    @property
    def end_timestamp(self):
        return self.end.timestamp() * 1000

    @property
    def has_timed_out(self):
        return datetime.now() > self.end

    @property
    def is_resolved(self):
        return self.outcome is not None and self.attempt_end is not None


class Player:
    def __init__(self, name: str):
        """
        Represents a Quiz player, and keeps track of their info

        :param name:
        """
        self.name = name

        self.current_question = 0
        self.score = 0
        self.current_streak = 0
        self.max_streak = 0
        self.num_correct = 0
        self.num_answered = 0

        self.question_attempts = []

    def start_question_attempt(self, time_limit: timedelta):
        now = datetime.now()

        self.question_attempts.append(QuestionAttempt(now, now + time_limit))

    def end_question_attempt(self, outcome: AnswerType):
        if self.current_attempt is None:
            return
        
        self.current_attempt.end = datetime.now()
        self.current_attempt.outcome = outcome

    @property
    def current_attempt(self) -> Optional[QuestionAttempt]:
        if len(self.question_attempts) == 0:
            return None

        return self.question_attempts[self.current_question]

    def next_question(self, time_limit):
        self.current_question += 1
        self.attempt_question(time_limit)


class Game:
    def __init__(
        self,
        game_id: str,
        questions: list[Question],
        update_score: Callable[[Player, AnswerType], int],
        time_per_question: timedelta,
    ):
        """
        Represents the state of a game

        :param game_id: the unique id of the game
        :param questions: questions to be asked in order
        :param update_score: function used to calculate and update player scores
        :param time_per_question: time per question as a `timedelta`
        """
        self.game_id = game_id
        self.questions = questions
        self.update_score = update_score
        self.time_per_question = time_per_question

        self.players = {}

    def get_player(self, player_name: str) -> Optional[Player]:
        return self.players[player_name]

    def player_has_next_question(self, player: Player) -> bool:
        return player.current_question == len(self.questions)

    def get_player_current_question(self, player: Player) -> Question:
        return self.questions[player.current_question]

    def on_question_answer(self, player: Player, choice: int) -> AnswerType:
        current_question = self.questions[player.current_question]
        outcome = current_question.get_answer_type(choice)

        player.end_question_attempt(outcome)

        self.update_score(player)

    def has_player_finished(self, player: Player):
        return player.current_question == len(self.questions)


class GameScoring:
    @staticmethod
    def score_with_timeout(player: Player) -> int:
        """
        :param status: Correct, Incorrect, Timeout
        """

        match player.current_attempt.outcome:
            case AnswerType.CORRECT:
                player.num_answered += 1
                player.num_correct += 1
                player.score += (time_left * 100) // 2 + player.current_streak * 100

                player.current_streak += 1
                player.max_streak = max(player.current_streak, player.max_streak)

            case AnswerType.INCORRECT:
                player.current_streak = 0
                player.num_answered += 1
