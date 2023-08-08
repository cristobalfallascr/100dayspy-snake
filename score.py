from turtle import Turtle
ALINGMENT = 'center'
FONT = ("Arial", 18, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.goto(15,275)

        self.color('green')
        self.hideturtle()
        self.read_score()
        self.update_scoreboard()


    def read_score(self):
        with open("high_score.txt") as file:
            self.high_score = int(file.read())

    def update_scoreboard(self):
        self.clear()
        self.read_score()
        self.write(f"Score: {self.score}   - | -   High Score: {self.high_score}", align=ALINGMENT, font=FONT)

    # def update_high_score(self):
    #     self.high_score = self.score
    #     self.update_scoreboard()
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.color('red')
    #     self.write("GAME OVER!", align=ALINGMENT, font=FONT)
    #     self.update_high_score()
    #
    def reset(self):
        if self.score > self.high_score:
            with open("high_score.txt",  mode='w') as file:
                file.write(str(self.score))
        self.score = 0
        self.update_scoreboard()

