from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.speed = 0.1

    def create_car(self):
        chance = random.randint(1, 6)
        if chance < 2:
            car = Turtle()
            color = random.choice(COLORS)
            car.color(color)
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            y = random.randint(-260, 280)
            car.goto(290, y)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def new_level(self):
        self.speed *= 0.9
