from turtle import Turtle, Screen
from player import Player
import time
from cars import Cars
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossy Road")
screen.tracer(0)

turt = Player()
scoreboard = Scoreboard()
scoreboard.update_score()


screen.listen()
screen.onkeypress(turt.move_up, "Up")
screen.onkeypress(turt.move_left, "Left")
screen.onkeypress(turt.move_right, "Right")


game_is_on = True

list_of_cars = []
loop_counter = 0

for i in range(6):
    car = Cars()
    list_of_cars.append(car)


while game_is_on:
    screen.update()
    time.sleep(0.1)
    loop_counter += 1


    if loop_counter % 6 == 0:
        new_car = Cars()
        new_car.goto(270, new_car.ycor())
        list_of_cars.append(new_car)

    for c in list_of_cars:
        c.move_left()
        if turt.distance(c) < 15:
            game_is_on = False
            scoreboard.game_over()
        if turt.ycor() > 260:
            turt.goto(0, -270)
            c.gain_speed()
            scoreboard.increase_score()












screen.exitonclick()

