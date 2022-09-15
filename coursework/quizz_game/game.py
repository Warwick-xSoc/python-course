class Question:
    def __init__(self, question, choices, correct_answer):
        """
        Represents a Quizz question 

        :param question: the actual question
        :param choices: tuple containing possible answers
        :param correct_answer: index of the correct answer
        """
        self.question = question
        self.choices = choices
        self.correct_answer = correct_answer


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