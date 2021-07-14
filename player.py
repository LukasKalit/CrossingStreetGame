from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 50
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.speed(0)
        self.penup()
        self.goto(x=0, y=-280)
        self.setheading(90)

    def run_turtle(self):

        self.forward(MOVE_DISTANCE)

    def win_level(self, level):

        if self.ycor() > FINISH_LINE_Y:
            self.goto(x=0, y=-280)
            level += 1
            return level
        return level
