class Cricket:
    def __init__(self, player, score):
        self.player = player
        self.score = score

    def info(self):
        print(f"Cricket  - Player: {self.player}, Score: {self.score}")

    def play(self):
        print(f"{self.player} hits a six!")


class Football:
    def __init__(self, player, score):
        self.player = player
        self.score = score

    def info(self):
        print(f"Football - Player: {self.player}, Score: {self.score}")

    def play(self):
        print(f"{self.player} scores a goal!")


cricket  = Cricket("Rohit",  85)
football = Football("Arjun", 2)

for sport in (cricket, football):
    sport.info()
    sport.play()
    print()
