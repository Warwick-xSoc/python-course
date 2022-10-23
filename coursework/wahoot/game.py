from typing import Optional, Callable
from enum import IntEnum
from datetime import datetime, timedelta
from random import shuffle


class AnswerType(IntEnum):
    CORRECT = 1
    INCORRECT = 2
    TIMEOUT = 3


class PlayerState(IntEnum):
    WAITING = 1
    ANSWERING = 2
    FINISHED = 3


class Question:
    def __init__(self, difficulty, text, correct, wrong):
        """
        Represents a Quiz question

        :param difficulty:
        :param text: the question's text
        :param correct: the correct answer
        :param wrong: list containing all of the wrong answers
        """
        self.difficulty: int = difficulty
        self.text: str = text
        self.correct: str = correct
        self.wrong: list[str] = wrong
    
    def get_options(self) -> tuple[list[str], int]:
        options = [self.correct] + self.wrong.copy()
        shuffle(options)
        return options, options.index(self.correct)

    @staticmethod
    def from_dict(dictionary: dict) -> "Question":
        return Question(
            difficulty=dictionary["difficulty"],
            text=dictionary["text"],
            correct=dictionary["correct"],
            wrong=[dictionary[f"wrong_{i}"] for i in range(1, 4)]
        )

    def __repr__(self):
        return f'Question({self.difficulty}, "{self.text}", {self.correct})'


class QuestionAttempt:
    def __init__(self, start, deadline, submitted_at=None):
        self.start: datetime = start
        self.deadline: datetime = deadline
        self.submitted_at: datetime = submitted_at

    @property
    def end_timestamp(self):
        return self.deadline.timestamp() * 1000

    @property
    def has_timed_out(self):
        return datetime.now() > self.deadline
    
    @property
    def time_left(self) -> float:
        """
        Returns time left in seconds
        """
        if not self.submitted_at:
            return 0.0
        
        return (self.deadline - self.submitted_at).total_seconds()


class Player:
    def __init__(self, name: str):
        """
        Represents a Quiz player, and keeps track of their info

        :param name:
        """
        self.name: str = name

        self.score: int = 0
        self.current_streak: int = 0
        self.max_streak: int = 0
        self.num_correct: int = 0
        self.num_answered: int = 0

        self.current_question: int = 0

        self.current_attempt: QuestionAttempt = None
        self.state: PlayerState = PlayerState.WAITING

    def start_question_attempt(self, time_limit: timedelta) -> None:
        now = datetime.now()
        self.state = PlayerState.ANSWERING
        self.current_attempt = QuestionAttempt(now, now + time_limit)

    def end_question_attempt(self, outcome: AnswerType) -> None:
        if self.current_attempt is None:
            return
        
        self.current_attempt.submitted_at = datetime.now()
        self.current_attempt.outcome = outcome

        self.current_attempt.question_score = self.apply_scoring(outcome)
        
        self.state = PlayerState.WAITING
        self.current_question += 1
    
    def apply_scoring(self, answer_type: AnswerType) -> int:
        if self.current_attempt is None:
            return 0
        
        question_score = 0

        match answer_type:
            case AnswerType.CORRECT:
                self.num_answered += 1
                self.num_correct += 1

                base_score = int((self.current_attempt.time_left * 100) // 2)
                streak_bonus = self.current_streak * 100
                question_score = base_score + streak_bonus
                
                self.score += question_score

                self.current_streak += 1
                self.max_streak = max(self.current_streak, self.max_streak)

            case AnswerType.INCORRECT:
                self.current_streak = 0
                self.num_answered += 1
            
            case AnswerType.TIMEOUT:
                self.current_streak = 0
        
        return question_score


class Game:
    def __init__(self, game_id: str, questions: list[Question], time_per_question: timedelta):
        """
        Represents the state of a game

        :param game_id: the unique id of the game
        :param questions: questions to be asked in order
        :param time_per_question: time per question as a `timedelta`
        """
        self.game_id = game_id
        self.questions = questions
        self.time_per_question = time_per_question

        self.players = {}

    @property
    def num_questions(self) -> int:
        return len(self.questions)

    @property
    def num_players(self) -> int:
        return len(self.players)

    def on_question_answer(self, player: Player, choice: int, correct_choice: int) -> AnswerType:
        if choice == correct_choice:
            outcome = AnswerType.CORRECT
        else:
            outcome = AnswerType.INCORRECT

        player.end_question_attempt(outcome)

        if self.has_player_finished(player):
            player.state = PlayerState.FINISHED

    def has_player_finished(self, player: Player) -> bool:
        return player.current_question >= self.num_questions

    def get_leaderboard(self) -> list[Player]:
        # TODO: make O(horrible) to fix in week 6, such as bubble sort
        return sorted(
            self.players.values(),
            key=lambda p: (p.score, p.max_streak, p.num_correct, p.name),
            reverse=True
        )