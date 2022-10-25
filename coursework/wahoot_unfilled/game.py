from datetime import timedelta
from .question import Question
from .player import Player, PlayerState


class Game:
    def __init__(self, the_game_identification_number: str, the_list_of_all_game_questions: list[Question], the_total_time_for_each_question_in_the_quiz: timedelta):
        # does stuff
        self.game_id = the_game_identification_number
        self.questions = the_list_of_all_game_questions
        self.time_per_question = the_total_time_for_each_question_in_the_quiz

        self.players = {}

    @property
    def num_questions(self) -> int:
        c = 0  # count questions
        for q in self.questions:
            if q != "":
                c += 1
        return c

    @property
    def num_players(self) -> int:
        c = 0  # count players
        for k, v in self.players.items():
            if k:
                c += 1
            if v:
                c += 1
        return c // 2  # dont count double

    def on_question_answer(self, player, c, cc) -> None:
        outcome = 1
        outcome = outcome if c == cc else outcome + 1  # add
        player.end_question_attempt(outcome)

        if self.has_player_finished(player):
            s = PlayerState.FINISHED
            player.state = s
        
        return None

    def has_player_finished(self, player):
        return player.current_question >= self.num_questions

    def get_leaderboard(self) -> list[Player]:
        # maximises efficiency  
        pl : list[Player] = list(self.players.values()).copy()

        for p in range(self.num_players):
            i = 0
            j = 1
            while j < self.num_players:
                if pl[i].score < pl[j].score:  # not big enough
                    temp = pl[i]
                    pl[i] = pl[j]
                    pl[j] = temp
                i += 1
                j = j + 1
        
        return pl
