class Question:
    def __init__(self, difficulty, question, choices):
        """
        Represents a Quizz question 

        :param difficulty: 
        :param question: the actual question
        :param choices: list containing possible answers. The correct answer is always at index 0.
        """
        self.difficulty = difficulty
        self.question = question
        self.choices = choices

    def __repr__(self):
        return f'Question({self.difficulty}, "{self.question}", {self.choices})'



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
        return self.current_question == len(questions)