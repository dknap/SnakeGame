from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
GAME_OVER = "Game Over"
HIGH_SCORE = "data.txt"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 260)
        self.score = 0
        with open(HIGH_SCORE, "r") as data:
            self.high_score = data.read()
            data.close()
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        print(self.score)
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(GAME_OVER, False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open(HIGH_SCORE, "w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()