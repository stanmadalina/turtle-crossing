from turtle import Turtle
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.level = 1
        self.write(f"Level {self.level}", align="left", font=FONT)
        self.write("\tPress W or Up to move the turtle.", align="left", font=FONT)

    def new_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 30, "bold"))


