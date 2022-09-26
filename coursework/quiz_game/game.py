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
    def __init__(self, uuid, questions, current_question=0):
        """
        Represents the state of a game

        :param uuid: the UUID of the game
        :param questions: questions to be asked in order
        :param current_question: current question index in questions
        """
        self.uuid = uuid
        self.questions = questions
        self.current_question = current_question

    @property
    def has_finished(self):
        return self.current_question == len(self.questions)