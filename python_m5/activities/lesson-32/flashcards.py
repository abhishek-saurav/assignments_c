class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def check(self, user_answer):
        return user_answer.strip().lower() == self.answer.lower()

cards = [
    Flashcard("Capital of France?", "Paris"),
    Flashcard("2 + 2 * 2 = ?", "6"),
    Flashcard("Chess piece that moves diagonally?", "Bishop"),
]

score = 0
for card in cards:
    user_answer = input(card.question + " ")
    if card.check(user_answer):
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The answer is", card.answer)

print("Your score:", score, "out of", len(cards))
