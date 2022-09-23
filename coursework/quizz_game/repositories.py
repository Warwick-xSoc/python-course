from game import Question
from random import choice

class QuestionRepository:
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
    def get_question(self, difficulty = -1):

        if difficulty <= -1 or difficulty > 2:
            # Pick a random question if no difficulty specified
            return choice(self.questions)
        
        # Otherwise, pick a question that has the specified difficulty
        diff_questions = [q for q in self.questions if q.difficulty == difficulty]
        return choice(diff_questions)

    # Should we get them to prevent the same q from appearing 2+ times in the same quiz?
                

class GameRepository:
    pass