from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.setposition(STARTING_POSITION[0], STARTING_POSITION[1])

    def move_up(self):
        self.forward(10)

    def restart(self):
        self.goto(STARTING_POSITION[0], STARTING_POSITION[1])


