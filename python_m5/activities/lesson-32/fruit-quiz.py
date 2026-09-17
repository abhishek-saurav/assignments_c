class FruitQuiz:
    def __init__(self):
        self.clues = {
            "I am red or green and keep the doctor away": "apple",
            "I am yellow and monkeys love me": "banana",
            "I am small, purple and grow in bunches": "grape",
        }

    def ask(self):
        score = 0
        for clue, fruit in self.clues.items():
            answer = input(clue + " -> ")
            if answer.strip().lower() == fruit:
                print("Correct!")
                score = score + 1
            else:
                print("Wrong! The answer is", fruit)
        return score

quiz = FruitQuiz()
final_score = quiz.ask()
print("You scored", final_score, "out of", len(quiz.clues))
