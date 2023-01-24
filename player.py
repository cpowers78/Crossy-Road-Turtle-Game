from turtle import Turtle
INITIAL_POSITION = (0,-270)

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(INITIAL_POSITION)
        self.color("black")
        self.right(270)




    def move_up(self):
        self.setheading(90)
        new_ycor = self.ycor() + 10
        self.goto(self.xcor(), new_ycor)

    def move_right(self):
        self.setheading(360)
        new_xcor = self.xcor() + 10
        self.goto(new_xcor, self.ycor())

    def move_left(self):
        self.setheading(180)
        new_xcor = self.xcor() - 10
        self.goto(new_xcor, self.ycor())



