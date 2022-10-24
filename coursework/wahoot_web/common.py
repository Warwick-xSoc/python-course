from wahoot.repositories import QuestionBank, GameHistory
from wahoot.services import GameService

# Retrieve stored game data and questions
game_history = GameHistory()
question_bank = QuestionBank("test.csv")
game_service = GameService(game_history, question_bank)