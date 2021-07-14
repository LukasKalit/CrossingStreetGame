from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=-150, y=240)
        self.color("black")

    def score(self, level_score):
        self.clear()
        self.write(arg=f"Level: {level_score}", move=False, align="center", font=FONT)

    def game_over_print(self, level_score):
        self.clear()
        self.write(arg=f"Level: {level_score}", move=False, align="center", font=FONT)
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER", move=False, align="center", font=FONT)