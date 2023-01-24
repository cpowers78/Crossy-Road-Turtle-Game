import turtle

COLOR_LIST = [ (43, 2, 176), (79, 253, 174), (226, 149, 109), (230, 225, 253),
 (160, 3, 82), (4, 211, 101), (3, 138, 64), (246, 42, 127), (109, 108, 247), (252, 253, 53), (184, 184, 251),
 (211, 106, 5), (35, 35, 252), (177, 112, 248), (139, 1, 0), (252, 36, 35), (50, 240, 56), (216, 114, 171),
 (16, 127, 144), (85, 248, 252), (188, 39, 109), (23, 5, 107), (8, 209, 215), (99, 8, 50), (231, 163, 205),
 (204, 119, 35), (112, 6, 4), (239, 165, 161), (8, 114, 21)]

MOTION_INCREMENT = 5

from turtle import Turtle
import random

turtle.colormode(255)

class Cars(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(random.choice(COLOR_LIST))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(random.randint(-240, 240), random.randint(-240,240))

    def move_left(self):
        new_x = self.xcor() - MOTION_INCREMENT
        self.goto(new_x, self.ycor())

    def gain_speed(self):
        new_speed = MOTION_INCREMENT * 2
        new_x = self.xcor() - new_speed
        self.goto(new_x, self.ycor())






