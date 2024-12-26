import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# player setup
player = Player()
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_up, "w")
game_is_on = True

# car setup
car_manager = CarManager()

# score
level = Scoreboard()

# food

while game_is_on:
    time.sleep(car_manager.speed)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    if player.ycor() > 280:
        player.restart()
        car_manager.new_level()
        level.new_level()

    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            level.game_over()

screen.exitonclick()

